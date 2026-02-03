---
layout: default
title: LiFlow: Flow Matching for 3D LiDAR Scene Completion
---

# LiFlow: Flow Matching for 3D LiDAR Scene Completion
**arXiv**：[2602.02232v1](https://arxiv.org/abs/2602.02232) · [PDF](https://arxiv.org/pdf/2602.02232.pdf)  
**作者**：Andrea Matteazzi, Dietmar Tutsch  

**一句话要点**：提出LiFlow流匹配框架以解决自动驾驶中LiDAR点云遮挡与稀疏导致的场景补全问题。

**关键词**：自动驾驶, LiDAR点云, 场景补全, 流匹配, 3D感知, 点云对齐

## 3 点简述
- 核心问题：自动驾驶中LiDAR点云因遮挡和远距离稀疏导致场景不完整，影响感知系统性能。
- 方法要点：采用流匹配框架替代扩散模型，通过最近邻流匹配损失和Chamfer距离损失，确保训练与推理初始分布一致，提升点云对齐的局部结构和全局覆盖。
- 实验或效果：在多个指标上达到最先进性能，代码已开源。

## 摘要（原文）

> In autonomous driving scenarios, the collected LiDAR point clouds can be challenged by occlusion and long-range sparsity, limiting the perception of autonomous driving systems. Scene completion methods can infer the missing parts of incomplete 3D LiDAR scenes. Recent methods adopt local point-level denoising diffusion probabilistic models, which require predicting Gaussian noise, leading to a mismatch between training and inference initial distributions. This paper introduces the first flow matching framework for 3D LiDAR scene completion, improving upon diffusion-based methods by ensuring consistent initial distributions between training and inference. The model employs a nearest neighbor flow matching loss and a Chamfer distance loss to enhance both local structure and global coverage in the alignment of point clouds. LiFlow achieves state-of-the-art performance across multiple metrics. Code: https://github.com/matteandre/LiFlow.

