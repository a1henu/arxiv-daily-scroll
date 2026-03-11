---
layout: default
title: M3GCLR: Multi-View Mini-Max Infinite Skeleton-Data Game Contrastive Learning For Skeleton-Based Action Recognition
---

# M3GCLR: Multi-View Mini-Max Infinite Skeleton-Data Game Contrastive Learning For Skeleton-Based Action Recognition
**arXiv**：[2603.09367v1](https://arxiv.org/abs/2603.09367) · [PDF](https://arxiv.org/pdf/2603.09367.pdf)  
**作者**：Yanshan Li, Ke Ma, Miaomiao Wei, Linhui Dai  

**一句话要点**：提出M3GCLR框架，通过博弈论对比学习解决骨架动作识别中视角差异建模不足、对抗机制缺失和增强扰动不可控的问题。

**关键词**：骨架动作识别, 对比学习, 博弈论, 自监督学习, 多视角学习, 数据增强

## 3 点简述
- 核心问题：现有自监督骨架动作识别方法存在视角差异建模不足、缺乏有效对抗机制和增强扰动不可控的局限性。
- 方法要点：建立无限骨架数据博弈模型，通过多视角旋转增强生成正常-极端数据对，并引入双损失均衡优化器进行极小极大优化。
- 实验或效果：在NTU RGB+D和PKU-MMD数据集上达到或超越最先进性能，消融研究验证了各组件有效性。

## 摘要（原文）

> In recent years, contrastive learning has drawn significant attention as an effective approach to reducing reliance on labeled data. However, existing methods for self-supervised skeleton-based action recognition still face three major limitations: insufficient modeling of view discrepancies, lack of effective adversarial mechanisms, and uncontrollable augmentation perturbations. To tackle these issues, we propose the Multi-view Mini-Max infinite skeleton-data Game Contrastive Learning for skeleton-based action Recognition (M3GCLR), a game-theoretic contrastive framework. First, we establish the Infinite Skeleton-data Game (ISG) model and the ISG equilibrium theorem, and further provide a rigorous proof, enabling mini-max optimization based on multi-view mutual information. Then, we generate normal-extreme data pairs through multi-view rotation augmentation and adopt temporally averaged input as a neutral anchor to achieve structural alignment, thereby explicitly characterizing perturbation strength. Next, leveraging the proposed equilibrium theorem, we construct a strongly adversarial mini-max skeleton-data game to encourage the model to mine richer action-discriminative information. Finally, we introduce the dual-loss equilibrium optimizer to optimize the game equilibrium, allowing the learning process to maximize action-relevant information while minimizing encoding redundancy, and we prove the equivalence between the proposed optimizer and the ISG model. Extensive Experiments show that M3GCLR achieves three-stream 82.1%, 85.8% accuracy on NTU RGB+D 60 (X-Sub, X-View) and 72.3%, 75.0% accuracy on NTU RGB+D 120 (X-Sub, X-Set). On PKU-MMD Part I and II, it attains 89.1%, 45.2% in three-stream respectively, all results matching or outperforming state-of-the-art performance. Ablation studies confirm the effectiveness of each component.

