---
layout: default
title: Adapting Actively on the Fly: Relevance-Guided Online Meta-Learning with Latent Concepts for Geospatial Discovery
---

# Adapting Actively on the Fly: Relevance-Guided Online Meta-Learning with Latent Concepts for Geospatial Discovery
**arXiv**：[2602.17605v1](https://arxiv.org/abs/2602.17605) · [PDF](https://arxiv.org/pdf/2602.17605.pdf)  
**作者**：Jowaria Khan, Anindya Sarkar, Yevgeniy Vorobeychik, Elizabeth Bondi-Kelly  

**一句话要点**：提出基于概念相关性的在线元学习框架，以解决资源受限下地理空间目标发现中的稀疏偏差数据问题。

**关键词**：地理空间发现, 在线元学习, 主动学习, 概念相关性, 不确定性采样, 动态环境

## 3 点简述
- 核心问题：地理空间数据收集成本高、环境动态，且地面真值稀疏偏差，限制现有学习方法应用。
- 方法要点：引入概念相关性，结合主动学习和在线元学习，通过概念加权不确定性采样和相关性感知元批形成策略提升效率。
- 实验或效果：在真实PFAS污染数据集上测试，展示方法在有限数据和变化环境中可靠发现目标。

## 摘要（原文）

> In many real-world settings, such as environmental monitoring, disaster response, or public health, with costly and difficult data collection and dynamic environments, strategically sampling from unobserved regions is essential for efficiently uncovering hidden targets under tight resource constraints. Yet, sparse and biased geospatial ground truth limits the applicability of existing learning-based methods, such as reinforcement learning. To address this, we propose a unified geospatial discovery framework that integrates active learning, online meta-learning, and concept-guided reasoning. Our approach introduces two key innovations built on a shared notion of *concept relevance*, which captures how domain-specific factors influence target presence: a *concept-weighted uncertainty sampling strategy*, where uncertainty is modulated by learned relevance based on readily-available domain-specific concepts (e.g., land cover, source proximity); and a *relevance-aware meta-batch formation strategy* that promotes semantic diversity during online-meta updates, improving generalization in dynamic environments. Our experiments include testing on a real-world dataset of cancer-causing PFAS (Per- and polyfluoroalkyl substances) contamination, showcasing our method's reliability at uncovering targets with limited data and a varying environment.

