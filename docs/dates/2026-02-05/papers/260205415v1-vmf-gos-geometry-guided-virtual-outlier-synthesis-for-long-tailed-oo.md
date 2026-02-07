---
layout: default
title: VMF-GOS: Geometry-guided virtual Outlier Synthesis for Long-Tailed OOD Detection
---

# VMF-GOS: Geometry-guided virtual Outlier Synthesis for Long-Tailed OOD Detection
**arXiv**：[2602.05415v1](https://arxiv.org/abs/2602.05415) · [PDF](https://arxiv.org/pdf/2602.05415.pdf)  
**作者**：Ningkang Peng, Qianfeng Yu, Yuhao Zhang, Yafei Liu, Xiaoqian Peng, Peirong Ma, Yi Chen, Peiheng Li, Yanhui Gu  

**一句话要点**：提出几何引导虚拟离群点合成方法以解决长尾分布下无外部数据的OOD检测问题

**关键词**：长尾分布, OOD检测, 虚拟离群点合成, vMF分布, 对比学习, 无外部数据

## 3 点简述
- 核心问题：长尾分布中尾类样本稀缺导致特征空间决策边界模糊，依赖外部数据的现有方法不实用
- 方法要点：基于vMF分布定位低似然环带并方向性采样虚拟离群点，结合双粒度语义损失增强ID与离群点区分
- 实验或效果：在CIFAR-LT等基准上超越使用外部真实图像的sota方法，验证了无外部数据框架的有效性

## 摘要（原文）

> Out-of-Distribution (OOD) detection under long-tailed distributions is a highly challenging task because the scarcity of samples in tail classes leads to blurred decision boundaries in the feature space. Current state-of-the-art (sota) methods typically employ Outlier Exposure (OE) strategies, relying on large-scale real external datasets (such as 80 Million Tiny Images) to regularize the feature space. However, this dependence on external data often becomes infeasible in practical deployment due to high data acquisition costs and privacy sensitivity. To this end, we propose a novel data-free framework aimed at completely eliminating reliance on external datasets while maintaining superior detection performance. We introduce a Geometry-guided virtual Outlier Synthesis (GOS) strategy that models statistical properties using the von Mises-Fisher (vMF) distribution on a hypersphere. Specifically, we locate a low-likelihood annulus in the feature space and perform directional sampling of virtual outliers in this region. Simultaneously, we introduce a new Dual-Granularity Semantic Loss (DGS) that utilizes contrastive learning to maximize the distinction between in-distribution (ID) features and these synthesized boundary outliers. Extensive experiments on benchmarks such as CIFAR-LT demonstrate that our method outperforms sota approaches that utilize external real images.

