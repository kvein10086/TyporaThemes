#!/usr/bin/env python3
"""
测试字体下载功能的脚本
"""

import json
import os
import sys
from check_font_updates import get_release_info

def test_font_check(repo, font_name):
    """测试字体检查功能"""
    print(f"测试 {repo} 仓库的 {font_name} 字体...")
    
    # 获取发布信息
    release_info = get_release_info(repo, font_name)
    
    if not release_info:
        print(f"❌ 无法获取 {repo} 的发布信息")
        return False
    
    print(f"✅ 成功获取发布信息:")
    print(f"  版本: {release_info['version']}")
    print(f"  发布名称: {release_info['release_name']}")
    print(f"  发布时间: {release_info['published_at']}")
    
    if 'font' in release_info and release_info['font']:
        font_info = release_info['font']
        print(f"✅ 字体信息:")
        print(f"  文件名: {font_info['name']}")
        print(f"  下载链接: {font_info['download_url']}")
        print(f"  文件大小: {font_info['size']:,} 字节")
        print(f"  下载次数: {font_info['download_count']}")
        return True
    else:
        print(f"❌ 未找到字体信息")
        return False

def main():
    """主函数"""
    print("开始测试字体下载功能...\n")
    
    # 测试 LXGWNeoZhiSong
    zhisong_success = test_font_check("lxgw/LxgwNeoZhiSong", "LXGWNeoZhiSongPlus.ttf")
    
    print("\n" + "="*50 + "\n")
    
    # 测试 LXGWNeoXiHei
    xihei_success = test_font_check("lxgw/LxgwNeoXiHei", "LXGWNeoXiHeiPlus.ttf")
    
    print("\n" + "="*50 + "\n")
    
    # 总结
    print("测试结果总结:")
    if zhisong_success:
        print("✅ LXGWNeoZhiSong: 正常")
    else:
        print("❌ LXGWNeoZhiSong: 失败")
    
    if xihei_success:
        print("✅ LXGWNeoXiHei: 正常")
    else:
        print("❌ LXGWNeoXiHei: 失败")
    
    if zhisong_success and xihei_success:
        print("\n🎉 所有测试通过!")
        return 0
    else:
        print("\n💥 部分测试失败!")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 