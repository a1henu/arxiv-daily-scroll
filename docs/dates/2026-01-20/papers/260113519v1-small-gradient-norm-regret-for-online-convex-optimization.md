---
layout: default
title: Small Gradient Norm Regret for Online Convex Optimization
---

# Small Gradient Norm Regret for Online Convex Optimization
**arXiv**：[2601.13519v1](https://arxiv.org/abs/2601.13519) · [PDF](https://arxiv.org/pdf/2601.13519.pdf)  
**作者**：Wenzhi Gao, Chang He, Madeleine Udell  

**一句话要点**：提出G*遗憾度量以改进在线凸优化中平滑损失的后悔分析

**关键词**：在线凸优化, 后悔分析, 平滑损失, 梯度范数, 动态后悔, 赌博机学习

## 3 点简述
- 针对平滑损失的在线凸优化，引入基于后见决策累积梯度平方范数的新后悔度量G*
- 证明G*遗憾严格优于现有L*遗憾，在损失函数于后见决策处曲率消失时可任意更尖锐
- 建立G*遗憾的上下界，扩展至动态后悔和赌博机设置，并改进插值机制下随机优化算法的收敛分析

## 摘要（原文）

> This paper introduces a new problem-dependent regret measure for online convex optimization with smooth losses. The notion, which we call the $G^\star$ regret, depends on the cumulative squared gradient norm evaluated at the decision in hindsight $\sum_{t=1}^T \\|\nabla \ell(x^\star)\\|^2$. We show that the $G^\star$ regret strictly refines the existing $L^\star$ (small loss) regret, and that it can be arbitrarily sharper when the losses have vanishing curvature around the hindsight decision. We establish upper and lower bounds on the $G^\star$ regret and extend our results to dynamic regret and bandit settings. As a byproduct, we refine the existing convergence analysis of stochastic optimization algorithms in the interpolation regime. Some experiments validate our theoretical findings.

