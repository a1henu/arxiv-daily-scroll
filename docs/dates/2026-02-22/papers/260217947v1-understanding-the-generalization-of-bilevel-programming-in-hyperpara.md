---
layout: default
title: Understanding the Generalization of Bilevel Programming in Hyperparameter Optimization: A Tale of Bias-Variance Decomposition
---

# Understanding the Generalization of Bilevel Programming in Hyperparameter Optimization: A Tale of Bias-Variance Decomposition
**arXiv**：[2602.17947v1](https://arxiv.org/abs/2602.17947) · [PDF](https://arxiv.org/pdf/2602.17947.pdf)  
**作者**：Yubo Zhou, Jun Shu, Junmin Liu, Deyu Meng  

**一句话要点**：提出集成超梯度策略以解决超参数优化中的方差误差问题

**关键词**：超参数优化, 双层规划, 偏差-方差分解, 超梯度估计, 集成学习, 正则化学习

## 3 点简述
- 核心问题：现有超梯度估计理论忽略数据分布导致的方差误差，影响性能
- 方法要点：对超梯度估计误差进行偏差-方差分解，分析方差项并提出集成策略降低方差
- 实验或效果：在正则化超参数学习等任务中验证策略提升超梯度估计，解释过拟合现象

## 摘要（原文）

> Gradient-based hyperparameter optimization (HPO) have emerged recently, leveraging bilevel programming techniques to optimize hyperparameter by estimating hypergradient w.r.t. validation loss. Nevertheless, previous theoretical works mainly focus on reducing the gap between the estimation and ground-truth (i.e., the bias), while ignoring the error due to data distribution (i.e., the variance), which degrades performance. To address this issue, we conduct a bias-variance decomposition for hypergradient estimation error and provide a supplemental detailed analysis of the variance term ignored by previous works. We also present a comprehensive analysis of the error bounds for hypergradient estimation. This facilitates an easy explanation of some phenomena commonly observed in practice, like overfitting to the validation set. Inspired by the derived theories, we propose an ensemble hypergradient strategy to reduce the variance in HPO algorithms effectively. Experimental results on tasks including regularization hyperparameter learning, data hyper-cleaning, and few-shot learning demonstrate that our variance reduction strategy improves hypergradient estimation. To explain the improved performance, we establish a connection between excess error and hypergradient estimation, offering some understanding of empirical observations.

