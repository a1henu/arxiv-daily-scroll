---
layout: default
title: CLAPS: Posterior-Aware Conformal Intervals via Last-Layer Laplace
---

# CLAPS: Posterior-Aware Conformal Intervals via Last-Layer Laplace
**arXiv**：[2512.01384v1](https://arxiv.org/abs/2512.01384) · [PDF](https://arxiv.org/pdf/2512.01384.pdf)  
**作者**：Dongseok Kim, Hyoungsun Choi, Mohamed Jismy Aashik Rasool, Gisung Oh  

**一句话要点**：提出CLAPS方法，通过后验感知的保形回归提升小到中型表格数据集的预测区间效率。

**关键词**：保形回归, 后验感知, 拉普拉斯近似, 预测区间, 不确定性建模, 表格数据

## 3 点简述
- 核心问题：传统保形回归依赖点估计，在数据稀缺时预测区间可能过宽，效率不足。
- 方法要点：结合最后一层拉普拉斯近似与分割保形校准，定义后验CDF分数对齐预测形状。
- 实验或效果：在相同MLP骨干下，CLAPS保持名义覆盖率，同时缩小区间，提供轻量诊断工具。

## 摘要（原文）

> We present CLAPS, a posterior-aware conformal regression method that pairs a Last-Layer Laplace Approximation with split-conformal calibration. From the resulting Gaussian posterior, CLAPS defines a simple two-sided posterior CDF score that aligns the conformity metric with the full predictive shape, not just a point estimate. This alignment yields narrower prediction intervals at the same target coverage, especially on small to medium tabular datasets where data are scarce and uncertainty modeling matters. We also provide a lightweight diagnostic suite that separates aleatoric and epistemic components and visualizes posterior behavior, helping practitioners understand why intervals shrink when they do. Across multiple benchmarks using the same MLP backbone, CLAPS consistently attains nominal coverage with improved efficiency and minimal overhead, offering a clear, practical upgrade to residual-based conformal baselines.

