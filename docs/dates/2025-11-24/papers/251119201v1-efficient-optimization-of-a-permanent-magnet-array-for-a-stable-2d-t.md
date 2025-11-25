---
layout: default
title: Efficient Optimization of a Permanent Magnet Array for a Stable 2D Trap
---

# Efficient Optimization of a Permanent Magnet Array for a Stable 2D Trap
**arXiv**：[2511.19201v1](https://arxiv.org/abs/2511.19201) · [PDF](https://arxiv.org/pdf/2511.19201.pdf)  
**作者**：Ann-Sophia Müller, Moonkwang Jeong, Jiyuan Tian, Meng Zhang, Tian Qiu  

**一句话要点**：提出基于GPU加速优化算法的永磁体阵列，实现稳定二维磁力陷阱以控制医疗微型机器人。

**关键词**：永磁体阵列, 磁力陷阱, GPU加速优化, 微型机器人控制, Adam优化器

## 3 点简述
- 核心问题：静态永磁体无法在三维空间实现稳定磁陷阱，且微型机器人在大距离下难以施加高驱动力。
- 方法要点：使用均方误差和Adam优化器，GPU加速计算永磁体阵列中磁体的最优角度。
- 实验或效果：通过仿真和物理实验验证，成功捕获并控制微型机器人沿复杂轨迹运动。

## 摘要（原文）

> Untethered magnetic manipulation of biomedical millirobots has a high potential for minimally invasive surgical applications. However, it is still challenging to exert high actuation forces on the small robots over a large distance. Permanent magnets offer stronger magnetic torques and forces than electromagnetic coils, however, feedback control is more difficult. As proven by Earnshaw's theorem, it is not possible to achieve a stable magnetic trap in 3D by static permanent magnets. Here, we report a stable 2D magnetic force trap by an array of permanent magnets to control a millirobot. The trap is located in an open space with a tunable distance to the magnet array in the range of 20 - 120mm, which is relevant to human anatomical scales. The design is achieved by a novel GPU-accelerated optimization algorithm that uses mean squared error (MSE) and Adam optimizer to efficiently compute the optimal angles for any number of magnets in the array. The algorithm is verified using numerical simulation and physical experiments with an array of two magnets. A millirobot is successfully trapped and controlled to follow a complex trajectory. The algorithm demonstrates high scalability by optimizing the angles for 100 magnets in under three seconds. Moreover, the optimization workflow can be adapted to optimize a permanent magnet array to achieve the desired force vector fields.

