---
layout: default
title: Multi-Timescale Model Predictive Control for Slow-Fast Systems
---

# Multi-Timescale Model Predictive Control for Slow-Fast Systems
**arXiv**：[2511.14311v1](https://arxiv.org/abs/2511.14311) · [PDF](https://arxiv.org/pdf/2511.14311.pdf)  
**作者**：Lukas Schroth, Daniel Morton, Amon Lahr, Daniele Gammelli, Andrea Carron, Marco Pavone  

**一句话要点**：提出多时间尺度模型预测控制方法，以提升快慢系统实时优化效率。

**关键词**：模型预测控制, 多时间尺度系统, 计算效率优化, 机器人控制, 灵敏度分析

## 3 点简述
- 核心问题：长预测时域与高保真模型结合时，实时求解优化问题计算成本高。
- 方法要点：基于灵敏度指数衰减，切换至慢动态简化模型并指数增大积分步长。
- 实验效果：在机器人控制仿真中，计算速度提升可达一个数量级。

## 摘要（原文）

> Model Predictive Control (MPC) has established itself as the primary methodology for constrained control, enabling autonomy across diverse applications. While model fidelity is crucial in MPC, solving the corresponding optimization problem in real time remains challenging when combining long horizons with high-fidelity models that capture both short-term dynamics and long-term behavior. Motivated by results on the Exponential Decay of Sensitivities (EDS), which imply that, under certain conditions, the influence of modeling inaccuracies decreases exponentially along the prediction horizon, this paper proposes a multi-timescale MPC scheme for fast-sampled control. Tailored to systems with both fast and slow dynamics, the proposed approach improves computational efficiency by i) switching to a reduced model that captures only the slow, dominant dynamics and ii) exponentially increasing integration step sizes to progressively reduce model detail along the horizon. We evaluate the method on three practically motivated robotic control problems in simulation and observe speed-ups of up to an order of magnitude.

