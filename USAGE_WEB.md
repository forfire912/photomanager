# Web UI Usage Guide / Web界面使用指南

## 启动Web界面 / Starting the Web Interface

```bash
python web_ui.py
```

然后在浏览器中打开 / Then open in your browser:
```
http://127.0.0.1:5000
```

## 使用步骤 / Usage Steps

### Step 1: 扫描目录 / Scan Directories
1. 在文本框中输入要扫描的目录路径（每行一个）
2. 勾选"递归扫描子目录"选项（默认启用）
3. 点击"Scan Directories"按钮
4. 查看扫描结果，包括找到的文件总数

1. Enter directory paths to scan (one per line) in the text box
2. Check "Scan subdirectories recursively" option (enabled by default)
3. Click "Scan Directories" button
4. View scan results including total files found

### Step 2: 查找重复文件 / Find Duplicates
1. 在扫描完成后，点击"Find Duplicates"按钮
2. 查看重复文件组，每组显示所有重复的文件路径
3. 系统会显示找到的重复文件总数

1. After scanning, click "Find Duplicates" button
2. View duplicate file groups showing all duplicate file paths
3. See total number of duplicate files found

### Step 3: 删除重复文件（可选）/ Remove Duplicates (Optional)
1. 点击"Preview Removal"预览将要删除的文件
2. 确认无误后，点击"Execute Removal"执行删除操作
3. 每组重复文件会保留第一个，删除其他副本

1. Click "Preview Removal" to preview files to be removed
2. After confirmation, click "Execute Removal" to delete files
3. First file in each group is kept, others are removed

### Step 4: 按日期整理 / Organize by Date
1. 输入输出目录路径
2. 点击"Preview Organization"预览整理结果
3. 确认无误后，点击"Execute Organization"执行整理操作
4. 文件会被复制到按日期分类的目录结构中（YYYY/MM/DD）

1. Enter output directory path
2. Click "Preview Organization" to preview organization
3. After confirmation, click "Execute Organization" to organize
4. Files will be copied to date-organized structure (YYYY/MM/DD)

## 安全提示 / Safety Tips

- ⚠️ 所有操作默认为预览模式，不会实际修改文件
- ⚠️ 必须点击"Execute"按钮才会真正执行操作
- ⚠️ 建议先使用预览功能，确认无误后再执行

- ⚠️ All operations default to preview mode, no files are modified
- ⚠️ Must click "Execute" buttons to actually perform operations
- ⚠️ Recommended to use preview first, then execute after confirmation

## 界面截图 / Screenshot

![Web UI](https://github.com/user-attachments/assets/5e7b22cf-6ea1-48bd-8d5b-973157aa4433)
