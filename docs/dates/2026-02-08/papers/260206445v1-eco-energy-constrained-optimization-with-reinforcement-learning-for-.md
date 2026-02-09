---
layout: default
title: ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking
---

# ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking
**arXiv**：[2602.06445v1](https://arxiv.org/abs/2602.06445) · [PDF](https://arxiv.org/pdf/2602.06445.pdf)  
**作者**：Weidong Huang, Jingwen Zhang, Jiongye Li, Shibowen Zhang, Jiayang Wu, Jiayi Wang, Hangxin Liu, Yaodong Yang, Yao Su  

**一句话要点**：提出ECO框架，通过约束强化学习实现人形机器人节能行走优化

**关键词**：约束强化学习, 人形机器人行走, 节能优化, 拉格朗日方法, sim-to-real

## 3 点简述
- 核心问题：现有方法依赖多目标优化中的能量指标，需大量调参且策略次优
- 方法要点：将能量指标从奖励中分离，作为显式不等式约束，使用拉格朗日方法强制
- 实验或效果：在BRUCE机器人上验证，相比基线显著降低能耗并保持稳定行走

## 摘要（原文）

> Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

