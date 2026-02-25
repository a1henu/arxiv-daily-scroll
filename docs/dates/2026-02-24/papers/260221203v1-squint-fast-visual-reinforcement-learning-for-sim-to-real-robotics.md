---
layout: default
title: Squint: Fast Visual Reinforcement Learning for Sim-to-Real Robotics
---

# Squint: Fast Visual Reinforcement Learning for Sim-to-Real Robotics
**arXiv**：[2602.21203v1](https://arxiv.org/abs/2602.21203) · [PDF](https://arxiv.org/pdf/2602.21203.pdf)  
**作者**：Abdulaziz Almuzairee, Henrik I. Christensen  

**一句话要点**：提出Squint视觉强化学习方法，在模拟到真实机器人任务中实现快速训练。

**关键词**：视觉强化学习, 模拟到真实, 快速训练, 机器人操作, 分布评论家, 并行模拟

## 3 点简述
- 核心问题：视觉强化学习样本效率低、训练速度慢，高维图像增加存储和编码开销。
- 方法要点：结合并行模拟、分布评论家、分辨率调整和优化实现，提升训练效率。
- 实验或效果：在SO-101任务集上，15分钟内训练策略，多数任务6分钟内收敛，并实现模拟到真实转移。

## 摘要（原文）

> Visual reinforcement learning is appealing for robotics but expensive -- off-policy methods are sample-efficient yet slow; on-policy methods parallelize well but waste samples. Recent work has shown that off-policy methods can train faster than on-policy methods in wall-clock time for state-based control. Extending this to vision remains challenging, where high-dimensional input images complicate training dynamics and introduce substantial storage and encoding overhead. To address these challenges, we introduce Squint, a visual Soft Actor Critic method that achieves faster wall-clock training than prior visual off-policy and on-policy methods. Squint achieves this via parallel simulation, a distributional critic, resolution squinting, layer normalization, a tuned update-to-data ratio, and an optimized implementation. We evaluate on the SO-101 Task Set, a new suite of eight manipulation tasks in ManiSkill3 with heavy domain randomization, and demonstrate sim-to-real transfer to a real SO-101 robot. We train policies for 15 minutes on a single RTX 3090 GPU, with most tasks converging in under 6 minutes.

