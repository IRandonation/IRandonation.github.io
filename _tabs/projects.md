---
layout: page
icon: fas fa-code-branch
order: 2
title: Projects
---

这里展示您的所有个人项目。请在发布文章时添加 `categories: [Projects]`。

<div id="post-list">
{% assign project_posts = site.categories.Projects %}
{% if project_posts.size > 0 %}
  {% for post in project_posts %}
  <article class="card-wrapper card">
    <a href="{{ post.url | relative_url }}" class="post-preview row g-0 flex-md-row-reverse">
      <div class="col-md-12">
        <div class="card-body d-flex flex-column">
          <h1 class="card-title my-2 mt-md-0">{{ post.title }}</h1>
          <div class="card-text content mt-0 mb-3">
            <p>
              {% if post.description %}
                {{ post.description }}
              {% else %}
                {{ post.excerpt | strip_html | truncate: 200 }}
              {% endif %}
            </p>
          </div>
          <div class="post-meta flex-grow-1 d-flex align-items-end">
            <div class="me-auto">
              <i class="far fa-calendar fa-fw me-1"></i>
              <time>{{ post.date | date: "%Y-%m-%d" }}</time>
              
              <i class="far fa-folder-open fa-fw me-1 ms-3"></i>
              <span class="categories">
                Projects
              </span>
            </div>
          </div>
        </div>
      </div>
    </a>
  </article>
  {% endfor %}
{% else %}
  <div class="card-wrapper card">
    <div class="card-body">
      <p class="card-text">暂无项目展示，请在文章中添加 <code>categories: [Projects]</code>。</p>
    </div>
  </div>
{% endif %}
</div>
