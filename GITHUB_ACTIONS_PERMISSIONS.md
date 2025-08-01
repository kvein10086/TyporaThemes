# GitHub Actions 权限设置说明

## 问题描述

工作流运行时出现权限错误：

### 问题1：推送权限错误
```
remote: Permission to kvein10086/TyporaThemes-Dissertation.git denied to github-actions[bot].
fatal: unable to access 'https://github.com/kvein10086/TyporaThemes-Dissertation/': The requested URL returned error: 403
```

### 问题2：Actions 使用限制
```
actions/checkout@v4 and actions/setup-python@v4 are not allowed to be used in kvein10086/TyporaThemes-Dissertation. Actions in this workflow must be: within a repository owned by kvein10086.
```

## 解决方案

### 1. 解决 Actions 使用限制问题

#### 方案A：修改仓库设置（推荐）

请在您的 GitHub 仓库设置中修改 Actions 权限：

1. **进入仓库设置**：
   - 访问：`https://github.com/kvein10086/TyporaThemes-Dissertation/settings`

2. **修改 Actions 权限**：
   - 在左侧菜单中找到 "Actions" → "General"
   - 找到 "Actions permissions" 部分
   - 将设置从 "Allow actions created by kvein10086" 改为 "Allow all actions and reusable workflows"
   - 或者选择 "Allow select actions" 并添加需要的 Actions

#### 方案B：使用本地版本工作流（备选）

如果无法修改权限设置，可以使用本地版本的工作流：

1. **重命名工作流文件**：
   ```bash
   mv .github/workflows/font-sync.yml .github/workflows/font-sync.yml.bak
   mv .github/workflows/font-sync-local.yml .github/workflows/font-sync.yml
   ```

2. **本地版本特点**：
   - 不使用外部 Actions（如 actions/checkout、actions/setup-python）
   - 手动设置 Python 环境
   - 手动检出代码
   - 功能完全相同

### 2. 在工作流中添加权限配置

已在 `.github/workflows/font-sync.yml` 中添加了以下权限配置：

```yaml
permissions:
  contents: write
  pull-requests: write
```

### 3. 仓库设置检查

请确保在您的 GitHub 仓库设置中：

1. **进入仓库设置**：
   - 点击仓库页面的 "Settings" 标签
   - 或直接访问：`https://github.com/kvein10086/TyporaThemes-Dissertation/settings`

2. **检查 Actions 权限**：
   - 在左侧菜单中找到 "Actions" → "General"
   - 确保 "Actions permissions" 设置为 "Allow all actions and reusable workflows"
   - 或者至少允许 "Allow GitHub Actions to create and approve pull requests"

3. **检查 Workflow permissions**：
   - 在同一页面找到 "Workflow permissions"
   - 选择 "Read and write permissions"
   - 勾选 "Allow GitHub Actions to create and approve pull requests"

### 4. 分支保护规则

如果您的仓库启用了分支保护规则：

1. **进入分支保护设置**：
   - Settings → Branches → Add rule 或编辑现有规则

2. **配置允许 Actions 推送**：
   - 在 "Restrict pushes that create files" 部分
   - 确保允许 GitHub Actions 机器人推送

### 5. 手动测试

您可以通过以下方式手动触发工作流来测试：

1. **在 GitHub 网页上**：
   - 进入仓库的 "Actions" 标签
   - 找到 "字体同步更新" 工作流
   - 点击 "Run workflow" 按钮

2. **检查工作流日志**：
   - 运行后查看详细日志
   - 确认权限问题是否已解决

## 权限说明

- `contents: write`: 允许工作流写入仓库内容（提交、推送等）
- `pull-requests: write`: 允许工作流创建和更新拉取请求

## 故障排除

如果仍然遇到权限问题：

1. **检查仓库可见性**：
   - 确保仓库是公开的，或者 Actions 有适当的访问权限

2. **检查组织设置**（如果是组织仓库）：
   - 确保组织允许 Actions 运行
   - 检查组织的 Actions 策略

3. **使用 Personal Access Token**（备选方案）：
   - 如果上述方法都不行，可以考虑使用 PAT
   - 但这需要额外的安全考虑

## 验证修复

修复后，工作流应该能够：
- ✅ 成功检查字体更新
- ✅ 下载新字体文件
- ✅ 转换字体格式
- ✅ 提交更改到仓库
- ✅ 推送更新到远程仓库 