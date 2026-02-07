---
layout: default
title: HiCrowd: Hierarchical Crowd Flow Alignment for Dense Human Environments
---

# HiCrowd: Hierarchical Crowd Flow Alignment for Dense Human Environments
**arXiv**：[2602.05608v1](https://arxiv.org/abs/2602.05608) · [PDF](https://arxiv.org/pdf/2602.05608.pdf)  
**作者**：Yufei Zhu, Shih-Min Yang, Martin Magnusson, Allan Wang  

**一句话要点**：提出HiCrowd分层框架，通过强化学习与模型预测控制结合，解决密集人群中的机器人冻结问题。

**关键词**：密集人群导航, 强化学习, 模型预测控制, 机器人冻结问题, 人群流对齐

## 3 点简述
- 核心问题：密集人群中机器人易陷入冻结，难以找到安全运动路径。
- 方法要点：高层RL生成跟随点对齐人群流，低层MPC安全跟踪，结合长期决策与短期执行。
- 实验或效果：在真实和合成数据集上评估，导航效率与安全性优于基线，减少冻结行为。

## 摘要（原文）

> Navigating through dense human crowds remains a significant challenge for mobile robots. A key issue is the freezing robot problem, where the robot struggles to find safe motions and becomes stuck within the crowd. To address this, we propose HiCrowd, a hierarchical framework that integrates reinforcement learning (RL) with model predictive control (MPC). HiCrowd leverages surrounding pedestrian motion as guidance, enabling the robot to align with compatible crowd flows. A high-level RL policy generates a follow point to align the robot with a suitable pedestrian group, while a low-level MPC safely tracks this guidance with short horizon planning. The method combines long-term crowd aware decision making with safe short-term execution. We evaluate HiCrowd against reactive and learning-based baselines in offline setting (replaying recorded human trajectories) and online setting (human trajectories are updated to react to the robot in simulation). Experiments on a real-world dataset and a synthetic crowd dataset show that our method outperforms in navigation efficiency and safety, while reducing freezing behaviors. Our results suggest that leveraging human motion as guidance, rather than treating humans solely as dynamic obstacles, provides a powerful principle for safe and efficient robot navigation in crowds.

