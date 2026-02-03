---
layout: default
title: Tilt-Ropter: A Novel Hybrid Aerial and Terrestrial Vehicle with Tilt Rotors and Passive Wheels
---

# Tilt-Ropter: A Novel Hybrid Aerial and Terrestrial Vehicle with Tilt Rotors and Passive Wheels
**arXiv**：[2602.01700v1](https://arxiv.org/abs/2602.01700) · [PDF](https://arxiv.org/pdf/2602.01700.pdf)  
**作者**：Ruoyu Wang, Xuchen Liu, Zongzhou Wu, Zixuan Guo, Wendi Ding, Ben M. Chen  

**一句话要点**：提出Tilt-Ropter混合飞行地面车辆，通过全驱动设计和NMPC控制实现高效多模式运动。

**关键词**：混合飞行地面车辆, 全驱动设计, 非线性模型预测控制, 能量效率优化, 外部力矩估计, 多模式运动

## 3 点简述
- 核心问题：现有欠驱动混合车辆在能量效率和环境适应性方面受限。
- 方法要点：采用全驱动设计结合倾斜旋翼和被动轮，开发非线性模型预测控制器和外部力矩估计算法。
- 实验或效果：实验显示地面运动功耗降低92.8%，支持无缝空-地转换和低跟踪误差。

## 摘要（原文）

> In this work, we present Tilt-Ropter, a novel hybrid aerial-terrestrial vehicle (HATV) that combines tilt rotors with passive wheels to achieve energy-efficient multi-mode locomotion. Unlike existing under-actuated HATVs, the fully actuated design of Tilt-Ropter enables decoupled force and torque control, greatly enhancing its mobility and environmental adaptability. A nonlinear model predictive controller (NMPC) is developed to track reference trajectories and handle contact constraints across locomotion modes, while a dedicated control allocation module exploits actuation redundancy to achieve energy-efficient control of actuators. Additionally, to enhance robustness during ground contact, we introduce an external wrench estimation algorithm that estimates environmental interaction forces and torques in real time. The system is validated through both simulation and real-world experiments, including seamless air-ground transitions and trajectory tracking. Results show low tracking errors in both modes and highlight a 92.8% reduction in power consumption during ground locomotion, demonstrating the system's potential for long-duration missions across large-scale and energy-constrained environments.

