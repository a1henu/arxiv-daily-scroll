---
layout: default
title: Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game
---

# Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game
**arXiv**：[2512.16626v1](https://arxiv.org/abs/2512.16626) · [PDF](https://arxiv.org/pdf/2512.16626.pdf)  
**作者**：Barna Pásztor, Thomas Kleine Buening, Andreas Krause  

**一句话要点**：提出Stackelberg Learning from Human Feedback，将偏好优化建模为顺序博弈以增强对齐能力。

**关键词**：偏好优化, 顺序博弈, 对齐学习, 推理时精炼, 大语言模型

## 3 点简述
- 核心问题：传统RLHF和NLHF在捕捉复杂偏好结构方面存在局限，如非传递性偏好。
- 方法要点：将策略分为领导者和跟随者，通过顺序博弈分解优化问题，支持推理时精炼。
- 实验或效果：在大语言模型上验证，实现强对齐、参数可扩展性及跨模型精炼迁移。

## 摘要（原文）

> We introduce Stackelberg Learning from Human Feedback (SLHF), a new framework for preference optimization. SLHF frames the alignment problem as a sequential-move game between two policies: a Leader, which commits to an action, and a Follower, which responds conditionally on the Leader's action. This approach decomposes preference optimization into a refinement problem for the Follower and an optimization problem against an adversary for the Leader. Unlike Reinforcement Learning from Human Feedback (RLHF), which assigns scalar rewards to actions, or Nash Learning from Human Feedback (NLHF), which seeks a simultaneous-move equilibrium, SLHF leverages the asymmetry of sequential play to capture richer preference structures. The sequential design of SLHF naturally enables inference-time refinement, as the Follower learns to improve the Leader's actions, and these refinements can be leveraged through iterative sampling. We compare the solution concepts of SLHF, RLHF, and NLHF, and lay out key advantages in consistency, data sensitivity, and robustness to intransitive preferences. Experiments on large language models demonstrate that SLHF achieves strong alignment across diverse preference datasets, scales from 0.5B to 8B parameters, and yields inference-time refinements that transfer across model families without further fine-tuning.

