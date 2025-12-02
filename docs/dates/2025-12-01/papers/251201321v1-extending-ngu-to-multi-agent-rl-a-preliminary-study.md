---
layout: default
title: Extending NGU to Multi-Agent RL: A Preliminary Study
---

# Extending NGU to Multi-Agent RL: A Preliminary Study
**arXiv**：[2512.01321v1](https://arxiv.org/abs/2512.01321) · [PDF](https://arxiv.org/pdf/2512.01321.pdf)  
**作者**：Juan Hernandez, Diego Fernández, Manuel Cifuentes, Denis Parra, Rodrigo Toro Icarte  

**一句话要点**：将NGU算法扩展至多智能体强化学习，在PettingZoo的simple_tag环境中评估性能

**关键词**：多智能体强化学习, NGU算法, 内在动机, 稀疏奖励, PettingZoo, 经验共享

## 3 点简述
- 核心问题：多智能体环境中稀疏奖励任务的学习效率与稳定性问题
- 方法要点：将NGU的episodic新奇性与内在动机结合，探索共享回放缓冲区和参数调优设计
- 实验或效果：相比多智能体DQN基线，NGU获得中等更高回报和更稳定学习动态，共享回放缓冲区表现最佳

## 摘要（原文）

> The Never Give Up (NGU) algorithm has proven effective in reinforcement learning tasks with sparse rewards by combining episodic novelty and intrinsic motivation. In this work, we extend NGU to multi-agent environments and evaluate its performance in the simple_tag environment from the PettingZoo suite. Compared to a multi-agent DQN baseline, NGU achieves moderately higher returns and more stable learning dynamics. We investigate three design choices: (1) shared replay buffer versus individual replay buffers, (2) sharing episodic novelty among agents using different k thresholds, and (3) using heterogeneous values of the beta parameter. Our results show that NGU with a shared replay buffer yields the best performance and stability, highlighting that the gains come from combining NGU intrinsic exploration with experience sharing. Novelty sharing performs comparably when k = 1 but degrades learning for larger values. Finally, heterogeneous beta values do not improve over a small common value. These findings suggest that NGU can be effectively applied in multi-agent settings when experiences are shared and intrinsic exploration signals are carefully tuned.

