---
layout: default
title: Preventing Learning Stagnation in PPO by Scaling to 1 Million Parallel Environments
---

# Preventing Learning Stagnation in PPO by Scaling to 1 Million Parallel Environments
**arXiv**：[2603.06009v1](https://arxiv.org/abs/2603.06009) · [PDF](https://arxiv.org/pdf/2603.06009.pdf)  
**作者**：Michael Beukman, Khimya Khetarpal, Zeyu Zheng, Will Dabney, Jakob Foerster, Michael Dennis, Clare Lyle  

**一句话要点**：通过扩展至百万并行环境解决PPO学习停滞问题

**关键词**：PPO算法, 学习停滞, 并行环境, 随机优化, 超参数缩放, 强化学习

## 3 点简述
- 核心问题：PPO训练中性能停滞源于样本估计损失与真实目标偏差，而非探索或优化挑战。
- 方法要点：将PPO外循环建模为随机优化，通过增加并行环境数减少步长和噪声以缓解停滞。
- 实验或效果：提出超参数协同缩放方法，在复杂开放域中实现单调性能提升至万亿转移。

## 摘要（原文）

> Plateaus, where an agent's performance stagnates at a suboptimal level, are a common problem in deep on-policy RL. Focusing on PPO due to its widespread adoption, we show that plateaus in certain regimes arise not because of known exploration, capacity, or optimization challenges, but because sample-based estimates of the loss eventually become poor proxies for the true objective over the course of training. As a recap, PPO switches between sampling rollouts from several parallel environments online using the current policy (which we call the outer loop) and performing repeated minibatch SGD steps against this offline dataset (the inner loop). In our work we consider only the outer loop, and conceptually model it as stochastic optimization. The step size is then controlled by the regularization strength towards the previous policy and the gradient noise by the number of samples collected between policy update steps. This model predicts that performance will plateau at a suboptimal level if the outer step size is too large relative to the noise. Recasting PPO in this light makes it clear that there are two ways to address this particular type of learning stagnation: either reduce the step size or increase the number of samples collected between updates. We first validate the predictions of our model and investigate how hyperparameter choices influence the step size and update noise, concluding that increasing the number of parallel environments is a simple and robust way to reduce both factors. Next, we propose a recipe for how to co-scale the other hyperparameters when increasing parallelization, and show that incorrectly doing so can lead to severe performance degradation. Finally, we vastly outperform prior baselines in a complex open-ended domain by scaling PPO to more than 1M parallel environments, thereby enabling monotonic performance improvement up to one trillion transitions.

