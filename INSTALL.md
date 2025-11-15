# Installation Guide / 安装指南

## 方法 1: 通过 pip 安装 (推荐)

```bash
# Clone the repository
git clone https://github.com/forfire912/photomanager.git
cd photomanager

# Install
pip install .
```

安装后，可以直接使用命令：
```bash
photo-manager -d ~/Photos --find-duplicates
```

## 方法 2: 开发模式安装

如果您想修改代码，可以使用开发模式：

```bash
pip install -e .
```

## 方法 3: 直接运行脚本

不需要安装，直接运行：

```bash
# Install dependencies first
pip install -r requirements.txt

# Run the script
python photo_manager.py -d ~/Photos --find-duplicates
```

## 依赖要求

- Python 3.6 或更高版本
- Pillow (用于 EXIF 元数据提取)

## 验证安装

安装后运行以下命令验证：

```bash
photo-manager --help
```

应该看到帮助信息输出。

## 卸载

```bash
pip uninstall photo-manager
```

---

## Method 1: Install via pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/forfire912/photomanager.git
cd photomanager

# Install
pip install .
```

After installation, use the command directly:
```bash
photo-manager -d ~/Photos --find-duplicates
```

## Method 2: Development Installation

If you want to modify the code:

```bash
pip install -e .
```

## Method 3: Run Script Directly

No installation needed:

```bash
# Install dependencies first
pip install -r requirements.txt

# Run the script
python photo_manager.py -d ~/Photos --find-duplicates
```

## Requirements

- Python 3.6 or higher
- Pillow (for EXIF metadata extraction)

## Verify Installation

After installation, run:

```bash
photo-manager --help
```

You should see the help information.

## Uninstall

```bash
pip uninstall photo-manager
```
