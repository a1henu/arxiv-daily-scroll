---
layout: default
title: FLEG: Feed-Forward Language Embedded Gaussian Splatting from Any Views
---

# FLEG: Feed-Forward Language Embedded Gaussian Splatting from Any Views
**arXiv**：[2512.17541v1](https://arxiv.org/abs/2512.17541) · [PDF](https://arxiv.org/pdf/2512.17541.pdf)  
**作者**：Qijian Tian, Xin Tan, Jiayu Ying, Xuhong Wang, Yuan Xie, Lizhuang Ma  

**一句话要点**：提出FLEG前馈网络，从任意视图重建语言嵌入3D高斯表示

**关键词**：3D重建, 语言嵌入, 高斯溅射, 前馈网络, 对比学习, 稀疏化策略

## 3 点简述
- 核心问题：现有方法依赖固定输入视图和3D标注，数据不足且灵活性差。
- 方法要点：无需3D标注，利用大规模视频数据，通过实例引导对比学习和几何语义分层稀疏化策略。
- 实验或效果：在多种任务上优于现有方法，高效重建几何、外观和语义对齐的3D表示。

## 摘要（原文）

> We present FLEG, a feed-forward network that reconstructs language-embedded 3D Gaussians from any views. Previous straightforward solutions combine feed-forward reconstruction with Gaussian heads but suffer from fixed input views and insufficient 3D training data. In contrast, we propose a 3D-annotation-free training framework for 2D-to-3D lifting from arbitrary uncalibrated and unposed multi-view images. Since the framework does not require 3D annotations, we can leverage large-scale video data with easily obtained 2D instance information to enrich semantic embedding. We also propose an instance-guided contrastive learning to align 2D semantics with the 3D representations. In addition, to mitigate the high memory and computational cost of dense views, we further propose a geometry-semantic hierarchical sparsification strategy. Our FLEG efficiently reconstructs language-embedded 3D Gaussian representation in a feed-forward manner from arbitrary sparse or dense views, jointly producing accurate geometry, high-fidelity appearance, and language-aligned semantics. Extensive experiments show that it outperforms existing methods on various related tasks. Project page: https://fangzhou2000.github.io/projects/fleg.

