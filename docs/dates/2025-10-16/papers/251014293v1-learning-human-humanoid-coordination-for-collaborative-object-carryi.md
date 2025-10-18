---
layout: default
title: Learning Human-Humanoid Coordination for Collaborative Object Carrying
---

# Learning Human-Humanoid Coordination for Collaborative Object Carrying
**arXiv**：[2510.14293v1](https://arxiv.org/abs/2510.14293) · [PDF](https://arxiv.org/pdf/2510.14293.pdf)  
**作者**：Yushi Du, Yixuan Li, Baoxiong Jia, Yutang Lin, Pei Zhou, Wei Liang, Yanchao Yang, Siyuan Huang  

**一句话要点**：提出COLA方法实现人形机器人与人类协作搬运，无需外部传感器

**关键词**：人形机器人协作, 强化学习, 本体感知, 轨迹规划, 负载平衡

## 3 点简述
- 核心问题：人形机器人全身动力学复杂，难以实现柔顺人机协作搬运
- 方法要点：使用仅本体感知的强化学习，单策略结合领导与跟随行为
- 实验或效果：仿真和真实实验显示减少人类努力24.7%，泛化性强

## 摘要（原文）

> Human-humanoid collaboration shows significant promise for applications in
> healthcare, domestic assistance, and manufacturing. While compliant robot-human
> collaboration has been extensively developed for robotic arms, enabling
> compliant human-humanoid collaboration remains largely unexplored due to
> humanoids' complex whole-body dynamics. In this paper, we propose a
> proprioception-only reinforcement learning approach, COLA, that combines leader
> and follower behaviors within a single policy. The model is trained in a
> closed-loop environment with dynamic object interactions to predict object
> motion patterns and human intentions implicitly, enabling compliant
> collaboration to maintain load balance through coordinated trajectory planning.
> We evaluate our approach through comprehensive simulator and real-world
> experiments on collaborative carrying tasks, demonstrating the effectiveness,
> generalization, and robustness of our model across various terrains and
> objects. Simulation experiments demonstrate that our model reduces human effort
> by 24.7%. compared to baseline approaches while maintaining object stability.
> Real-world experiments validate robust collaborative carrying across different
> object types (boxes, desks, stretchers, etc.) and movement patterns
> (straight-line, turning, slope climbing). Human user studies with 23
> participants confirm an average improvement of 27.4% compared to baseline
> models. Our method enables compliant human-humanoid collaborative carrying
> without requiring external sensors or complex interaction models, offering a
> practical solution for real-world deployment.

