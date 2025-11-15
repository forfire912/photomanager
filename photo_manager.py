#!/usr/bin/env python3
"""
Photo Manager - A tool to organize and manage photo/video collections
"""

import os
import sys
import hashlib
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import logging

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    print("Warning: Pillow not installed. Install with: pip install Pillow")
    Image = None
    TAGS = None

# Supported file extensions
PHOTO_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.heif', '.webp'}
VIDEO_EXTENSIONS = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.m4v', '.3gp'}
ALL_EXTENSIONS = PHOTO_EXTENSIONS | VIDEO_EXTENSIONS

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_file_hash(filepath, hash_algorithm='md5'):
    """Calculate hash of a file for duplicate detection"""
    hash_func = hashlib.md5() if hash_algorithm == 'md5' else hashlib.sha256()
    
    try:
        with open(filepath, 'rb') as f:
            # Read file in chunks to handle large files
            for chunk in iter(lambda: f.read(8192), b''):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        logger.error(f"Error hashing file {filepath}: {e}")
        return None


def get_exif_date(filepath):
    """Extract date from EXIF metadata"""
    if Image is None:
        return None
    
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        
        if exif_data:
            # Try to get DateTimeOriginal (when photo was taken)
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'DateTimeOriginal':
                    # Format: 'YYYY:MM:DD HH:MM:SS'
                    return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        logger.debug(f"Could not extract EXIF from {filepath}: {e}")
    
    return None


def get_file_date(filepath):
    """Get the best available date for a file"""
    # Try EXIF first for photos
    file_ext = Path(filepath).suffix.lower()
    
    if file_ext in PHOTO_EXTENSIONS:
        exif_date = get_exif_date(filepath)
        if exif_date:
            return exif_date
    
    # Fall back to file modification time
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.fromtimestamp(mtime)
    except Exception as e:
        logger.error(f"Error getting date for {filepath}: {e}")
        return None


def scan_directory(directory, recursive=True):
    """Scan directory for photos and videos"""
    files = []
    directory = Path(directory)
    
    if not directory.exists():
        logger.error(f"Directory does not exist: {directory}")
        return files
    
    logger.info(f"Scanning directory: {directory}")
    
    if recursive:
        pattern = '**/*'
    else:
        pattern = '*'
    
    for filepath in directory.glob(pattern):
        if filepath.is_file():
            ext = filepath.suffix.lower()
            if ext in ALL_EXTENSIONS:
                files.append(filepath)
    
    logger.info(f"Found {len(files)} media files")
    return files


def find_duplicates(files):
    """Find duplicate files based on hash"""
    logger.info("Detecting duplicates...")
    hash_to_files = defaultdict(list)
    
    for filepath in files:
        file_hash = get_file_hash(filepath)
        if file_hash:
            hash_to_files[file_hash].append(filepath)
    
    # Keep only groups with duplicates
    duplicates = {k: v for k, v in hash_to_files.items() if len(v) > 1}
    
    total_duplicates = sum(len(files) - 1 for files in duplicates.values())
    logger.info(f"Found {total_duplicates} duplicate files in {len(duplicates)} groups")
    
    return duplicates


def remove_duplicates(duplicates, keep_first=True, dry_run=True):
    """Remove duplicate files, keeping one copy"""
    removed_count = 0
    
    for file_hash, file_list in duplicates.items():
        # Sort by path to have consistent behavior
        file_list = sorted(file_list, key=lambda x: str(x))
        
        # Keep the first file, remove the rest
        files_to_remove = file_list[1:] if keep_first else file_list[:-1]
        
        for filepath in files_to_remove:
            if dry_run:
                logger.info(f"[DRY RUN] Would remove: {filepath}")
            else:
                try:
                    os.remove(filepath)
                    logger.info(f"Removed duplicate: {filepath}")
                    removed_count += 1
                except Exception as e:
                    logger.error(f"Error removing {filepath}: {e}")
    
    if dry_run:
        logger.info(f"[DRY RUN] Would remove {sum(len(files) - 1 for files in duplicates.values())} duplicate files")
    else:
        logger.info(f"Removed {removed_count} duplicate files")
    
    return removed_count


