---
layout: default
title: Higher-Order Action Regularization in Deep Reinforcement Learning: From Continuous Control to Building Energy Management
---

# Higher-Order Action Regularization in Deep Reinforcement Learning: From Continuous Control to Building Energy Management
**arXiv**：[2601.02061v1](https://arxiv.org/abs/2601.02061) · [PDF](https://arxiv.org/pdf/2601.02061.pdf)  
**作者**：Faizan Ahmed, Aniket Dixit, James Brusey  

**一句话要点**：提出高阶动作正则化方法，以平滑深度强化学习控制行为，应用于连续控制和建筑能源管理。

**关键词**：深度强化学习, 动作正则化, 连续控制, 建筑能源管理, 高阶导数惩罚, HVAC控制

## 3 点简述
- 深度强化学习代理常产生高频控制行为，导致能耗和机械磨损问题。
- 通过高阶导数惩罚（如三阶导数最小化）正则化动作，提升平滑性。
- 在连续控制基准和HVAC系统中验证，平滑策略减少设备切换60%，保持性能。

## 摘要（原文）

> Deep reinforcement learning agents often exhibit erratic, high-frequency control behaviors that hinder real-world deployment due to excessive energy consumption and mechanical wear. We systematically investigate action smoothness regularization through higher-order derivative penalties, progressing from theoretical understanding in continuous control benchmarks to practical validation in building energy management. Our comprehensive evaluation across four continuous control environments demonstrates that third-order derivative penalties (jerk minimization) consistently achieve superior smoothness while maintaining competitive performance. We extend these findings to HVAC control systems where smooth policies reduce equipment switching by 60%, translating to significant operational benefits. Our work establishes higher-order action regularization as an effective bridge between RL optimization and operational constraints in energy-critical applications.

