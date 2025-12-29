---
layout: default
title: Optimal Trajectory Planning for Orbital Robot Rendezvous and Docking
---

# Optimal Trajectory Planning for Orbital Robot Rendezvous and Docking
**arXiv**：[2512.21882v1](https://arxiv.org/abs/2512.21882) · [PDF](https://arxiv.org/pdf/2512.21882.pdf)  
**作者**：Kenta Iizuka, Akiyoshi Uchida, Kentaro Uno, Kazuya Yoshida  

**一句话要点**：提出基于非线性优化的轨迹规划方法，用于空间碎片近距离交会，以安全接近翻滚目标。

**关键词**：轨迹规划, 非线性优化, 空间机器人, 交会对接, 动态禁区球体, 离散推进器控制

## 3 点简述
- 核心问题：空间碎片移除任务中，安全接近翻滚目标是关键挑战，需将自由漂浮旋转碎片引入机械臂工作空间。
- 方法要点：引入动态禁区球体，根据接近条件自适应调整，实现更近更安全的访问；基于非线性优化进行轨迹规划。
- 实验或效果：开发控制策略，使用离散开关推进器复现优化轨迹，考虑实际实施约束，未知具体实验效果。

## 摘要（原文）

> Approaching a tumbling target safely is a critical challenge in space debris removal missions utilizing robotic manipulators onboard servicing satellites. In this work, we propose a trajectory planning method based on nonlinear optimization for a close-range rendezvous to bring a free-floating, rotating debris object in a two-dimensional plane into the manipulator's workspace, as a preliminary step for its capture. The proposed method introduces a dynamic keep-out sphere that adapts depending on the approach conditions, allowing for closer and safer access to the target. Furthermore, a control strategy is developed to reproduce the optimized trajectory using discrete ON/OFF thrusters, considering practical implementation constraints.

