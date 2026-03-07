---
layout: default
title: Latent Policy Steering through One-Step Flow Policies
---

# Latent Policy Steering through One-Step Flow Policies
**arXiv**：[2603.05296v1](https://arxiv.org/abs/2603.05296) · [PDF](https://arxiv.org/pdf/2603.05296.pdf)  
**作者**：Hokyun Im, Andrey Kolobov, Jianlong Fu, Youngwoon Lee  

**一句话要点**：提出Latent Policy Steering，通过可微分一步流策略实现离线强化学习中的高保真隐空间策略优化。

**关键词**：离线强化学习, 隐空间策略优化, 可微分流策略, 行为约束, 机器人学习

## 3 点简述
- 离线强化学习面临回报最大化与行为约束间的脆弱权衡，易导致策略偏离数据集支持。
- LPS方法通过可微分一步MeanFlow策略，将原始动作空间Q梯度反向传播以更新隐空间行动者，消除代理隐空间评论家。
- 在OGBench和真实机器人任务中，LPS实现最先进性能，优于行为克隆和强隐空间引导基线。

## 摘要（原文）

> Offline reinforcement learning (RL) allows robots to learn from offline datasets without risky exploration. Yet, offline RL's performance often hinges on a brittle trade-off between (1) return maximization, which can push policies outside the dataset support, and (2) behavioral constraints, which typically require sensitive hyperparameter tuning. Latent steering offers a structural way to stay within the dataset support during RL, but existing offline adaptations commonly approximate action values using latent-space critics learned via indirect distillation, which can lose information and hinder convergence. We propose Latent Policy Steering (LPS), which enables high-fidelity latent policy improvement by backpropagating original-action-space Q-gradients through a differentiable one-step MeanFlow policy to update a latent-action-space actor. By eliminating proxy latent critics, LPS allows an original-action-space critic to guide end-to-end latent-space optimization, while the one-step MeanFlow policy serves as a behavior-constrained generative prior. This decoupling yields a robust method that works out-of-the-box with minimal tuning. Across OGBench and real-world robotic tasks, LPS achieves state-of-the-art performance and consistently outperforms behavioral cloning and strong latent steering baselines.

