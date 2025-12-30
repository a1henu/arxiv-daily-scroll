---
layout: default
title: Clipped Gradient Methods for Nonsmooth Convex Optimization under Heavy-Tailed Noise: A Refined Analysis
---

# Clipped Gradient Methods for Nonsmooth Convex Optimization under Heavy-Tailed Noise: A Refined Analysis
**arXiv**：[2512.23178v1](https://arxiv.org/abs/2512.23178) · [PDF](https://arxiv.org/pdf/2512.23178.pdf)  
**作者**：Zijian Liu  

**一句话要点**：提出改进的梯度裁剪方法，在重尾噪声下优化非光滑凸问题，提升收敛速率。

**关键词**：重尾噪声优化, 梯度裁剪, 非光滑凸优化, 收敛分析, 广义有效维度, 高概率收敛

## 3 点简述
- 研究重尾噪声下的非光滑凸优化问题，噪声具有有界p阶矩而非有限二阶矩。
- 通过改进Freedman不等式和裁剪误差分析，提出更快的收敛速率，引入广义有效维度概念。
- 获得新的高概率和期望收敛速率，匹配下界，证明期望收敛最优性。

## 摘要（原文）

> Optimization under heavy-tailed noise has become popular recently, since it better fits many modern machine learning tasks, as captured by empirical observations. Concretely, instead of a finite second moment on gradient noise, a bounded ${\frak p}$-th moment where ${\frak p}\in(1,2]$ has been recognized to be more realistic (say being upper bounded by $σ_{\frak l}^{\frak p}$ for some $σ_{\frak l}\ge0$). A simple yet effective operation, gradient clipping, is known to handle this new challenge successfully. Specifically, Clipped Stochastic Gradient Descent (Clipped SGD) guarantees a high-probability rate ${\cal O}(σ_{\frak l}\ln(1/δ)T^{1/{\frak p}-1})$ (resp. ${\cal O}(σ_{\frak l}^2\ln^2(1/δ)T^{2/{\frak p}-2})$) for nonsmooth convex (resp. strongly convex) problems, where $δ\in(0,1]$ is the failure probability and $T\in\mathbb{N}$ is the time horizon. In this work, we provide a refined analysis for Clipped SGD and offer two faster rates, ${\cal O}(σ_{\frak l}d_{\rm eff}^{-1/2{\frak p}}\ln^{1-1/{\frak p}}(1/δ)T^{1/{\frak p}-1})$ and ${\cal O}(σ_{\frak l}^2d_{\rm eff}^{-1/{\frak p}}\ln^{2-2/{\frak p}}(1/δ)T^{2/{\frak p}-2})$, than the aforementioned best results, where $d_{\rm eff}\ge1$ is a quantity we call the $\textit{generalized effective dimension}$. Our analysis improves upon the existing approach on two sides: better utilization of Freedman's inequality and finer bounds for clipping error under heavy-tailed noise. In addition, we extend the refined analysis to convergence in expectation and obtain new rates that break the known lower bounds. Lastly, to complement the study, we establish new lower bounds for both high-probability and in-expectation convergence. Notably, the in-expectation lower bounds match our new upper bounds, indicating the optimality of our refined analysis for convergence in expectation.

