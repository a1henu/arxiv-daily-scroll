---
layout: default
title: Reward-Conditioned Reinforcement Learning
---

# Reward-Conditioned Reinforcement Learning
**arXiv**：[2603.05066v1](https://arxiv.org/abs/2603.05066) · [PDF](https://arxiv.org/pdf/2603.05066.pdf)  
**作者**：Michal Nauman, Marek Cygan, Pieter Abbeel  

**一句话要点**：提出奖励条件强化学习框架，以解决单一奖励函数下策略脆弱和适应性问题。

**关键词**：奖励条件强化学习, 离策略学习, 多任务学习, 策略适应, 奖励参数化, 稳健策略

## 3 点简述
- 核心问题：传统强化学习在固定奖励函数下训练，导致策略对奖励误设敏感且难以适应任务偏好变化。
- 方法要点：通过奖励参数化条件化智能体，利用共享回放数据离策略学习多个奖励目标，实现单一策略表示奖励特定行为。
- 实验或效果：在单任务、多任务和视觉基准测试中，提升名义奖励性能并高效适应新参数化，展示可扩展的稳健可控策略学习。

## 摘要（原文）

> RL agents are typically trained under a single, fixed reward function, which makes them brittle to reward misspecification and limits their ability to adapt to changing task preferences. We introduce Reward-Conditioned Reinforcement Learning (RCRL), a framework that trains a single agent to optimize a family of reward specifications while collecting experience under only one nominal objective. RCRL conditions the agent on reward parameterizations and learns multiple reward objectives from a shared replay data entirely off-policy, enabling a single policy to represent reward-specific behaviors. Across single-task, multi-task, and vision-based benchmarks, we show that RCRL not only improves performance under the nominal reward parameterization, but also enables efficient adaptation to new parameterizations. Our results demonstrate that RCRL provides a scalable mechanism for learning robust, steerable policies without sacrificing the simplicity of single-task training.

