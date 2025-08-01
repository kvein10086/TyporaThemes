#!/bin/bash

# 字体同步工作流修复脚本
# 用于解决 GitHub Actions 权限问题

echo "🔄 字体同步工作流修复脚本"
echo "================================"

# 检查当前工作流文件
if [ -f ".github/workflows/font-sync.yml" ]; then
    echo "✅ 发现主工作流文件: .github/workflows/font-sync.yml"
    
    # 备份原文件
    cp .github/workflows/font-sync.yml .github/workflows/font-sync.yml.backup
    echo "📋 已备份原工作流文件"
    
    # 检查是否有本地版本
    if [ -f ".github/workflows/font-sync-local.yml" ]; then
        echo "✅ 发现本地版本工作流文件"
        
        echo ""
        echo "请选择修复方案："
        echo "1. 修改仓库设置（推荐）- 允许使用外部 Actions"
        echo "2. 使用本地版本工作流 - 不使用外部 Actions"
        echo ""
        read -p "请输入选择 (1 或 2): " choice
        
        case $choice in
            1)
                echo ""
                echo "📝 请按照以下步骤修改仓库设置："
                echo "1. 访问: https://github.com/kvein10086/TyporaThemes-Dissertation/settings"
                echo "2. 进入 Actions → General"
                echo "3. 将 'Actions permissions' 改为 'Allow all actions and reusable workflows'"
                echo "4. 保存设置"
                echo ""
                echo "修改完成后，原工作流应该可以正常运行。"
                ;;
            2)
                echo ""
                echo "🔄 切换到本地版本工作流..."
                mv .github/workflows/font-sync-local.yml .github/workflows/font-sync.yml
                echo "✅ 已切换到本地版本工作流"
                echo "📝 本地版本特点："
                echo "   - 不使用外部 Actions"
                echo "   - 手动设置 Python 环境"
                echo "   - 功能完全相同"
                ;;
            *)
                echo "❌ 无效选择"
                exit 1
                ;;
        esac
    else
        echo "❌ 未找到本地版本工作流文件"
        echo "请确保 .github/workflows/font-sync-local.yml 文件存在"
    fi
else
    echo "❌ 未找到主工作流文件"
    echo "请确保 .github/workflows/font-sync.yml 文件存在"
fi

echo ""
echo "📋 修复完成！"
echo "现在可以尝试运行工作流了。" 