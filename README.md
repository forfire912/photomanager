# Photo Manager / 照片管理工具

一个用于整理照片和视频的工具，可以按拍摄时间排序并清理重复文件。

A tool for organizing photos and videos by shooting time and removing duplicates.

## 功能特点 / Features

- ✅ **Web可视化界面** / **Web Visualization Interface** - Easy-to-use web UI for managing photos
- ✅ 扫描多个目录中的照片和视频 / Scan photos and videos from multiple directories
- ✅ 支持多种格式 / Support multiple formats:
  - 图片 / Images: JPG, JPEG, PNG, GIF, BMP, TIFF, HEIC, WebP
  - 视频 / Videos: MP4, MOV, AVI, MKV, WMV, FLV, M4V, 3GP
- ✅ 按拍摄时间排序整理 / Organize by shooting time (from EXIF data)
- ✅ 自动检测并清理重复照片 / Automatically detect and remove duplicate photos
- ✅ 创建按日期分类的目录结构 / Create directory structure organized by date (YYYY/YYYY-MM/YYYY-MM-DD/)
- ✅ 预览模式（dry-run）/ Dry-run mode for preview
- ✅ 详细的日志输出 / Detailed logging

## 安装 / Installation

1. 克隆仓库 / Clone the repository:
```bash
git clone https://github.com/forfire912/photomanager.git
cd photomanager
```

2. 安装依赖 / Install dependencies:
```bash
pip install -r requirements.txt
```

## 使用方法 / Usage

### Web界面 / Web Interface (推荐 / Recommended)

启动Web可视化界面 / Start the web visualization interface:

```bash
python web_ui.py
```

然后在浏览器中打开 / Then open in your browser: `http://127.0.0.1:5000`

Web界面提供了友好的可视化操作界面，包括：
- 📂 扫描目录并查看文件列表
- 🔍 查找和查看重复文件
- 🗑️ 预览或执行删除重复文件
- 📅 按日期整理文件

The web interface provides a user-friendly visualization with:
- 📂 Scan directories and view file lists
- 🔍 Find and view duplicate files
- 🗑️ Preview or execute duplicate removal
- 📅 Organize files by date

