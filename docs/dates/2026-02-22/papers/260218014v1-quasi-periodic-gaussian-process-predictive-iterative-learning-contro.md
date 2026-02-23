---
layout: default
title: Quasi-Periodic Gaussian Process Predictive Iterative Learning Control
---

# Quasi-Periodic Gaussian Process Predictive Iterative Learning Control
**arXiv**：[2602.18014v1](https://arxiv.org/abs/2602.18014) · [PDF](https://arxiv.org/pdf/2602.18014.pdf)  
**作者**：Unnati Nigam, Radhendushka Srivastava, Faezeh Marzbanrad, Michael Burke  

**一句话要点**：提出基于准周期高斯过程的预测迭代学习控制方法，以提升机器人重复任务在时变扰动下的收敛速度和鲁棒性。

**关键词**：迭代学习控制, 准周期高斯过程, 预测控制, 机器人控制, 计算效率, 鲁棒性

## 3 点简述
- 核心问题：机器人重复运动中，环境变化和设备磨损导致性能随时间下降，传统迭代学习控制依赖历史误差，收敛慢且对时变扰动敏感。
- 方法要点：将准周期高斯过程融入预测框架，建模迭代间扰动和漂移，利用结构方程实现高效推理和参数估计，降低计算复杂度至O(p³)。
- 实验或效果：在自动驾驶轨迹跟踪、机械臂控制和真实机器人实验中，相比标准及高斯过程预测方法，收敛更快、鲁棒性更强且计算成本更低。

## 摘要（原文）

> Repetitive motion tasks are common in robotics, but performance can degrade over time due to environmental changes and robot wear and tear. Iterative learning control (ILC) improves performance by using information from previous iterations to compensate for expected errors in future iterations. This work incorporates the use of Quasi-Periodic Gaussian Processes (QPGPs) into a predictive ILC framework to model and forecast disturbances and drift across iterations. Using a recent structural equation formulation of QPGPs, the proposed approach enables efficient inference with complexity $\mathcal{O}(p^3)$ instead of $\mathcal{O}(i^2p^3)$, where $p$ denotes the number of points within an iteration and $i$ represents the total number of iterations, specially for larger $i$. This formulation also enables parameter estimation without loss of information, making continual GP learning computationally feasible within the control loop. By predicting next-iteration error profiles rather than relying only on past errors, the controller achieves faster convergence and maintains this under time-varying disturbances. We benchmark the method against both standard ILC and conventional Gaussian Process (GP)-based predictive ILC on three tasks, autonomous vehicle trajectory tracking, a three-link robotic manipulator, and a real-world Stretch robot experiment. Across all cases, the proposed approach converges faster and remains robust under injected and natural disturbances while reducing computational cost. This highlights its practicality across a range of repetitive dynamical systems.

