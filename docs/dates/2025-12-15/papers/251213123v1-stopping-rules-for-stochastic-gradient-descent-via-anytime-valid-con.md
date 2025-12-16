---
layout: default
title: Stopping Rules for Stochastic Gradient Descent via Anytime-Valid Confidence Sequences
---

# Stopping Rules for Stochastic Gradient Descent via Anytime-Valid Confidence Sequences
**arXiv**：[2512.13123v1](https://arxiv.org/abs/2512.13123) · [PDF](https://arxiv.org/pdf/2512.13123.pdf)  
**作者**：Liviu Aolaritei, Michael I. Jordan  

**一句话要点**：提出基于任意时间有效置信序列的随机梯度下降停止规则，用于凸优化

**关键词**：随机梯度下降, 凸优化, 停止规则, 置信序列, 任意时间有效性, 非负超鞅

## 3 点简述
- 核心问题：传统SGD分析缺乏在任意时间评估当前迭代接近最优解的统计有效方法
- 方法要点：通过非负超鞅构建投影SGD加权平均次优性的任意时间有效置信序列，无需平滑性或强凸性
- 实验或效果：停止规则在概率至少1-α下证明为ε-最优，且在标准步长下几乎必然有限

## 摘要（原文）

> We study stopping rules for stochastic gradient descent (SGD) for convex optimization from the perspective of anytime-valid confidence sequences. Classical analyses of SGD provide convergence guarantees in expectation or at a fixed horizon, but offer no statistically valid way to assess, at an arbitrary time, how close the current iterate is to the optimum. We develop an anytime-valid, data-dependent upper confidence sequence for the weighted average suboptimality of projected SGD, constructed via nonnegative supermartingales and requiring no smoothness or strong convexity. This confidence sequence yields a simple stopping rule that is provably $\varepsilon$-optimal with probability at least $1-α$ and is almost surely finite under standard stochastic approximation stepsizes. To the best of our knowledge, these are the first rigorous, time-uniform performance guarantees and finite-time $\varepsilon$-optimality certificates for projected SGD with general convex objectives, based solely on observable trajectory quantities.

