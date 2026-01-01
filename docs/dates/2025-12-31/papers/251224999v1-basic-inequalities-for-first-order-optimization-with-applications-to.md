---
layout: default
title: Basic Inequalities for First-Order Optimization with Applications to Statistical Risk Analysis
---

# Basic Inequalities for First-Order Optimization with Applications to Statistical Risk Analysis
**arXiv**：[2512.24999v1](https://arxiv.org/abs/2512.24999) · [PDF](https://arxiv.org/pdf/2512.24999.pdf)  
**作者**：Seunghoon Paik, Kangjie Zhou, Matus Telgarsky, Ryan J. Tibshirani  

**一句话要点**：提出一阶优化基本不等式框架，连接隐式和显式正则化以分析统计风险。

**关键词**：一阶优化, 统计风险分析, 正则化, 梯度下降, 镜像下降, 广义线性模型

## 3 点简述
- 核心问题：一阶迭代优化算法的统计风险分析缺乏统一框架。
- 方法要点：引入基本不等式，通过步长和距离上界目标函数差，将迭代次数转化为有效正则化系数。
- 实验或效果：应用于梯度下降、镜像下降等算法，提供新理论结果并通过广义线性模型实验验证。

## 摘要（原文）

> We introduce \textit{basic inequalities} for first-order iterative optimization algorithms, forming a simple and versatile framework that connects implicit and explicit regularization. While related inequalities appear in the literature, we isolate and highlight a specific form and develop it as a well-rounded tool for statistical analysis. Let $f$ denote the objective function to be optimized. Given a first-order iterative algorithm initialized at $θ_0$ with current iterate $θ_T$, the basic inequality upper bounds $f(θ_T)-f(z)$ for any reference point $z$ in terms of the accumulated step sizes and the distances between $θ_0$, $θ_T$, and $z$. The bound translates the number of iterations into an effective regularization coefficient in the loss function. We demonstrate this framework through analyses of training dynamics and prediction risk bounds. In addition to revisiting and refining known results on gradient descent, we provide new results for mirror descent with Bregman divergence projection, for generalized linear models trained by gradient descent and exponentiated gradient descent, and for randomized predictors. We illustrate and supplement these theoretical findings with experiments on generalized linear models.

