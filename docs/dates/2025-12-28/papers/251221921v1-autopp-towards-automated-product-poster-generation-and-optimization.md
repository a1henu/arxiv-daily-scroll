---
layout: default
title: AutoPP: Towards Automated Product Poster Generation and Optimization
---

# AutoPP: Towards Automated Product Poster Generation and Optimization
**arXiv**：[2512.21921v1](https://arxiv.org/abs/2512.21921) · [PDF](https://arxiv.org/pdf/2512.21921.pdf)  
**作者**：Jiahao Fan, Yuxin Qin, Wei Feng, Yanyin Chen, Yaoyu Li, Ao Ma, Yixiu Li, Li Zhuang, Haoyi Bian, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law  

**一句话要点**：提出AutoPP自动化流水线以解决产品海报生成与优化的高成本问题

**关键词**：产品海报生成, 自动化优化, 点击率优化, 统一设计模块, 元素渲染, IDPO

## 3 点简述
- 核心问题：手动制作和优化产品海报耗时耗力，依赖人工干预。
- 方法要点：通过统一设计模块整合背景、文本和布局，并利用元素渲染模块可控生成海报；基于在线反馈，使用IDPO优化点击率。
- 实验或效果：在AutoPP1M数据集上验证，离线与在线实验均达到先进水平。

## 摘要（原文）

> Product posters blend striking visuals with informative text to highlight the product and capture customer attention. However, crafting appealing posters and manually optimizing them based on online performance is laborious and resource-consuming. To address this, we introduce AutoPP, an automated pipeline for product poster generation and optimization that eliminates the need for human intervention. Specifically, the generator, relying solely on basic product information, first uses a unified design module to integrate the three key elements of a poster (background, text, and layout) into a cohesive output. Then, an element rendering module encodes these elements into condition tokens, efficiently and controllably generating the product poster. Based on the generated poster, the optimizer enhances its Click-Through Rate (CTR) by leveraging online feedback. It systematically replaces elements to gather fine-grained CTR comparisons and utilizes Isolated Direct Preference Optimization (IDPO) to attribute CTR gains to isolated elements. Our work is supported by AutoPP1M, the largest dataset specifically designed for product poster generation and optimization, which contains one million high-quality posters and feedback collected from over one million users. Experiments demonstrate that AutoPP achieves state-of-the-art results in both offline and online settings. Our code and dataset are publicly available at: https://github.com/JD-GenX/AutoPP

