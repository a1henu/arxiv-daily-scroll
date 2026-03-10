---
layout: default
title: Towards Batch-to-Streaming Deep Reinforcement Learning for Continuous Control
---

# Towards Batch-to-Streaming Deep Reinforcement Learning for Continuous Control
**arXiv**：[2603.08588v1](https://arxiv.org/abs/2603.08588) · [PDF](https://arxiv.org/pdf/2603.08588.pdf)  
**作者**：Riccardo De Monte, Matteo Cederle, Gian Antonio Susto  

**一句话要点**：提出S2AC和SDAC流式深度强化学习算法，用于连续控制任务中的设备端微调。

**关键词**：流式深度强化学习, 连续控制, 设备端微调, 在线更新, Sim2Real迁移

## 3 点简述
- 核心问题：传统深度强化学习方法计算复杂，不适用于资源受限硬件。
- 方法要点：设计流式算法，通过纯在线更新，兼容批量方法，无需繁琐超参数调优。
- 实验或效果：在标准基准测试中性能与先进流式基线相当，并探讨批量到流式微调的实践挑战。

## 摘要（原文）

> State-of-the-art deep reinforcement learning (RL) methods have achieved remarkable performance in continuous control tasks, yet their computational complexity is often incompatible with the constraints of resource-limited hardware, due to their reliance on replay buffers, batch updates, and target networks. The emerging paradigm of streaming deep RL addresses this limitation through purely online updates, achieving strong empirical performance on standard benchmarks. In this work, we propose two novel streaming deep RL algorithms, Streaming Soft Actor-Critic (S2AC) and Streaming Deterministic Actor-Critic (SDAC), explicitly designed to be compatible with state-of-the-art batch RL methods, making them particularly suitable for on-device finetuning applications such as Sim2Real transfer. Both algorithms achieve performance comparable to state-of-the-art streaming baselines on standard benchmarks without requiring tedious hyperparameter tuning. Finally, we further investigate the practical challenges of transitioning from batch to streaming learning during finetuning and propose concrete strategies to tackle them.

