---
layout: default
title: A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer
---

# A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer
**arXiv**：[2602.09810v1](https://arxiv.org/abs/2602.09810) · [PDF](https://arxiv.org/pdf/2602.09810.pdf)  
**作者**：Azka Nasir, Fatima Dossa, Muhammad Ahmed Atif, Mohammad Ahmed Atif  

**一句话要点**：比较DDQN与Dueling DQN在跨环境迁移中的表现，发现DDQN避免负迁移而Dueling DQN易受负迁移影响。

**关键词**：深度强化学习, 迁移学习, 负迁移, DDQN, Dueling DQN, 跨环境迁移

## 3 点简述
- 核心问题：深度强化学习中架构差异如何影响跨环境迁移的稳定性与性能。
- 方法要点：使用固定层表示迁移协议，在CartPole和LunarLander环境中对比DDQN与Dueling DQN。
- 实验或效果：DDQN避免负迁移，性能接近基线；Dueling DQN出现负迁移，奖励下降且优化不稳定。

## 摘要（原文）

> Transfer learning in deep reinforcement learning is often motivated by improved stability and reduced training cost, but it can also fail under substantial domain shift. This paper presents a controlled empirical study examining how architectural differences between Double Deep Q-Networks (DDQN) and Dueling DQN influence transfer behavior across environments. Using CartPole as a source task and LunarLander as a structurally distinct target task, we evaluate a fixed layer-wise representation transfer protocol under identical hyperparameters and training conditions, with baseline agents trained from scratch used to contextualize transfer effects. Empirical results show that DDQN consistently avoids negative transfer under the examined setup and maintains learning dynamics comparable to baseline performance in the target environment. In contrast, Dueling DQN consistently exhibits negative transfer under identical conditions, characterized by degraded rewards and unstable optimization behavior. Statistical analysis across multiple random seeds confirms a significant performance gap under transfer. These findings suggest that architectural inductive bias is strongly associated with robustness to cross-environment transfer in value-based deep reinforcement learning under the examined transfer protocol.

