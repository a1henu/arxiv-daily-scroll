---
layout: default
title: RN-D: Discretized Categorical Actors with Regularized Networks for On-Policy Reinforcement Learning
---

# RN-D: Discretized Categorical Actors with Regularized Networks for On-Policy Reinforcement Learning
**arXiv**：[2601.23075v1](https://arxiv.org/abs/2601.23075) · [PDF](https://arxiv.org/pdf/2601.23075.pdf)  
**作者**：Yuexin Bian, Jie Feng, Tao Wang, Yijiang Li, Sicun Gao, Yuanyuan Shi  

**一句话要点**：提出离散化分类演员与正则化网络，以提升连续控制中策略优化的鲁棒性。

**关键词**：连续控制, 策略优化, 离散化演员, 正则化网络, 强化学习

## 3 点简述
- 核心问题：连续控制中高斯演员和浅层MLP策略导致梯度噪声下的脆弱优化。
- 方法要点：使用离散化分类演员表示动作维度分布，结合正则化网络改进策略表示。
- 实验或效果：在多样连续控制基准测试中实现一致性能提升和最优结果。

## 摘要（原文）

> On-policy deep reinforcement learning remains a dominant paradigm for continuous control, yet standard implementations rely on Gaussian actors and relatively shallow MLP policies, often leading to brittle optimization when gradients are noisy and policy updates must be conservative. In this paper, we revisit policy representation as a first-class design choice for on-policy optimization. We study discretized categorical actors that represent each action dimension with a distribution over bins, yielding a policy objective that resembles a cross-entropy loss. Building on architectural advances from supervised learning, we further propose regularized actor networks, while keeping critic design fixed. Our results show that simply replacing the standard actor network with our discretized regularized actor yields consistent gains and achieve the state-of-the-art performance across diverse continuous-control benchmarks.

