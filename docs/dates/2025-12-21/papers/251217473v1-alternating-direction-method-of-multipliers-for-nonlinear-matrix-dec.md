---
layout: default
title: Alternating Direction Method of Multipliers for Nonlinear Matrix Decompositions
---

# Alternating Direction Method of Multipliers for Nonlinear Matrix Decompositions
**arXiv**：[2512.17473v1](https://arxiv.org/abs/2512.17473) · [PDF](https://arxiv.org/pdf/2512.17473.pdf)  
**作者**：Atharva Awari, Nicolas Gillis, Arnaud Vandaele  

**一句话要点**：提出基于ADMM的算法以解决非线性矩阵分解问题，适用于稀疏数据、概率电路和推荐系统等场景。

**关键词**：非线性矩阵分解, 交替方向乘子法, 稀疏数据近似, 概率电路表示, 推荐系统, 损失函数灵活性

## 3 点简述
- 核心问题：非线性矩阵分解，寻找矩阵W和H使X近似于f(WH)，其中f为逐元素非线性函数。
- 方法要点：使用交替方向乘子法（ADMM）框架，支持多种损失函数如最小二乘、ℓ1范数和KL散度。
- 实验或效果：在真实数据集上评估，涵盖ReLU、平方和MinMax变换等非线性模型，展示方法的适用性和效率。

## 摘要（原文）

> We present an algorithm based on the alternating direction method of multipliers (ADMM) for solving nonlinear matrix decompositions (NMD). Given an input matrix $X \in \mathbb{R}^{m \times n}$ and a factorization rank $r \ll \min(m, n)$, NMD seeks matrices $W \in \mathbb{R}^{m \times r}$ and $H \in \mathbb{R}^{r \times n}$ such that $X \approx f(WH)$, where $f$ is an element-wise nonlinear function. We evaluate our method on several representative nonlinear models: the rectified linear unit activation $f(x) = \max(0, x)$, suitable for nonnegative sparse data approximation, the component-wise square $f(x) = x^2$, applicable to probabilistic circuit representation, and the MinMax transform $f(x) = \min(b, \max(a, x))$, relevant for recommender systems. The proposed framework flexibly supports diverse loss functions, including least squares, $\ell_1$ norm, and the Kullback-Leibler divergence, and can be readily extended to other nonlinearities and metrics. We illustrate the applicability, efficiency, and adaptability of the approach on real-world datasets, highlighting its potential for a broad range of applications.

