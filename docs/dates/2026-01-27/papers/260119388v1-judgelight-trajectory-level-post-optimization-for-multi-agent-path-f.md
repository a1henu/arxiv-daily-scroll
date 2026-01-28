---
layout: default
title: Judgelight: Trajectory-Level Post-Optimization for Multi-Agent Path Finding via Closed-Subwalk Collapsing
---

# Judgelight: Trajectory-Level Post-Optimization for Multi-Agent Path Finding via Closed-Subwalk Collapsing
**arXiv**：[2601.19388v1](https://arxiv.org/abs/2601.19388) · [PDF](https://arxiv.org/pdf/2601.19388.pdf)  
**作者**：Yimin Tang, Sven Koenig, Erdem Bıyık  

**一句话要点**：提出Judgelight轨迹级后优化方法，通过闭合子游走折叠改进多智能体路径规划轨迹质量。

**关键词**：多智能体路径规划, 轨迹优化, 闭合子游走折叠, 整数线性规划, 后优化方法, 学习型求解器

## 3 点简述
- 多智能体路径规划中学习型求解器常产生含冗余或振荡运动的可行轨迹。
- Judgelight通过折叠轨迹中的闭合子游走来移除冗余运动，同时保持所有可行性约束。
- 实验显示Judgelight能持续降低约20%的解决方案成本，尤其适用于学习型求解器。

## 摘要（原文）

> Multi-Agent Path Finding (MAPF) is an NP-hard problem with applications in warehouse automation and multi-robot coordination. Learning-based MAPF solvers offer fast and scalable planning but often produce feasible trajectories that contain unnecessary or oscillatory movements. We propose Judgelight, a post-optimization method that improves trajectory quality after a MAPF solver generates a feasible schedule. Judgelight collapses closed subwalks in agents' trajectories to remove redundant movements while preserving all feasibility constraints. We formalize this process as MAPF-Collapse, prove that it is NP-hard, and present an exact optimization approach by formulating it as integer linear programming (ILP) problem. Experimental results show Judgelight consistently reduces solution cost by around 20%, particularly for learning-based solvers, producing trajectories that are better suited for real-world deployment.

