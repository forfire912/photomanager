# Windows Executable Build Guide / Windows可执行文件构建指南

## 自动构建 / Automatic Build (Recommended)

### 使用GitHub Actions自动构建和发布 / Using GitHub Actions for Automatic Build and Release

本项目配置了GitHub Actions工作流，可以自动构建Windows可执行文件并发布到GitHub Releases。

The project is configured with a GitHub Actions workflow that automatically builds Windows executables and publishes them to GitHub Releases.

#### 触发自动构建 / Triggering Automatic Build

**方法1：创建版本标签 / Method 1: Create a Version Tag**

```bash
# 创建并推送版本标签 / Create and push version tag
git tag v1.0.0
git push origin v1.0.0
```

这将自动触发构建流程并创建GitHub Release。
This will automatically trigger the build process and create a GitHub Release.

**方法2：手动触发 / Method 2: Manual Trigger**

1. 访问仓库的Actions页面 / Go to the repository's Actions page
2. 选择 "Build and Release Windows Executable" 工作流
3. 点击 "Run workflow" 按钮
4. 选择分支并运行

#### 自动构建产物 / Build Artifacts

构建完成后，将生成以下文件：
After the build completes, the following files will be generated:

- `photo-manager-cli.exe` - 命令行工具 / CLI tool
- `photo-manager-web.exe` - Web界面版本 / Web UI version
- `photo-manager-windows-x64.zip` - 完整打包版本 / Complete package

如果是通过版本标签触发，这些文件会自动发布到GitHub Releases。
If triggered by a version tag, these files will be automatically published to GitHub Releases.

---

## 手动构建 / Manual Build

### 在Windows系统上手动构建 / Manual Build on Windows

#### 前置要求 / Prerequisites

- Windows 10/11 (64-bit)
- Python 3.6 或更高版本 / Python 3.6 or higher
- Git (可选) / Git (optional)

#### 构建步骤 / Build Steps

**方法1：使用构建脚本 / Method 1: Using Build Script**

```bash
# 运行构建脚本 / Run build script
build-windows.bat
```

构建脚本会自动完成以下步骤：
The build script will automatically:
1. 安装依赖 / Install dependencies
2. 构建CLI可执行文件 / Build CLI executable
3. 构建Web UI可执行文件 / Build Web UI executable
4. 创建发布包 / Create release package

**方法2：手动执行命令 / Method 2: Manual Commands**

```bash
# 1. 安装依赖 / Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# 2. 构建CLI版本 / Build CLI version
pyinstaller --onefile --name photo-manager-cli photo_manager.py

# 3. 构建Web UI版本 / Build Web UI version
pyinstaller --onefile --name photo-manager-web --add-data "templates;templates" --add-data "static;static" web_ui.py

# 4. 查看生成的文件 / Check generated files
dir dist
```

#### 使用PyInstaller Spec文件 / Using PyInstaller Spec File

```bash
# 使用spec文件构建 / Build using spec file
pyinstaller photo-manager.spec
```

---

## 构建产物 / Build Output

### 文件位置 / File Locations

构建完成后，可执行文件位于：
After building, executables are located in:

```
dist/
├── photo-manager-cli.exe    # CLI工具 / CLI tool
└── photo-manager-web.exe    # Web界面 / Web UI

release/                      # 发布包 / Release package
├── photo-manager-cli.exe
├── photo-manager-web.exe
├── README.md
├── USAGE_WEB.md
└── LICENSE
```

### 文件大小 / File Sizes

- CLI版本约 20-30 MB / CLI version approximately 20-30 MB
- Web UI版本约 30-40 MB / Web UI version approximately 30-40 MB

---

## 使用可执行文件 / Using the Executables

### CLI工具 / CLI Tool

```bash
# 查找重复文件 / Find duplicates
photo-manager-cli.exe -d C:\Photos --find-duplicates

# 删除重复文件 / Remove duplicates
photo-manager-cli.exe -d C:\Photos --remove-duplicates --execute

# 按日期整理 / Organize by date
photo-manager-cli.exe -d C:\Photos --organize -o C:\Organized --execute

# 查看帮助 / View help
photo-manager-cli.exe --help
```

