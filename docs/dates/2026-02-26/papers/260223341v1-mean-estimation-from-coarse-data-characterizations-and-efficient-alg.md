---
layout: default
title: Mean Estimation from Coarse Data: Characterizations and Efficient Algorithms
---

# Mean Estimation from Coarse Data: Characterizations and Efficient Algorithms
**arXiv**：[2602.23341v1](https://arxiv.org/abs/2602.23341) · [PDF](https://arxiv.org/pdf/2602.23341.pdf)  
**作者**：Alkis Kalavasis, Anay Mehrotra, Manolis Zampetakis, Felix Zhou, Ziyu Zhu  

**一句话要点**：解决高斯均值估计在凸划分下的可识别性与高效算法问题

**关键词**：高斯均值估计, 粗数据, 凸划分, 可识别性, 高效算法

## 3 点简述
- 核心问题：确定凸划分下高斯均值可识别的条件
- 方法要点：建立可识别性理论并设计计算高效估计算法
- 实验或效果：验证算法在可识别条件下的样本效率与计算可行性

## 摘要（原文）

> Coarse data arise when learners observe only partial information about samples; namely, a set containing the sample rather than its exact value. This occurs naturally through measurement rounding, sensor limitations, and lag in economic systems. We study Gaussian mean estimation from coarse data, where each true sample $x$ is drawn from a $d$-dimensional Gaussian distribution with identity covariance, but is revealed only through the set of a partition containing $x$. When the coarse samples, roughly speaking, have ``low'' information, the mean cannot be uniquely recovered from observed samples (i.e., the problem is not identifiable). Recent work by Fotakis, Kalavasis, Kontonis, and Tzamos [FKKT21] established that sample-efficient mean estimation is possible when the unknown mean is identifiable and the partition consists of only convex sets. Moreover, they showed that without convexity, mean estimation becomes NP-hard. However, two fundamental questions remained open: (1) When is the mean identifiable under convex partitions? (2) Is computationally efficient estimation possible under identifiability and convex partitions? This work resolves both questions. [...]

