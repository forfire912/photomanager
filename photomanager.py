#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Photo Manager - Organize photos and videos by shooting time and remove duplicates
整理照片 - 按拍摄时间整理照片和视频，并清理重复文件
"""

import os
import sys
import hashlib
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import logging

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    print("Error: Pillow library not installed. Please run: pip install Pillow")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PhotoManager:
    """Photo and video manager to organize files by date and remove duplicates"""
    
    # Supported file extensions
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.heic', '.webp'}
    VIDEO_EXTENSIONS = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.m4v', '.3gp'}
    
    def __init__(self, source_dirs, output_dir, remove_duplicates=True, dry_run=False):
        """
        Initialize PhotoManager
        
        Args:
            source_dirs: List of source directories to scan
            output_dir: Output directory for organized files
            remove_duplicates: Whether to remove duplicate files
            dry_run: If True, only show what would be done without actually moving files
        """
        self.source_dirs = [Path(d) for d in source_dirs]
        self.output_dir = Path(output_dir)
        self.remove_duplicates = remove_duplicates
        self.dry_run = dry_run
        self.file_hashes = {}  # hash -> file_path mapping for duplicate detection
        self.stats = {
            'total_files': 0,
            'organized_files': 0,
            'duplicates_found': 0,
            'errors': 0
        }
    
    def calculate_file_hash(self, file_path):
        """Calculate SHA256 hash of a file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                # Read file in chunks to handle large files
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            logger.error(f"Error calculating hash for {file_path}: {e}")
            return None
    
    def get_exif_date(self, file_path):
        """Extract shooting date from EXIF data"""
        try:
            image = Image.open(file_path)
            exif_data = image._getexif()
            
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag in ['DateTimeOriginal', 'DateTime', 'DateTimeDigitized']:
                        # EXIF date format: "2023:11:14 17:08:02"
                        try:
                            return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                        except ValueError:
                            continue
        except Exception as e:
            logger.debug(f"Could not read EXIF from {file_path}: {e}")
        
        return None
    
    def get_file_date(self, file_path):
        """Get file date from EXIF or file modification time"""
        # Try to get EXIF date first
        exif_date = self.get_exif_date(file_path)
        if exif_date:
            return exif_date
        
        # Fall back to file modification time
        try:
            mtime = os.path.getmtime(file_path)
            return datetime.fromtimestamp(mtime)
        except Exception as e:
            logger.error(f"Error getting date for {file_path}: {e}")
            return None
    
    def is_supported_file(self, file_path):
        """Check if file is a supported image or video"""
        ext = file_path.suffix.lower()
        return ext in self.IMAGE_EXTENSIONS or ext in self.VIDEO_EXTENSIONS
    
    def scan_files(self):
        """Scan all source directories for supported files"""
        files = []
        for source_dir in self.source_dirs:
            if not source_dir.exists():
                logger.warning(f"Source directory does not exist: {source_dir}")
                continue
            
            logger.info(f"Scanning directory: {source_dir}")
            for root, dirs, filenames in os.walk(source_dir):
                for filename in filenames:
                    file_path = Path(root) / filename
                    if self.is_supported_file(file_path):
                        files.append(file_path)
                        self.stats['total_files'] += 1
        
        logger.info(f"Found {len(files)} supported files")
        return files
    
    def get_output_path(self, file_path, file_date):
        """Generate output path based on date"""
        # Create directory structure: YYYY/YYYY-MM/YYYY-MM-DD/
        year = file_date.strftime('%Y')
        month = file_date.strftime('%Y-%m')
        day = file_date.strftime('%Y-%m-%d')
        
        output_subdir = self.output_dir / year / month / day
        output_file = output_subdir / file_path.name
        
        # Handle filename conflicts
        counter = 1
        while output_file.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            output_file = output_subdir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        return output_file
    
    def organize_files(self):
        """Main method to organize files"""
        files = self.scan_files()
        
        if not files:
            logger.warning("No files found to organize")
            return
        
        logger.info(f"Starting organization (dry_run={self.dry_run})")
        
        for file_path in files:
            try:
                # Check for duplicates
                if self.remove_duplicates:
                    file_hash = self.calculate_file_hash(file_path)
                    if file_hash:
                        if file_hash in self.file_hashes:
                            logger.info(f"Duplicate found: {file_path} (same as {self.file_hashes[file_hash]})")
                            self.stats['duplicates_found'] += 1
                            continue
                        self.file_hashes[file_hash] = file_path
                
                # Get file date
                file_date = self.get_file_date(file_path)
                if not file_date:
                    logger.warning(f"Could not determine date for {file_path}, skipping")
                    self.stats['errors'] += 1
                    continue
                
                # Get output path
                output_path = self.get_output_path(file_path, file_date)
                
                # Create directory and copy/move file
                if not self.dry_run:
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, output_path)
                    logger.info(f"Organized: {file_path} -> {output_path}")
                else:
                    logger.info(f"[DRY RUN] Would organize: {file_path} -> {output_path}")
                
                self.stats['organized_files'] += 1
                
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
                self.stats['errors'] += 1
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print organization summary"""
        logger.info("=" * 60)
        logger.info("Organization Summary:")
        logger.info(f"  Total files scanned: {self.stats['total_files']}")
        logger.info(f"  Files organized: {self.stats['organized_files']}")
        logger.info(f"  Duplicates found: {self.stats['duplicates_found']}")
        logger.info(f"  Errors: {self.stats['errors']}")
        logger.info("=" * 60)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='照片管理工具 - 按拍摄时间整理照片和视频，并清理重复文件\n'
                    'Photo Manager - Organize photos and videos by shooting time and remove duplicates',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'source_dirs',
        nargs='+',
        help='源目录（可指定多个）/ Source directories (can specify multiple)'
    )
    
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='输出目录 / Output directory'
    )
    
    parser.add_argument(
        '--no-remove-duplicates',
        action='store_true',
        help='不删除重复文件 / Do not remove duplicate files'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='预览模式，不实际移动文件 / Dry run mode, do not actually move files'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='详细日志 / Verbose logging'
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate source directories
    for source_dir in args.source_dirs:
        if not os.path.exists(source_dir):
            logger.error(f"Source directory does not exist: {source_dir}")
            sys.exit(1)
    
    # Create photo manager and organize files
    manager = PhotoManager(
        source_dirs=args.source_dirs,
        output_dir=args.output,
        remove_duplicates=not args.no_remove_duplicates,
        dry_run=args.dry_run
    )
    
    manager.organize_files()


if __name__ == '__main__':
    main()
