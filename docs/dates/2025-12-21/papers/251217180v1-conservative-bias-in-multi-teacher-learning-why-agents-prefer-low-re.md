---
layout: default
title: Conservative Bias in Multi-Teacher Learning: Why Agents Prefer Low-Reward Advisors
---

# Conservative Bias in Multi-Teacher Learning: Why Agents Prefer Low-Reward Advisors
**arXiv**：[2512.17180v1](https://arxiv.org/abs/2512.17180) · [PDF](https://arxiv.org/pdf/2512.17180.pdf)  
**作者**：Maher Mesto, Francisco Cruz  

**一句话要点**：揭示交互式强化学习中代理偏好低奖励教师的保守偏差现象

**关键词**：交互式强化学习, 教师选择, 保守偏差, 多教师学习, 机器人训练

## 3 点简述
- 核心问题：交互式强化学习中教师选择动态机制不明确，代理为何偏好低奖励教师
- 方法要点：通过多专家教师导航任务实验，分析教师选择行为与性能阈值
- 实验或效果：代理93.16%选择低奖励教师，框架在概念漂移下性能提升159%

## 摘要（原文）

> Interactive reinforcement learning (IRL) has shown promise in enabling autonomous agents and robots to learn complex behaviours from human teachers, yet the dynamics of teacher selection remain poorly understood. This paper reveals an unexpected phenomenon in IRL: when given a choice between teachers with different reward structures, learning agents overwhelmingly prefer conservative, low-reward teachers (93.16% selection rate) over those offering 20x higher rewards. Through 1,250 experimental runs in navigation tasks with multiple expert teachers, we discovered: (1) Conservative bias dominates teacher selection: agents systematically choose the lowest-reward teacher, prioritising consistency over optimality; (2) Critical performance thresholds exist at teacher availability rho >= 0.6 and accuracy omega >= 0.6, below which the framework fails catastrophically; (3) The framework achieves 159% improvement over baseline Q-learning under concept drift. These findings challenge fundamental assumptions about optimal teaching in RL and suggest potential implications for human-robot collaboration, where human preferences for safety and consistency may align with the observed agent selection behaviour, potentially informing training paradigms for safety-critical robotic applications.

