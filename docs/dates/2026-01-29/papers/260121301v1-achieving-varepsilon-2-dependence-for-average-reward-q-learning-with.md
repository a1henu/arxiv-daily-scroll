---
layout: default
title: Achieving $\varepsilon^{-2}$ Dependence for Average-Reward Q-Learning with a New Contraction Principle
---

# Achieving $\varepsilon^{-2}$ Dependence for Average-Reward Q-Learning with a New Contraction Principle
**arXiv**：[2601.21301v1](https://arxiv.org/abs/2601.21301) · [PDF](https://arxiv.org/pdf/2601.21301.pdf)  
**作者**：Zijun Chen, Zaiwei Chen, Nian Si, Shengbo Wang  

**一句话要点**：提出基于惰性变换的Q学习变体，在平均奖励MDP中实现最优样本复杂度

**关键词**：平均奖励马尔可夫决策过程, Q学习, 样本复杂度, 惰性变换, 半范数收缩

## 3 点简述
- 核心问题：平均奖励MDP中Bellman算子缺乏收缩性，导致收敛分析困难
- 方法要点：引入惰性变换构造实例依赖半范数，证明Bellman算子单步收缩
- 实验或效果：在可达性假设下，同步与异步Q学习达到O(ε^{-2})样本复杂度

## 摘要（原文）

> We present the convergence rates of synchronous and asynchronous Q-learning for average-reward Markov decision processes, where the absence of contraction poses a fundamental challenge. Existing non-asymptotic results overcome this challenge by either imposing strong assumptions to enforce seminorm contraction or relying on discounted or episodic Markov decision processes as successive approximations, which either require unknown parameters or result in suboptimal sample complexity. In this work, under a reachability assumption, we establish optimal $\widetilde{O}(\varepsilon^{-2})$ sample complexity guarantees (up to logarithmic factors) for a simple variant of synchronous and asynchronous Q-learning that samples from the lazified dynamics, where the system remains in the current state with some fixed probability. At the core of our analysis is the construction of an instance-dependent seminorm and showing that, after a lazy transformation of the Markov decision process, the Bellman operator becomes one-step contractive under this seminorm.

