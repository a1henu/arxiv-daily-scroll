---
layout: default
title: Multi-Objective Reinforcement Learning for Efficient Tactical Decision Making for Trucks in Highway Traffic
---

# Multi-Objective Reinforcement Learning for Efficient Tactical Decision Making for Trucks in Highway Traffic
**arXiv**：[2601.18783v1](https://arxiv.org/abs/2601.18783) · [PDF](https://arxiv.org/pdf/2601.18783.pdf)  
**作者**：Deepthi Pathare, Leo Laine, Morteza Haghir Chehreghani  

**一句话要点**：提出基于近端策略优化的多目标强化学习框架，用于高速公路卡车战术决策，平衡安全、效率和成本。

**关键词**：多目标强化学习, 近端策略优化, 卡车战术决策, 帕累托最优, 高速公路驾驶, 自适应决策

## 3 点简述
- 核心问题：传统标量奖励聚合竞争目标（安全、效率、成本）时，模糊了权衡结构，难以优化。
- 方法要点：采用PPO学习连续帕累托最优策略集，显式表示目标间的权衡，实现平滑可解释的帕累托前沿。
- 实验或效果：在可扩展模拟平台上评估，框架无需重新训练即可切换驾驶策略，提升自适应决策能力。

## 摘要（原文）

> Balancing safety, efficiency, and operational costs in highway driving poses a challenging decision-making problem for heavy-duty vehicles. A central difficulty is that conventional scalar reward formulations, obtained by aggregating these competing objectives, often obscure the structure of their trade-offs. We present a Proximal Policy Optimization based multi-objective reinforcement learning framework that learns a continuous set of policies explicitly representing these trade-offs and evaluates it on a scalable simulation platform for tactical decision making in trucks. The proposed approach learns a continuous set of Pareto-optimal policies that capture the trade-offs among three conflicting objectives: safety, quantified in terms of collisions and successful completion; energy efficiency and time efficiency, quantified using energy cost and driver cost, respectively. The resulting Pareto frontier is smooth and interpretable, enabling flexibility in choosing driving behavior along different conflicting objectives. This framework allows seamless transitions between different driving policies without retraining, yielding a robust and adaptive decision-making strategy for autonomous trucking applications.

