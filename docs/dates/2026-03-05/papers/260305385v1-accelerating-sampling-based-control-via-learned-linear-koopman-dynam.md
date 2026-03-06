---
layout: default
title: Accelerating Sampling-Based Control via Learned Linear Koopman Dynamics
---

# Accelerating Sampling-Based Control via Learned Linear Koopman Dynamics
**arXiv**：[2603.05385v1](https://arxiv.org/abs/2603.05385) · [PDF](https://arxiv.org/pdf/2603.05385.pdf)  
**作者**：Wenjian Hao, Yuxuan Fang, Zehui Lu, Shaoshuai Mou  

**一句话要点**：提出基于学习线性Koopman动力学的MPPI-DK控制器，以加速非线性系统采样控制

**关键词**：模型预测路径积分控制, Koopman算子, 非线性系统控制, 实时控制, 机器人控制

## 3 点简述
- 核心问题：经典MPPI在复杂非线性系统中计算效率低，影响实时控制性能
- 方法要点：用学习线性深度Koopman算子替代非线性动力学，提升轨迹传播和采样效率
- 实验或效果：在仿真和硬件实验中，MPPI-DK保持接近真实动力学的控制性能，显著降低计算成本

## 摘要（原文）

> This paper presents an efficient model predictive path integral (MPPI) control framework for systems with complex nonlinear dynamics. To improve the computational efficiency of classic MPPI while preserving control performance, we replace the nonlinear dynamics used for trajectory propagation with a learned linear deep Koopman operator (DKO) model, enabling faster rollout and more efficient trajectory sampling. The DKO dynamics are learned directly from interaction data, eliminating the need for analytical system models. The resulting controller, termed MPPI-DK, is evaluated in simulation on pendulum balancing and surface vehicle navigation tasks, and validated on hardware through reference-tracking experiments on a quadruped robot. Experimental results demonstrate that MPPI-DK achieves control performance close to MPPI with true dynamics while substantially reducing computational cost, enabling efficient real-time control on robotic platforms.

