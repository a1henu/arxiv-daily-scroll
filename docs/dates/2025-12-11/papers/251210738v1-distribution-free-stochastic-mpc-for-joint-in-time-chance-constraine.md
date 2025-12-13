---
layout: default
title: Distribution-Free Stochastic MPC for Joint-in-Time Chance-Constrained Linear Systems
---

# Distribution-Free Stochastic MPC for Joint-in-Time Chance-Constrained Linear Systems
**arXiv**：[2512.10738v1](https://arxiv.org/abs/2512.10738) · [PDF](https://arxiv.org/pdf/2512.10738.pdf)  
**作者**：Lukas Vogel, Andrea Carron, Eleftherios E. Vlahakis, Dimos V. Dimarogonas  

**一句话要点**：提出基于共形预测的分布无关随机MPC，用于未知分布下的联合机会约束线性系统。

**关键词**：随机模型预测控制, 联合机会约束, 共形预测, 分布无关控制, 输出反馈, 递归可行性

## 3 点简述
- 核心问题：未知扰动分布下线性系统的联合机会约束随机MPC设计。
- 方法要点：利用共形预测构建有限样本置信区域，提供形式化保证，支持间接反馈和输出反馈。
- 实验或效果：数值示例验证方法有效性，相比现有方法具有计算优势。

## 摘要（原文）

> This work presents a stochastic model predictive control (MPC) framework for linear systems subject to joint-in-time chance constraints under unknown disturbance distributions. Unlike existing stochastic MPC formulations that rely on parametric or Gaussian assumptions or require expensive offline computations, the proposed method leverages conformal prediction (CP) as a streamlined tool to construct finite-sample confidence regions for the system's stochastic error trajectories with minimal computational effort. These regions enable the relaxation of probabilistic constraints while providing formal guarantees. By employing an indirect feedback mechanism and a probabilistic set-based formulation, we prove recursive feasibility of the relaxed optimization problem and establish chance constraint satisfaction in closed-loop. Furthermore, we extend the approach to the more general output feedback setting with unknown measurement noise distributions. Given available noise samples, we establish satisfaction of the joint chance constraints and recursive feasibility via output measurements alone. Numerical examples demonstrate the effectiveness and advantages of the proposed method compared to existing approaches.

