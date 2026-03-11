---
layout: default
title: Kinodynamic Motion Retargeting for Humanoid Locomotion via Multi-Contact Whole-Body Trajectory Optimization
---

# Kinodynamic Motion Retargeting for Humanoid Locomotion via Multi-Contact Whole-Body Trajectory Optimization
**arXiv**：[2603.09956v1](https://arxiv.org/abs/2603.09956) · [PDF](https://arxiv.org/pdf/2603.09956.pdf)  
**作者**：Xiaoyu Zhang, Steven Haener, Varun Madabushi, Maegan Tucker  

**一句话要点**：提出KinoDynamic Motion Retargeting框架，通过多接触全身轨迹优化解决人形机器人运动重定向的动态可行性问题。

**关键词**：人形机器人运动重定向, 多接触轨迹优化, 刚体动力学约束, 地面反作用力测量, 模仿学习策略, 运动捕捉数据

## 3 点简述
- 核心问题：传统基于运动捕捉的运动重定向方法存在物理不一致性，如脚滑和地面穿透，影响下游模仿学习策略性能。
- 方法要点：KDMR通过强制刚体动力学和接触互补约束，结合地面反作用力测量，自动检测脚跟-脚趾接触事件，实现动态可行的运动重定向。
- 实验或效果：KDMR在动态可行性、地面反作用力跟踪准确性和下游策略训练效率方面显著优于纯运动学方法，提升运动稳定性和收敛速度。

## 摘要（原文）

> We present the KinoDynamic Motion Retargeting (KDMR) framework, a novel approach for humanoid locomotion that models the retargeting process as a multi-contact, whole-body trajectory optimization problem. Conventional kinematics-based retargeting methods rely solely on spatial motion capture (MoCap) data, inevitably introducing physically inconsistent artifacts, such as foot sliding and ground penetration, that severely degrade the performance of downstream imitation learning policies. To bridge this gap, KDMR extends beyond pure kinematics by explicitly enforcing rigid-body dynamics and contact complementarity constraints. Further, by integrating ground reaction force (GRF) measurements alongside MoCap data, our method automatically detects heel-toe contact events to accurately replicate complex human-like contact patterns. We evaluate KDMR against the state-of-the-art baseline, GMR, across three key dimensions: 1) the dynamic feasibility and smoothness of the retargeted motions, 2) the accuracy of GRF tracking compared to raw source data, and 3) the training efficiency and final performance of downstream control policies trained via the BeyondMimic framework. Experimental results demonstrate that KDMR significantly outperforms purely kinematic methods, yielding dynamically viable reference trajectories that accelerate policy convergence and enhance overall locomotion stability. Our end-to-end pipeline will be open-sourced upon publication.

