# Photo Manager / 照片管理工具

一个用于整理照片和视频的工具，可以按拍摄时间排序并清理重复文件。

A tool for organizing photos and videos by shooting time and removing duplicates.

## 功能特点 / Features

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

## 许可证 / License

MIT License

## 贡献 / Contributing

欢迎提交问题和拉取请求 / Issues and pull requests are welcome!
