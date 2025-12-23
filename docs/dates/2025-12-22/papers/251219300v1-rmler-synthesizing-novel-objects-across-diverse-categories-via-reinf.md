---
layout: default
title: RMLer: Synthesizing Novel Objects across Diverse Categories via Reinforcement Mixing Learning
---

# RMLer: Synthesizing Novel Objects across Diverse Categories via Reinforcement Mixing Learning
**arXiv**：[2512.19300v1](https://arxiv.org/abs/2512.19300) · [PDF](https://arxiv.org/pdf/2512.19300.pdf)  
**作者**：Jun Li, Zikun Chen, Haibo Chen, Shuo Chen, Jian Yang  

**一句话要点**：提出RMLer框架，通过强化学习解决跨类别文本概念融合生成新颖对象的问题

**关键词**：文本到图像生成, 概念融合, 强化学习, 跨类别合成, 视觉奖励

## 3 点简述
- 核心问题：现有T2I方法在跨类别概念融合时存在概念不平衡、组合肤浅或简单并置等不足
- 方法要点：将概念融合建模为强化学习问题，使用MLP策略网络动态混合文本嵌入，基于语义相似性和组合平衡优化策略
- 实验或效果：实验显示RMLer在合成连贯、高保真跨类别对象方面优于现有方法，适用于影视、游戏和设计领域

## 摘要（原文）

> Novel object synthesis by integrating distinct textual concepts from diverse categories remains a significant challenge in Text-to-Image (T2I) generation. Existing methods often suffer from insufficient concept mixing, lack of rigorous evaluation, and suboptimal outputs-manifesting as conceptual imbalance, superficial combinations, or mere juxtapositions. To address these limitations, we propose Reinforcement Mixing Learning (RMLer), a framework that formulates cross-category concept fusion as a reinforcement learning problem: mixed features serve as states, mixing strategies as actions, and visual outcomes as rewards. Specifically, we design an MLP-policy network to predict dynamic coefficients for blending cross-category text embeddings. We further introduce visual rewards based on (1) semantic similarity and (2) compositional balance between the fused object and its constituent concepts, optimizing the policy via proximal policy optimization. At inference, a selection strategy leverages these rewards to curate the highest-quality fused objects. Extensive experiments demonstrate RMLer's superiority in synthesizing coherent, high-fidelity objects from diverse categories, outperforming existing methods. Our work provides a robust framework for generating novel visual concepts, with promising applications in film, gaming, and design.

