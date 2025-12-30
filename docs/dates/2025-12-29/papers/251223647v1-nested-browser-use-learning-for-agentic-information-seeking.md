---
layout: default
title: Nested Browser-Use Learning for Agentic Information Seeking
---

# Nested Browser-Use Learning for Agentic Information Seeking
**arXiv**：[2512.23647v1](https://arxiv.org/abs/2512.23647) · [PDF](https://arxiv.org/pdf/2512.23647.pdf)  
**作者**：Baixuan Li, Jialong Wu, Wenbiao Yin, Kuan Li, Zhongwang Zhang, Huifeng Yin, Zhengwei Tao, Liwen Zhang, Pengjun Xie, Jingren Zhou, Yong Jiang  

**一句话要点**：提出NestBrowse框架以解决浏览器交互中信息获取的复杂性

**关键词**：浏览器交互, 信息搜索代理, 嵌套结构, 深度网络获取, 代理推理

## 3 点简述
- 核心问题：现有信息搜索代理工具使用受限，难以通过真实浏览器交互获取深层信息
- 方法要点：引入嵌套浏览器动作框架，解耦交互控制与页面探索，简化代理推理
- 实验或效果：在深度信息搜索基准测试中展示实践优势，分析强调效率与灵活性

## 摘要（原文）

> Information-seeking (IS) agents have achieved strong performance across a range of wide and deep search tasks, yet their tool use remains largely restricted to API-level snippet retrieval and URL-based page fetching, limiting access to the richer information available through real browsing. While full browser interaction could unlock deeper capabilities, its fine-grained control and verbose page content returns introduce substantial complexity for ReAct-style function-calling agents. To bridge this gap, we propose Nested Browser-Use Learning (NestBrowse), which introduces a minimal and complete browser-action framework that decouples interaction control from page exploration through a nested structure. This design simplifies agentic reasoning while enabling effective deep-web information acquisition. Empirical results on challenging deep IS benchmarks demonstrate that NestBrowse offers clear benefits in practice. Further in-depth analyses underscore its efficiency and flexibility.

