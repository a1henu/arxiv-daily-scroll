---
layout: default
title: Gauss-Newton accelerated MPPI Control
---

# Gauss-Newton accelerated MPPI Control
**arXiv**：[2512.04579v1](https://arxiv.org/abs/2512.04579) · [PDF](https://arxiv.org/pdf/2512.04579.pdf)  
**作者**：Hannes Homburger, Katrin Baumgärtner, Moritz Diehl, Johannes Reuter  

**一句话要点**：提出Gauss-Newton加速MPPI控制方法以解决高维场景下性能下降问题

**关键词**：模型预测控制, 路径积分控制, Gauss-Newton加速, 高维优化, 机器人控制, 采样优化

## 3 点简述
- 核心问题：MPPI在高维设置中性能因蒙特卡洛采样而下降
- 方法要点：结合雅可比重构技术和二阶广义Gauss-Newton方法增强MPPI
- 实验或效果：数值结果显示显著提升可扩展性和计算效率，保留经典MPPI优势

## 摘要（原文）

> Model Predictive Path Integral (MPPI) control is a sampling-based optimization method that has recently attracted attention, particularly in the robotics and reinforcement learning communities. MPPI has been widely applied as a GPU-accelerated random search method to deterministic direct single-shooting optimal control problems arising in model predictive control (MPC) formulations. MPPI offers several key advantages, including flexibility, robustness, ease of implementation, and inherent parallelizability. However, its performance can deteriorate in high-dimensional settings since the optimal control problem is solved via Monte Carlo sampling. To address this limitation, this paper proposes an enhanced MPPI method that incorporates a Jacobian reconstruction technique and the second-order Generalized Gauss-Newton method. This novel approach is called \textit{Gauss-Newton accelerated MPPI}. The numerical results show that the Gauss-Newton accelerated MPPI approach substantially improves MPPI scalability and computational efficiency while preserving the key benefits of the classical MPPI framework, making it a promising approach even for high-dimensional problems.

