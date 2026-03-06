---
layout: default
title: Curve-Induced Dynamical Systems on Riemannian Manifolds and Lie Groups
---

# Curve-Induced Dynamical Systems on Riemannian Manifolds and Lie Groups
**arXiv**：[2603.05268v1](https://arxiv.org/abs/2603.05268) · [PDF](https://arxiv.org/pdf/2603.05268.pdf)  
**作者**：Saray Bakker, Martin Schonger, Tobias Löw, Javier Alonso-Mora, Sylvain Calinon  

**一句话要点**：提出曲线诱导动态系统框架，在黎曼流形和李群上实现机器人安全自适应行为生成。

**关键词**：黎曼流形, 李群动态系统, 机器人行为生成, SE(3)位姿, SPD矩阵, 曲线诱导控制

## 3 点简述
- 核心问题：机器人需在几何结构任务中生成安全、可解释的动态行为，如SE(3)位姿或SPD矩阵。
- 方法要点：构建流形上的名义曲线，结合切向驱动和法向吸引的动态系统，确保稳定性和实时性。
- 实验或效果：在S2基准上提升轨迹精度和速度，并在机械臂和移动操作器上验证在线适应性。

## 摘要（原文）

> Deploying robots in household environments requires safe, adaptable, and interpretable behaviors that respect the geometric structure of tasks. Often represented on Lie groups and Riemannian manifolds, this includes poses on SE(3) or symmetric positive definite matrices encoding stiffness or damping matrices. In this context, dynamical system-based approaches offer a natural framework for generating such behavior, providing stability and convergence while remaining responsive to changes in the environment. We introduce Curve-induced Dynamical systems on Smooth Manifolds (CDSM), a real-time framework for constructing dynamical systems directly on Riemannian manifolds and Lie groups. The proposed approach constructs a nominal curve on the manifold, and generates a dynamical system which combines a tangential component that drives motion along the curve and a normal component that attracts the state toward the curve. We provide a stability analysis of the resulting dynamical system and validate the method quantitatively. On an S2 benchmark, CDSM demonstrates improved trajectory accuracy, reduced path deviation, and faster generation and query times compared to state-of-the-art methods. Finally, we demonstrate the practical applicability of the framework on both a robotic manipulator, where poses on SE(3) and damping matrices on SPD(n) are adapted online, and a mobile manipulator.

