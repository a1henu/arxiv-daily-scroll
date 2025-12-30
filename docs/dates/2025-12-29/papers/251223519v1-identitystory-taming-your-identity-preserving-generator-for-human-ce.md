---
layout: default
title: IdentityStory: Taming Your Identity-Preserving Generator for Human-Centric Story Generation
---

# IdentityStory: Taming Your Identity-Preserving Generator for Human-Centric Story Generation
**arXiv**：[2512.23519v1](https://arxiv.org/abs/2512.23519) · [PDF](https://arxiv.org/pdf/2512.23519.pdf)  
**作者**：Donghao Zhou, Jingyu Lin, Guibao Shen, Quande Liu, Jialin Gao, Lihao Liu, Lan Du, Cunjian Chen, Chi-Wing Fu, Xiaowei Hu, Pheng-Ann Heng  

**一句话要点**：提出IdentityStory框架以解决人本故事生成中的角色身份一致性问题

**关键词**：人本故事生成, 身份一致性, 迭代身份发现, 重去噪身份注入, 多角色协调, 视觉生成模型

## 3 点简述
- 核心问题：人本故事生成需保持人脸细节一致性和多角色协调
- 方法要点：通过迭代身份发现和重去噪身份注入来驯化身份保持生成器
- 实验或效果：在ConsiStory-Human基准上优于现有方法，支持多角色组合

## 摘要（原文）

> Recent visual generative models enable story generation with consistent characters from text, but human-centric story generation faces additional challenges, such as maintaining detailed and diverse human face consistency and coordinating multiple characters across different images. This paper presents IdentityStory, a framework for human-centric story generation that ensures consistent character identity across multiple sequential images. By taming identity-preserving generators, the framework features two key components: Iterative Identity Discovery, which extracts cohesive character identities, and Re-denoising Identity Injection, which re-denoises images to inject identities while preserving desired context. Experiments on the ConsiStory-Human benchmark demonstrate that IdentityStory outperforms existing methods, particularly in face consistency, and supports multi-character combinations. The framework also shows strong potential for applications such as infinite-length story generation and dynamic character composition.

