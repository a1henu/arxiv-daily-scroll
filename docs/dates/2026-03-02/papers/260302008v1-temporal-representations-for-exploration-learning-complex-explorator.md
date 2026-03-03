---
layout: default
title: Temporal Representations for Exploration: Learning Complex Exploratory Behavior without Extrinsic Rewards
---

# Temporal Representations for Exploration: Learning Complex Exploratory Behavior without Extrinsic Rewards
**arXiv**：[2603.02008v1](https://arxiv.org/abs/2603.02008) · [PDF](https://arxiv.org/pdf/2603.02008.pdf)  
**作者**：Faisal Mohamed, Catherine Ji, Benjamin Eysenbach, Glen Berseth  

**一句话要点**：提出基于时间对比表示的探索方法，以在无外部奖励下学习复杂探索行为

**关键词**：时间表示学习, 强化学习探索, 对比学习, 无奖励学习, 具身AI

## 3 点简述
- 核心问题：强化学习中有效探索需理解环境表示，避免高计算成本
- 方法要点：利用时间对比表示引导探索，优先未来结果不可预测的状态
- 实验或效果：在运动、操作和具身AI任务中展示复杂探索能力，无需外部奖励

## 摘要（原文）

> Effective exploration in reinforcement learning requires not only tracking where an agent has been, but also understanding how the agent perceives and represents the world. To learn powerful representations, an agent should actively explore states that contribute to its knowledge of the environment. Temporal representations can capture the information necessary to solve a wide range of potential tasks while avoiding the computational cost associated with full state reconstruction. In this paper, we propose an exploration method that leverages temporal contrastive representations to guide exploration, prioritizing states with unpredictable future outcomes. We demonstrate that such representations can enable the learning of complex exploratory x in locomotion, manipulation, and embodied-AI tasks, revealing capabilities and behaviors that traditionally require extrinsic rewards. Unlike approaches that rely on explicit distance learning or episodic memory mechanisms (e.g., quasimetric-based methods), our method builds directly on temporal similarities, yielding a simpler yet effective strategy for exploration.

