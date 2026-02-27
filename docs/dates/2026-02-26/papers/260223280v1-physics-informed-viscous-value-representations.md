---
layout: default
title: Physics Informed Viscous Value Representations
---

# Physics Informed Viscous Value Representations
**arXiv**：[2602.23280v1](https://arxiv.org/abs/2602.23280) · [PDF](https://arxiv.org/pdf/2602.23280.pdf)  
**作者**：Hrishikesh Viswanath, Juanwu Lu, S. Talha Bukhari, Damon Conover, Ziran Wang, Aniket Bera  

**一句话要点**：提出基于HJB方程粘性解的物理正则化方法，以改进离线目标条件强化学习中的价值估计。

**关键词**：离线强化学习, 目标条件强化学习, 物理正则化, HJB方程, 价值估计, 蒙特卡洛估计

## 3 点简述
- 离线目标条件强化学习中，状态-动作空间覆盖有限导致价值估计不准确。
- 方法通过HJB方程的粘性解提供物理归纳偏置，正则化价值迭代更新。
- 实验表明，该方法提升几何一致性，适用于导航和高维复杂操作任务。

## 摘要（原文）

> Offline goal-conditioned reinforcement learning (GCRL) learns goal-conditioned policies from static pre-collected datasets. However, accurate value estimation remains a challenge due to the limited coverage of the state-action space. Recent physics-informed approaches have sought to address this by imposing physical and geometric constraints on the value function through regularization defined over first-order partial differential equations (PDEs), such as the Eikonal equation. However, these formulations can often be ill-posed in complex, high-dimensional environments. In this work, we propose a physics-informed regularization derived from the viscosity solution of the Hamilton-Jacobi-Bellman (HJB) equation. By providing a physics-based inductive bias, our approach grounds the learning process in optimal control theory, explicitly regularizing and bounding updates during value iterations. Furthermore, we leverage the Feynman-Kac theorem to recast the PDE solution as an expectation, enabling a tractable Monte Carlo estimation of the objective that avoids numerical instability in higher-order gradients. Experiments demonstrate that our method improves geometric consistency, making it broadly applicable to navigation and high-dimensional, complex manipulation tasks. Open-source codes are available at https://github.com/HrishikeshVish/phys-fk-value-GCRL.

