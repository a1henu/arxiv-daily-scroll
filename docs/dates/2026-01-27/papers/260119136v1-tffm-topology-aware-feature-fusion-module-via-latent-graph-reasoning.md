---
layout: default
title: TFFM: Topology-Aware Feature Fusion Module via Latent Graph Reasoning for Retinal Vessel Segmentation
---

# TFFM: Topology-Aware Feature Fusion Module via Latent Graph Reasoning for Retinal Vessel Segmentation
**arXiv**：[2601.19136v1](https://arxiv.org/abs/2601.19136) · [PDF](https://arxiv.org/pdf/2601.19136.pdf)  
**作者**：Iftekhar Ahmed, Shakib Absar, Aftar Ahmad Sami, Shadman Sakib, Debojyoti Biswas, Seraj Al Mahmud Mostafa  

**一句话要点**：提出拓扑感知特征融合模块，通过潜在图推理解决视网膜血管分割中的拓扑断裂问题。

**关键词**：视网膜血管分割, 拓扑感知, 图注意力网络, 特征融合, 混合损失函数, 生物医学图像分析

## 3 点简述
- 核心问题：标准卷积架构在视网膜血管分割中产生拓扑断裂，影响基于图的临床分析。
- 方法要点：融合拓扑特征融合模块，利用图注意力网络在潜在图空间捕获全局结构依赖。
- 实验或效果：在Fundus-AVSeg数据集上达到90.97% Dice分数，血管断裂减少约38%。

## 摘要（原文）

> Precise segmentation of retinal arteries and veins carries the diagnosis of systemic cardiovascular conditions. However, standard convolutional architectures often yield topologically disjointed segmentations, characterized by gaps and discontinuities that render reliable graph-based clinical analysis impossible despite high pixel-level accuracy. To address this, we introduce a topology-aware framework engineered to maintain vascular connectivity. Our architecture fuses a Topological Feature Fusion Module (TFFM) that maps local feature representations into a latent graph space, deploying Graph Attention Networks to capture global structural dependencies often missed by fixed receptive fields. Furthermore, we drive the learning process with a hybrid objective function, coupling Tversky loss for class imbalance with soft clDice loss to explicitly penalize topological disconnects. Evaluation on the Fundus-AVSeg dataset reveals state-of-the-art performance, achieving a combined Dice score of 90.97% and a 95% Hausdorff Distance of 3.50 pixels. Notably, our method decreases vessel fragmentation by approximately 38% relative to baselines, yielding topologically coherent vascular trees viable for automated biomarker quantification. We open-source our code at https://tffm-module.github.io/.

