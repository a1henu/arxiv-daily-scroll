---
layout: default
title: Minimum-Cost Network Flow with Dual Predictions
---

# Minimum-Cost Network Flow with Dual Predictions
**arXiv**：[2601.20203v1](https://arxiv.org/abs/2601.20203) · [PDF](https://arxiv.org/pdf/2601.20203.pdf)  
**作者**：Zhiyang Chen, Hailong Yao, Xia Yin  

**一句话要点**：提出基于对偶预测的最小成本网络流算法，提升经典算法性能。

**关键词**：最小成本网络流, 对偶预测, 机器学习增强算法, ε-松弛算法, 网络优化, 预测误差分析

## 3 点简述
- 核心问题：如何利用机器学习预测改进最小成本网络流算法的效率。
- 方法要点：基于ε-松弛算法，引入对偶预测，理论分析预测误差对时间复杂度的界。
- 实验或效果：在交通网络和芯片逃逸路由应用中，分别实现12.74倍和1.64倍的平均加速。

## 摘要（原文）

> Recent work has shown that machine-learned predictions can provably improve the performance of classic algorithms. In this work, we propose the first minimum-cost network flow algorithm augmented with a dual prediction. Our method is based on a classic minimum-cost flow algorithm, namely $\varepsilon$-relaxation. We provide time complexity bounds in terms of the infinity norm prediction error, which is both consistent and robust. We also prove sample complexity bounds for PAC-learning the prediction. We empirically validate our theoretical results on two applications of minimum-cost flow, i.e., traffic networks and chip escape routing, in which we learn a fixed prediction, and a feature-based neural network model to infer the prediction, respectively. Experimental results illustrate $12.74\times$ and $1.64\times$ average speedup on two applications.

