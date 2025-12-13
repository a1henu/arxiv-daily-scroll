---
layout: default
title: Flexible Deep Neural Networks for Partially Linear Survival Data
---

# Flexible Deep Neural Networks for Partially Linear Survival Data
**arXiv**：[2512.10570v1](https://arxiv.org/abs/2512.10570) · [PDF](https://arxiv.org/pdf/2512.10570.pdf)  
**作者**：Asaf Ben Arie, Malka Gorfine  

**一句话要点**：提出FLEXI-Haz框架，用于部分线性生存数据的灵活建模，无需比例风险假设。

**关键词**：生存分析, 深度神经网络, 部分线性模型, 非参数估计, 比例风险假设

## 3 点简述
- 核心问题：生存数据建模需平衡解释性与灵活性，现有方法依赖比例风险假设。
- 方法要点：结合参数线性与非参数深度神经网络，分别处理主变量和干扰变量交互。
- 实验或效果：理论保证最优收敛率，模拟和真实数据验证线性效应估计准确。

## 摘要（原文）

> We propose a flexible deep neural network (DNN) framework for modeling survival data within a partially linear regression structure. The approach preserves interpretability through a parametric linear component for covariates of primary interest, while a nonparametric DNN component captures complex time-covariate interactions among nuisance variables. We refer to the method as FLEXI-Haz, a flexible hazard model with a partially linear structure. In contrast to existing DNN approaches for partially linear Cox models, FLEXI-Haz does not rely on the proportional hazards assumption. We establish theoretical guarantees: the neural network component attains minimax-optimal convergence rates based on composite Holder classes, and the linear estimator is root-n consistent, asymptotically normal, and semiparametrically efficient. Extensive simulations and real-data analyses demonstrate that FLEXI-Haz provides accurate estimation of the linear effect, offering a principled and interpretable alternative to modern methods based on proportional hazards. Code for implementing FLEXI-Haz, as well as scripts for reproducing data analyses and simulations, is available at: https://github.com/AsafBanana/FLEXI-Haz

