---
layout: default
title: Adapting Reinforcement Learning for Path Planning in Constrained Parking Scenarios
---

# Adapting Reinforcement Learning for Path Planning in Constrained Parking Scenarios
**arXiv**：[2601.22545v1](https://arxiv.org/abs/2601.22545) · [PDF](https://arxiv.org/pdf/2601.22545.pdf)  
**作者**：Feng Tao, Luca Paparusso, Chenyi Gu, Robin Koehler, Chenxu Wu, Xinyu Huang, Christian Juette, David Paz, Ren Liu  

**一句话要点**：提出深度强化学习框架以解决受限停车场景中的实时路径规划问题

**关键词**：深度强化学习, 路径规划, 停车场景, 实时系统, 闭环控制, 基准数据集

## 3 点简述
- 核心问题：传统规划器在受限环境中计算成本高，对感知约束敏感，难以实时部署。
- 方法要点：基于自行车模型动力学，通过深度强化学习直接学习闭环导航策略，无需理想感知或额外模块。
- 实验或效果：在新建基准上实现领先成功率与效率，超越基线规划器成功率96%、效率52%。

## 摘要（原文）

> Real-time path planning in constrained environments remains a fundamental challenge for autonomous systems. Traditional classical planners, while effective under perfect perception assumptions, are often sensitive to real-world perception constraints and rely on online search procedures that incur high computational costs. In complex surroundings, this renders real-time deployment prohibitive. To overcome these limitations, we introduce a Deep Reinforcement Learning (DRL) framework for real-time path planning in parking scenarios. In particular, we focus on challenging scenes with tight spaces that require a high number of reversal maneuvers and adjustments. Unlike classical planners, our solution does not require ideal and structured perception, and in principle, could avoid the need for additional modules such as localization and tracking, resulting in a simpler and more practical implementation. Also, at test time, the policy generates actions through a single forward pass at each step, which is lightweight enough for real-time deployment. The task is formulated as a sequential decision-making problem grounded in a bicycle model dynamics, enabling the agent to directly learn navigation policies that respect vehicle kinematics and environmental constraints in the closed-loop setting. A new benchmark is developed to support both training and evaluation, capturing diverse and challenging scenarios. Our approach achieves state-of-the-art success rates and efficiency, surpassing classical planner baselines by +96% in success rate and +52% in efficiency. Furthermore, we release our benchmark as an open-source resource for the community to foster future research in autonomous systems. The benchmark and accompanying tools are available at https://github.com/dqm5rtfg9b-collab/Constrained_Parking_Scenarios.

