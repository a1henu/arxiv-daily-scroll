---
layout: default
title: Deep Legendre Transform
---

# Deep Legendre Transform
**arXiv**：[2512.19649v1](https://arxiv.org/abs/2512.19649) · [PDF](https://arxiv.org/pdf/2512.19649.pdf)  
**作者**：Aleksey Minabutdinov, Patrick Cheridito  

**一句话要点**：提出基于隐式Fenchel公式的深度学习算法，高效计算高维可微凸函数的凸共轭。

**关键词**：凸共轭计算, 深度学习算法, 高维优化, 隐式Fenchel公式, 符号回归

## 3 点简述
- 核心问题：传统数值方法在高维下计算凸共轭面临维度灾难，现有神经网络方法多针对最优传输问题且优化复杂。
- 方法要点：利用隐式Fenchel公式，构建梯度优化框架最小化近似误差，并提供后验误差估计。
- 实验或效果：数值实验显示方法在高维示例中准确，结合符号回归可精确获得特定函数的凸共轭。

## 摘要（原文）

> We introduce a novel deep learning algorithm for computing convex conjugates of differentiable convex functions, a fundamental operation in convex analysis with various applications in different fields such as optimization, control theory, physics and economics. While traditional numerical methods suffer from the curse of dimensionality and become computationally intractable in high dimensions, more recent neural network-based approaches scale better, but have mostly been studied with the aim of solving optimal transport problems and require the solution of complicated optimization or max-min problems. Using an implicit Fenchel formulation of convex conjugation, our approach facilitates an efficient gradient-based framework for the minimization of approximation errors and, as a byproduct, also provides a posteriori error estimates for the approximation quality. Numerical experiments demonstrate our method's ability to deliver accurate results across different high-dimensional examples. Moreover, by employing symbolic regression with Kolmogorov--Arnold networks, it is able to obtain the exact convex conjugates of specific convex functions.

