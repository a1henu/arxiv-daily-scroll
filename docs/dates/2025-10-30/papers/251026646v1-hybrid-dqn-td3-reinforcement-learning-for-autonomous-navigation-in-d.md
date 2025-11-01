---
layout: default
title: Hybrid DQN-TD3 Reinforcement Learning for Autonomous Navigation in Dynamic Environments
---

# Hybrid DQN-TD3 Reinforcement Learning for Autonomous Navigation in Dynamic Environments
**arXiv**：[2510.26646v1](https://arxiv.org/abs/2510.26646) · [PDF](https://arxiv.org/pdf/2510.26646.pdf)  
**作者**：Xiaoyi He, Danggui Chen, Zhenshuo Zhang, Zimeng Bai  

**一句话要点**：提出混合DQN-TD3强化学习框架，用于动态环境中的自主导航。

**关键词**：强化学习, 自主导航, 路径规划, 动态环境, DQN-TD3混合, ROS仿真

## 3 点简述
- 核心问题：动态和部分可观测环境中的自主导航路径规划与控制。
- 方法要点：高层DQN选择离散子目标，低层TD3执行连续控制，结合奖励函数和安全门。
- 实验或效果：在ROS+Gazebo中评估，相比基线提高成功率、样本效率和泛化能力。

## 摘要（原文）

> This paper presents a hierarchical path-planning and control framework that
> combines a high-level Deep Q-Network (DQN) for discrete sub-goal selection with
> a low-level Twin Delayed Deep Deterministic Policy Gradient (TD3) controller
> for continuous actuation. The high-level module selects behaviors and
> sub-goals; the low-level module executes smooth velocity commands. We design a
> practical reward shaping scheme (direction, distance, obstacle avoidance,
> action smoothness, collision penalty, time penalty, and progress), together
> with a LiDAR-based safety gate that prevents unsafe motions. The system is
> implemented in ROS + Gazebo (TurtleBot3) and evaluated with PathBench metrics,
> including success rate, collision rate, path efficiency, and re-planning
> efficiency, in dynamic and partially observable environments. Experiments show
> improved success rate and sample efficiency over single-algorithm baselines
> (DQN or TD3 alone) and rule-based planners, with better generalization to
> unseen obstacle configurations and reduced abrupt control changes. Code and
> evaluation scripts are available at the project repository.

