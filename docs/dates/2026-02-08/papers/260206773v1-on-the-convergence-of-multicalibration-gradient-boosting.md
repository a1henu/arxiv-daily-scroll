---
layout: default
title: On the Convergence of Multicalibration Gradient Boosting
---

# On the Convergence of Multicalibration Gradient Boosting
**arXiv**：[2602.06773v1](https://arxiv.org/abs/2602.06773) · [PDF](https://arxiv.org/pdf/2602.06773.pdf)  
**作者**：Daniel Haimovich, Fridolin Linder, Lorenzo Perini, Niek Tax, Milan Vojnovic  

**一句话要点**：分析多校准梯度提升在回归中的收敛性，提供理论保证与实验验证

**关键词**：多校准, 梯度提升, 收敛分析, 回归, 弱学习器, 平方误差损失

## 3 点简述
- 核心问题：多校准梯度提升的收敛性质未充分理解，需理论分析
- 方法要点：证明预测更新幅度以O(1/√T)衰减，弱学习器平滑时可达线性收敛
- 实验或效果：真实数据集实验支持理论，阐明快速收敛与强多校准的适用场景

## 摘要（原文）

> Multicalibration gradient boosting has recently emerged as a scalable method that empirically produces approximately multicalibrated predictors and has been deployed at web scale. Despite this empirical success, its convergence properties are not well understood. In this paper, we bridge the gap by providing convergence guarantees for multicalibration gradient boosting in regression with squared-error loss. We show that the magnitude of successive prediction updates decays at $O(1/\sqrt{T})$, which implies the same convergence rate bound for the multicalibration error over rounds. Under additional smoothness assumptions on the weak learners, this rate improves to linear convergence. We further analyze adaptive variants, showing local quadratic convergence of the training loss, and we study rescaling schemes that preserve convergence. Experiments on real-world datasets support our theory and clarify the regimes in which the method achieves fast convergence and strong multicalibration.