### Web界面 / Web UI

```bash
# 启动Web界面 / Start Web UI
photo-manager-web.exe

# 然后在浏览器中打开 / Then open in browser
# http://127.0.0.1:5000
```

或者直接双击 `photo-manager-web.exe` 文件。
Or simply double-click the `photo-manager-web.exe` file.

---

## 发布到GitHub Releases / Publishing to GitHub Releases

### 自动发布 / Automatic Publishing

使用版本标签触发GitHub Actions时，会自动创建Release：
When triggered by a version tag, GitHub Actions will automatically create a Release:

```bash
git tag v1.0.0
git push origin v1.0.0
```

### 手动发布 / Manual Publishing

如果手动构建，可以通过以下步骤发布：
If built manually, publish using these steps:

1. 访问仓库的Releases页面 / Go to repository's Releases page
2. 点击 "Create a new release" / Click "Create a new release"
3. 创建新标签 (如 v1.0.0) / Create a new tag (e.g., v1.0.0)
4. 填写发布说明 / Fill in release notes
5. 上传构建的文件：
   - `photo-manager-windows-x64.zip`
   - `photo-manager-cli.exe`
   - `photo-manager-web.exe`
6. 点击 "Publish release" / Click "Publish release"

---

## 故障排查 / Troubleshooting

### 常见问题 / Common Issues

**问题1：构建失败 - 缺少模块**
**Issue 1: Build fails - Missing modules**

```bash
# 解决方案：重新安装依赖 / Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**问题2：Web UI找不到模板文件**
**Issue 2: Web UI cannot find template files**

```bash
# 确保使用--add-data参数 / Ensure using --add-data parameter
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" web_ui.py
```

**问题3：可执行文件被杀毒软件拦截**
**Issue 3: Executable blocked by antivirus**

这是PyInstaller打包的常见问题。解决方案：
This is a common issue with PyInstaller. Solutions:
- 将可执行文件添加到杀毒软件白名单 / Add executable to antivirus whitelist
- 从源码运行Python脚本 / Run Python scripts from source

**问题4：GitHub Actions构建失败**
**Issue 4: GitHub Actions build fails**

检查Actions日志，常见原因：
Check Actions logs, common causes:
- 依赖版本冲突 / Dependency version conflicts
- 权限问题 / Permission issues
- 网络问题 / Network issues

---

## 版本管理 / Version Management

### 版本号规范 / Version Numbering

使用语义化版本 / Use Semantic Versioning:
- `v1.0.0` - 主要版本 / Major version
- `v1.1.0` - 次要版本 / Minor version
- `v1.1.1` - 补丁版本 / Patch version

### 发布检查清单 / Release Checklist

发布新版本前检查：
Before releasing a new version:

- [ ] 所有测试通过 / All tests pass
- [ ] 文档已更新 / Documentation updated
- [ ] 更新版本号 / Version number updated
- [ ] 创建变更日志 / Changelog created
- [ ] 本地构建测试 / Local build tested
- [ ] GitHub Actions工作流测试 / GitHub Actions workflow tested

---

## 技术细节 / Technical Details

### PyInstaller配置 / PyInstaller Configuration

- `--onefile`: 打包为单个可执行文件 / Package as single executable
- `--name`: 指定输出文件名 / Specify output filename
- `--add-data`: 包含数据文件 / Include data files
- `--console`: 显示控制台窗口 / Show console window
- `--icon`: 添加图标（可选）/ Add icon (optional)

### GitHub Actions工作流 / GitHub Actions Workflow

工作流文件位置：`.github/workflows/build-release.yml`
Workflow file location: `.github/workflows/build-release.yml`

触发条件 / Trigger conditions:
- 推送版本标签 / Push version tag: `git push origin v*`
- 手动触发 / Manual trigger: workflow_dispatch

---

## 参考资源 / References

- [PyInstaller Documentation](https://pyinstaller.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Semantic Versioning](https://semver.org/)
- [项目主页 / Project Homepage](https://github.com/forfire912/photomanager)
