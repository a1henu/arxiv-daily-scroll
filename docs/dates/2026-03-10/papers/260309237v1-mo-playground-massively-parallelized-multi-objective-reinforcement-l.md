---
layout: default
title: MO-Playground: Massively Parallelized Multi-Objective Reinforcement Learning for Robotics
---

# MO-Playground: Massively Parallelized Multi-Objective Reinforcement Learning for Robotics
**arXiv**：[2603.09237v1](https://arxiv.org/abs/2603.09237) · [PDF](https://arxiv.org/pdf/2603.09237.pdf)  
**作者**：Neil Janwani, Ellen Novoseller, Vernon J. Lawhern, Maegan Tucker  

**一句话要点**：提出MORLAX算法与MO-Playground环境以加速多目标强化学习在机器人应用中的计算。

**关键词**：多目标强化学习, GPU加速, 机器人控制, 帕累托优化, 并行计算

## 3 点简述
- 核心问题：现有MORL算法无法有效利用大规模并行化，导致计算时间长，限制复杂机器人问题应用。
- 方法要点：开发GPU原生的MORLAX算法和可pip安装的MO-Playground环境，支持GPU加速并行模拟。
- 实验或效果：相比传统CPU方法，实现25-270倍加速，并在BRUCE人形机器人环境中学习6个目标的帕累托最优策略。

## 摘要（原文）

> Multi-objective reinforcement learning (MORL) is a powerful tool to learn Pareto-optimal policy families across conflicting objectives. However, unlike traditional RL algorithms, existing MORL algorithms do not effectively leverage large-scale parallelization to concurrently simulate thousands of environments, resulting in vastly increased computation time. Ultimately, this has limited MORL's application towards complex multi-objective robotics problems. To address these challenges, we present 1) MORLAX, a new GPU-native, fast MORL algorithm, and 2) MO-Playground, a pip-installable playground of GPU-accelerated multi-objective environments. Together, MORLAX and MO-Playground approximate Pareto sets within minutes, offering 25-270x speed-ups compared to legacy CPU-based approaches whilst achieving superior Pareto front hypervolumes. We demonstrate the versatility of our approach by implementing a custom BRUCE humanoid robot environment using MO-Playground and learning Pareto-optimal locomotion policies across 6 realistic objectives for BRUCE, such as smoothness, efficiency and arm swinging.

