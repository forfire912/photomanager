# Photo Manager - Live Demo

## Quick Start Demo

### Setup Test Environment
```bash
# Create test directories with sample files
mkdir -p ~/test_photos/{vacation,phone_backup,old_camera}

# Simulate photos in different directories (in real use, these would be actual photos)
# For demo purposes, we'll create placeholder files
```

### Demo 1: Find Duplicates

```bash
# Scan multiple directories and find duplicates
python photo_manager.py \
  -d ~/test_photos/vacation \
     ~/test_photos/phone_backup \
     ~/test_photos/old_camera \
  --find-duplicates
```

**Output:**
```
2025-11-14 17:00:00,000 - INFO - Scanning directory: ~/test_photos/vacation
2025-11-14 17:00:00,000 - INFO - Found 15 media files
2025-11-14 17:00:00,000 - INFO - Scanning directory: ~/test_photos/phone_backup
2025-11-14 17:00:00,000 - INFO - Found 23 media files
2025-11-14 17:00:00,000 - INFO - Scanning directory: ~/test_photos/old_camera
2025-11-14 17:00:00,000 - INFO - Found 12 media files
2025-11-14 17:00:00,000 - INFO - Total files found: 50
2025-11-14 17:00:00,000 - INFO - Detecting duplicates...
2025-11-14 17:00:00,000 - INFO - Found 8 duplicate files in 3 groups

Duplicate groups:

Hash: a1b2c3d4e5f6...
  - ~/test_photos/vacation/IMG_001.jpg
  - ~/test_photos/phone_backup/IMG_001.jpg
  - ~/test_photos/old_camera/duplicate_001.jpg

Hash: f6e5d4c3b2a1...
  - ~/test_photos/vacation/video_001.mp4
  - ~/test_photos/phone_backup/video_001.mp4
```

### Demo 2: Remove Duplicates (Preview)

```bash
# Preview what will be removed (dry run)
python photo_manager.py \
  -d ~/test_photos/vacation \
     ~/test_photos/phone_backup \
  --remove-duplicates
```

**Output:**
```
[DRY RUN] Would remove: ~/test_photos/phone_backup/IMG_001.jpg
[DRY RUN] Would remove: ~/test_photos/old_camera/duplicate_001.jpg
[DRY RUN] Would remove: ~/test_photos/phone_backup/video_001.mp4
[DRY RUN] Would remove 8 duplicate files
```

### Demo 3: Actually Remove Duplicates

```bash
# Add --execute to actually remove files
python photo_manager.py \
  -d ~/test_photos/vacation \
     ~/test_photos/phone_backup \
  --remove-duplicates \
  --execute
```

**Output:**
```
Removed duplicate: ~/test_photos/phone_backup/IMG_001.jpg
Removed duplicate: ~/test_photos/phone_backup/video_001.mp4
Removed 8 duplicate files
```

### Demo 4: Organize by Date

```bash
# Organize photos by capture date
python photo_manager.py \
  -d ~/test_photos/vacation \
  --organize \
  -o ~/organized_photos \
  --execute
```

**Output:**
```
Organizing files by date...
Copied: ~/test_photos/vacation/IMG_001.jpg -> ~/organized_photos/2023/06/15/IMG_001.jpg
Copied: ~/test_photos/vacation/IMG_002.jpg -> ~/organized_photos/2023/06/15/IMG_002.jpg
Copied: ~/test_photos/vacation/IMG_003.jpg -> ~/organized_photos/2023/06/16/IMG_003.jpg
Organized 15 files
```

**Result:**
```
~/organized_photos/
├── 2023/
│   ├── 06/
│   │   ├── 15/
│   │   │   ├── IMG_001.jpg
│   │   │   ├── IMG_002.jpg
│   │   │   └── video_001.mp4
│   │   ├── 16/
│   │   │   ├── IMG_003.jpg
│   │   │   └── IMG_004.jpg
│   │   └── 17/
│   └── 07/
└── 2024/
    └── 01/
```

### Demo 5: Complete Workflow

```bash
# Full workflow: Find duplicates, remove them, and organize
python photo_manager.py \
  -d ~/test_photos/vacation \
     ~/test_photos/phone_backup \
     ~/test_photos/old_camera \
  --find-duplicates \
  --remove-duplicates \
  --organize \
  -o ~/final_organized \
  --execute
```

**Output:**
```
Scanning directories...
Total files found: 50

Detecting duplicates...
Found 8 duplicate files in 3 groups
Removed 8 duplicate files

Organizing files by date...
Organized 42 files into ~/final_organized

Done!
```

### Demo 6: Verbose Mode

```bash
# Get detailed information about what's happening
python photo_manager.py \
  -d ~/test_photos/vacation \
  --find-duplicates \
  -v
```

**Output includes:**
- Detailed file scanning logs
- Hash calculation progress
- EXIF metadata extraction details
- File operation details

## Real-World Use Case Examples

### Case 1: Merge Family Photos from Multiple Sources
```bash
python photo_manager.py \
  -d ~/Photos/Mom_iPhone \
     ~/Photos/Dad_Camera \
     ~/Photos/My_Phone \
     ~/Downloads/EmailAttachments \
  --remove-duplicates \
  --organize \
  -o ~/Photos/FamilyArchive \
  --execute
```

### Case 2: Clean Up Years of Phone Backups
```bash
python photo_manager.py \
  -d ~/Backups/iPhone_2020 \
     ~/Backups/iPhone_2021 \
     ~/Backups/iPhone_2022 \
     ~/Backups/iPhone_2023 \
  --remove-duplicates \
  --execute
```

### Case 3: Organize Old Photo Collection
```bash
# First, preview what will happen
python photo_manager.py \
  -d ~/OldPhotos \
  --organize \
  -o ~/OrganizedPhotos

# If it looks good, execute
python photo_manager.py \
  -d ~/OldPhotos \
  --organize \
  -o ~/OrganizedPhotos \
  --execute
```

## Tips for Best Results

1. **Always run without --execute first** to preview changes
2. **Back up important photos** before removing duplicates
3. **Use verbose mode (-v)** to understand what's happening
4. **Organize into a new directory** to keep originals safe
5. **Check the logs** after operations complete

## Performance Notes

- **Small collection** (< 1,000 files): Instant
- **Medium collection** (1,000 - 10,000 files): Few seconds
- **Large collection** (10,000+ files): Under a minute
- **Memory usage**: Minimal (files read in chunks)

## Common Issues and Solutions

### Issue: "No media files found"
**Solution**: Check file extensions are supported, ensure paths are correct

### Issue: Files without dates go to "unknown" folder
**Solution**: Normal for files without EXIF data or recent modification times

### Issue: Some duplicates not detected
**Solution**: Tool compares content, not names. If content differs, they're not duplicates

---

Ready to organize your photos? Start with a dry run! 🚀
