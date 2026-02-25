---
layout: default
title: Optimizing Occupancy Sensor Placement in Smart Environments
---

# Optimizing Occupancy Sensor Placement in Smart Environments
**arXiv**：[2602.21098v1](https://arxiv.org/abs/2602.21098) · [PDF](https://arxiv.org/pdf/2602.21098.pdf)  
**作者**：Hao Lu, Richard J. Radke  

**一句话要点**：提出自动传感器布局优化方法，以提升智能办公环境中基于飞行时间传感器的区域人数计数准确性。

**关键词**：传感器布局优化, 整数线性规划, 飞行时间传感器, 区域人数计数, 智能办公环境, 隐私保护

## 3 点简述
- 核心问题：传感器布局对隐私保护型飞行时间传感器网络在区域人数计数中的性能有显著影响，需优化布局以最大化准确性。
- 方法要点：基于办公室几何约束模拟大量人员轨迹，将传感器布局问题建模为整数线性规划问题，采用分支定界法求解。
- 实验或效果：通过多个办公环境模拟验证了方法的有效性，能预测布局的计数准确性并确定最优传感器配置。

## 摘要（原文）

> Understanding the locations of occupants in a commercial built environment is critical for realizing energy savings by delivering lighting, heating, and cooling only where it is needed. The key to achieving this goal is being able to recognize zone occupancy in real time, without impeding occupants' activities or compromising privacy. While low-resolution, privacy-preserving time-of-flight (ToF) sensor networks have demonstrated good performance in zone counting, the performance depends on careful sensor placement. To address this issue, we propose an automatic sensor placement method that determines optimal sensor layouts for a given number of sensors, and can predict the counting accuracy of such a layout. In particular, given the geometric constraints of an office environment, we simulate a large number of occupant trajectories. We then formulate the sensor placement problem as an integer linear programming (ILP) problem and solve it with the branch and bound method. We demonstrate the effectiveness of the proposed method based on simulations of several different office environments.

