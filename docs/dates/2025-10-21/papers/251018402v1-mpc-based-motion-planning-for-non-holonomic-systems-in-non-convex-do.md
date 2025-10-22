---
layout: default
title: MPC-based motion planning for non-holonomic systems in non-convex domains
---

# MPC-based motion planning for non-holonomic systems in non-convex domains
**arXiv**：[2510.18402v1](https://arxiv.org/abs/2510.18402) · [PDF](https://arxiv.org/pdf/2510.18402.pdf)  
**作者**：Matthias Lorenzen, Teodoro Alamo, Martina Mammarella, Fabrizio Dabbene  

**一句话要点**：提出基于MPC的运动规划方法，保证非完整系统在非凸域中收敛到目标

**关键词**：模型预测控制, 运动规划, 非完整系统, 非凸约束, 收敛保证

## 3 点简述
- 核心问题：非完整系统在非凸约束下MPC运动规划的收敛性缺乏理论保证
- 方法要点：设计新型MPC公式，在现实假设下确保目标可达
- 实验或效果：未知具体实验，但声称在相关现实场景中可验证收敛

## 摘要（原文）

> Motivated by the application of using model predictive control (MPC) for
> motion planning of autonomous mobile robots, a form of output tracking MPC for
> non- holonomic systems and with non-convex constraints is studied. Although the
> advantages of using MPC for motion planning have been demonstrated in several
> papers, in most of the available fundamental literature on output tracking MPC
> it is assumed, often implicitly, that the model is holonomic and generally the
> state or output constraints must be convex. Thus, in application-oriented
> publications, empirical results dominate and the topic of proving completeness,
> in particular under which assumptions the target is always reached, has
> received comparatively little attention. To address this gap, we present a
> novel MPC formulation that guarantees convergence to the desired target under
> realistic assumptions, which can be verified in relevant real-world scenarios.

