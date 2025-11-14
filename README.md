# Photo Manager / 照片管理工具

一个用于整理和管理照片/视频收藏的Python工具。

A Python tool for organizing and managing photo/video collections.

## 功能特性 / Features

- ✅ 扫描多个目录中的照片和视频 / Scan multiple directories for photos and videos
- ✅ 支持多种照片和视频格式 / Support various photo and video formats
  - 照片: JPG, JPEG, PNG, GIF, BMP, TIFF, HEIC, HEIF, WebP
  - 视频: MP4, MOV, AVI, MKV, WMV, FLV, M4V, 3GP
- ✅ 基于文件哈希检测重复文件 / Detect duplicate files based on file hash
- ✅ 清理重复照片 / Remove duplicate photos
- ✅ 从EXIF元数据提取拍摄时间 / Extract capture time from EXIF metadata
- ✅ 按拍摄日期整理照片（YYYY/MM/DD文件夹结构）/ Organize photos by date (YYYY/MM/DD folder structure)
- ✅ 干运行模式，预览操作结果 / Dry run mode to preview operations
- ✅ 详细的日志记录 / Detailed logging

## 安装 / Installation

### 要求 / Requirements

- Python 3.6+
- Pillow (用于EXIF元数据提取 / for EXIF metadata extraction)

### 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

## 使用方法 / Usage

### 基本命令 / Basic Commands

#### 1. 查找重复文件（预览模式）/ Find Duplicates (Preview Mode)

```bash
python photo_manager.py -d /path/to/photos --find-duplicates
```

#### 2. 删除重复文件 / Remove Duplicates

```bash
# 预览要删除的文件 / Preview files to be removed
python photo_manager.py -d /path/to/photos --remove-duplicates

# 实际删除文件 / Actually remove files
python photo_manager.py -d /path/to/photos --remove-duplicates --execute
```

#### 3. 按日期整理照片 / Organize Photos by Date

```bash
# 预览整理结果 / Preview organization
python photo_manager.py -d /path/to/photos --organize -o /path/to/organized

# 实际整理文件 / Actually organize files
python photo_manager.py -d /path/to/photos --organize -o /path/to/organized --execute
```

#### 4. 扫描多个目录 / Scan Multiple Directories

```bash
python photo_manager.py -d /path/to/photos1 /path/to/photos2 /path/to/photos3 --find-duplicates
```

#### 5. 组合操作 / Combined Operations

```bash
# 查找重复文件并按日期整理 / Find duplicates and organize by date
python photo_manager.py -d /path/to/photos --find-duplicates --organize -o /path/to/organized --execute
```

### 命令行参数 / Command Line Options

| 参数 / Option | 说明 / Description |
|--------------|-------------------|
| `-d, --directories` | 要扫描的目录（必需，可以指定多个）/ Directories to scan (required, can specify multiple) |
| `--recursive` | 递归扫描子目录（默认启用）/ Recursively scan subdirectories (default: enabled) |
| `--find-duplicates` | 查找并报告重复文件 / Find and report duplicate files |
| `--remove-duplicates` | 删除重复文件（保留第一个）/ Remove duplicate files (keeps first occurrence) |
| `--organize` | 按日期将文件整理到YYYY/MM/DD文件夹 / Organize files by date into YYYY/MM/DD folders |
| `-o, --output` | 整理文件的输出目录 / Output directory for organized files |
| `--execute` | 实际执行操作（默认为预览模式）/ Actually perform operations (default is dry run) |
| `-v, --verbose` | 启用详细日志 / Enable verbose logging |

## 工作原理 / How It Works

### 重复检测 / Duplicate Detection

该工具使用MD5哈希算法计算文件内容的哈希值。具有相同哈希值的文件被视为重复文件。这种方法：
- 比较文件内容而非文件名
- 即使文件在不同目录中也能检测到重复
- 处理大文件时内存效率高（分块读取）

The tool calculates MD5 hash of file contents. Files with identical hashes are considered duplicates. This approach:
- Compares file contents, not filenames
- Detects duplicates even if files are in different directories
- Memory efficient for large files (reads in chunks)

### 日期提取 / Date Extraction

对于照片，工具会：
1. 首先尝试从EXIF元数据中提取DateTimeOriginal
2. 如果EXIF不可用，则使用文件修改时间
3. 没有日期信息的文件会被放入'unknown'文件夹

For photos, the tool:
1. First tries to extract DateTimeOriginal from EXIF metadata
2. Falls back to file modification time if EXIF is unavailable
3. Files without date info are placed in an 'unknown' folder

### 文件组织 / File Organization

文件按以下层次结构组织：
```
output_directory/
├── 2023/
│   ├── 01/
│   │   ├── 15/
│   │   │   ├── photo1.jpg
│   │   │   └── photo2.jpg
│   │   └── 16/
│   └── 02/
├── 2024/
└── unknown/
```

Files are organized in the following hierarchy:
```
output_directory/
├── 2023/
│   ├── 01/
│   │   ├── 15/
│   │   │   ├── photo1.jpg
│   │   │   └── photo2.jpg
│   │   └── 16/
│   └── 02/
├── 2024/
└── unknown/
```

## 安全特性 / Safety Features

- **预览模式（默认）/ Dry Run Mode (Default)**: 所有操作默认为预览模式。必须使用`--execute`标志才能实际修改文件。/ All operations default to dry run mode. Must use `--execute` flag to actually modify files.
- **日志记录 / Logging**: 详细记录所有操作，便于审查。/ All operations are logged in detail for review.
- **文件名冲突处理 / Filename Conflict Handling**: 如果目标位置已存在同名文件，会自动添加数字后缀。/ Automatically adds numeric suffix if a file with the same name exists at the destination.

## 示例场景 / Example Scenarios

### 场景1：整理老照片 / Scenario 1: Organize Old Photos

假设你有多个文件夹的老照片：/ Suppose you have old photos in multiple folders:
```bash
# 第一步：扫描并查找重复文件 / Step 1: Scan and find duplicates
python photo_manager.py -d ~/Pictures/OldPhotos ~/Pictures/Family ~/Pictures/Vacation --find-duplicates

# 第二步：删除重复文件 / Step 2: Remove duplicates
python photo_manager.py -d ~/Pictures/OldPhotos ~/Pictures/Family ~/Pictures/Vacation --remove-duplicates --execute

# 第三步：按日期整理 / Step 3: Organize by date
python photo_manager.py -d ~/Pictures/OldPhotos ~/Pictures/Family ~/Pictures/Vacation --organize -o ~/Pictures/Organized --execute
```

### 场景2：清理手机备份 / Scenario 2: Clean Up Phone Backups

```bash
# 查找并删除多次备份中的重复照片 / Find and remove duplicates from multiple backups
python photo_manager.py -d ~/PhoneBackup2023 ~/PhoneBackup2024 --remove-duplicates --execute
```

## 许可证 / License

MIT License

## 贡献 / Contributing

欢迎贡献！请随时提交问题或拉取请求。

Contributions are welcome! Please feel free to submit issues or pull requests.
