---
layout: default
title: Riesz Representer Fitting under Bregman Divergence: A Unified Framework for Debiased Machine Learning
---

# Riesz Representer Fitting under Bregman Divergence: A Unified Framework for Debiased Machine Learning
**arXiv**：[2601.07752v1](https://arxiv.org/abs/2601.07752) · [PDF](https://arxiv.org/pdf/2601.07752.pdf)  
**作者**：Masahiro Kato  

**一句话要点**：提出广义Riesz回归框架，在Bregman散度下统一Riesz表示器估计方法，用于去偏机器学习。

**关键词**：去偏机器学习, Riesz表示器估计, Bregman散度, 广义Riesz回归, 协变量平衡

## 3 点简述
- 核心问题：Riesz表示器估计是去偏机器学习中因果和结构参数估计的关键问题。
- 方法要点：在Bregman散度下拟合Riesz表示器模型，统一Riesz回归和协变量平衡等方法。
- 实验或效果：提供收敛分析，覆盖再生核希尔伯特空间和神经网络模型类。

## 摘要（原文）

> Estimating the Riesz representer is a central problem in debiased machine learning for causal and structural parameter estimation. Various methods for Riesz representer estimation have been proposed, including Riesz regression and covariate balancing. This study unifies these methods within a single framework. Our framework fits a Riesz representer model to the true Riesz representer under a Bregman divergence, which includes the squared loss and the Kullback--Leibler (KL) divergence as special cases. We show that the squared loss corresponds to Riesz regression, and the KL divergence corresponds to tailored loss minimization, where the dual solutions correspond to stable balancing weights and entropy balancing weights, respectively, under specific model specifications. We refer to our method as generalized Riesz regression, and we refer to the associated duality as automatic covariate balancing. Our framework also generalizes density ratio fitting under a Bregman divergence to Riesz representer estimation, and it includes various applications beyond density ratio estimation. We also provide a convergence analysis for both cases where the model class is a reproducing kernel Hilbert space (RKHS) and where it is a neural network.

