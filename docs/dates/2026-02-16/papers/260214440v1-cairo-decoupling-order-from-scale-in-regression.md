---
layout: default
title: CAIRO: Decoupling Order from Scale in Regression
---

# CAIRO: Decoupling Order from Scale in Regression
**arXiv**：[2602.14440v1](https://arxiv.org/abs/2602.14440) · [PDF](https://arxiv.org/pdf/2602.14440.pdf)  
**作者**：Harri Vanhems, Yue Zhao, Peng Shi, Archer Y. Yang  

**一句话要点**：提出CAIRO框架，通过解耦排序与尺度学习，提升回归模型在重尾噪声下的鲁棒性。

**关键词**：回归分析, 排序学习, 鲁棒性, 保序回归, 神经网络

## 3 点简述
- 标准回归方法耦合排序与尺度学习，易受异常值和重尾噪声影响。
- CAIRO分两阶段：先学习尺度不变的排序函数，再通过保序回归恢复目标尺度。
- 实验显示CAIRO在重尾或异方差噪声下优于标准回归，匹配树集成性能。

## 摘要（原文）

> Standard regression methods typically optimize a single pointwise objective, such as mean squared error, which conflates the learning of ordering with the learning of scale. This coupling renders models vulnerable to outliers and heavy-tailed noise. We propose CAIRO (Calibrate After Initial Rank Ordering), a framework that decouples regression into two distinct stages. In the first stage, we learn a scoring function by minimizing a scale-invariant ranking loss; in the second, we recover the target scale via isotonic regression. We theoretically characterize a class of "Optimal-in-Rank-Order" objectives -- including variants of RankNet and Gini covariance -- and prove that they recover the ordering of the true conditional mean under mild assumptions. We further show that subsequent monotone calibration guarantees recovery of the true regression function. Empirically, CAIRO combines the representation learning of neural networks with the robustness of rank-based statistics. It matches the performance of state-of-the-art tree ensembles on tabular benchmarks and significantly outperforms standard regression objectives in regimes with heavy-tailed or heteroskedastic noise.

