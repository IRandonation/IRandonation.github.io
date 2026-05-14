# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 提供在此仓库中工作的指导。

## 项目概述

这是一个基于 [Jekyll](https://jekyllrb.com/) 构建的个人博客网站，使用 [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 主题。部署在 GitHub Pages 上，地址为 https://IRandonation.github.io。

## 常用命令

### 本地开发服务器

```bash
# 运行 Jekyll 服务器并启用实时重载（默认主机: 127.0.0.1）
bash tools/run.sh

# 以生产模式运行
bash tools/run.sh -p

# 在指定主机上运行
bash tools/run.sh -H 0.0.0.0

# 或使用 bundle 手动运行
bundle exec jekyll serve -l
```

### 构建和测试

```bash
# 构建生产版本并运行 html-proofer 测试
bash tools/test.sh

# 仅构建（生产模式）
JEKYLL_ENV=production bundle exec jekyll build -d _site
```

### 创建新文章

```bash
# 交互式 Python 脚本用于创建新博客文章
python create_post.py
```

此脚本会交互式提示输入标题、分类（Projects/Sharing）、标签，并生成带有正确 Front Matter 的文件到 `_posts/YYYY-MM-DD-slug.md`。

## 项目架构

### Jekyll 目录结构

- **`_posts/`** - Markdown 格式的博客文章，命名约定为 `YYYY-MM-DD-title.md`
- **`_tabs/`** - 自定义页面标签（projects.md、sharing.md、resume.md）
- **`_data/`** - 数据文件（contact.yml、share.yml）
- **`_plugins/`** - 自定义 Ruby 插件（posts-lastmod-hook.rb 用于基于 Git 的最后修改日期）
- **`assets/`** - 静态资源（图片、CSS、JS）
- **`_config.yml`** - Jekyll 主配置文件

### 内容组织

网站使用**分类（categories）**来组织文章到不同的板块：

- **`Projects`** - 技术项目和代码工作（在 Projects 标签页展示）
- **`Sharing`** - 个人写作、指南和想法（在 Sharing 标签页展示）

在文章 Front Matter 中设置分类：`categories: [Projects]` 或 `categories: [Sharing]`

### 文章 Front Matter

文章的标准 Front Matter：

```yaml
---
title: "文章标题"
date: YYYY-MM-DD HH:MM:SS +0800
categories: [Projects]  # 或 [Sharing]
tags: [标签1, 标签2]
math: true              # 启用 MathJax 渲染
toc: true               # 显示目录
description: "用于 SEO 和预览的简短描述"
---
```

### 自定义标签页

`_tabs/` 目录下的文件定义自定义页面：
- 使用 `layout: page`，指定 `icon`（FontAwesome 图标），以及 `order` 用于排序
- 通过 Liquid 访问文章：`site.categories.Projects` 或 `site.categories.Sharing`
- 使用 `{% post_url YYYY-MM-DD-file-name %}` 链接到其他文章

### 部署

- **平台**: GitHub Pages
- **工作流**: `.github/workflows/pages-deploy.yml`
- **触发条件**: 推送到 `main` 或 `master` 分支
- **Ruby 版本**: 3.3
- 工作流会在部署前运行 html-proofer 检查链接

### 主题配置

- 主题以 gem 形式加载（`jekyll-theme-chirpy` ~> 7.4）
- 自定义配置在 `_config.yml` 中
- 启用 PWA（渐进式 Web 应用）支持
- Jekyll Archives 插件自动处理分类/标签页面

### DevContainer 支持

项目包含 DevContainer 配置（`.devcontainer/`）：
- 镜像: `mcr.microsoft.com/devcontainers/jekyll:2-bullseye`
- 预配置了 Liquid、Markdown 和 shell 脚本的 VS Code 扩展
- 创建后脚本自动安装 npm 依赖和 shell 工具

### VS Code 集成

预配置的任务在 `.vscode/tasks.json`：
- **运行 Jekyll 服务器**: `./tools/run.sh`
- **构建 Jekyll 站点**: `./tools/test.sh`

推荐扩展：
- Shopify Liquid 语法高亮和格式化
- Markdown All in One
- Prettier 格式化工具
