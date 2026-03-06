---
layout: default
title: Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics
---

# Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics
**arXiv**：[2603.05113v1](https://arxiv.org/abs/2603.05113) · [PDF](https://arxiv.org/pdf/2603.05113.pdf)  
**作者**：Kilian Freitag, Knut Åkesson, Morteza Haghir Chehreghani  

**一句话要点**：提出两阶段奖励课程以解决机器人强化学习中多目标奖励函数设计难题

**关键词**：强化学习, 机器人控制, 奖励函数设计, 课程学习, 多目标优化

## 3 点简述
- 核心问题：机器人控制中多目标奖励函数设计复杂，需精确调参以学习理想策略
- 方法要点：先训练简化任务奖励，再引入行为相关奖励，实现任务与行为解耦
- 实验或效果：在多个机器人环境中验证，性能优于直接训练全奖励，对奖励权重更鲁棒

## 摘要（原文）

> Deep Reinforcement Learning is a promising tool for robotic control, yet practical application is often hindered by the difficulty of designing effective reward functions. Real-world tasks typically require optimizing multiple objectives simultaneously, necessitating precise tuning of their weights to learn a policy with the desired characteristics. To address this, we propose a two-stage reward curriculum where we decouple task-specific objectives from behavioral terms. In our method, we first train the agent on a simplified task-only reward function to ensure effective exploration before introducing the full reward that includes auxiliary behavior-related terms such as energy efficiency. Further, we analyze various transition strategies and demonstrate that reusing samples between phases is critical for training stability. We validate our approach on the DeepMind Control Suite, ManiSkill3, and a mobile robot environment, modified to include auxiliary behavioral objectives. Our method proves to be simple yet effective, substantially outperforming baselines trained directly on the full reward while exhibiting higher robustness to specific reward weightings.

