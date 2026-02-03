---
layout: default
title: Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards
---

# Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards
**arXiv**：[2602.01601v1](https://arxiv.org/abs/2602.01601) · [PDF](https://arxiv.org/pdf/2602.01601.pdf)  
**作者**：Hieu Trung Nguyen, Bao Nguyen, Wenao Ma, Yuzhi Zhao, Ruifeng She, Viet Anh Nguyen  

**一句话要点**：提出VIP策略以优化可验证奖励强化学习中的采样效率

**关键词**：强化学习, 采样效率, 可验证奖励, 高斯过程, 凸优化, 策略优化

## 3 点简述
- 核心问题：固定采样分配忽视提示信息差异，导致计算预算浪费
- 方法要点：基于高斯过程预测成功概率，通过凸优化最小化梯度方差分配采样
- 实验或效果：在多个基准测试中提升采样效率和性能，优于均匀或启发式分配

## 摘要（原文）

> Sampling efficiency is a key bottleneck in reinforcement learning with verifiable rewards. Existing group-based policy optimization methods, such as GRPO, allocate a fixed number of rollouts for all training prompts. This uniform allocation implicitly treats all prompts as equally informative, and could lead to inefficient computational budget usage and impede training progress. We introduce \Ours, a Variance-Informed Predictive allocation strategy that allocates a given rollout budget to the prompts in the incumbent batch to minimize the expected gradient variance of the policy update. At each iteration, \Ours~uses a lightweight Gaussian process model to predict per-prompt success probabilities based on recent rollouts. These probability predictions are translated into variance estimates, which are then fed into a convex optimization problem to determine the optimal rollout allocations under a hard compute budget constraint. Empirical results show that \Ours~consistently improves sampling efficiency and achieves higher performance than uniform or heuristic allocation strategies in multiple benchmarks. Our code will be available at https://github.com/HieuNT91/VIP.

