---
layout: default
title: HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation
---

# HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation
**arXiv**：[2602.06341v1](https://arxiv.org/abs/2602.06341) · [PDF](https://arxiv.org/pdf/2602.06341.pdf)  
**作者**：Zhanxiang Cao, Liyun Yan, Yang Zhang, Sirui Chen, Jianming Ma, Tianyue Zhan, Shengcheng Fu, Yufei Jia, Cewu Lu, Yue Gao  

**一句话要点**：提出HiWET分层强化学习框架，以解决人形机器人长时程世界坐标系末端执行器跟踪问题。

**关键词**：人形机器人操作, 分层强化学习, 世界坐标系跟踪, 运动学流形先验, 仿真到现实迁移

## 3 点简述
- 核心问题：现有方法在身体坐标系下规划，无法纠正腿部运动导致的世界坐标系累积漂移。
- 方法要点：高层策略生成世界坐标系子目标，低层策略在稳定性约束下执行，引入运动学流形先验降低探索维度。
- 实验或效果：仿真和消融研究验证精确稳定跟踪，零样本仿真到现实迁移展示物理人形机器人稳定运动。

## 摘要（原文）

> Humanoid loco-manipulation requires executing precise manipulation tasks while maintaining dynamic stability amid base motion and impacts. Existing approaches typically formulate commands in body-centric frames, fail to inherently correct cumulative world-frame drift induced by legged locomotion. We reformulate the problem as world-frame end-effector tracking and propose HiWET, a hierarchical reinforcement learning framework that decouples global reasoning from dynamic execution. The high-level policy generates subgoals that jointly optimize end-effector accuracy and base positioning in the world frame, while the low-level policy executes these commands under stability constraints. We introduce a Kinematic Manifold Prior (KMP) that embeds the manipulation manifold into the action space via residual learning, reducing exploration dimensionality and mitigating kinematically invalid behaviors. Extensive simulation and ablation studies demonstrate that HiWET achieves precise and stable end-effector tracking in long-horizon world-frame tasks. We validate zero-shot sim-to-real transfer of the low-level policy on a physical humanoid, demonstrating stable locomotion under diverse manipulation commands. These results indicate that explicit world-frame reasoning combined with hierarchical control provides an effective and scalable solution for long-horizon humanoid loco-manipulation.

