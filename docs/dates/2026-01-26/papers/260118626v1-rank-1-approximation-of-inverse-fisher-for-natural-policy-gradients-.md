---
layout: default
title: Rank-1 Approximation of Inverse Fisher for Natural Policy Gradients in Deep Reinforcement Learning
---

# Rank-1 Approximation of Inverse Fisher for Natural Policy Gradients in Deep Reinforcement Learning
**arXiv**：[2601.18626v1](https://arxiv.org/abs/2601.18626) · [PDF](https://arxiv.org/pdf/2601.18626.pdf)  
**作者**：Yingxiao Huo, Satya Prakash Dash, Radu Stoican, Samuel Kaski, Mingfei Sun  

**一句话要点**：提出基于秩-1近似的自然策略梯度方法，以高效计算逆Fisher信息矩阵。

**关键词**：深度强化学习, 自然策略梯度, Fisher信息矩阵, 秩-1近似, 策略优化, 计算效率

## 3 点简述
- 核心问题：自然梯度计算需迭代求逆Fisher信息矩阵，计算成本高。
- 方法要点：利用秩-1近似替代全逆Fisher信息矩阵，提升效率与可扩展性。
- 实验或效果：在多样环境中验证，性能优于标准演员-评论家和信任区域基线。

## 摘要（原文）

> Natural gradients have long been studied in deep reinforcement learning due to their fast convergence properties and covariant weight updates. However, computing natural gradients requires inversion of the Fisher Information Matrix (FIM) at each iteration, which is computationally prohibitive in nature. In this paper, we present an efficient and scalable natural policy optimization technique that leverages a rank-1 approximation to full inverse-FIM. We theoretically show that under certain conditions, a rank-1 approximation to inverse-FIM converges faster than policy gradients and, under some conditions, enjoys the same sample complexity as stochastic policy gradient methods. We benchmark our method on a diverse set of environments and show that it achieves superior performance to standard actor-critic and trust-region baselines.

