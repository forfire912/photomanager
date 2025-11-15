#!/bin/bash
# Example usage script for Photo Manager / 照片管理工具使用示例

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Photo Manager Example Usage / 照片管理工具使用示例 ===${NC}\n"

echo -e "${GREEN}1. Basic usage - organize photos from one directory / 基本用法 - 整理一个目录中的照片:${NC}"
echo "   python photomanager.py /path/to/photos -o /path/to/organized"
echo ""

echo -e "${GREEN}2. Multiple source directories / 多个源目录:${NC}"
echo "   python photomanager.py /path/to/photos1 /path/to/photos2 /path/to/photos3 -o /path/to/organized"
echo ""

echo -e "${GREEN}3. Preview mode (dry-run) / 预览模式:${NC}"
echo "   python photomanager.py /path/to/photos -o /path/to/organized --dry-run"
echo ""

echo -e "${GREEN}4. Keep duplicates / 保留重复文件:${NC}"
echo "   python photomanager.py /path/to/photos -o /path/to/organized --no-remove-duplicates"
echo ""

echo -e "${GREEN}5. Verbose logging / 详细日志:${NC}"
echo "   python photomanager.py /path/to/photos -o /path/to/organized -v"
echo ""

echo -e "${GREEN}6. Combined options / 组合选项:${NC}"
echo "   python photomanager.py /path/to/photos1 /path/to/photos2 -o /path/to/organized --dry-run -v"
echo ""

echo -e "${BLUE}For more information, see README.md or run: python photomanager.py --help${NC}"
echo -e "${BLUE}更多信息请查看 README.md 或运行: python photomanager.py --help${NC}"
