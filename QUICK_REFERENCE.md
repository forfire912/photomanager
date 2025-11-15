# 快速参考：Windows可执行文件发布 / Quick Reference: Windows Executable Release

## 🎯 一键发布 / One-Command Release

```bash
# 创建并推送标签，自动触发构建和发布
git tag -a v1.0.0 -m "Release version 1.0.0" && git push origin v1.0.0
```

⏱️ **构建时间 / Build Time:** 5-10 分钟 / minutes

## 📥 发布结果 / Release Output

构建完成后，在 GitHub Releases 页面可以下载：

After build completes, download from GitHub Releases page:

- 🎁 **photo-manager-windows-x64.zip** - 完整包（推荐）/ Complete package (Recommended)
- 💻 **photo-manager-cli.exe** - 命令行工具 / CLI tool
- 🌐 **photo-manager-web.exe** - Web界面 / Web UI

## 📚 详细文档 / Detailed Docs

| 文档 / Document | 说明 / Description |
|----------------|-------------------|
| [TRIGGER_RELEASE.md](TRIGGER_RELEASE.md) | 完整的发布触发指南 / Complete release guide |
| [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) | 实现总结和说明 / Implementation summary |
| [BUILD.md](BUILD.md) | 构建详细说明 / Build details |
| [RELEASE_GUIDE.md](RELEASE_GUIDE.md) | 发布流程 / Release process |

## 🚀 使用可执行文件 / Using Executables

### CLI工具 / CLI Tool
```bash
# 查找重复 / Find duplicates
photo-manager-cli.exe -d C:\Photos --find-duplicates

# 删除重复 / Remove duplicates
photo-manager-cli.exe -d C:\Photos --remove-duplicates --execute

# 按日期整理 / Organize by date
photo-manager-cli.exe -d C:\Photos --organize -o C:\Organized --execute
```

### Web界面 / Web UI
```bash
# 双击运行 / Double-click to run
photo-manager-web.exe

# 然后访问 / Then visit
http://127.0.0.1:5000
```

## 🔧 故障排查 / Troubleshooting

| 问题 / Issue | 解决方案 / Solution |
|-------------|-------------------|
| 构建失败 / Build fails | 查看 GitHub Actions 日志 / Check Actions logs |
| 无法创建Release / Can't create release | 检查仓库权限设置 / Check repository permissions |
| 标签推送失败 / Tag push fails | 确认Git配置正确 / Verify Git configuration |

详细故障排查请参考 [TRIGGER_RELEASE.md](TRIGGER_RELEASE.md#故障排查--troubleshooting)

## 📞 获取帮助 / Get Help

- 📖 查看文档 / Read docs: TRIGGER_RELEASE.md, BUILD.md
- 🐛 提交问题 / Report issues: [GitHub Issues](https://github.com/forfire912/photomanager/issues)

---

**快速链接 / Quick Links:**
- 🚀 [Actions 页面](https://github.com/forfire912/photomanager/actions)
- 📦 [Releases 页面](https://github.com/forfire912/photomanager/releases)
- 📚 [完整文档](README.md)
