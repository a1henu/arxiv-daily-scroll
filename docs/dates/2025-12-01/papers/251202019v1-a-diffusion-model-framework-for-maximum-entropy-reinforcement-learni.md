---
layout: default
title: A Diffusion Model Framework for Maximum Entropy Reinforcement Learning
---

# A Diffusion Model Framework for Maximum Entropy Reinforcement Learning
**arXiv**：[2512.02019v1](https://arxiv.org/abs/2512.02019) · [PDF](https://arxiv.org/pdf/2512.02019.pdf)  
**作者**：Sebastian Sanokowski, Kaustubh Patil, Alois Knoll  

**一句话要点**：提出基于扩散模型的框架以改进最大熵强化学习，提升连续控制任务的性能与样本效率。

**关键词**：扩散模型, 最大熵强化学习, 策略优化, 连续控制, 样本效率

## 3 点简述
- 核心问题：将最大熵强化学习重新解释为扩散模型采样问题，以处理复杂策略分布。
- 方法要点：通过最小化反向KL散度的上界，结合扩散动态推导改进的代理目标。
- 实验或效果：在标准基准上，DiffSAC、DiffPPO和DiffWPO优于SAC和PPO，实现更高回报和样本效率。

## 摘要（原文）

> Diffusion models have achieved remarkable success in data-driven learning and in sampling from complex, unnormalized target distributions. Building on this progress, we reinterpret Maximum Entropy Reinforcement Learning (MaxEntRL) as a diffusion model-based sampling problem. We tackle this problem by minimizing the reverse Kullback-Leibler (KL) divergence between the diffusion policy and the optimal policy distribution using a tractable upper bound. By applying the policy gradient theorem to this objective, we derive a modified surrogate objective for MaxEntRL that incorporates diffusion dynamics in a principled way. This leads to simple diffusion-based variants of Soft Actor-Critic (SAC), Proximal Policy Optimization (PPO) and Wasserstein Policy Optimization (WPO), termed DiffSAC, DiffPPO and DiffWPO. All of these methods require only minor implementation changes to their base algorithm. We find that on standard continuous control benchmarks, DiffSAC, DiffPPO and DiffWPO achieve better returns and higher sample efficiency than SAC and PPO.

