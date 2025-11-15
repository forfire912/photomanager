# Release Guide for Maintainers / 维护者发布指南

## 准备工作 / Preparation

✅ 所有代码已准备就绪 / All code is ready
✅ 版本 1.0.0 已配置 / Version 1.0.0 configured
✅ 测试已完成 / Testing completed
✅ 文档已完善 / Documentation complete

## 发布步骤 / Release Steps

### 1️⃣ 合并 PR 到 main 分支 / Merge PR to Main Branch

在 GitHub 上：
1. 进入 Pull Request 页面
2. 检查所有测试通过
3. 点击 "Merge pull request"
4. 选择 "Squash and merge" 或 "Create a merge commit"
5. 确认合并

On GitHub:
1. Go to Pull Request page
2. Verify all tests pass
3. Click "Merge pull request"
4. Choose "Squash and merge" or "Create a merge commit"
5. Confirm merge

### 2️⃣ 创建 GitHub Release / Create GitHub Release

#### 方法 A: 通过 GitHub 网页界面 / Via GitHub Web Interface

1. 进入仓库主页 / Go to repository homepage
2. 点击 "Releases" → "Draft a new release" / Click "Releases" → "Draft a new release"
3. 填写以下信息 / Fill in the following:

   **Tag version:** `v1.0.0`
   
   **Release title:** `Photo Manager v1.0.0 - 照片管理工具首次发布`
   
   **Description:** (复制以下内容 / Copy the following)

```markdown
# Photo Manager v1.0.0 - Initial Release

## 🎉 首次发布 / First Release

完整实现照片管理工具的所有核心功能。
Full implementation of all core photo management features.

## ✨ 核心功能 / Core Features

- ✅ 多目录扫描 / Multi-directory scanning
- ✅ 16+ 种格式支持 / 16+ format support
- ✅ 重复文件检测 / Duplicate detection
- ✅ 安全删除重复文件 / Safe duplicate removal
- ✅ 按日期整理 (YYYY/MM/DD) / Date-based organization
- ✅ 完整中文支持 / Full Chinese support

## 📦 安装 / Installation

### 方法 1: 通过 pip 安装
```bash
git clone https://github.com/forfire912/photomanager.git
cd photomanager
pip install .
```

### 方法 2: 直接运行
```bash
pip install -r requirements.txt
python photo_manager.py -d ~/Photos --find-duplicates
```

## 🚀 快速开始 / Quick Start

```bash
# 安装后使用命令
photo-manager -d ~/Photos --find-duplicates

# 删除重复文件
photo-manager -d ~/Photos --remove-duplicates --execute

# 按日期整理
photo-manager -d ~/Photos --organize -o ~/Organized --execute
```

## 📚 文档 / Documentation

- [README.md](README.md) - 完整用户指南
- [INSTALL.md](INSTALL.md) - 安装指南
- [QUICKSTART.md](QUICKSTART.md) - 快速入门
- [FEATURES.md](FEATURES.md) - 功能详解
- [DEMO.md](DEMO.md) - 使用演示
- [TEST_RESULTS.md](TEST_RESULTS.md) - 测试报告

## 🧪 测试状态 / Test Status

✅ 所有核心功能测试通过 / All core features tested
✅ 中文支持验证通过 / Chinese support verified
✅ 性能测试通过 / Performance tested
✅ 安全扫描通过 (0 漏洞) / Security scan passed (0 vulnerabilities)

## 📋 完整更新日志 / Full Changelog

详见 [RELEASE_NOTES.md](RELEASE_NOTES.md)

**完整提交历史 / Full Commit History:** https://github.com/forfire912/photomanager/commits/main
```

4. 上传资产文件 (可选) / Upload assets (optional):
   - 可以添加 README.pdf 或其他文档
   - Can add README.pdf or other documentation

5. 勾选 "Set as the latest release" / Check "Set as the latest release"
6. 点击 "Publish release" / Click "Publish release"

#### 方法 B: 通过命令行 / Via Command Line

如果安装了 GitHub CLI (gh):

```bash
# 切换到 main 分支
git checkout main
git pull

# 创建 release
gh release create v1.0.0 \
  --title "Photo Manager v1.0.0 - 照片管理工具首次发布" \
  --notes-file RELEASE_NOTES.md \
  --latest
```

### 3️⃣ 验证发布 / Verify Release

1. 检查 Release 页面是否正确显示 / Check Release page displays correctly
2. 验证下载链接工作 / Verify download links work
3. 测试从 release 安装 / Test installation from release:

```bash
# 下载并安装
git clone --branch v1.0.0 https://github.com/forfire912/photomanager.git
cd photomanager
pip install .
photo-manager --help
```

### 4️⃣ 公告发布 / Announce Release

可以在以下地方宣布新版本发布：
- GitHub Discussions
- 项目 README
- 社交媒体

## 🔄 后续版本发布 / Future Releases

对于未来的版本更新：

1. 更新 `setup.py` 中的版本号
2. 更新 `RELEASE_NOTES.md`
3. 创建新的 PR
4. 合并后重复上述步骤，使用新的版本号

## 📞 需要帮助？/ Need Help?

如有问题，请在 GitHub Issues 中提问。
For questions, please ask in GitHub Issues.

---

**准备者:** @copilot  
**日期:** 2025-11-14  
**版本:** 1.0.0
