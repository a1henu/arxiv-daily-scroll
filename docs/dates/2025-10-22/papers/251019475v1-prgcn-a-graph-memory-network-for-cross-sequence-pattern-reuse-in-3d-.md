---
layout: default
title: PRGCN: A Graph Memory Network for Cross-Sequence Pattern Reuse in 3D Human Pose Estimation
---

# PRGCN: A Graph Memory Network for Cross-Sequence Pattern Reuse in 3D Human Pose Estimation
**arXiv**：[2510.19475v1](https://arxiv.org/abs/2510.19475) · [PDF](https://arxiv.org/pdf/2510.19475.pdf)  
**作者**：Zhuoyang Xie, Yibo Zhao, Hui Huang, Riwei Wang, Zan Gao  

**一句话要点**：提出PRGCN以解决单目3D人体姿态估计中的跨序列模式重用问题

**关键词**：3D人体姿态估计, 图卷积网络, 模式重用, 记忆网络, 时空建模, 跨序列学习

## 3 点简述
- 核心问题：单目3D姿态估计因2D到3D提升的深度模糊性而病态，现有方法孤立处理序列，忽略跨序列运动模式。
- 方法要点：设计图记忆网络，通过注意力机制检索和融合姿态原型，结合Mamba与自注意力进行时空特征提取。
- 实验或效果：在Human3.6M和MPI-INF-3DHP基准上达到SOTA，MPJPE分别为37.1mm和13.4mm，提升跨域泛化能力。

## 摘要（原文）

> Monocular 3D human pose estimation remains a fundamentally ill-posed inverse
> problem due to the inherent depth ambiguity in 2D-to-3D lifting. While
> contemporary video-based methods leverage temporal context to enhance spatial
> reasoning, they operate under a critical paradigm limitation: processing each
> sequence in isolation, thereby failing to exploit the strong structural
> regularities and repetitive motion patterns that pervade human movement across
> sequences. This work introduces the Pattern Reuse Graph Convolutional Network
> (PRGCN), a novel framework that formalizes pose estimation as a problem of
> pattern retrieval and adaptation. At its core, PRGCN features a graph memory
> bank that learns and stores a compact set of pose prototypes, encoded as
> relational graphs, which are dynamically retrieved via an attention mechanism
> to provide structured priors. These priors are adaptively fused with hard-coded
> anatomical constraints through a memory-driven graph convolution, ensuring
> geometrical plausibility. To underpin this retrieval process with robust
> spatiotemporal features, we design a dual-stream hybrid architecture that
> synergistically combines the linear-complexity, local temporal modeling of
> Mamba-based state-space models with the global relational capacity of
> self-attention. Extensive evaluations on Human3.6M and MPI-INF-3DHP benchmarks
> demonstrate that PRGCN establishes a new state-of-the-art, achieving an MPJPE
> of 37.1mm and 13.4mm, respectively, while exhibiting enhanced cross-domain
> generalization capability. Our work posits that the long-overlooked mechanism
> of cross-sequence pattern reuse is pivotal to advancing the field, shifting the
> paradigm from per-sequence optimization towards cumulative knowledge learning.

