---
layout: default
title: NeuroHJR: Hamilton-Jacobi Reachability-based Obstacle Avoidance in Complex Environments with Physics-Informed Neural Networks
---

# NeuroHJR: Hamilton-Jacobi Reachability-based Obstacle Avoidance in Complex Environments with Physics-Informed Neural Networks
**arXiv**：[2512.01897v1](https://arxiv.org/abs/2512.01897) · [PDF](https://arxiv.org/pdf/2512.01897.pdf)  
**作者**：Granthik Halder, Rudrashis Majumder, Rakshith M R, Rahi Shah, Suresh Sundaram  

**一句话要点**：提出NeuroHJR框架，利用物理信息神经网络近似汉密尔顿-雅可比可达性，以在复杂环境中实现实时避障。

**关键词**：汉密尔顿-雅可比可达性, 物理信息神经网络, 实时避障, 可达集估计, 自主地面车辆

## 3 点简述
- 核心问题：汉密尔顿-雅可比可达性在密集障碍物环境中计算可扩展性差，阻碍实时应用。
- 方法要点：通过物理信息神经网络嵌入系统动力学和安全约束，避免网格离散化，在连续状态空间高效估计可达集。
- 实验或效果：在密集杂乱场景的仿真中，安全性能接近经典求解器，同时显著降低计算成本。

## 摘要（原文）

> Autonomous ground vehicles (AGVs) must navigate safely in cluttered environments while accounting for complex dynamics and environmental uncertainty. Hamilton-Jacobi Reachability (HJR) offers formal safety guarantees through the computation of forward and backward reachable sets, but its application is hindered by poor scalability in environments with numerous obstacles. In this paper, we present a novel framework called NeuroHJR that leverages Physics-Informed Neural Networks (PINNs) to approximate the HJR solution for real-time obstacle avoidance. By embedding system dynamics and safety constraints directly into the neural network loss function, our method bypasses the need for grid-based discretization and enables efficient estimation of reachable sets in continuous state spaces. We demonstrate the effectiveness of our approach through simulation results in densely cluttered scenarios, showing that it achieves safety performance comparable to that of classical HJR solvers while significantly reducing the computational cost. This work provides a new step toward real-time, scalable deployment of reachability-based obstacle avoidance in robotics.

