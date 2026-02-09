---
layout: default
title: Consensus-based optimization (CBO): Towards Global Optimality in Robotics
---

# Consensus-based optimization (CBO): Towards Global Optimality in Robotics
**arXiv**：[2602.06868v1](https://arxiv.org/abs/2602.06868) · [PDF](https://arxiv.org/pdf/2602.06868.pdf)  
**作者**：Xudong Sun, Armand Jordana, Massimo Fornasier, Jalal Etesami, Majid Khadiv  

**一句话要点**：提出共识优化方法以解决机器人轨迹优化中的全局最优问题

**关键词**：机器人轨迹优化, 全局优化, 零阶优化, 共识优化, 长时域规划, 欠驱动系统

## 3 点简述
- 现有零阶优化方法依赖梯度估计，本质上是局部优化，难以保证全局最优
- 引入共识优化方法，在温和假设下理论保证收敛到全局最优，提供理论分析和直观示例
- 在三个挑战性轨迹优化场景中实验，相比现有方法实现更低成本，展示可扩展性

## 摘要（原文）

> Zero-order optimization has recently received significant attention for designing optimal trajectories and policies for robotic systems. However, most existing methods (e.g., MPPI, CEM, and CMA-ES) are local in nature, as they rely on gradient estimation. In this paper, we introduce consensus-based optimization (CBO) to robotics, which is guaranteed to converge to a global optimum under mild assumptions. We provide theoretical analysis and illustrative examples that give intuition into the fundamental differences between CBO and existing methods. To demonstrate the scalability of CBO for robotics problems, we consider three challenging trajectory optimization scenarios: (1) a long-horizon problem for a simple system, (2) a dynamic balance problem for a highly underactuated system, and (3) a high-dimensional problem with only a terminal cost. Our results show that CBO is able to achieve lower costs with respect to existing methods on all three challenging settings. This opens a new framework to study global trajectory optimization in robotics.

