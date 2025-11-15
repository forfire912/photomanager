# Photo Manager - Quick Start Guide / 快速入门指南

## 快速开始 (5 分钟)

### 1. 安装

```bash
# 克隆仓库
git clone https://github.com/forfire912/photomanager.git
cd photomanager

# 安装
pip install .
```

### 2. 基本使用

#### 查找重复照片
```bash
photo-manager -d ~/Pictures --find-duplicates
```

#### 删除重复照片
```bash
# 先预览
photo-manager -d ~/Pictures --remove-duplicates

# 确认后执行
photo-manager -d ~/Pictures --remove-duplicates --execute
```

#### 按日期整理
```bash
photo-manager -d ~/Pictures --organize -o ~/Organized --execute
```

### 3. 完整工作流

处理多个文件夹的完整示例：

```bash
photo-manager \
  -d ~/Pictures/2020 ~/Pictures/2021 ~/Pictures/手机备份 \
  --find-duplicates \
  --remove-duplicates \
  --organize -o ~/整理后的照片 \
  --execute
```

## Quick Start (5 Minutes)

### 1. Installation

```bash
# Clone repository
git clone https://github.com/forfire912/photomanager.git
cd photomanager

# Install
pip install .
```

### 2. Basic Usage

#### Find Duplicates
```bash
photo-manager -d ~/Pictures --find-duplicates
```

#### Remove Duplicates
```bash
# Preview first
photo-manager -d ~/Pictures --remove-duplicates

# Execute after confirmation
photo-manager -d ~/Pictures --remove-duplicates --execute
```

#### Organize by Date
```bash
photo-manager -d ~/Pictures --organize -o ~/Organized --execute
```

### 3. Complete Workflow

Full example processing multiple folders:

```bash
photo-manager \
  -d ~/Pictures/2020 ~/Pictures/2021 ~/PhoneBackup \
  --find-duplicates \
  --remove-duplicates \
  --organize -o ~/OrganizedPhotos \
  --execute
```

## Common Options / 常用选项

| Option | Description | 说明 |
|--------|-------------|------|
| `-d DIR [DIR ...]` | Directories to scan | 要扫描的目录 |
| `--find-duplicates` | Find duplicate files | 查找重复文件 |
| `--remove-duplicates` | Remove duplicates | 删除重复文件 |
| `--organize` | Organize by date | 按日期整理 |
| `-o DIR` | Output directory | 输出目录 |
| `--execute` | Actually perform actions | 实际执行操作 |
| `-v` | Verbose mode | 详细模式 |

## Important Notes / 重要提示

⚠️ **Safety First / 安全第一**
- 默认为预览模式 / Defaults to preview mode
- 使用 `--execute` 才会实际修改文件 / Use `--execute` to actually modify files
- 建议先备份重要照片 / Backup important photos first

✅ **Best Practices / 最佳实践**
- 先运行不带 `--execute` 查看效果 / Run without `--execute` first to preview
- 使用 `-v` 查看详细信息 / Use `-v` for detailed information
- 整理功能会复制文件，不会移动原文件 / Organize copies files, doesn't move originals

## Need Help? / 需要帮助？

查看完整文档 / See full documentation:
- `README.md` - 完整指南 / Complete guide
- `FEATURES.md` - 功能详解 / Feature details
- `DEMO.md` - 使用示例 / Usage examples
- `photo-manager --help` - 命令行帮助 / CLI help
