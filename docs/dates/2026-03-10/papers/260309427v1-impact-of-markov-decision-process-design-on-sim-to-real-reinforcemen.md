---
layout: default
title: Impact of Markov Decision Process Design on Sim-to-Real Reinforcement Learning
---

# Impact of Markov Decision Process Design on Sim-to-Real Reinforcement Learning
**arXiv**：[2603.09427v1](https://arxiv.org/abs/2603.09427) · [PDF](https://arxiv.org/pdf/2603.09427.pdf)  
**作者**：Tatjana Krau, Jorge Mandlmaier, Tobias Damm, Frieder Heieck  

**一句话要点**：分析MDP设计对强化学习仿真到现实迁移的影响，提供工业过程控制部署指南

**关键词**：强化学习, 仿真到现实迁移, 马尔可夫决策过程设计, 工业过程控制, 动力学模型

## 3 点简述
- 核心问题：仿真训练的强化学习策略在物理硬件部署时存在显著的仿真到现实差距
- 方法要点：系统分析MDP设计选择，包括状态组成、目标包含、奖励公式、终止标准和环境动力学模型
- 实验或效果：基于颜色混合任务验证，物理动力学模型在严格精度约束下实现高达50%的现实成功率

## 摘要（原文）

> Reinforcement Learning (RL) has demonstrated strong potential for industrial process control, yet policies trained in simulation often suffer from a significant sim-to-real gap when deployed on physical hardware. This work systematically analyzes how core Markov Decision Process (MDP) design choices -- state composition, target inclusion, reward formulation, termination criteria, and environment dynamics models -- affect this transfer. Using a color mixing task, we evaluate different MDP configurations and mixing dynamics across simulation and real-world experiments. We validate our findings on physical hardware, demonstrating that physics-based dynamics models achieve up to 50% real-world success under strict precision constraints where simplified models fail entirely. Our results provide practical MDP design guidelines for deploying RL in industrial process control.

