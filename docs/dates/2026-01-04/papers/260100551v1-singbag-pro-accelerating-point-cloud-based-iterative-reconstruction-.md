---
layout: default
title: SingBAG Pro: Accelerating point cloud-based iterative reconstruction for 3D photoacoustic imaging under arbitrary array
---

# SingBAG Pro: Accelerating point cloud-based iterative reconstruction for 3D photoacoustic imaging under arbitrary array
**arXiv**：[2601.00551v1](https://arxiv.org/abs/2601.00551) · [PDF](https://arxiv.org/pdf/2601.00551.pdf)  
**作者**：Shuang Li, Yibing Wang, Jian Gao, Chulhong Kim, Seongwook Choi, Yu Zhang, Qian Chen, Yao Yao, Changhui Li  

**一句话要点**：提出SlingBAG Pro算法，加速不规则阵列下的点云迭代重建，用于三维光声成像。

**关键词**：三维光声成像, 点云迭代重建, 不规则阵列, 分层优化, 计算加速

## 3 点简述
- 问题：传统迭代算法在不规则阵列下计算复杂、内存需求高、重建时间长。
- 方法：基于点云迭代，结合零梯度滤波和渐进时间采样率的分层优化策略。
- 效果：相比原算法，速度提升达2.2倍，并通过仿真和活体小鼠实验验证。

## 摘要（原文）

> High-quality three-dimensional (3D) photoacoustic imaging (PAI) is gaining increasing attention in clinical applications. To address the challenges of limited space and high costs, irregular geometric transducer arrays that conform to specific imaging regions are promising for achieving high-quality 3D PAI with fewer transducers. However, traditional iterative reconstruction algorithms struggle with irregular array configurations, suffering from high computational complexity, substantial memory requirements, and lengthy reconstruction times. In this work, we introduce SlingBAG Pro, an advanced reconstruction algorithm based on the point cloud iteration concept of the Sliding ball adaptive growth (SlingBAG) method, while extending its compatibility to arbitrary array geometries. SlingBAG Pro maintains high reconstruction quality, reduces the number of required transducers, and employs a hierarchical optimization strategy that combines zero-gradient filtering with progressively increased temporal sampling rates during iteration. This strategy rapidly removes redundant spatial point clouds, accelerates convergence, and significantly shortens overall reconstruction time. Compared to the original SlingBAG algorithm, SlingBAG Pro achieves up to a 2.2-fold speed improvement in point cloud-based 3D PA reconstruction under irregular array geometries. The proposed method is validated through both simulation and in vivo mouse experiments, and the source code is publicly available at https://github.com/JaegerCQ/SlingBAG_Pro.

