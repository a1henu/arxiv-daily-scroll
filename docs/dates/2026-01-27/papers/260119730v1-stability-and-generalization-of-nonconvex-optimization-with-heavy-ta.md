---
layout: default
title: Stability and Generalization of Nonconvex Optimization with Heavy-Tailed Noise
---

# Stability and Generalization of Nonconvex Optimization with Heavy-Tailed Noise
**arXiv**：[2601.19730v1](https://arxiv.org/abs/2601.19730) · [PDF](https://arxiv.org/pdf/2601.19730.pdf)  
**作者**：Hongxu Chen, Ke Wei, Xiaoming Yuan, Luo Luo  

**一句话要点**：提出基于截断论证的框架，分析重尾梯度噪声下随机算法的稳定性与泛化界

**关键词**：重尾噪声, 泛化界, 算法稳定性, 随机优化, 截断论证, 非凸优化

## 3 点简述
- 核心问题：重尾梯度噪声下随机优化算法的泛化界分析有限，现有研究多关注收敛性
- 方法要点：引入截断论证，在p阶中心矩有界假设下，基于算法稳定性建立泛化误差界
- 实验或效果：框架应用于裁剪和归一化SGD及其变体，提供稳定性与泛化分析

## 摘要（原文）

> The empirical evidence indicates that stochastic optimization with heavy-tailed gradient noise is more appropriate to characterize the training of machine learning models than that with standard bounded gradient variance noise. Most existing works on this phenomenon focus on the convergence of optimization errors, while the analysis for generalization bounds under the heavy-tailed gradient noise remains limited. In this paper, we develop a general framework for establishing generalization bounds under heavy-tailed noise. Specifically, we introduce a truncation argument to achieve the generalization error bound based on the algorithmic stability under the assumption of bounded $p$th centered moment with $p\in(1,2]$. Building on this framework, we further provide the stability and generalization analysis for several popular stochastic algorithms under heavy-tailed noise, including clipped and normalized stochastic gradient descent, as well as their mini-batch and momentum variants.

