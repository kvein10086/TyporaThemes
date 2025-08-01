# 字体下载错误修复说明

## 问题描述

在工作流运行时出现以下错误：
```
Run mkdir -p temp_fonts
下载LXGWNeoZhiSong字体...
--2025-08-01 06:15:46--  http://null/
Resolving null (null)... failed: Temporary failure in name resolution.
wget: unable to resolve host address 'null'
Error: 进程已结束，退出代码为 4.
```

## 问题原因

1. **JSON 路径错误**: 工作流脚本中使用了错误的 JSON 路径来获取下载链接
   - 错误路径: `.download_url`
   - 正确路径: `.font.download_url`

2. **缺少错误处理**: 当下载链接为空或 null 时，没有适当的错误处理机制

## 修复内容

### 1. 修复工作流脚本 (`font-sync.yml`)

**修改前:**
```yaml
ZHISONG_URL=$(jq -r '.download_url' .github/scripts/zhisong_latest.json)
wget -O temp_fonts/LXGWNeoZhiSongPlus.ttf "$ZHISONG_URL"
```

**修改后:**
```yaml
ZHISONG_URL=$(jq -r '.font.download_url' .github/scripts/zhisong_latest.json)
if [ "$ZHISONG_URL" != "null" ] && [ -n "$ZHISONG_URL" ]; then
  wget -O temp_fonts/LXGWNeoZhiSongPlus.ttf "$ZHISONG_URL"
else
  echo "错误: 无法获取LXGWNeoZhiSong下载链接"
  exit 1
fi
```

### 2. 改进字体检查脚本 (`check_font_updates.py`)

- 添加了详细的调试信息输出
- 改进了错误处理机制
- 添加了字体信息验证

### 3. 创建测试脚本 (`test_font_download.py`)

用于验证字体下载功能是否正常工作。

## 测试结果

修复后的脚本能够正确：

1. ✅ 获取 LXGWNeoZhiSong 字体信息
   - 版本: v1.032.1
   - 下载链接: https://github.com/lxgw/LxgwNeoZhiSong/releases/download/v1.032.1/LXGWNeoZhiSongPlus.ttf

2. ✅ 获取 LXGWNeoXiHei 字体信息
   - 版本: v1.218.1
   - 下载链接: https://github.com/lxgw/LxgwNeoXiHei/releases/download/v1.218.1/LXGWNeoXiHeiPlus.ttf

## 使用方法

1. 手动测试字体下载功能：
   ```bash
   python .github/scripts/test_font_download.py
   ```

2. 测试单个字体检查：
   ```bash
   python .github/scripts/check_font_updates.py --repo lxgw/LxgwNeoZhiSong --font-name "LXGWNeoZhiSongPlus.ttf" --output-file test.json
   ```

## 注意事项

- 确保网络连接正常，能够访问 GitHub API
- 字体文件较大，下载可能需要一些时间
- 工作流会自动检查字体更新并下载最新版本 