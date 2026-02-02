---
layout: default
title: Reinforcement Learning-Based Co-Design and Operation of Chiller and Thermal Energy Storage for Cost-Optimal HVAC Systems
---

# Reinforcement Learning-Based Co-Design and Operation of Chiller and Thermal Energy Storage for Cost-Optimal HVAC Systems
**arXiv**：[2601.22880v1](https://arxiv.org/abs/2601.22880) · [PDF](https://arxiv.org/pdf/2601.22880.pdf)  
**作者**：Tanay Raghunandan Srinivasa, Vivek Deulkar, Aviruch Bhatia, Vishal Garg  

**一句话要点**：提出基于强化学习的冷却系统联合设计与运行方法，以最小化商业HVAC系统的全生命周期成本。

**关键词**：强化学习, HVAC系统优化, 冷却基础设施设计, 马尔可夫决策过程, 深度Q网络, 全生命周期成本

## 3 点简述
- 研究商业HVAC系统中冷却基础设施的联合运行与容量设计问题，目标是最小化30年全生命周期成本。
- 将固定配置下的冷却器运行建模为有限时域马尔可夫决策过程，使用深度Q网络求解以优化电力成本。
- 通过评估候选配置并筛选可行集，确定最优冷却器和储热容量分别为700和1500。

## 摘要（原文）

> We study the joint operation and sizing of cooling infrastructure for commercial HVAC systems using reinforcement learning, with the objective of minimizing life-cycle cost over a 30-year horizon. The cooling system consists of a fixed-capacity electric chiller and a thermal energy storage (TES) unit, jointly operated to meet stochastic hourly cooling demands under time-varying electricity prices. The life-cycle cost accounts for both capital expenditure and discounted operating cost, including electricity consumption and maintenance. A key challenge arises from the strong asymmetry in capital costs: increasing chiller capacity by one unit is far more expensive than an equivalent increase in TES capacity. As a result, identifying the right combination of chiller and TES sizes, while ensuring zero loss-of-cooling-load under optimal operation, is a non-trivial co-design problem. To address this, we formulate the chiller operation problem for a fixed infrastructure configuration as a finite-horizon Markov Decision Process (MDP), in which the control action is the chiller part-load ratio (PLR). The MDP is solved using a Deep Q Network (DQN) with a constrained action space. The learned DQN RL policy minimizes electricity cost over historical traces of cooling demand and electricity prices. For each candidate chiller-TES sizing configuration, the trained policy is evaluated. We then restrict attention to configurations that fully satisfy the cooling demand and perform a life-cycle cost minimization over this feasible set to identify the cost-optimal infrastructure design. Using this approach, we determine the optimal chiller and thermal energy storage capacities to be 700 and 1500, respectively.

