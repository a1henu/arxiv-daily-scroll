---
layout: default
title: CHORAL: Traversal-Aware Planning for Safe and Efficient Heterogeneous Multi-Robot Routing
---

# CHORAL: Traversal-Aware Planning for Safe and Efficient Heterogeneous Multi-Robot Routing
**arXiv**：[2601.10340v1](https://arxiv.org/abs/2601.10340) · [PDF](https://arxiv.org/pdf/2601.10340.pdf)  
**作者**：David Morilla-Cabello, Eduardo Montijano  

**一句话要点**：提出CHORAL框架，通过语义感知规划解决异构多机器人巡检中的安全高效路由问题。

**关键词**：异构多机器人路由, 语义感知规划, 度量-语义地图, 车辆路由问题, 机器人巡检

## 3 点简述
- 核心问题：异构机器人团队在复杂环境中巡检时，现有方法未充分集成场景理解，限制路由适应性和机器人优势利用。
- 方法要点：基于侦察飞行构建度量-语义地图，识别需巡检区域，结合机器人能力规划路径，并集成到异构车辆路由模型中。
- 实验或效果：在仿真和真实巡检任务中验证，通过显式考虑机器人导航能力，规划出更安全高效的路线。

## 摘要（原文）

> Monitoring large, unknown, and complex environments with autonomous robots poses significant navigation challenges, where deploying teams of heterogeneous robots with complementary capabilities can substantially improve both mission performance and feasibility. However, effectively modeling how different robotic platforms interact with the environment requires rich, semantic scene understanding. Despite this, existing approaches often assume homogeneous robot teams or focus on discrete task compatibility rather than continuous routing. Consequently, scene understanding is not fully integrated into routing decisions, limiting their ability to adapt to the environment and to leverage each robot's strengths. In this paper, we propose an integrated semantic-aware framework for coordinating heterogeneous robots. Starting from a reconnaissance flight, we build a metric-semantic map using open-vocabulary vision models and use it to identify regions requiring closer inspection and capability-aware paths for each platform to reach them. These are then incorporated into a heterogeneous vehicle routing formulation that jointly assigns inspection tasks and computes robot trajectories. Experiments in simulation and in a real inspection mission with three robotic platforms demonstrate the effectiveness of our approach in planning safer and more efficient routes by explicitly accounting for each platform's navigation capabilities. We release our framework, CHORAL, as open source to support reproducibility and deployment of diverse robot teams.

