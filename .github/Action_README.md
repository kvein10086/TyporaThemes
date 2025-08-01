# GitHub Actions 工作流

本项目包含自动化的字体同步工作流，用于保持字体文件的最新状态。

## 工作流说明

### font-sync.yml

**功能**：自动检测和同步字体更新

**触发条件**：
- 定时触发：每天凌晨2点（UTC时间）
- 手动触发：在GitHub Actions页面手动运行

**监控的字体**：
- [LXGWNeoZhiSong](https://github.com/lxgw/LxgwNeoZhiSong) - 霞鹜新致宋
- [LXGWNeoXiHei](https://github.com/lxgw/LxgwNeoXiHei) - 霞鹜新晰黑

**工作流程**：
1. 检查字体仓库的最新发布版本
2. 比较当前版本与最新版本
3. 如有更新，下载新的TTF字体文件
4. 转换为WOFF2格式（提升加载性能）
5. 更新版本信息文件
6. 自动提交更改到仓库

## 脚本说明

### check_font_updates.py

字体更新检查脚本，用于：
- 获取GitHub仓库的最新发布版本
- 查找指定的字体文件
- 生成版本信息JSON文件

**使用方法**：
```bash
python check_font_updates.py --repo owner/repo --font-name "FontName.ttf" --output-file output.json
```

### convert_font.py

字体格式转换脚本，用于：
- 将TTF格式字体转换为WOFF2格式
- 使用Brotli压缩算法
- 计算压缩比和文件大小

**使用方法**：
```bash
python convert_font.py input.ttf output.woff2
```

## 依赖说明

工作流依赖以下Python包：
- `requests` - HTTP请求库
- `beautifulsoup4` - HTML解析库
- `fonttools` - 字体处理库
- `brotli` - 压缩算法库

## 版本管理

工作流会维护 `font_versions.json` 文件，记录：
- 当前使用的字体版本
- 更新时间
- 字体来源仓库

## 注意事项

1. **权限要求**：工作流需要仓库的写入权限才能自动提交更改
2. **API限制**：GitHub API有速率限制，工作流已考虑此限制
3. **错误处理**：工作流包含完善的错误处理机制
4. **日志记录**：所有操作都有详细的日志记录

## 故障排除

### 常见问题

1. **工作流失败**
   - 检查GitHub Actions日志
   - 确认字体仓库是否正常
   - 验证网络连接

2. **字体下载失败**
   - 检查字体文件名是否正确
   - 确认发布版本是否包含目标字体
   - 验证下载链接是否有效

3. **转换失败**
   - 确认TTF文件是否有效
   - 检查磁盘空间是否充足
   - 验证Python依赖是否正确安装

### 手动运行

如需手动运行工作流：
1. 进入GitHub仓库的Actions页面
2. 选择"字体同步更新"工作流
3. 点击"Run workflow"按钮
4. 选择分支并运行 