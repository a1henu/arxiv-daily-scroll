---
layout: default
title: Sparse Masked Attention Policies for Reliable Generalization
---

# Sparse Masked Attention Policies for Reliable Generalization
**arXiv**：[2602.19956v1](https://arxiv.org/abs/2602.19956) · [PDF](https://arxiv.org/pdf/2602.19956.pdf)  
**作者**：Caroline Horsch, Laurens Engwegen, Max Weltevrede, Matthijs T. J. Spaan, Wendelin Böhmer  

**一句话要点**：提出稀疏掩码注意力策略，以提升强化学习中策略在未见任务上的可靠泛化能力。

**关键词**：强化学习, 策略泛化, 注意力机制, 稀疏掩码, Procgen基准, 信息移除

## 3 点简述
- 核心问题：现有抽象方法中，信息提取函数的泛化能力在未见观测中未知，影响策略可靠性。
- 方法要点：通过学习的掩码函数，在基于注意力的策略网络中操作和集成注意力权重，以移除不必要信息。
- 实验或效果：在Procgen基准测试中，相比标准PPO和掩码方法，显著提升了策略在未见任务上的泛化性能。

## 摘要（原文）

> In reinforcement learning, abstraction methods that remove unnecessary information from the observation are commonly used to learn policies which generalize better to unseen tasks. However, these methods often overlook a crucial weakness: the function which extracts the reduced-information representation has unknown generalization ability in unseen observations. In this paper, we address this problem by presenting an information removal method which more reliably generalizes to new states. We accomplish this by using a learned masking function which operates on, and is integrated with, the attention weights within an attention-based policy network. We demonstrate that our method significantly improves policy generalization to unseen tasks in the Procgen benchmark compared to standard PPO and masking approaches.

