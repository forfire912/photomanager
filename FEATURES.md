# Photo Manager - Feature Summary

## 核心功能 / Core Features

### 1. 多目录扫描 / Multi-Directory Scanning
```bash
python photo_manager.py -d /photos1 /photos2 /photos3 --find-duplicates
```
- ✅ Recursively scans multiple directories
- ✅ Finds all supported media files
- ✅ Works across different folder structures

### 2. 重复检测 / Duplicate Detection
```bash
python photo_manager.py -d /photos --find-duplicates
```
- ✅ Content-based comparison (MD5 hash)
- ✅ Works regardless of file names
- ✅ Detects duplicates across different folders
- ✅ Groups duplicates for easy review

**Example Output:**
```
Found 3 duplicate files in 2 groups

Hash: cccb2c39dc0f1765bd3efb4433e6527b
  - /photos/vacation/img001.jpg
  - /photos/backup/img001_copy.jpg
  - /photos/old/duplicate.jpg
```

### 3. 智能清理 / Smart Cleanup
```bash
# Preview what will be removed
python photo_manager.py -d /photos --remove-duplicates

# Actually remove duplicates
python photo_manager.py -d /photos --remove-duplicates --execute
```
- ✅ Keeps first occurrence (sorted by path)
- ✅ Dry-run mode by default (safe preview)
- ✅ Detailed logging of all deletions
- ✅ Preserves original files

### 4. 日期整理 / Date-Based Organization
```bash
python photo_manager.py -d /photos --organize -o /organized --execute
```
- ✅ Extracts EXIF DateTimeOriginal from photos
- ✅ Falls back to file modification time
- ✅ Creates YYYY/MM/DD folder structure
- ✅ Handles files without dates (unknown folder)

**Output Structure:**
```
organized/
├── 2023/
│   ├── 01/
│   │   ├── 15/
│   │   │   ├── photo1.jpg
│   │   │   └── photo2.jpg
│   │   └── 16/
│   └── 02/
├── 2024/
│   ├── 06/
│   └── 12/
└── unknown/
    └── no-date.jpg
```

## 支持的文件格式 / Supported File Formats

### 照片格式 / Photo Formats
- JPG/JPEG
- PNG
- GIF
- BMP
- TIFF
- HEIC/HEIF (Apple photos)
- WebP

### 视频格式 / Video Formats
- MP4
- MOV (QuickTime)
- AVI
- MKV
- WMV
- FLV
- M4V
- 3GP

## 安全特性 / Safety Features

### 1. 预览模式 / Dry-Run Mode
- All operations default to preview mode
- Must explicitly use `--execute` to make changes
- See exactly what will happen before it happens

### 2. 详细日志 / Detailed Logging
- Every operation is logged
- File paths shown for all actions
- Easy to review what was done

### 3. 文件名冲突处理 / Conflict Handling
- Automatically detects filename conflicts
- Adds numeric suffix (file_1.jpg, file_2.jpg)
- Never overwrites existing files

## 实际使用场景 / Real-World Use Cases

### Scenario 1: 整理多年照片 / Organize Years of Photos
```bash
# Step 1: Find duplicates across all photo folders
python photo_manager.py \
  -d ~/Pictures/2020 ~/Pictures/2021 ~/Pictures/2022 \
  --find-duplicates

# Step 2: Remove duplicates
python photo_manager.py \
  -d ~/Pictures/2020 ~/Pictures/2021 ~/Pictures/2022 \
  --remove-duplicates --execute

# Step 3: Organize by date
python photo_manager.py \
  -d ~/Pictures/2020 ~/Pictures/2021 ~/Pictures/2022 \
  --organize -o ~/Pictures/Organized --execute
```

### Scenario 2: 清理手机备份 / Clean Phone Backups
```bash
# Multiple phone backups with duplicates
python photo_manager.py \
  -d ~/PhoneBackup2023 ~/PhoneBackup2024 ~/Cloud \
  --remove-duplicates --execute
```

### Scenario 3: 合并家庭照片 / Merge Family Photos
```bash
# Combine photos from different family members
python photo_manager.py \
  -d ~/Mom/Photos ~/Dad/Photos ~/MyPhotos \
  --find-duplicates \
  --organize -o ~/FamilyPhotos \
  --execute
```

## 性能特点 / Performance

- **内存高效 / Memory Efficient**: Reads files in chunks (8KB), handles large files
- **快速哈希 / Fast Hashing**: MD5 algorithm for quick duplicate detection
- **批量处理 / Batch Processing**: Processes multiple directories at once
- **进度日志 / Progress Logging**: Real-time updates during operations

## 命令行快速参考 / CLI Quick Reference

| Option | Description | Example |
|--------|-------------|---------|
| `-d, --directories` | Directories to scan | `-d /photos /backup` |
| `--find-duplicates` | Find duplicate files | `--find-duplicates` |
| `--remove-duplicates` | Remove duplicates | `--remove-duplicates` |
| `--organize` | Organize by date | `--organize` |
| `-o, --output` | Output directory | `-o /organized` |
| `--execute` | Actually perform actions | `--execute` |
| `-v, --verbose` | Verbose logging | `-v` |

## 最佳实践 / Best Practices

1. **Always test with dry-run first** (default behavior)
2. **Backup important photos** before removing duplicates
3. **Review the output** before using --execute
4. **Use verbose mode** (`-v`) for detailed information
5. **Organize in a new directory** to keep originals safe

---

💡 **Tip**: Combine operations for efficiency:
```bash
python photo_manager.py \
  -d /photos \
  --find-duplicates \
  --remove-duplicates \
  --organize -o /organized \
  --execute
```