def organize_by_date(files, output_dir, dry_run=True):
    """Organize files into folders by date (YYYY/MM/DD)"""
    logger.info("Organizing files by date...")
    output_dir = Path(output_dir)
    organized_count = 0
    
    for filepath in files:
        file_date = get_file_date(filepath)
        
        if file_date is None:
            # Put files without dates in an 'unknown' folder
            dest_dir = output_dir / 'unknown'
        else:
            # Create folder structure: YYYY/MM/DD
            dest_dir = output_dir / file_date.strftime('%Y') / file_date.strftime('%m') / file_date.strftime('%d')
        
        # Create destination directory
        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)
        
        dest_path = dest_dir / filepath.name
        
        # Handle filename conflicts
        counter = 1
        while dest_path.exists() and not dry_run:
            stem = filepath.stem
            suffix = filepath.suffix
            dest_path = dest_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        if dry_run:
            logger.info(f"[DRY RUN] Would copy: {filepath} -> {dest_path}")
        else:
            try:
                shutil.copy2(filepath, dest_path)
                logger.info(f"Copied: {filepath} -> {dest_path}")
                organized_count += 1
            except Exception as e:
                logger.error(f"Error copying {filepath}: {e}")
    
    if dry_run:
        logger.info(f"[DRY RUN] Would organize {len(files)} files")
    else:
        logger.info(f"Organized {organized_count} files")
    
    return organized_count


def main():
    parser = argparse.ArgumentParser(
        description='Photo Manager - Organize and manage photo/video collections',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan directory and find duplicates (dry run)
  python photo_manager.py -d /path/to/photos --find-duplicates
  
  # Remove duplicates (actually delete them)
  python photo_manager.py -d /path/to/photos --remove-duplicates --execute
  
  # Organize photos by date
  python photo_manager.py -d /path/to/photos --organize -o /path/to/organized --execute
  
  # Scan multiple directories
  python photo_manager.py -d /path/to/photos1 /path/to/photos2 --find-duplicates
        """
    )
    
    parser.add_argument('-d', '--directories', nargs='+', required=True,
                        help='Directories to scan for photos/videos')
    parser.add_argument('--recursive', action='store_true', default=True,
                        help='Scan directories recursively (default: True)')
    parser.add_argument('--find-duplicates', action='store_true',
                        help='Find and report duplicate files')
    parser.add_argument('--remove-duplicates', action='store_true',
                        help='Remove duplicate files (keeps first occurrence)')
    parser.add_argument('--organize', action='store_true',
                        help='Organize files by date into YYYY/MM/DD folders')
    parser.add_argument('-o', '--output', type=str,
                        help='Output directory for organized files')
    parser.add_argument('--execute', action='store_true',
                        help='Actually perform operations (default is dry run)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Scan all directories
    all_files = []
    for directory in args.directories:
        files = scan_directory(directory, recursive=args.recursive)
        all_files.extend(files)
    
    if not all_files:
        logger.warning("No media files found!")
        return
    
    logger.info(f"Total files found: {len(all_files)}")
    
    # Find duplicates
    if args.find_duplicates or args.remove_duplicates:
        duplicates = find_duplicates(all_files)
        
        if duplicates:
            logger.info("\nDuplicate groups:")
            for file_hash, file_list in duplicates.items():
                logger.info(f"\nHash: {file_hash}")
                for filepath in file_list:
                    logger.info(f"  - {filepath}")
        
        # Remove duplicates if requested
        if args.remove_duplicates:
            remove_duplicates(duplicates, dry_run=not args.execute)
    
    # Organize by date
    if args.organize:
        if not args.output:
            logger.error("--output directory is required for --organize")
            sys.exit(1)
        
        organize_by_date(all_files, args.output, dry_run=not args.execute)
    
    logger.info("\nDone!")


if __name__ == '__main__':
    main()
