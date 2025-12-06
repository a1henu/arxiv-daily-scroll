---
layout: default
title: Gradient Descent with Provably Tuned Learning-rate Schedules
---

# Gradient Descent with Provably Tuned Learning-rate Schedules
**arXiv**：[2512.05084v1](https://arxiv.org/abs/2512.05084) · [PDF](https://arxiv.org/pdf/2512.05084.pdf)  
**作者**：Dravyansh Sharma  

**一句话要点**：提出可证明调优学习率计划的方法，适用于非凸非光滑函数优化。

**关键词**：梯度下降, 超参数调优, 非凸优化, 学习率计划, 样本复杂度, 神经网络优化

## 3 点简述
- 核心问题：梯度优化中学习率等超参数通常依赖启发式设置，缺乏理论保证。
- 方法要点：开发新分析工具，在非凸非光滑函数上提供超参数调优的样本复杂度界限。
- 实验或效果：应用于神经网络常用激活函数，扩展至多超参数调优，如学习率计划和动量。

## 摘要（原文）

> Gradient-based iterative optimization methods are the workhorse of modern machine learning. They crucially rely on careful tuning of parameters like learning rate and momentum. However, one typically sets them using heuristic approaches without formal near-optimality guarantees. Recent work by Gupta and Roughgarden studies how to learn a good step-size in gradient descent. However, like most of the literature with theoretical guarantees for gradient-based optimization, their results rely on strong assumptions on the function class including convexity and smoothness which do not hold in typical applications. In this work, we develop novel analytical tools for provably tuning hyperparameters in gradient-based algorithms that apply to non-convex and non-smooth functions. We obtain matching sample complexity bounds for learning the step-size in gradient descent shown for smooth, convex functions in prior work (up to logarithmic factors) but for a much broader class of functions. Our analysis applies to gradient descent on neural networks with commonly used activation functions (including ReLU, sigmoid and tanh). We extend our framework to tuning multiple hyperparameters, including tuning the learning rate schedule, simultaneously tuning momentum and step-size, and pre-training the initialization vector. Our approach can be used to bound the sample complexity for minimizing both the validation loss as well as the number of gradient descent iterations.

