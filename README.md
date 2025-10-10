# 学术论文排版样式系统

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![CSS](https://img.shields.io/badge/CSS-3-1572B6.svg)](https://www.w3.org/Style/CSS/)
[![Fonts](https://img.shields.io/badge/Fonts-WOFF2-orange.svg)](https://www.w3.org/TR/WOFF2/)

一个专为学术论文设计的完整排版样式系统，符合学术规范要求，支持明暗主题切换，提供模块化的CSS样式库。

> **项目说明**：本项目由 [Cursor](https://cursor.sh/) AI 编程助手协助开发完成。

## ✨ 特性

- 🎯 **学术规范**：严格遵循学术论文排版标准
- 🎨 **双主题支持**：内置明暗两种主题
- 📝 **自动编号**：章节标题自动编号（第N章、1.1、1.1.1等）
- 🔤 **混合字体**：中英文分别使用最适合的字体
- 📊 **完整功能**：支持表格、代码、公式、图表等所有学术元素
- 🧩 **模块化设计**：每个功能独立成模块，便于定制
- 📱 **响应式**：同时支持屏幕显示和打印输出
- ⚡ **性能优化**：使用WOFF2字体格式，加载速度更快
- 🖨️ **PDF导出**：完美支持PDF导出，页边距和格式正确
- 📋 **标题对齐**：所有标题正确顶格显示，无缩进

## 🚀 快速开始

### Typora 用户 (推荐)

1. **下载主题包**
   - 前往本项目的 [**最新发布页面 (Latest Release)**](https://github.com/kvein10086/TyporaThemes-Dissertation-1/releases/latest)。
   - 下载页面下方的 `Typora-Dissertation-Theme-vX.X.X.zip` 压缩包。

2. **解压并安装**
   - 解压下载的 `.zip` 文件。
   - 你会得到 `dissertation-f-l.css`, `dissertation-f-d.css` 和一个 `dissertation` 文件夹。
   - 将这 **两个 .css 文件** 和 **整个 dissertation 文件夹** 一同复制到 Typora 的主题目录：
     - **Windows:** `%APPDATA%\Typora\themes\`
     - **macOS:** `~/Library/Application Support/abnerworks.Typora/themes/`
     - **Linux:** `~/.config/Typora/themes/`

   > **重要提示**：必须将 `dissertation` 文件夹与 `.css` 文件放在同一目录下，否则主题将无法加载字体和模块而失效。

3. **应用主题**
   - 重启 Typora。
   - 进入 `文件` → `偏好设置` → `外观`。
   - 在主题列表中选择 `dissertation-f-l` (浅色) 或 `dissertation-f-d` (深色)。

4. **开始写作**
   - 享受专业的论文排版体验，支持实时预览和PDF导出。

### 其他用途

如果您想在其他项目中使用本样式系统，可以从 [最新发布页面 (Latest Release)](https://github.com/kvein10086/TyporaThemes-Dissertation-1/releases/latest) 下载最新的 `.zip` 包，解压后按需引入 `dissertation-f-l.css` 或 `dissertation-f-d.css`。请确保 `dissertation` 文件夹与 CSS 文件的相对路径正确。

2. **应用主题**
   - 打开 Typora
   - 进入 `文件` → `偏好设置` → `外观`
   - 在主题列表中选择 `dissertation-f-l` 或 `dissertation-f-d`

3. **开始写作**
   - 享受专业的论文排版体验
   - 支持实时预览和PDF导出

## 📋 排版规范

### 标题格式

| 级别 | 格式 | 字体 | 大小 | 对齐方式 | 行距 |
|------|------|------|------|----------|------|
| h1 | 第 N 章 | LXGWNeoXiHeiPlus | 三号(21.33px) | 居中 | 37.33px |
| h2 | 1.1 | LXGWNeoXiHeiPlus | 小三(20px) | 左对齐顶格 | 37.33px |
| h3 | 1.1.1 | LXGWNeoXiHeiPlus | 四号(18.67px) | 左对齐顶格 | 37.33px |
| h4 | 1.1.1.1 | LXGWNeoXiHeiPlus | 小四(16px) | 左对齐顶格 | 37.33px |
| h5 | 1.1.1.1.1 | LXGWNeoXiHeiPlus | 小四(16px) | 左对齐顶格 | 37.33px |
| h6 | 1.1.1.1.1.1 | LXGWNeoXiHeiPlus | 小四(16px) | 左对齐顶格 | 37.33px |

### 正文格式

- **字体**：LXGWNeoZhiSongPlus（中文）+ TimesNewerRoman（英文数字）
- **字号**：小四号（16px）
- **行距**：固定28磅（约37.33px）
- **首行缩进**：2字符
- **段间距**：适中
- **对齐方式**：两端对齐

### 页面设置

- **上边距**：2.5cm
- **下边距**：2.0cm  
- **左边距**：2.8cm
- **右边距**：2.0cm
- **纸张大小**：A4
- **打印支持**：完美支持PDF导出和打印

## 🎨 主题配置

### 浅色主题 (dissertation-f-l.css)
- 白色背景，黑色文字
- 适合日间阅读和打印
- 经典学术风格
- 推荐用于正式文档和打印输出

### 深色主题 (dissertation-f-d.css)
- 深灰背景，浅色文字
- 护眼模式，适合夜间写作
- 现代简约风格
- 推荐用于夜间写作和屏幕阅读
- 优化的颜色对比度，确保所有文字清晰可见
- 无深色文字在深色背景上的问题

## 📁 项目结构

```
dissertation-style/
├── README.md                    # 项目说明文档
├── dissertation-f-l.css         # 浅色主题入口文件
├── dissertation-f-d.css         # 深色主题入口文件
├── test-comprehensive.md       # 综合测试文档
├── font_versions.json          # 字体版本信息
├── *.ttf/*.otf                  # 字体文件（备用格式）
├── .github/                     # GitHub Actions工作流
│   └── workflows/
│       └── font-sync.yml       # 字体同步更新工作流
│   └── scripts/
│       ├── check_font_updates.py # 字体更新检查脚本
│       └── convert_font.py     # 字体格式转换脚本
└── dissertation/                # 样式模块目录
```
    ├── basic/                   # 基础样式模块
    │   ├── include.css          # 模块导入入口
    │   ├── outline.css          # 标题编号和大纲
    │   ├── font.css             # 字体设置
    │   ├── basic.css            # 基础页面样式
    │   ├── code.css             # 代码块样式
    │   ├── table.css            # 表格样式（三线表）
    │   ├── toc.css              # 目录样式
    │   ├── math.css             # 数学公式样式
    │   ├── quote.css            # 引用样式
    │   ├── list.css             # 列表样式
    │   ├── footnote.css         # 脚注样式
    │   ├── mermaid.css          # 图表样式
    │   └── ui.css               # 界面元素样式
    ├── font/                    # 字体文件（WOFF2格式）
    │   ├── LXGWNeoXiHeiPlus.woff2     # 中文黑体（标题）
    │   ├── LXGWNeoZhiSongPlus.woff2   # 中文宋体（正文）
    │   └── TimesNewerRoman-*.woff2    # 英文字体系列
    ├── light/                   # 浅色主题配置
    │   ├── basic-light-config.css
    │   └── code-light.css
    └── dark/                    # 深色主题配置
        ├── basic-dark-config.css
        └── code-dark.css
```

## 🔧 功能模块

### 代码块支持
- 语法高亮
- 行号显示
- 多种编程语言支持
- 内联代码样式
- 代码块边框和背景

### 表格样式
- 标准三线表格式
- 自动居中对齐
- 避免跨页断开
- 清晰的边框样式
- 表头加粗显示

### 数学公式
- LaTeX 数学公式支持
- 行内和块级公式
- 专业的数学排版
- 公式居中显示

### 图表支持
- Mermaid 图表样式
- 流程图、时序图等
- 与文档风格一致
- 图表居中显示

### 引用格式
- 标准学术引用样式
- 缩进和字体设置
- 清晰的视觉层次
- 引用块边框

### 列表样式
- 有序列表自动编号
- 无序列表项目符号
- 嵌套列表缩进
- 列表项间距合理

### 脚注样式
- 脚注编号自动生成
- 脚注字体和大小
- 脚注分隔线
- 脚注位置正确

## 🧪 测试文档

项目包含多个测试文档，用于验证样式效果：

### 1. 页边距测试 (test-margin.md)
- 验证PDF导出时的页边距设置
- 测试各种内容类型的显示效果
- 检查打印时的格式正确性

### 2. 标题对齐测试 (test-heading-alignment.md)
- 验证所有标题是否正确顶格显示
- 测试标题编号的正确性
- 检查标题字体的正确性

### 3. 5、6级标题格式测试 (test-h5-h6-format.md)
- 验证5、6级标题的字号设置
- 测试标题行间距的正确性
- 对比不同级别标题的显示效果

## 🧪 测试文档

项目包含一个综合测试文档，用于全面验证样式效果：

### 综合测试 (test-comprehensive.md)
- 验证PDF导出时的页边距设置
- 测试所有标题的对齐和格式
- 验证5、6级标题的字号和行间距
- 测试深色主题的视觉体验和颜色对比度
- 检查各种内容类型的显示效果
- 确保所有文字元素在深色背景下清晰可见

## 🔄 字体同步工作流

项目集成了自动字体同步工作流，确保字体文件始终保持最新版本：

### 自动更新机制
- **定时检查**：每天凌晨2点自动检查字体更新
- **手动触发**：支持手动触发字体同步
- **智能检测**：自动检测LXGWNeoZhiSong和LXGWNeoXiHei的最新版本
- **格式转换**：自动将TTF格式转换为WOFF2格式，提升加载性能
- **版本管理**：维护字体版本信息，记录更新历史
- **自动发布**：字体更新后，会自动创建一个包含完整主题包（`.zip`）的 GitHub Release，方便用户下载使用。

### 监控的字体仓库
- [LXGWNeoZhiSong](https://github.com/lxgw/LxgwNeoZhiSong) - 霞鹜新致宋
- [LXGWNeoXiHei](https://github.com/lxgw/LxgwNeoXiHei) - 霞鹜新晰黑

### 工作流特性
- **无损转换**：保持字体质量的同时大幅减小文件大小
- **自动提交**：检测到更新时自动提交到仓库
- **详细日志**：提供完整的更新日志和版本信息
- **错误处理**：完善的错误处理和重试机制

## 🛠️ 自定义配置

### 修改字体
在 `dissertation/basic/font.css` 中修改字体设置：
```css
:root {
  --base-Chinese-font: "你的中文字体";
  --base-Latin-font: "你的英文字体";
}
```

### 调整页边距
在 `dissertation/basic/font.css` 中修改页边距：
```css
:root {
  --set-margin: 上边距 右边距 下边距 左边距 !important;
}
```

### 修改标题字号
在 `dissertation/basic/font.css` 中修改标题字号：
```css
:root {
  --h1-font-size: 1.9em;
  --h2-font-size: 1.5em;
  --h3-font-size: 1.25em;
  --h4-font-size: 1.15em;
  --h5-font-size: 16px;
  --h6-font-size: 16px;
}
```

### 自定义颜色主题
创建新的主题配置文件，参考 `dissertation/light/` 或 `dissertation/dark/` 目录结构。

## 🔧 故障排除

### 常见问题

#### 1. PDF导出页边距不正确
**问题**：导出PDF后页边距不符合规范
**解决方案**：
- 检查Typora的PDF导出设置
- 使用 `test-comprehensive.md` 进行测试
- 确认主题已正确应用

#### 2. 标题没有顶格显示
**问题**：2、3、4级标题有缩进
**解决方案**：
- 使用 `test-comprehensive.md` 进行测试
- 检查是否有其他CSS文件冲突
- 确认主题已正确应用

#### 3. 5、6级标题字号错误
**问题**：5、6级标题字号太小或行间距不正确
**解决方案**：
- 使用 `test-comprehensive.md` 进行测试
- 检查字体文件是否正确加载
- 确认主题已正确应用

#### 4. 字体显示不正确
**问题**：中英文字体显示异常
**解决方案**：
- 确保字体文件在正确位置
- 检查字体文件是否损坏
- 尝试使用备用字体格式

#### 5. 主题切换不生效
**问题**：切换主题后样式没有变化
**解决方案**：
- 重启Typora
- 清除浏览器缓存（如果使用Web版本）
- 检查CSS文件路径是否正确

### 调试技巧

1. **使用测试文档**：项目提供的测试文档可以帮助快速定位问题
2. **检查浏览器开发者工具**：在Web版本中使用F12查看CSS应用情况
3. **查看Typora日志**：在Typora中查看错误日志
4. **对比原始文件**：与项目中的原始CSS文件进行对比

## 📝 更新历史 (Changelog)

本项目的所有版本发布，包括由字体更新触发的自动发布，都记录在 **[GitHub Releases](https://github.com/kvein10086/TyporaThemes-Dissertation-1/releases)** 页面。

请访问 Releases 页面查看详细的更新日志和下载特定版本的主题包。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

### 贡献步骤

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 贡献规范

- 提交前请运行测试文档验证效果
- 遵循现有的代码风格
- 添加必要的注释和文档
- 确保向后兼容性

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Cursor](https://cursor.sh/) - AI 编程助手，协助完成本项目的开发和优化
- [LXGWNeoXiHei](https://github.com/lxgw/LxgwNeoXiHei) - 一款衍生于「IPAexゴシック」的中文黑体字型。
- [LXGWNeoZhiSong](https://github.com/lxgw/LxgwNeoZhiSong) - 一款衍生于「IPAmj明朝」的中文宋体字型。
- [Times Newer Roman](https://timesnewerroman.com) - 一种看起来与 TimesNewRoman 完全相同的字体，但每个字符宽了 5-10%。
- [Typora](https://typora.io/) - 优秀的Markdown编辑器

## 📞 支持

如果您在使用过程中遇到问题，可以通过以下方式获取帮助：

1. 查看本README文档的故障排除部分
2. 使用项目提供的测试文档进行验证
3. 在GitHub上提交Issue
4. 查看项目的Wiki页面（如果有）

---

**让学术写作更专业，让排版更简单！** 🎓