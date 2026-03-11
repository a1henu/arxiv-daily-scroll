---
layout: default
title: SEA-Nav: Efficient Policy Learning for Safe and Agile Quadruped Navigation in Cluttered Environments
---

# SEA-Nav: Efficient Policy Learning for Safe and Agile Quadruped Navigation in Cluttered Environments
**arXiv**：[2603.09460v1](https://arxiv.org/abs/2603.09460) · [PDF](https://arxiv.org/pdf/2603.09460.pdf)  
**作者**：Shiyi Chen, Mingye Yang, Haiyan Mao, Jiaqi Zhang, Haiyi Liu, Shuheng He, Debing Zhang, Zihao Qiu, Chun Zhang  

**一句话要点**：提出SEA-Nav强化学习框架，以解决四足机器人在密集杂乱环境中安全敏捷导航的训练挑战。

**关键词**：四足机器人导航, 强化学习, 控制屏障函数, 安全约束, 高效训练, 密集环境

## 3 点简述
- 核心问题：现有方法在密集杂乱环境中训练四足导航时，常面临安全性不足、敏捷性差或训练时间过长的问题。
- 方法要点：采用可微分控制屏障函数作为安全屏蔽，结合自适应碰撞回放和危险探索奖励，以加速策略学习。
- 实验或效果：在真实世界中实现高挑战性导航，训练时间缩短至分钟级，提升了部署效率。

## 摘要（原文）

> Efficiently training quadruped robot navigation in densely cluttered environments remains a significant challenge. Existing methods are either limited by a lack of safety and agility in simple obstacle distributions or suffer from slow locomotion in complex environments, often requiring excessively long training phases. To this end, we propose SEA-Nav (Safe, Efficient, and Agile Navigation), a reinforcement learning framework for quadruped navigation. Within diverse and dense obstacle environments, a differentiable control barrier function (CBF)-based shield constraints the navigation policy to output safe velocity commands. An adaptive collision replay mechanism and hazardous exploration rewards are introduced to increase the probability of learning from critical experiences, guiding efficient exploration and exploitation. Finally, kinematic action constraints are incorporated to ensure safe velocity commands, facilitating successful physical deployment. To the best of our knowledge, this is the first approach that achieves highly challenging quadruped navigation in the real world with minute-level training time.

