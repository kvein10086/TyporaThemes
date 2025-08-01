#!/usr/bin/env python3
"""
字体转换脚本
将TTF格式字体转换为WOFF2格式
"""

import argparse
import os
import sys
from fontTools.ttLib import TTFont
import brotli


def convert_ttf_to_woff2(input_path, output_path):
    """将TTF字体转换为WOFF2格式"""
    try:
        # 读取TTF字体
        print(f"读取字体文件: {input_path}")
        font = TTFont(input_path)
        
        # 获取字体数据
        font_data = font.reader.file.read()
        
        # 使用Brotli压缩
        print("压缩字体数据...")
        compressed_data = brotli.compress(font_data, quality=11)
        
        # 写入WOFF2文件
        print(f"写入WOFF2文件: {output_path}")
        with open(output_path, 'wb') as f:
            f.write(compressed_data)
        
        # 计算压缩比
        original_size = len(font_data)
        compressed_size = len(compressed_data)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f"转换完成!")
        print(f"原始大小: {original_size:,} 字节")
        print(f"压缩后大小: {compressed_size:,} 字节")
        print(f"压缩比: {compression_ratio:.1f}%")
        
        return True
        
    except Exception as e:
        print(f"转换失败: {e}")
        return False


def validate_ttf_file(file_path):
    """验证TTF文件是否有效"""
    if not os.path.exists(file_path):
        print(f"错误: 文件不存在: {file_path}")
        return False
    
    if not file_path.lower().endswith('.ttf'):
        print(f"错误: 文件不是TTF格式: {file_path}")
        return False
    
    try:
        font = TTFont(file_path)
        font.close()
        return True
    except Exception as e:
        print(f"错误: 无效的TTF文件: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='将TTF字体转换为WOFF2格式')
    parser.add_argument('input', help='输入的TTF文件路径')
    parser.add_argument('output', help='输出的WOFF2文件路径')
    
    args = parser.parse_args()
    
    # 验证输入文件
    if not validate_ttf_file(args.input):
        sys.exit(1)
    
    # 确保输出目录存在
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 转换字体
    success = convert_ttf_to_woff2(args.input, args.output)
    
    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main() 