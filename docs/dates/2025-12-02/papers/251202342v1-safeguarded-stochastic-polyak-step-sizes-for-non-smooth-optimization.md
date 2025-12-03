---
layout: default
title: Safeguarded Stochastic Polyak Step Sizes for Non-smooth Optimization: Robust Performance Without Small (Sub)Gradients
---

# Safeguarded Stochastic Polyak Step Sizes for Non-smooth Optimization: Robust Performance Without Small (Sub)Gradients
**arXiv**：[2512.02342v1](https://arxiv.org/abs/2512.02342) · [PDF](https://arxiv.org/pdf/2512.02342.pdf)  
**作者**：Dimitris Oikonomou, Nicolas Loizou  

**一句话要点**：提出Safeguarded SPS以解决非光滑优化中随机梯度消失问题

**关键词**：非光滑优化, 随机梯度下降, 自适应步长, 深度神经网络训练, 收敛分析

## 3 点简述
- 核心问题：随机Polyak步长在非光滑优化中依赖强假设或最优解知识，限制应用。
- 方法要点：引入Safeguarded SPS，结合动量，提供无需强假设的收敛保证。
- 实验或效果：在凸基准和深度神经网络上加速收敛、降低方差，优于现有自适应方法。

## 摘要（原文）

> The stochastic Polyak step size (SPS) has proven to be a promising choice for stochastic gradient descent (SGD), delivering competitive performance relative to state-of-the-art methods on smooth convex and non-convex optimization problems, including deep neural network training. However, extensions of this approach to non-smooth settings remain in their early stages, often relying on interpolation assumptions or requiring knowledge of the optimal solution. In this work, we propose a novel SPS variant, Safeguarded SPS (SPS$_{safe}$), for the stochastic subgradient method, and provide rigorous convergence guarantees for non-smooth convex optimization with no need for strong assumptions. We further incorporate momentum into the update rule, yielding equally tight theoretical results. Comprehensive experiments on convex benchmarks and deep neural networks corroborate our theory: the proposed step size accelerates convergence, reduces variance, and consistently outperforms existing adaptive baselines. Finally, in the context of deep neural network training, our method demonstrates robust performance by addressing the vanishing gradient problem.

