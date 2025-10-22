---
layout: default
title: Latent-Info and Low-Dimensional Learning for Human Mesh Recovery and Parallel Optimization
---

# Latent-Info and Low-Dimensional Learning for Human Mesh Recovery and Parallel Optimization
**arXiv**：[2510.18267v1](https://arxiv.org/abs/2510.18267) · [PDF](https://arxiv.org/pdf/2510.18267.pdf)  
**作者**：Xiang Zhang, Suping Wu, Sheng Yang  

**一句话要点**：提出基于潜在信息和低维学习的两阶段网络，以解决3D人体网格恢复中的对齐问题和计算成本高的问题。

**关键词**：3D人体网格恢复, 潜在信息提取, 低维学习, 并行优化, 频率域特征

## 3 点简述
- 现有方法未充分利用潜在信息，导致网格对齐和细节不足，且注意力机制计算成本高。
- 设计两阶段网络：第一阶段提取并聚合潜在频率特征；第二阶段通过低维交互和并行优化降低计算成本。
- 在公开数据集上实验显示，该方法在保持精度的同时显著优于现有先进方法。

## 摘要（原文）

> Existing 3D human mesh recovery methods often fail to fully exploit the
> latent information (e.g., human motion, shape alignment), leading to issues
> with limb misalignment and insufficient local details in the reconstructed
> human mesh (especially in complex scenes). Furthermore, the performance
> improvement gained by modelling mesh vertices and pose node interactions using
> attention mechanisms comes at a high computational cost. To address these
> issues, we propose a two-stage network for human mesh recovery based on latent
> information and low dimensional learning. Specifically, the first stage of the
> network fully excavates global (e.g., the overall shape alignment) and local
> (e.g., textures, detail) information from the low and high-frequency components
> of image features and aggregates this information into a hybrid latent
> frequency domain feature. This strategy effectively extracts latent
> information. Subsequently, utilizing extracted hybrid latent frequency domain
> features collaborates to enhance 2D poses to 3D learning. In the second stage,
> with the assistance of hybrid latent features, we model the interaction
> learning between the rough 3D human mesh template and the 3D pose, optimizing
> the pose and shape of the human mesh. Unlike existing mesh pose interaction
> methods, we design a low-dimensional mesh pose interaction method through
> dimensionality reduction and parallel optimization that significantly reduces
> computational costs without sacrificing reconstruction accuracy. Extensive
> experimental results on large publicly available datasets indicate superiority
> compared to the most state-of-the-art.

