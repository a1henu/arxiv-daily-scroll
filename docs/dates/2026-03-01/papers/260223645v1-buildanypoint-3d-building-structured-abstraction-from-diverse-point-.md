---
layout: default
title: BuildAnyPoint: 3D Building Structured Abstraction from Diverse Point Clouds
---

# BuildAnyPoint: 3D Building Structured Abstraction from Diverse Point Clouds
**arXiv**：[2602.23645v1](https://arxiv.org/abs/2602.23645) · [PDF](https://arxiv.org/pdf/2602.23645.pdf)  
**作者**：Tongyan Hua, Haoran Gong, Yuan Liu, Di Wang, Ying-Cong Chen, Wufan Zhao  

**一句话要点**：提出BuildAnyPoint框架，从多样点云生成结构化3D建筑抽象

**关键词**：3D建筑重建, 点云生成, 扩散模型, 自回归网格生成, 结构化抽象, 条件生成

## 3 点简述
- 核心问题：从空中LiDAR和SfM等多样分布点云中恢复结构化3D建筑抽象，面临高度欠约束挑战。
- 方法要点：设计Loosely Cascaded Diffusion Transformer，先通过条件扩散模型恢复点云分布，再用仅解码器Transformer自回归生成紧凑网格。
- 实验或效果：在建筑抽象任务上实现显著质与量提升，恢复点云在补全基准中表现优异，表面精度和分布均匀性改善。

## 摘要（原文）

> We introduce BuildAnyPoint, a novel generative framework for structured 3D building reconstruction from point clouds with diverse distributions, such as those captured by airborne LiDAR and Structure-from-Motion. To recover artist-created building abstraction in this highly underconstrained setting, we capitalize on the role of explicit 3D generative priors in autoregressive mesh generation. Specifically, we design a Loosely Cascaded Diffusion Transformer (Loca-DiT) that initially recovers the underlying distribution from noisy or sparse points, followed by autoregressively encapsulating them into compact meshes. We first formulate distribution recovery as a conditional generation task by training latent diffusion models conditioned on input point clouds, and then tailor a decoder-only transformer for conditional autoregressive mesh generation based on the recovered point clouds. Our method delivers substantial qualitative and quantitative improvements over prior building abstraction methods. Furthermore, the effectiveness of our approach is evidenced by the strong performance of its recovered point clouds on building point cloud completion benchmarks, which exhibit improved surface accuracy and distribution uniformity.

