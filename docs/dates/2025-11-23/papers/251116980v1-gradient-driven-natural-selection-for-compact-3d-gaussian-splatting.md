---
layout: default
title: Gradient-Driven Natural Selection for Compact 3D Gaussian Splatting
---

# Gradient-Driven Natural Selection for Compact 3D Gaussian Splatting
**arXiv**：[2511.16980v1](https://arxiv.org/abs/2511.16980) · [PDF](https://arxiv.org/pdf/2511.16980.pdf)  
**作者**：Xiaobin Deng, Qiuli Yu, Changyu Diao, Min Li, Duanqing Xu  

**一句话要点**：提出基于自然选择的剪枝框架以压缩3D高斯溅射存储与计算开销

**关键词**：3D高斯溅射, 剪枝优化, 自然选择, 渲染质量, 紧凑表示, 梯度驱动

## 3 点简述
- 3D高斯溅射使用大量高斯基元导致高存储与计算成本
- 利用优化梯度驱动自然选择剪枝，无需人工干预或额外参数
- 在15%预算下PSNR增益超0.6dB，实现紧凑3D高斯溅射最优性能

## 摘要（原文）

> 3DGS employs a large number of Gaussian primitives to fit scenes, resulting in substantial storage and computational overhead. Existing pruning methods rely on manually designed criteria or introduce additional learnable parameters, yielding suboptimal results. To address this, we propose an natural selection inspired pruning framework that models survival pressure as a regularization gradient field applied to opacity, allowing the optimization gradients--driven by the goal of maximizing rendering quality--to autonomously determine which Gaussians to retain or prune. This process is fully learnable and requires no human intervention. We further introduce an opacity decay technique with a finite opacity prior, which accelerates the selection process without compromising pruning effectiveness. Compared to 3DGS, our method achieves over 0.6 dB PSNR gain under 15\% budgets, establishing state-of-the-art performance for compact 3DGS. Project page https://xiaobin2001.github.io/GNS-web.

