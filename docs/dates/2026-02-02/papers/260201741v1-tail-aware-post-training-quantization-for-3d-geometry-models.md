---
layout: default
title: Tail-Aware Post-Training Quantization for 3D Geometry Models
---

# Tail-Aware Post-Training Quantization for 3D Geometry Models
**arXiv**：[2602.01741v1](https://arxiv.org/abs/2602.01741) · [PDF](https://arxiv.org/pdf/2602.01741.pdf)  
**作者**：Sicheng Pan, Chen Tang, Shuzhao Xie, Ke Yang, Weixiang Zhang, Jiawei Li, Bin Chen, Shu-Tao Xia, Zhi Wang  

**一句话要点**：提出TAPTQ以解决3D几何模型后训练量化中的校准与误差累积问题

**关键词**：3D几何模型, 后训练量化, 尾部感知, 校准优化, 误差补偿

## 3 点简述
- 核心问题：传统后训练量化方法在3D几何模型中因特征分布复杂和校准开销大而失效
- 方法要点：采用渐进校准构建、三元搜索优化和基于尾部相对误差的模块补偿
- 实验或效果：在VGGT和Pi3基准上优于现有方法，显著减少校准时间

## 摘要（原文）

> The burgeoning complexity and scale of 3D geometry models pose significant challenges for deployment on resource-constrained platforms. While Post-Training Quantization (PTQ) enables efficient inference without retraining, conventional methods, primarily optimized for 2D Vision Transformers, fail to transfer effectively to 3D models due to intricate feature distributions and prohibitive calibration overhead. To address these challenges, we propose TAPTQ, a Tail-Aware Post-Training Quantization pipeline specifically engineered for 3D geometric learning. Our contribution is threefold: (1) To overcome the data-scale bottleneck in 3D datasets, we develop a progressive coarse-to-fine calibration construction strategy that constructs a highly compact subset to achieve both statistical purity and geometric representativeness. (2) We reformulate the quantization interval search as an optimization problem and introduce a ternary-search-based solver, reducing the computational complexity from $\mathcal{O}(N)$ to $\mathcal{O}(\log N)$ for accelerated deployment. (3) To mitigate quantization error accumulation, we propose TRE-Guided Module-wise Compensation, which utilizes a Tail Relative Error (TRE) metric to adaptively identify and rectify distortions in modules sensitive to long-tailed activation outliers. Extensive experiments on the VGGT and Pi3 benchmarks demonstrate that TAPTQ consistently outperforms state-of-the-art PTQ methods in accuracy while significantly reducing calibration time. The code will be released soon.

