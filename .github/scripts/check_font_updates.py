#!/usr/bin/env python3
"""
检查字体更新的脚本
用于检查GitHub仓库中指定字体的最新版本
"""

import argparse
import json
import re
import requests
from urllib.parse import urljoin
import sys


def get_latest_release(repo):
    """获取仓库的最新发布版本"""
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    
    try:
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"获取最新发布版本失败: {e}")
        return None


def find_font_asset(release, font_name):
    """在发布版本中查找指定的字体文件"""
    if not release or 'assets' not in release:
        return None
    
    for asset in release['assets']:
        if asset['name'] == font_name:
            return {
                'name': asset['name'],
                'download_url': asset['browser_download_url'],
                'size': asset['size'],
                'download_count': asset['download_count']
            }
    
    return None


def get_release_info(repo, font_name):
    """获取发布版本信息"""
    release = get_latest_release(repo)
    if not release:
        return None
    
    font_asset = find_font_asset(release, font_name)
    if not font_asset:
        print(f"在 {repo} 的最新发布版本中未找到字体文件: {font_name}")
        return None
    
    return {
        'repo': repo,
        'version': release['tag_name'],
        'release_name': release['name'],
        'published_at': release['published_at'],
        'font': font_asset,
        'release_url': release['html_url']
    }


def main():
    parser = argparse.ArgumentParser(description='检查字体更新')
    parser.add_argument('--repo', required=True, help='GitHub仓库名称 (格式: owner/repo)')
    parser.add_argument('--font-name', required=True, help='字体文件名')
    parser.add_argument('--output-file', required=True, help='输出JSON文件路径')
    
    args = parser.parse_args()
    
    # 检查仓库格式
    if '/' not in args.repo:
        print("错误: 仓库名称格式应为 'owner/repo'")
        sys.exit(1)
    
    # 获取发布信息
    release_info = get_release_info(args.repo, args.font_name)
    
    if not release_info:
        print(f"无法获取 {args.repo} 的发布信息")
        sys.exit(1)
    
    # 保存到JSON文件
    try:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            json.dump(release_info, f, ensure_ascii=False, indent=2)
        
        print(f"已保存发布信息到: {args.output_file}")
        print(f"版本: {release_info['version']}")
        print(f"字体文件: {release_info['font']['name']}")
        print(f"下载链接: {release_info['font']['download_url']}")
        
    except IOError as e:
        print(f"保存文件失败: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main() 