---
layout: default
title: A Dual Quaternion based RRT* Path Planning Approach for Satellite Rendezvous and Docking
---

# A Dual Quaternion based RRT* Path Planning Approach for Satellite Rendezvous and Docking
**arXiv**：[2512.17680v1](https://arxiv.org/abs/2512.17680) · [PDF](https://arxiv.org/pdf/2512.17680.pdf)  
**作者**：Ana Stankovic, Mohamed Khalil Ben-Larbi, Wolfgang H. Müller  

**一句话要点**：提出基于对偶四元数的RRT*路径规划方法，用于卫星交会对接的六自由度平滑轨迹生成。

**关键词**：卫星交会对接, 路径规划, 对偶四元数, RRT*算法, 六自由度运动, 避障约束

## 3 点简述
- 核心问题：在避障约束下，为卫星交会对接生成平滑、无碰撞的六自由度姿态轨迹。
- 方法要点：将对偶四元数代数直接集成到RRT*框架中，实现SE(3)空间中的自然螺旋运动插值。
- 实验或效果：在Python中实现，多障碍场景演示，相比标准RRT*提升了姿态连续性和避障能力。

## 摘要（原文）

> This paper proposes a sampling-based motion planner that employs a dual quaternion representation to generate smooth, collision-free six-degree-of-freedom pose trajectories for satellite rendezvous and docking under keep-out zone constraints. The proposed planner integrates the dual quaternion algebra directly into an RRT* framework, thereby enabling natural screw motion interpolation in SE(3). The dual quaternion-based RRT* has been implemented in Python and demonstrated on a representative multi-obstacle scenario. A comparison with a standard RRT* using separate translation and quaternion steering highlights the enhanced pose continuity and obstacle avoidance of the proposed method. The present approach is purely kinematic in nature and does not take into account relative orbital dynamics. Consequently, the resulting path provides a preliminary estimate for a subsequent optimisation-based trajectory planner, which will refine the motion with dynamic constraints for the purpose of practical satellite rendezvous and docking missions.

