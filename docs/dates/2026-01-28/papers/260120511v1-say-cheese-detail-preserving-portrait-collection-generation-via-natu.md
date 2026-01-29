---
layout: default
title: Say Cheese! Detail-Preserving Portrait Collection Generation via Natural Language Edits
---

# Say Cheese! Detail-Preserving Portrait Collection Generation via Natural Language Edits
**arXiv**：[2601.20511v1](https://arxiv.org/abs/2601.20511) · [PDF](https://arxiv.org/pdf/2601.20511.pdf)  
**作者**：Zelong Sun, Jiahui Wu, Ying Ba, Dong Jing, Zhiwu Lu  

**一句话要点**：提出CHEESE数据集与SCheese框架，通过自然语言编辑生成细节保持的肖像集合

**关键词**：肖像集合生成, 自然语言编辑, 细节保持, 身份一致性, 数据集构建, 自适应特征融合

## 3 点简述
- 核心问题：肖像集合生成需处理多属性修改与高保真细节保持，现有方法面临挑战
- 方法要点：构建CHEESE数据集提供高质量文本标注，SCheese框架结合文本引导生成与分层身份细节保持机制
- 实验或效果：SCheese在实验中实现最先进性能，验证CHEESE数据集对任务的有效性

## 摘要（原文）

> As social media platforms proliferate, users increasingly demand intuitive ways to create diverse, high-quality portrait collections. In this work, we introduce Portrait Collection Generation (PCG), a novel task that generates coherent portrait collections by editing a reference portrait image through natural language instructions. This task poses two unique challenges to existing methods: (1) complex multi-attribute modifications such as pose, spatial layout, and camera viewpoint; and (2) high-fidelity detail preservation including identity, clothing, and accessories. To address these challenges, we propose CHEESE, the first large-scale PCG dataset containing 24K portrait collections and 573K samples with high-quality modification text annotations, constructed through an Large Vison-Language Model-based pipeline with inversion-based verification. We further propose SCheese, a framework that combines text-guided generation with hierarchical identity and detail preservation. SCheese employs adaptive feature fusion mechanism to maintain identity consistency, and ConsistencyNet to inject fine-grained features for detail consistency. Comprehensive experiments validate the effectiveness of CHEESE in advancing PCG, with SCheese achieving state-of-the-art performance.

