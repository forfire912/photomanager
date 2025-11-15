# Photo Manager - Project Structure / 项目结构

## 文件清单 / File List

### 核心文件 / Core Files
- `photo_manager.py` - 主程序，CLI 入口点 / Main program, CLI entry point
- `setup.py` - Python 包安装配置 / Python package setup
- `requirements.txt` - 项目依赖 / Project dependencies

### 文档文件 / Documentation Files
- `README.md` - 项目主文档 (中英双语) / Main documentation (bilingual)
- `INSTALL.md` - 安装指南 / Installation guide
- `QUICKSTART.md` - 快速入门 / Quick start guide
- `FEATURES.md` - 功能详解 / Feature details
- `DEMO.md` - 使用演示 / Usage demonstrations
- `TEST_RESULTS.md` - 测试报告 / Test results
- `RELEASE_NOTES.md` - 版本发布说明 / Release notes
- `RELEASE_GUIDE.md` - 维护者发布指南 / Maintainer release guide
- `PROJECT_STRUCTURE.md` - 本文件，项目结构说明 / This file

### 示例和工具 / Examples and Tools
- `examples.py` - 使用示例脚本 / Example usage script

### 配置文件 / Configuration Files
- `.gitignore` - Git 忽略文件配置 / Git ignore configuration
- `MANIFEST.in` - 打包清单 / Distribution manifest
- `LICENSE` - MIT 许可证 / MIT License

## 目录说明 / Directory Description

```
photomanager/
├── photo_manager.py      # 主程序 (297 行)
├── setup.py              # 包安装配置
├── requirements.txt      # 依赖: Pillow
│
├── README.md             # 主文档 (200+ 行，中英双语)
├── INSTALL.md            # 安装指南
├── QUICKSTART.md         # 快速入门
├── FEATURES.md           # 功能详解
├── DEMO.md               # 使用演示
├── TEST_RESULTS.md       # 测试报告
├── RELEASE_NOTES.md      # 发布说明
├── RELEASE_GUIDE.md      # 发布指南
├── PROJECT_STRUCTURE.md  # 项目结构
│
├── examples.py           # 示例脚本
├── LICENSE               # MIT 许可证
├── MANIFEST.in           # 打包清单
└── .gitignore            # Git 配置
```

## 代码统计 / Code Statistics

| 类型 / Type | 文件数 / Files | 行数 / Lines |
|------------|---------------|-------------|
| Python 代码 | 2 | ~350 |
| 文档 | 9 | ~1000 |
| 配置 | 4 | ~100 |
| **总计** | **15** | **~1450** |

## 功能模块 / Functional Modules

### photo_manager.py 模块结构

1. **文件扫描** / File Scanning
   - `scan_directory()` - 扫描目录
   
2. **哈希计算** / Hash Calculation
   - `get_file_hash()` - 计算文件哈希
   
3. **EXIF 提取** / EXIF Extraction
   - `get_exif_date()` - 提取 EXIF 日期
   - `get_file_date()` - 获取文件日期
   
4. **重复检测** / Duplicate Detection
   - `find_duplicates()` - 查找重复文件
   - `remove_duplicates()` - 删除重复文件
   
5. **文件组织** / File Organization
   - `organize_by_date()` - 按日期组织
   
6. **命令行接口** / CLI Interface
   - `main()` - 主入口函数

## 支持的格式 / Supported Formats

### 照片格式 (9 种)
JPG, JPEG, PNG, GIF, BMP, TIFF, HEIC, HEIF, WebP

### 视频格式 (8 种)
MP4, MOV, AVI, MKV, WMV, FLV, M4V, 3GP

**总计:** 17 种媒体格式

## 文档语言 / Documentation Languages

- 🇨🇳 中文 (Chinese)
- 🇬🇧 英文 (English)

所有主要文档都提供中英双语支持。
All major documentation provides bilingual support.

## 版本信息 / Version Info

- **当前版本 / Current Version:** 1.0.0
- **发布日期 / Release Date:** 2025-11-14
- **许可证 / License:** MIT
- **Python 要求 / Python Required:** 3.6+

## 贡献者 / Contributors

- @copilot - 开发与文档 / Development & Documentation
- @forfire912 - 项目维护 / Project Maintenance

---

最后更新 / Last Updated: 2025-11-14
