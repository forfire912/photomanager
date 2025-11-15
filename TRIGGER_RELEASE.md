# 触发Windows可执行文件编译和发布 / Trigger Windows Executable Build and Release

本文档说明如何触发自动构建Windows可执行程序并发布到GitHub Releases。

This document explains how to trigger the automatic build of Windows executables and publish to GitHub Releases.

## 🎯 目标 / Objective

自动编译生成以下Windows可执行文件并发布：
- `photo-manager-cli.exe` - 命令行工具
- `photo-manager-web.exe` - Web界面版本
- `photo-manager-windows-x64.zip` - 完整打包版本

Automatically build and publish the following Windows executables:
- `photo-manager-cli.exe` - CLI tool
- `photo-manager-web.exe` - Web UI version
- `photo-manager-windows-x64.zip` - Complete package

---

## 📋 前置条件 / Prerequisites

✅ 所有代码已合并到主分支 / All code merged to main branch
✅ GitHub Actions工作流已配置 / GitHub Actions workflow configured
✅ 仓库具有发布权限 / Repository has release permissions

---

## 🚀 方法一：通过Git标签触发（推荐）/ Method 1: Trigger via Git Tag (Recommended)

这是最推荐的方法，会自动构建并创建GitHub Release。

This is the recommended method that automatically builds and creates a GitHub Release.

### 步骤 / Steps:

**1. 确保在主分支上 / Ensure on main branch:**
```bash
git checkout main
git pull origin main
```

**2. 创建版本标签 / Create version tag:**
```bash
# 创建标签 (例如 v1.0.0) / Create tag (e.g., v1.0.0)
git tag -a v1.0.0 -m "Release version 1.0.0 - Initial release with Windows executables"

# 查看标签 / View tag
git tag -l
```

**3. 推送标签到GitHub / Push tag to GitHub:**
```bash
git push origin v1.0.0
```

**4. 监控构建过程 / Monitor build process:**
- 访问仓库的 Actions 页面 / Go to repository's Actions page
- 查看 "Build and Release Windows Executable" 工作流
- 等待构建完成（大约5-10分钟）/ Wait for build to complete (about 5-10 minutes)

**5. 验证发布 / Verify release:**
- 访问仓库的 Releases 页面 / Go to repository's Releases page
- 应该能看到新创建的 v1.0.0 release / Should see the new v1.0.0 release
- 验证包含以下文件：
  - `photo-manager-windows-x64.zip`
  - `photo-manager-cli.exe`
  - `photo-manager-web.exe`

---

## 🔧 方法二：手动触发工作流 / Method 2: Manual Workflow Trigger

如果只想测试构建而不创建正式发布，可以手动触发。

Use this if you just want to test the build without creating an official release.

### 步骤 / Steps:

**1. 访问GitHub Actions页面 / Go to GitHub Actions page:**
- 打开 `https://github.com/forfire912/photomanager/actions`
- 点击 "Build and Release Windows Executable" 工作流

**2. 手动运行 / Manual run:**
- 点击右上角的 "Run workflow" 按钮
- 选择分支（通常是 main）
- 点击绿色的 "Run workflow" 按钮

**3. 下载构建产物 / Download build artifacts:**
- 等待构建完成
- 在工作流运行页面，找到 "Artifacts" 部分
- 下载 `windows-executables` 压缩包

**注意：** 手动触发不会创建GitHub Release，只会生成构建产物。

**Note:** Manual trigger will NOT create a GitHub Release, only build artifacts.

---

## 🏷️ 版本号规范 / Version Numbering

使用语义化版本控制 / Use Semantic Versioning:

- **v1.0.0** - 主要版本（重大变更）/ Major version (breaking changes)
- **v1.1.0** - 次要版本（新功能）/ Minor version (new features)
- **v1.0.1** - 补丁版本（bug修复）/ Patch version (bug fixes)

### 示例 / Examples:

```bash
# 首次发布 / Initial release
git tag -a v1.0.0 -m "Initial release"

# 添加新功能 / Add new feature
git tag -a v1.1.0 -m "Add batch processing feature"

# Bug修复 / Bug fix
git tag -a v1.0.1 -m "Fix duplicate detection issue"
```

