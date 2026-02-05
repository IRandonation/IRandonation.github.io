---
layout: page
icon: fas fa-code-branch
order: 2
title: 个人项目
---

这里展示您的所有个人项目。请在发布文章时添加 `categories: [Projects]`。

{% assign project_posts = site.categories.Projects %}
{% if project_posts.size > 0 %}
  {% for post in project_posts %}
  <div class="post-preview">
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <div class="post-content">
          <p>
            {% if post.description %}
              {{ post.description }}
            {% else %}
              {{ post.excerpt | strip_html | truncate: 200 }}
            {% endif %}
          </p>
      </div>
      <div class="post-meta text-muted">
          <i class="far fa-calendar fa-fw"></i>
          {{ post.date | date: "%Y-%m-%d" }}
      </div>
  </div>
  <hr>
  {% endfor %}
{% else %}
  <p>暂无项目展示。</p>
{% endif %}
