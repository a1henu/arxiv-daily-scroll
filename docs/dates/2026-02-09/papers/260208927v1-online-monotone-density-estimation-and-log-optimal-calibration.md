---
layout: default
title: Online monotone density estimation and log-optimal calibration
---

# Online monotone density estimation and log-optimal calibration
**arXiv**：[2602.08927v1](https://arxiv.org/abs/2602.08927) · [PDF](https://arxiv.org/pdf/2602.08927.pdf)  
**作者**：Rohan Hore, Ruodu Wang, Aaditya Ramdas  

**一句话要点**：提出在线单调密度估计器以解决序列数据预测性密度估计问题

**关键词**：在线学习, 单调密度估计, 对数最优校准, 序列假设检验, 专家聚合

## 3 点简述
- 研究在线单调密度估计问题，需基于序列观测数据构建预测性密度估计器
- 提出两种在线估计器：在线Grenander估计器和专家聚合估计器，后者基于指数加权方法
- 在正确设定下，期望累积对数似然差距为O(n^{1/3})，专家聚合估计器路径后悔界为√(n log n)

## 摘要（原文）

> We study the problem of online monotone density estimation, where density estimators must be constructed in a predictable manner from sequentially observed data. We propose two online estimators: an online analogue of the classical Grenander estimator, and an expert aggregation estimator inspired by exponential weighting methods from the online learning literature. In the well-specified stochastic setting, where the underlying density is monotone, we show that the expected cumulative log-likelihood gap between the online estimators and the true density admits an $O(n^{1/3})$ bound. We further establish a $\sqrt{n\log{n}}$ pathwise regret bound for the expert aggregation estimator relative to the best offline monotone estimator chosen in hindsight, under minimal regularity assumptions on the observed sequence. As an application of independent interest, we show that the problem of constructing log-optimal p-to-e calibrators for sequential hypothesis testing can be formulated as an online monotone density estimation problem. We adapt the proposed estimators to build empirically adaptive p-to-e calibrators and establish their optimality. Numerical experiments illustrate the theoretical results.

