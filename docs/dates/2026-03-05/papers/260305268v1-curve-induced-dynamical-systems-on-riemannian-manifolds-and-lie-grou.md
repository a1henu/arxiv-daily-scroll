---
layout: default
title: Curve-Induced Dynamical Systems on Riemannian Manifolds and Lie Groups
---

# Curve-Induced Dynamical Systems on Riemannian Manifolds and Lie Groups
**arXiv**：[2603.05268v1](https://arxiv.org/abs/2603.05268) · [PDF](https://arxiv.org/pdf/2603.05268.pdf)  
**作者**：Saray Bakker, Martin Schonger, Tobias Löw, Javier Alonso-Mora, Sylvain Calinon  

**一句话要点**：提出曲线诱导黎曼流形与李群上的动态系统框架，以提升机器人任务中的几何适应性

**关键词**：黎曼流形动态系统, 李群控制, 机器人几何适应性, SE(3)位姿, SPD矩阵编码, 实时框架

## 3 点简述
- 核心问题：机器人需在家庭环境中执行安全、可解释且尊重几何结构的任务，如SE(3)位姿或SPD矩阵编码。
- 方法要点：在黎曼流形和李群上构建名义曲线，结合切向驱动和法向吸引的动态系统，实现实时稳定运动。
- 实验或效果：在S2基准上展示更高轨迹精度、更低路径偏差和更快生成时间，并在机器人操作器上验证在线适应性。

## 摘要（原文）

> Deploying robots in household environments requires safe, adaptable, and interpretable behaviors that respect the geometric structure of tasks. Often represented on Lie groups and Riemannian manifolds, this includes poses on SE(3) or symmetric positive definite matrices encoding stiffness or damping matrices. In this context, dynamical system-based approaches offer a natural framework for generating such behavior, providing stability and convergence while remaining responsive to changes in the environment. We introduce Curve-induced Dynamical systems on Smooth Manifolds (CDSM), a real-time framework for constructing dynamical systems directly on Riemannian manifolds and Lie groups. The proposed approach constructs a nominal curve on the manifold, and generates a dynamical system which combines a tangential component that drives motion along the curve and a normal component that attracts the state toward the curve. We provide a stability analysis of the resulting dynamical system and validate the method quantitatively. On an S2 benchmark, CDSM demonstrates improved trajectory accuracy, reduced path deviation, and faster generation and query times compared to state-of-the-art methods. Finally, we demonstrate the practical applicability of the framework on both a robotic manipulator, where poses on SE(3) and damping matrices on SPD(n) are adapted online, and a mobile manipulator.

