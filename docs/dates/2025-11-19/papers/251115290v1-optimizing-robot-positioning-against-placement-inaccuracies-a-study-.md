---
layout: default
title: Optimizing Robot Positioning Against Placement Inaccuracies: A Study on the Fanuc CRX10iA/L
---

# Optimizing Robot Positioning Against Placement Inaccuracies: A Study on the Fanuc CRX10iA/L
**arXiv**：[2511.15290v1](https://arxiv.org/abs/2511.15290) · [PDF](https://arxiv.org/pdf/2511.15290.pdf)  
**作者**：Nicolas Gautier, Yves Guillermit, Mathieu Porez, David Lemoine, Damien Chablat  

**一句话要点**：提出基于粒子群优化的机器人基座定位方法，以应对工业任务中的放置不准确性。

**关键词**：机器人定位优化, 粒子群优化, 逆运动学, 轨迹规划, 工业机器人, 鲁棒性分析

## 3 点简述
- 核心问题：机器人基座放置不准确影响轨迹执行，如移动基座部署时的误差。
- 方法要点：使用粒子群优化探索基座位置，结合逆运动学和雅可比矩阵评估轨迹可行性。
- 实验或效果：计算可行性区域边界和最大内切圆，提供鲁棒性标准以优化轨迹执行。

## 摘要（原文）

> This study presents a methodology for determining the optimal base placement of a Fanuc CRX10iA/L collaborative robot for a desired trajectory corresponding to an industrial task. The proposed method uses a particle swarm optimization algorithm that explores the search space to find positions for performing the trajectory. An $α$-shape algorithm is then used to draw the borders of the feasibility areas, and the largest circle inscribed is calculated from the Voronoi diagrams. The aim of this approach is to provide a robustness criterion in the context of robot placement inaccuracies that may be encountered, for example, if the robot is placed on a mobile base when the system is deployed by an operator. The approach developed uses an inverse kinematics model to evaluate all initial configurations, then moves the robot end-effector along the reference trajectory using the Jacobian matrix and assigns a score to the attempt. For the Fanuc CRX10iA/L robot, there can be up to 16 solutions to the inverse kinematics model. The calculation of these solutions is not trivial and requires a specific study that planning tools such as MoveIt cannot fully take into account. Additionally, the optimization process must consider constraints such as joint limits, singularities, and workspace limitations to ensure feasible and efficient trajectory execution.

