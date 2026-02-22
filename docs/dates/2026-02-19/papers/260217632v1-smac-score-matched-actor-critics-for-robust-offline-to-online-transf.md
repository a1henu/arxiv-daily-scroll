---
layout: default
title: SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer
---

# SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer
**arXiv**：[2602.17632v1](https://arxiv.org/abs/2602.17632) · [PDF](https://arxiv.org/pdf/2602.17632.pdf)  
**作者**：Nathan S. de Lara, Florian Shkurti  

**一句话要点**：提出SMAC方法以解决离线强化学习微调时性能下降问题

**关键词**：离线强化学习, 在线微调, 损失景观, Q函数正则化, 性能平滑迁移

## 3 点简述
- 离线强化学习微调时因损失景观中的低性能谷导致性能下降
- SMAC通过正则化Q函数，使策略得分与Q函数动作梯度满足一阶导数等式
- 实验显示SMAC在6/6任务中平滑迁移，在4/6环境中减少遗憾34-58%

## 摘要（原文）

> Modern offline Reinforcement Learning (RL) methods find performant actor-critics, however, fine-tuning these actor-critics online with value-based RL algorithms typically causes immediate drops in performance. We provide evidence consistent with the hypothesis that, in the loss landscape, offline maxima for prior algorithms and online maxima are separated by low-performance valleys that gradient-based fine-tuning traverses. Following this, we present Score Matched Actor-Critic (SMAC), an offline RL method designed to learn actor-critics that transition to online value-based RL algorithms with no drop in performance. SMAC avoids valleys between offline and online maxima by regularizing the Q-function during the offline phase to respect a first-order derivative equality between the score of the policy and action-gradient of the Q-function. We experimentally demonstrate that SMAC converges to offline maxima that are connected to better online maxima via paths with monotonically increasing reward found by first-order optimization. SMAC achieves smooth transfer to Soft Actor-Critic and TD3 in 6/6 D4RL tasks. In 4/6 environments, it reduces regret by 34-58% over the best baseline.

