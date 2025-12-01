---
layout: default
title: A Trainable Centrality Framework for Modern Data
---

# A Trainable Centrality Framework for Modern Data
**arXiv**：[2511.22959v1](https://arxiv.org/abs/2511.22959) · [PDF](https://arxiv.org/pdf/2511.22959.pdf)  
**作者**：Minh Duc Vu, Mingshuo Liu, Doudou Zhou  

**一句话要点**：提出FUSE框架以解决高维和非欧数据中的中心性度量问题

**关键词**：中心性度量, 神经网络框架, 异常检测, 高维数据, 非欧数据

## 3 点简述
- 核心问题：经典深度方法在高维和非欧数据中计算昂贵、不稳定且难以扩展
- 方法要点：结合全局头（基于成对距离学习中心性）和局部头（去噪分数匹配近似密度）的神经网络框架
- 实验或效果：在合成分布、图像、时间序列和文本数据中恢复经典排序，并在异常检测基准上表现竞争性

## 摘要（原文）

> Measuring how central or typical a data point is underpins robust estimation, ranking, and outlier detection, but classical depth notions become expensive and unstable in high dimensions and are hard to extend beyond Euclidean data. We introduce Fused Unified centrality Score Estimation (FUSE), a neural centrality framework that operates on top of arbitrary representations. FUSE combines a global head, trained from pairwise distance-based comparisons to learn an anchor-free centrality score, with a local head, trained by denoising score matching to approximate a smoothed log-density potential. A single parameter between 0 and 1 interpolates between these calibrated signals, yielding depth-like centrality from different views via one forward pass. Across synthetic distributions, real images, time series, and text data, and standard outlier detection benchmarks, FUSE recovers meaningful classical ordering, reveals multi-scale geometric structures, and attains competitive performance with strong classical baselines while remaining simple and efficient.

