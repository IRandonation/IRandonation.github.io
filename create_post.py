import os
import datetime
import re

def slugify(text):
    # 简单的 slug 处理：转小写，非字母数字替换为连字符
    text = text.lower()
    text = re.sub(r'[^a-z0-9\u4e00-\u9fa5]+', '-', text)
    text = text.strip('-')
    return text

def create_post():
    print("=== 创建新博客文章 ===")
    
    # 1. 获取标题
    title = input("请输入文章标题: ").strip()
    if not title:
        print("标题不能为空！")
        return

    # 2. 选择分类
    print("\n请选择文章分类:")
    print("1. 个人项目 (Projects)")
    print("2. 个人分享 (Sharing)")
    print("3. 其他 (默认)")
    
    cat_choice = input("请输入选项 (1/2/3): ").strip()
    
    categories = []
    if cat_choice == '1':
        categories = ['Projects']
    elif cat_choice == '2':
        categories = ['Sharing']
    else:
        # 如果用户想自定义分类，也可以支持，但为了简单先留空或默认
        pass

    # 3. 获取标签
    tags_input = input("\n请输入标签 (用空格分隔，例如: python ai demo): ").strip()
    tags = [t for t in tags_input.split() if t]

    # 4. 生成文件名
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    # 如果标题包含中文，建议提供一个英文别名用于文件名，或者直接用拼音/简单处理
    # 这里为了简单，如果全是中文，可能文件名会有点怪，建议用户输入英文 slug
    
    filename_slug = input("\n请输入文件名的英文别名 (留空则自动根据标题生成): ").strip()
    if not filename_slug:
        filename_slug = slugify(title)
        if not filename_slug: # 如果标题全是特殊字符
            filename_slug = "new-post"
    
    filename = f"{date_str}-{filename_slug}.md"
    filepath = os.path.join("_posts", filename)

    # 5. 生成 Front Matter 内容
    content = "---\n"
    content += f"title: {title}\n"
    content += f"date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')} +0800\n"
    
    if categories:
        content += f"categories: [{', '.join(categories)}]\n"
    else:
        content += "categories: []\n"
        
    if tags:
        content += f"tags: [{', '.join(tags)}]\n"
    else:
        content += "tags: []\n"
        
    content += "---\n\n"
    content += "# 在这里开始写作...\n\n"

    # 6. 写入文件
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ 文章创建成功！")
        print(f"📂 文件路径: {filepath}")
        print("您可以开始编辑了。")
    except Exception as e:
        print(f"\n❌ 创建失败: {e}")

if __name__ == "__main__":
    create_post()
