---
layout: default
title: Intrinsic Reward Policy Optimization for Sparse-Reward Environments
---

# Intrinsic Reward Policy Optimization for Sparse-Reward Environments
**arXiv**：[2601.21391v1](https://arxiv.org/abs/2601.21391) · [PDF](https://arxiv.org/pdf/2601.21391.pdf)  
**作者**：Minjae Cho, Huy Trong Tran  

**一句话要点**：提出内在奖励策略优化框架，以解决稀疏奖励环境中的探索问题。

**关键词**：强化学习, 稀疏奖励, 内在奖励, 策略优化, 探索策略, 样本效率

## 3 点简述
- 核心问题：稀疏奖励下，传统探索策略如噪声注入效果不佳，内在奖励方法存在信用分配不稳定或样本效率低。
- 方法要点：利用多个内在奖励直接优化策略，无需预训练子策略，通过代理策略梯度提供更丰富学习信号。
- 实验或效果：在离散和连续环境中，相比基线方法，提升了性能和样本效率，并进行了形式化分析。

## 摘要（原文）

> Exploration is essential in reinforcement learning as an agent relies on trial and error to learn an optimal policy. However, when rewards are sparse, naive exploration strategies, like noise injection, are often insufficient. Intrinsic rewards can also provide principled guidance for exploration by, for example, combining them with extrinsic rewards to optimize a policy or using them to train subpolicies for hierarchical learning. However, the former approach suffers from unstable credit assignment, while the latter exhibits sample inefficiency and sub-optimality. We propose a policy optimization framework that leverages multiple intrinsic rewards to directly optimize a policy for an extrinsic reward without pretraining subpolicies. Our algorithm -- intrinsic reward policy optimization (IRPO) -- achieves this by using a surrogate policy gradient that provides a more informative learning signal than the true gradient in sparse-reward environments. We demonstrate that IRPO improves performance and sample efficiency relative to baselines in discrete and continuous environments, and formally analyze the optimization problem solved by IRPO. Our code is available at https://github.com/Mgineer117/IRPO.