![Web UI Screenshot](https://github.com/user-attachments/assets/5e7b22cf-6ea1-48bd-8d5b-973157aa4433)

### 命令行界面 / Command Line Interface

### 基本用法 / Basic Usage

```bash
python photomanager.py /path/to/source/dir -o /path/to/output/dir
```

### 多个源目录 / Multiple source directories

```bash
python photomanager.py /path/to/dir1 /path/to/dir2 /path/to/dir3 -o /path/to/output
```

### 预览模式（不实际移动文件）/ Dry-run mode (preview only)

```bash
python photomanager.py /path/to/source -o /path/to/output --dry-run
```

### 保留重复文件 / Keep duplicates

```bash
python photomanager.py /path/to/source -o /path/to/output --no-remove-duplicates
```

### 详细日志 / Verbose logging

```bash
python photomanager.py /path/to/source -o /path/to/output -v
```

## 命令行参数 / Command-line Arguments

| 参数 / Argument | 说明 / Description |
|----------------|-------------------|
| `source_dirs` | 源目录（必需，可指定多个）/ Source directories (required, multiple allowed) |
| `-o, --output` | 输出目录（必需）/ Output directory (required) |
| `--no-remove-duplicates` | 不删除重复文件 / Do not remove duplicate files |
| `--dry-run` | 预览模式，不实际移动文件 / Preview mode, do not actually move files |
| `-v, --verbose` | 详细日志 / Verbose logging |

## 输出目录结构 / Output Directory Structure

文件将按以下结构组织 / Files will be organized in the following structure:

```
output/
├── 2023/
│   ├── 2023-01/
│   │   ├── 2023-01-15/
│   │   │   ├── photo1.jpg
│   │   │   └── photo2.jpg
│   │   └── 2023-01-20/
│   │       └── video1.mp4
│   └── 2023-12/
│       └── 2023-12-25/
│           └── photo3.jpg
└── 2024/
    └── 2024-11/
        └── 2024-11-14/
            └── photo4.jpg
```

## 工作原理 / How It Works

1. **扫描文件** / **Scan Files**: 递归扫描所有指定的源目录，查找支持的照片和视频文件 / Recursively scan all specified source directories for supported photo and video files

2. **检测重复** / **Detect Duplicates**: 使用 SHA256 哈希算法检测重复文件 / Use SHA256 hash algorithm to detect duplicate files

3. **提取拍摄时间** / **Extract Shooting Time**: 
   - 优先从 EXIF 数据中读取拍摄时间 / Prefer shooting time from EXIF data
   - 如果没有 EXIF 数据，使用文件修改时间 / Fall back to file modification time if no EXIF data

4. **整理文件** / **Organize Files**: 按照日期创建目录结构并复制文件 / Create directory structure by date and copy files

5. **生成报告** / **Generate Report**: 输出整理结果统计 / Output organization statistics

## 注意事项 / Notes

- 程序会复制文件而不是移动，原始文件保持不变 / The program copies files instead of moving them, original files remain unchanged
- 建议先使用 `--dry-run` 参数预览结果 / Recommended to use `--dry-run` first to preview results
- 确保输出目录有足够的存储空间 / Ensure output directory has enough storage space
- 重复文件检测基于文件内容（SHA256），而非文件名 / Duplicate detection is based on file content (SHA256), not filename
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

### 方法 1: 通过 pip 安装 (推荐) / Method 1: Install via pip (Recommended)

```bash
# 克隆仓库 / Clone repository
git clone https://github.com/forfire912/photomanager.git
cd photomanager

# 安装 / Install
pip install .
```

安装后可以直接使用命令 / After installation, use command directly:
```bash
photo-manager -d ~/Photos --find-duplicates
```

### 方法 2: 直接运行脚本 / Method 2: Run Script Directly

```bash
# 安装依赖 / Install dependencies
pip install -r requirements.txt

# 运行脚本 / Run script
python photo_manager.py -d /path/to/photos --find-duplicates
```

### 要求 / Requirements

- Python 3.6+
- Pillow (用于EXIF元数据提取 / for EXIF metadata extraction)

详细安装说明请查看 [INSTALL.md](INSTALL.md) / See [INSTALL.md](INSTALL.md) for detailed installation instructions.

## 使用方法 / Usage

### 基本命令 / Basic Commands

**注意**: 如果已通过 pip 安装，使用 `photo-manager` 命令。否则使用 `python photo_manager.py`  
**Note**: If installed via pip, use `photo-manager` command. Otherwise use `python photo_manager.py`

#### 1. 查找重复文件（预览模式）/ Find Duplicates (Preview Mode)

```bash
photo-manager -d /path/to/photos --find-duplicates
# 或 / Or: python photo_manager.py -d /path/to/photos --find-duplicates
```

#### 2. 删除重复文件 / Remove Duplicates

```bash
# 预览要删除的文件 / Preview files to be removed
photo-manager -d /path/to/photos --remove-duplicates

# 实际删除文件 / Actually remove files
photo-manager -d /path/to/photos --remove-duplicates --execute
```

#### 3. 按日期整理照片 / Organize Photos by Date

```bash
# 预览整理结果 / Preview organization
photo-manager -d /path/to/photos --organize -o /path/to/organized

# 实际整理文件 / Actually organize files
photo-manager -d /path/to/photos --organize -o /path/to/organized --execute
```

#### 4. 扫描多个目录 / Scan Multiple Directories

```bash
photo-manager -d /path/to/photos1 /path/to/photos2 /path/to/photos3 --find-duplicates
```

#### 5. 组合操作 / Combined Operations

```bash
# 查找重复文件并按日期整理 / Find duplicates and organize by date
photo-manager -d /path/to/photos --find-duplicates --organize -o /path/to/organized --execute
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
photo-manager -d ~/Pictures/OldPhotos ~/Pictures/Family ~/Pictures/Vacation --find-duplicates

# 第二步：删除重复文件 / Step 2: Remove duplicates
photo-manager -d ~/Pictures/OldPhotos ~/Pictures/Family ~/Pictures/Vacation --remove-duplicates --execute

# 第三步：按日期整理 / Step 3: Organize by date
photo-manager -d ~/Pictures/OldPhotos ~/Pictures/Family ~/Pictures/Vacation --organize -o ~/Pictures/Organized --execute
```

### 场景2：清理手机备份 / Scenario 2: Clean Up Phone Backups

```bash
# 查找并删除多次备份中的重复照片 / Find and remove duplicates from multiple backups
photo-manager -d ~/PhoneBackup2023 ~/PhoneBackup2024 --remove-duplicates --execute
```

## 许可证 / License

MIT License

## 贡献 / Contributing

欢迎提交问题和拉取请求 / Issues and pull requests are welcome!

Contributions are welcome! Please feel free to submit issues or pull requests.
