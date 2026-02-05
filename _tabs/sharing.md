---
layout: page
icon: fas fa-share-alt
order: 3
title: 个人分享
---

这里是您的技术分享和想法。请在发布文章时添加 `categories: [Sharing]`。

{% assign sharing_posts = site.categories.Sharing %}
{% if sharing_posts.size > 0 %}
  {% for post in sharing_posts %}
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
  <p>暂无分享内容。</p>
{% endif %}
