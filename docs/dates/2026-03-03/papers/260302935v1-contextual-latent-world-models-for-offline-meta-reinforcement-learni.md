---
layout: default
title: Contextual Latent World Models for Offline Meta Reinforcement Learning
---

# Contextual Latent World Models for Offline Meta Reinforcement Learning
**arXiv**：[2603.02935v1](https://arxiv.org/abs/2603.02935) · [PDF](https://arxiv.org/pdf/2603.02935.pdf)  
**作者**：Mohammadreza Nakheai, Aidan Scannell, Kevin Luck, Joni Pajarinen  

**一句话要点**：提出上下文潜在世界模型，通过任务条件化时间一致性改进离线元强化学习的任务表示学习。

**关键词**：离线元强化学习, 任务表示学习, 潜在世界模型, 上下文编码, 时间一致性, 泛化性能

## 3 点简述
- 核心问题：离线元强化学习中，无监督学习有效任务表示以泛化到未见任务仍具挑战。
- 方法要点：结合上下文编码器与潜在世界模型，通过任务条件化时间一致性联合训练，捕获任务依赖动态。
- 实验或效果：在MuJoCo、Contextual-DeepMind Control和Meta-World基准上显著提升泛化性能。

## 摘要（原文）

> Offline meta-reinforcement learning seeks to learn policies that generalize across related tasks from fixed datasets. Context-based methods infer a task representation from transition histories, but learning effective task representations without supervision remains a challenge. In parallel, latent world models have demonstrated strong self-supervised representation learning through temporal consistency. We introduce contextual latent world models, which condition latent world models on inferred task representations and train them jointly with the context encoder. This enforces task-conditioned temporal consistency, yielding task representations that capture task-dependent dynamics rather than merely discriminating between tasks. Our method learns more expressive task representations and significantly improves generalization to unseen tasks across MuJoCo, Contextual-DeepMind Control, and Meta-World benchmarks.

