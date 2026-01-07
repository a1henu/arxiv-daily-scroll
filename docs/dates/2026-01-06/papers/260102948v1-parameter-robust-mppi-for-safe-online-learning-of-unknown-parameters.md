---
layout: default
title: Parameter-Robust MPPI for Safe Online Learning of Unknown Parameters
---

# Parameter-Robust MPPI for Safe Online Learning of Unknown Parameters
**arXiv**：[2601.02948v1](https://arxiv.org/abs/2601.02948) · [PDF](https://arxiv.org/pdf/2601.02948.pdf)  
**作者**：Matti Vahs, Jaeyoun Choi, Niklas Schmid, Jana Tumova, Chuchu Fan  

**一句话要点**：提出参数鲁棒MPPI控制框架，集成在线参数学习与概率安全约束，确保机器人在动态环境中的安全操作。

**关键词**：机器人控制, 在线参数学习, 概率安全约束, 模型预测路径积分, Stein变分梯度下降, Conformal Prediction

## 3 点简述
- 核心问题：机器人在动态环境中面临物理参数不确定或变化时，如何保持安全操作。
- 方法要点：通过Stein变分梯度下降维护参数粒子信念，使用Conformal Prediction评估安全约束，并行优化性能驱动和安全备份轨迹。
- 实验或效果：仿真和硬件实验显示，相比基线方法，具有更高成功率、更低跟踪误差和更准确参数估计。

## 摘要（原文）

> Robots deployed in dynamic environments must remain safe even when key physical parameters are uncertain or change over time. We propose Parameter-Robust Model Predictive Path Integral (PRMPPI) control, a framework that integrates online parameter learning with probabilistic safety constraints. PRMPPI maintains a particle-based belief over parameters via Stein Variational Gradient Descent, evaluates safety constraints using Conformal Prediction, and optimizes both a nominal performance-driven and a safety-focused backup trajectory in parallel. This yields a controller that is cautious at first, improves performance as parameters are learned, and ensures safety throughout. Simulation and hardware experiments demonstrate higher success rates, lower tracking error, and more accurate parameter estimates than baselines.

