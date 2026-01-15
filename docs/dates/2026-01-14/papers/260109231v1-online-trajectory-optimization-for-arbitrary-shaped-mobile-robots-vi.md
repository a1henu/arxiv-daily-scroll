---
layout: default
title: Online Trajectory Optimization for Arbitrary-Shaped Mobile Robots via Polynomial Separating Hypersurfaces
---

# Online Trajectory Optimization for Arbitrary-Shaped Mobile Robots via Polynomial Separating Hypersurfaces
**arXiv**：[2601.09231v1](https://arxiv.org/abs/2601.09231) · [PDF](https://arxiv.org/pdf/2601.09231.pdf)  
**作者**：Shuoye Li, Zhiyuan Song, Yulin Li, Zhihai Bi, Jun Ma  

**一句话要点**：提出基于多项式分离超曲面的在线轨迹优化方法，以解决任意形状移动机器人在非凸环境中的碰撞避免问题。

**关键词**：轨迹优化, 碰撞避免, 多项式分离超曲面, 非线性规划, 移动机器人, 几何感知

## 3 点简述
- 核心问题：现有方法依赖凸近似处理机器人和障碍物，在复杂狭窄环境中过于保守，导致轨迹优化失败。
- 方法要点：引入多项式函数参数化的非线性分离超曲面，通过非线性规划联合优化轨迹和多项式系数，实现几何感知的碰撞避免。
- 实验或效果：仿真和真实实验显示，该方法在非凸机器人环境中实现平滑、无碰撞和敏捷的机动，优于凸近似基线。

## 摘要（原文）

> An emerging class of trajectory optimization methods enforces collision avoidance by jointly optimizing the robot's configuration and a separating hyperplane. However, as linear separators only apply to convex sets, these methods require convex approximations of both the robot and obstacles, which becomes an overly conservative assumption in cluttered and narrow environments. In this work, we unequivocally remove this limitation by introducing nonlinear separating hypersurfaces parameterized by polynomial functions. We first generalize the classical separating hyperplane theorem and prove that any two disjoint bounded closed sets in Euclidean space can be separated by a polynomial hypersurface, serving as the theoretical foundation for nonlinear separation of arbitrary geometries. Building on this result, we formulate a nonlinear programming (NLP) problem that jointly optimizes the robot's trajectory and the coefficients of the separating polynomials, enabling geometry-aware collision avoidance without conservative convex simplifications. The optimization remains efficiently solvable using standard NLP solvers. Simulation and real-world experiments with nonconvex robots demonstrate that our method achieves smooth, collision-free, and agile maneuvers in environments where convex-approximation baselines fail.

