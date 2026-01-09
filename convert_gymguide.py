import os
import markdown
import re
from bs4 import BeautifulSoup

# 路径配置
PROJECT_ROOT = r"d:\Project"
GYM_GUIDE_PATH = os.path.join(PROJECT_ROOT, "GymGuide", "README.md")
BLOG_ROOT = os.path.join(PROJECT_ROOT, "IRandonation.github.io")
TEMPLATE_PATH = os.path.join(BLOG_ROOT, "generic.html")
OUTPUT_PATH = os.path.join(BLOG_ROOT, "gym-guide.html")
INDEX_PATH = os.path.join(BLOG_ROOT, "index.html")

def convert_md_to_html():
    print(f"Reading Markdown from {GYM_GUIDE_PATH}...")
    with open(GYM_GUIDE_PATH, "r", encoding="utf-8") as f:
        md_content = f.read()

    # 处理 Markdown 中的公式
    # 简单的处理：将 $$ ... $$ 替换为 MathJax 识别的格式，或者保持原样，并在 HTML 中引入 MathJax
    # 我们将在 HTML 头部添加 MathJax CDN
    
    print("Converting Markdown to HTML...")
    html_body = markdown.markdown(md_content, extensions=['extra', 'toc', 'codehilite', 'tables'])

    print(f"Reading Template from {TEMPLATE_PATH}...")
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_content = f.read()

    soup = BeautifulSoup(template_content, 'html.parser')

    # 1. 修改 Title
    if soup.title:
        soup.title.string = "Gym Guide - IRandonation"

    # 2. 修改 Header
    # 找到 section id="wrapper" 下的 header
    wrapper_section = soup.find('section', id='wrapper')
    if wrapper_section:
        header = wrapper_section.find('header')
        if header:
            inner = header.find('div', class_='inner')
            if inner:
                h2 = inner.find('h2')
                if h2: h2.string = "Gym Guide"
                p = inner.find('p')
                if p: p.string = "Build your own body：构建自己的训练体系"

    # 3. 插入内容
    # 找到 <!-- Content --> 下面的 div.wrapper > div.inner
    # BS4 不保留注释，所以直接找结构
    # wrapper_section 已经在上面找到了
    if wrapper_section:
        content_wrapper = wrapper_section.find('div', class_='wrapper')
        if content_wrapper:
            content_inner = content_wrapper.find('div', class_='inner')
            if content_inner:
                # 清空原有内容
                content_inner.clear()
                
                # 创建新的内容节点
                # 添加回到 GitHub 的链接
                github_link = soup.new_tag('a', href="https://github.com/IRandonation/GymGuide", target="_blank", **{'class': 'button small icon brands fa-github'})
                github_link.string = " View on GitHub"
                content_inner.append(github_link)
                content_inner.append(soup.new_tag('br'))
                content_inner.append(soup.new_tag('br'))
                
                # 解析 markdown 生成的 html 并插入
                # 为了防止 html 结构混乱，再次用 BS 解析片段
                body_soup = BeautifulSoup(html_body, 'html.parser')
                content_inner.append(body_soup)

    # 4. 添加 MathJax 支持
    head = soup.find('head')
    if head:
        mathjax_script = soup.new_tag('script', src="https://polyfill.io/v3/polyfill.min.js?features=es6")
        head.append(mathjax_script)
        # async 是 Python 关键字，需要用字典传参
        mathjax_script2 = soup.new_tag('script', id="MathJax-script", src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js")
        mathjax_script2['async'] = True
        head.append(mathjax_script2)

    print(f"Writing output to {OUTPUT_PATH}...")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))

def update_index_html():
    print(f"Updating {INDEX_PATH}...")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    soup = BeautifulSoup(index_content, 'html.parser')
    
    # 1. 添加到 Menu
    nav_menu = soup.find('nav', id='menu')
    if nav_menu:
        ul = nav_menu.find('ul', class_='links')
        if ul:
            # 检查是否已经存在
            if not ul.find('a', href='gym-guide.html'):
                li = soup.new_tag('li')
                a = soup.new_tag('a', href='gym-guide.html')
                a.string = "Gym Guide"
                li.append(a)
                ul.append(li)
                print("Added to Menu.")

    # 2. 添加到 Features (Section Four)
    section_four = soup.find('section', id='four')
    if section_four:
        features = section_four.find('section', class_='features')
        if features:
            # 检查是否已经存在
            # 简单的检查方法：看是否有链接指向 gym-guide.html
            if not features.find('a', href='gym-guide.html'):
                article = soup.new_tag('article')
                
                # Image
                a_img = soup.new_tag('a', href='gym-guide.html', class_='image')
                # 使用现有的图片，或者随机选一个
                img = soup.new_tag('img', src='images/pic07.jpg', alt='') 
                a_img.append(img)
                article.append(a_img)
                
                # Title
                h3 = soup.new_tag('h3', class_='major')
                h3.string = "Gym Guide"
                article.append(h3)
                
                # Description
                p = soup.new_tag('p')
                p.string = "构建自己的训练体系：从力量训练到身体控制的完整指南。"
                article.append(p)
                
                # Link
                a_more = soup.new_tag('a', href='gym-guide.html', class_='special')
                a_more.string = "Learn more"
                article.append(a_more)
                
                features.append(article)
                print("Added to Features.")

    print(f"Writing updated index to {INDEX_PATH}...")
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))

if __name__ == "__main__":
    convert_md_to_html()
    update_index_html()
