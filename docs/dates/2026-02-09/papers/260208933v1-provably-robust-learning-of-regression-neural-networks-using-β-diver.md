---
layout: default
title: Provably robust learning of regression neural networks using $β$-divergences
---

# Provably robust learning of regression neural networks using $β$-divergences
**arXiv**：[2602.08933v1](https://arxiv.org/abs/2602.08933) · [PDF](https://arxiv.org/pdf/2602.08933.pdf)  
**作者**：Abhik Ghosh, Suryasis Jana  

**一句话要点**：提出基于β-散度的回归神经网络鲁棒学习框架rRNet，以应对异常值和数据污染。

**关键词**：回归神经网络, 鲁棒学习, β-散度, 理论保证, 异常值处理, 函数逼近

## 3 点简述
- 回归神经网络常用均方误差训练，对异常值敏感，现有方法缺乏理论保证。
- rRNet基于β-散度，适用于广泛网络类型，提供收敛性和局部鲁棒性理论分析。
- 实验显示rRNet在函数逼近和噪声预测任务中优于现有方法，达到50%渐近崩溃点。

## 摘要（原文）

> Regression neural networks (NNs) are most commonly trained by minimizing the mean squared prediction error, which is highly sensitive to outliers and data contamination. Existing robust training methods for regression NNs are often limited in scope and rely primarily on empirical validation, with only a few offering partial theoretical guarantees. In this paper, we propose a new robust learning framework for regression NNs based on the $β$-divergence (also known as the density power divergence) which we call `rRNet'. It applies to a broad class of regression NNs, including models with non-smooth activation functions and error densities, and recovers the classical maximum likelihood learning as a special case. The rRNet is implemented via an alternating optimization scheme, for which we establish convergence guarantees to stationary points under mild, verifiable conditions. The (local) robustness of rRNet is theoretically characterized through the influence functions of both the parameter estimates and the resulting rRNet predictor, which are shown to be bounded for suitable choices of the tuning parameter $β$, depending on the error density. We further prove that rRNet attains the optimal 50\% asymptotic breakdown point at the assumed model for all $β\in(0, 1]$, providing a strong global robustness guarantee that is largely absent for existing NN learning methods. Our theoretical results are complemented by simulation experiments and real-data analyses, illustrating practical advantages of rRNet over existing approaches in both function approximation problems and prediction tasks with noisy observations.

