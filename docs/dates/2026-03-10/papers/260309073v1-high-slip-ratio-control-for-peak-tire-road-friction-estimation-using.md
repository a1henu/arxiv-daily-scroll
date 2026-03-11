---
layout: default
title: High-Slip-Ratio Control for Peak Tire-Road Friction Estimation Using Automated Vehicles
---

# High-Slip-Ratio Control for Peak Tire-Road Friction Estimation Using Automated Vehicles
**arXiv**：[2603.09073v1](https://arxiv.org/abs/2603.09073) · [PDF](https://arxiv.org/pdf/2603.09073.pdf)  
**作者**：Zhaohui Liang, Hang Zhou, Heye Huanh, Xiaopeng Li  

**一句话要点**：提出高滑移率控制框架，用于自动车辆在空载时主动激发峰值轮胎-路面摩擦系数估计。

**关键词**：轮胎-路面摩擦系数估计, 高滑移率控制, 自动车辆, 最优控制, Magic Formula模型, 道路摩擦筛查

## 3 点简述
- 现有方法依赖常规车辆自然驾驶数据，滑移激励不足，峰值摩擦系数可观测性有限。
- 采用简化Magic Formula轮胎模型，结合约束最优控制平衡滑移激励、轨迹跟踪和防撞。
- 通过闭环仿真和实车实验验证，框架在噪声和局部稀疏下能准确、安全地估计峰值摩擦系数。

## 摘要（原文）

> Accurate estimation of the tire-road friction coefficient (TRFC) is critical for ensuring safe vehicle control, especially under adverse road conditions. However, most existing methods rely on naturalistic driving data from regular vehicles, which typically operate under mild acceleration and braking. As a result, the data provide insufficient slip excitation and offer limited observability of the peak TRFC. This paper presents a high-slip-ratio control framework that enables automated vehicles (AVs) to actively excite the peak friction region during empty-haul operations while maintaining operational safety. A simplified Magic Formula tire model is adopted to represent nonlinear slip-force dynamics and is locally fitted using repeated high-slip measurements. To support safe execution in car-following scenarios, we formulate a constrained optimal control strategy that balances slip excitation, trajectory tracking, and collision avoidance. In parallel, a binning-based statistical projection method is introduced to robustly estimate peak TRFC under noise and local sparsity. The framework is validated through both closed-loop simulations and real-vehicle experiments, demonstrating its accuracy, safety, and feasibility for scalable, cost-effective roadway friction screening.

