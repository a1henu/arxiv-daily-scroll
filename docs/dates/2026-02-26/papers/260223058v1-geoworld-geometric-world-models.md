---
layout: default
title: GeoWorld: Geometric World Models
---

# GeoWorld: Geometric World Models
**arXiv**：[2602.23058v1](https://arxiv.org/abs/2602.23058) · [PDF](https://arxiv.org/pdf/2602.23058.pdf)  
**作者**：Zeyu Zhang, Danning Li, Ian Reid, Richard Hartley  

**一句话要点**：提出GeoWorld几何世界模型，通过双曲JEPA和几何强化学习解决多步视觉规划中的几何结构缺失和长时预测退化问题。

**关键词**：几何世界模型, 双曲表示学习, 多步视觉规划, 能量基模型, 长时预测, 强化学习

## 3 点简述
- 现有基于能量的预测世界模型在欧氏空间中学习潜在表示，忽略状态间的几何和层次结构。
- GeoWorld引入双曲JEPA，将潜在表示映射到双曲流形，以保留几何结构和层次关系。
- 在CrossTask和COIN数据集上，相比V-JEPA 2，3步和4步规划分别提升约3%和2%的成功率。

## 摘要（原文）

> Energy-based predictive world models provide a powerful approach for multi-step visual planning by reasoning over latent energy landscapes rather than generating pixels. However, existing approaches face two major challenges: (i) their latent representations are typically learned in Euclidean space, neglecting the underlying geometric and hierarchical structure among states, and (ii) they struggle with long-horizon prediction, which leads to rapid degradation across extended rollouts. To address these challenges, we introduce GeoWorld, a geometric world model that preserves geometric structure and hierarchical relations through a Hyperbolic JEPA, which maps latent representations from Euclidean space onto hyperbolic manifolds. We further introduce Geometric Reinforcement Learning for energy-based optimization, enabling stable multi-step planning in hyperbolic latent space. Extensive experiments on CrossTask and COIN demonstrate around 3% SR improvement in 3-step planning and 2% SR improvement in 4-step planning compared to the state-of-the-art V-JEPA 2. Project website: https://steve-zeyu-zhang.github.io/GeoWorld.

