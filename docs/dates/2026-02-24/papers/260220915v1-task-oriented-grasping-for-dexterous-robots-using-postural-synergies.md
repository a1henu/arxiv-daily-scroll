---
layout: default
title: Task-oriented grasping for dexterous robots using postural synergies and reinforcement learning
---

# Task-oriented grasping for dexterous robots using postural synergies and reinforcement learning
**arXiv**：[2602.20915v1](https://arxiv.org/abs/2602.20915) · [PDF](https://arxiv.org/pdf/2602.20915.pdf)  
**作者**：Dimitrios Dimou, José Santos-Victor, Plinio Moreno  

**一句话要点**：提出基于姿态协同与强化学习的任务导向抓取方法，以提升人形机器人抓取能力

**关键词**：任务导向抓取, 姿态协同, 强化学习, 人形机器人, 变分自编码器

## 3 点简述
- 核心问题：现有方法缺乏考虑下游任务约束的端到端抓取解决方案
- 方法要点：结合人类抓取数据训练VAE模型，并利用强化学习优化任务导向抓取
- 实验或效果：训练智能体抓取多物体，考虑任务特定意图，实现上下文感知操作

## 摘要（原文）

> In this paper, we address the problem of task-oriented grasping for humanoid robots, emphasizing the need to align with human social norms and task-specific objectives. Existing methods, employ a variety of open-loop and closed-loop approaches but lack an end-to-end solution that can grasp several objects while taking into account the downstream task's constraints. Our proposed approach employs reinforcement learning to enhance task-oriented grasping, prioritizing the post-grasp intention of the agent. We extract human grasp preferences from the ContactPose dataset, and train a hand synergy model based on the Variational Autoencoder (VAE) to imitate the participant's grasping actions. Based on this data, we train an agent able to grasp multiple objects while taking into account distinct post-grasp intentions that are task-specific. By combining data-driven insights from human grasping behavior with learning by exploration provided by reinforcement learning, we can develop humanoid robots capable of context-aware manipulation actions, facilitating collaboration in human-centered environments.

