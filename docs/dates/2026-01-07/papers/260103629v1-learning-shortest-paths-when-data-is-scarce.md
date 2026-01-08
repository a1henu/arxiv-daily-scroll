---
layout: default
title: Learning Shortest Paths When Data is Scarce
---

# Learning Shortest Paths When Data is Scarce
**arXiv**：[2601.03629v1](https://arxiv.org/abs/2601.03629) · [PDF](https://arxiv.org/pdf/2601.03629.pdf)  
**作者**：Dmytro Matsypura, Yu Pan, Hanzhao Wang  

**一句话要点**：提出拉普拉斯正则化最小二乘法，在数据稀缺时校准数字孪生偏差以优化最短路径

**关键词**：最短路径优化, 数字孪生偏差校准, 拉普拉斯正则化, 数据稀缺学习, 主动学习算法

## 3 点简述
- 研究数据稀缺下数字孪生偏差的随机最短路径问题
- 使用拉普拉斯正则化最小二乘估计平滑边偏差，提供误差界和路径次优性保证
- 实验在道路网络和交通图上验证方法的有效性

## 摘要（原文）

> Digital twins and other simulators are increasingly used to support routing decisions in large-scale networks. However, simulator outputs often exhibit systematic bias, while ground-truth measurements are costly and scarce. We study a stochastic shortest-path problem in which a planner has access to abundant synthetic samples, limited real-world observations, and an edge-similarity structure capturing expected behavioral similarity across links. We model the simulator-to-reality discrepancy as an unknown, edge-specific bias that varies smoothly over the similarity graph, and estimate it using Laplacian-regularized least squares. This approach yields calibrated edge cost estimates even in data-scarce regimes. We establish finite-sample error bounds, translate estimation error into path-level suboptimality guarantees, and propose a computable, data-driven certificate that verifies near-optimality of a candidate route. For cold-start settings without initial real data, we develop a bias-aware active learning algorithm that leverages the simulator and adaptively selects edges to measure until a prescribed accuracy is met. Numerical experiments on multiple road networks and traffic graphs further demonstrate the effectiveness of our methods.