---

## 🔍 故障排查 / Troubleshooting

### 问题1：推送标签失败 / Issue 1: Tag push failed

```bash
# 检查是否有权限 / Check permissions
git remote -v

# 确保已登录GitHub / Ensure logged in to GitHub
git config user.name
git config user.email
```

### 问题2：构建失败 / Issue 2: Build failed

**检查Actions日志 / Check Actions logs:**
1. 访问 Actions 页面
2. 点击失败的工作流运行
3. 查看详细日志

**常见原因 / Common causes:**
- 依赖安装失败 / Dependency installation failed
- PyInstaller编译错误 / PyInstaller compilation error
- 文件路径问题 / File path issues

### 问题3：Release创建失败 / Issue 3: Release creation failed

**检查权限 / Check permissions:**
- 确保仓库设置中启用了 Actions 的写权限
- Settings → Actions → General → Workflow permissions → Read and write permissions

### 问题4：删除错误的标签 / Issue 4: Delete wrong tag

```bash
# 删除本地标签 / Delete local tag
git tag -d v1.0.0

# 删除远程标签 / Delete remote tag
git push origin :refs/tags/v1.0.0
```

---

## 📊 构建时间估计 / Build Time Estimate

- **安装依赖 / Install dependencies:** ~1-2 分钟 / minutes
- **构建CLI可执行文件 / Build CLI executable:** ~1-2 分钟 / minutes
- **构建Web UI可执行文件 / Build Web UI executable:** ~2-3 分钟 / minutes
- **创建压缩包 / Create archive:** ~30 秒 / seconds
- **上传到Release / Upload to Release:** ~1 分钟 / minute

**总计 / Total:** 约 5-10 分钟 / Approximately 5-10 minutes

---

## 🎓 最佳实践 / Best Practices

### 发布前检查清单 / Pre-Release Checklist

- [ ] 所有测试通过 / All tests pass
- [ ] 文档已更新 / Documentation updated
- [ ] RELEASE_NOTES.md 已更新 / RELEASE_NOTES.md updated
- [ ] setup.py 版本号正确 / setup.py version number correct
- [ ] 本地测试构建成功 / Local build test successful
- [ ] 代码已推送到main分支 / Code pushed to main branch

### 发布后验证 / Post-Release Verification

- [ ] Release页面显示正确 / Release page displays correctly
- [ ] 所有文件可下载 / All files downloadable
- [ ] 下载并测试可执行文件 / Download and test executables
- [ ] 发布说明准确 / Release notes accurate

---

## 📞 需要帮助？/ Need Help?

如遇到问题：
1. 查看 [BUILD.md](BUILD.md) 了解构建细节
2. 查看 [RELEASE_GUIDE.md](RELEASE_GUIDE.md) 了解发布流程
3. 在 GitHub Issues 提问

For issues:
1. See [BUILD.md](BUILD.md) for build details
2. See [RELEASE_GUIDE.md](RELEASE_GUIDE.md) for release process
3. Ask in GitHub Issues

---

## 🎉 快速开始示例 / Quick Start Example

假设你准备发布 v1.0.0 版本：

Assuming you're ready to release v1.0.0:

```bash
# 1. 切换到主分支并更新
git checkout main
git pull origin main

# 2. 创建并推送标签
git tag -a v1.0.0 -m "Release version 1.0.0 - Photo Manager with Windows executables"
git push origin v1.0.0

# 3. 访问 Actions 页面监控构建
# https://github.com/forfire912/photomanager/actions

# 4. 构建完成后，访问 Releases 页面
# https://github.com/forfire912/photomanager/releases

# 5. 下载并测试可执行文件
# 下载 photo-manager-windows-x64.zip
# 解压并运行 photo-manager-cli.exe 或 photo-manager-web.exe
```

---

**准备者 / Prepared by:** GitHub Copilot  
**日期 / Date:** 2025-11-15  
**版本 / Version:** 1.0
