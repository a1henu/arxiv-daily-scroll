---
layout: default
title: Swimming Under Constraints: A Safe Reinforcement Learning Framework for Quadrupedal Bio-Inspired Propulsion
---

# Swimming Under Constraints: A Safe Reinforcement Learning Framework for Quadrupedal Bio-Inspired Propulsion
**arXiv**：[2603.04073v1](https://arxiv.org/abs/2603.04073) · [PDF](https://arxiv.org/pdf/2603.04073.pdf)  
**作者**：Xinyu Cui, Fei Han, Hang Xu, Yongcheng Zeng, Luoyang Sun, Ruizhi Zhang, Jian Zhao, Haifeng Zhang, Weikun Li, Hao Chen, Jun Wang, Dixia Fan  

**一句话要点**：提出ACPPO-PID强化学习框架，以约束优化解决四足仿生游泳中的推力最大化与失稳力最小化问题。

**关键词**：仿生游泳, 约束强化学习, 四足机器人, 流体动力学, PID控制, 硬件实验

## 3 点简述
- 核心问题：四足仿生游泳在6自由度流体耦合下易受升力波动等失稳力影响，需平衡推力与稳定性。
- 方法要点：采用PID调节拉格朗日乘子的约束强化学习，结合条件非对称裁剪加速学习，并通过循环几何聚合稳定更新。
- 实验或效果：通过模仿学习初始化与硬件拖曳池实验，实现高效推力、减少失稳力，并优于现有基线，提升收敛速度。

## 摘要（原文）

> Bio-inspired aquatic propulsion offers high thrust and maneuverability but is prone to destabilizing forces such as lift fluctuations, which are further amplified by six-degree-of-freedom (6-DoF) fluid coupling. We formulate quadrupedal swimming as a constrained optimization problem that maximizes forward thrust while minimizing destabilizing fluctuations. Our proposed framework, Accelerated Constrained Proximal Policy Optimization with a PID-regulated Lagrange multiplier (ACPPO-PID), enforces constraints with a PID-regulated Lagrange multiplier, accelerates learning via conditional asymmetric clipping, and stabilizes updates through cycle-wise geometric aggregation. Initialized with imitation learning and refined through on-hardware towing-tank experiments, ACPPO-PID produces control policies that transfer effectively to quadrupedal free-swimming trials. Results demonstrate improved thrust efficiency, reduced destabilizing forces, and faster convergence compared with state-of-the-art baselines, underscoring the importance of constraint-aware safe RL for robust and generalizable bio-inspired locomotion in complex fluid environments.

