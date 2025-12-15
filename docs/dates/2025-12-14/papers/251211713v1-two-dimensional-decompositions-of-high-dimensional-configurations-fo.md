---
layout: default
title: Two-dimensional Decompositions of High-dimensional Configurations for Efficient Multi-vehicle Coordination at Intelligent Intersections
---

# Two-dimensional Decompositions of High-dimensional Configurations for Efficient Multi-vehicle Coordination at Intelligent Intersections
**arXiv**：[2512.11713v1](https://arxiv.org/abs/2512.11713) · [PDF](https://arxiv.org/pdf/2512.11713.pdf)  
**作者**：Amirreza Akbari, Johan Thunberg  

**一句话要点**：提出基于二维分解的高维配置空间方法，以高效解决智能交叉口多车辆协调问题

**关键词**：多车辆协调, 轨迹规划, 配置空间分解, 非线性模型预测控制, 智能交叉口

## 3 点简述
- 核心问题：多车辆在智能交叉口等共享空间中的安全协调与轨迹规划计算复杂度高
- 方法要点：将高维配置空间问题分解为序列二维图搜索，结合非线性模型预测控制确保平滑运动
- 实验或效果：数值评估显示在目标值和计算时间上显著优于现有基于混合整数线性规划的方法

## 摘要（原文）

> For multi-vehicle complex traffic scenarios in shared spaces such as intelligent intersections, safe coordination and trajectory planning is challenging due to computational complexity. To meet this challenge, we introduce a computationally efficient method for generating collision-free trajectories along predefined vehicle paths. We reformulate a constrained minimum-time trajectory planning problem as a problem in a high-dimensional configuration space, where conflict zones are modeled by high-dimensional polyhedra constructed from two-dimensional rectangles. Still, in such a formulation, as the number of vehicles involved increases, the computational complexity increases significantly. To address this, we propose two algorithms for near-optimal local optimization that significantly reduce the computational complexity by decomposing the high-dimensional problem into a sequence of 2D graph search problems. The resulting trajectories are then incorporated into a Nonlinear Model Predictive Control (NMPC) framework to ensure safe and smooth vehicle motion. We furthermore show in numerical evaluation that this approach significantly outperforms existing MILP-based time-scheduling; both in terms of objective-value and computational time.

