---
layout: default
title: SandWorm: Event-based Visuotactile Perception with Active Vibration for Screw-Actuated Robot in Granular Media
---

# SandWorm: Event-based Visuotactile Perception with Active Vibration for Screw-Actuated Robot in Granular Media
**arXiv**：[2601.14128v1](https://arxiv.org/abs/2601.14128) · [PDF](https://arxiv.org/pdf/2601.14128.pdf)  
**作者**：Shoujie Li, Changqing Guo, Junhao Gong, Chenxin Liang, Wenhua Ding, Wenbo Ding  

**一句话要点**：提出SandWorm机器人与SWTac传感器以解决颗粒介质中感知与运动的挑战

**关键词**：颗粒介质机器人, 事件相机感知, 视觉触觉传感器, 仿生运动, 主动振动, 传感器优化

## 3 点简述
- 核心问题：颗粒介质中粒子动态不可预测，导致感知困难。
- 方法要点：结合仿生螺旋驱动与蠕动运动增强移动，并开发基于事件相机和主动振动弹性体的视觉触觉传感器。
- 实验或效果：传感器实现0.2毫米纹理分辨率，机器人成功执行管道疏浚和地下探索，成功率90%。

## 摘要（原文）

> Perception in granular media remains challenging due to unpredictable particle dynamics. To address this challenge, we present SandWorm, a biomimetic screw-actuated robot augmented by peristaltic motion to enhance locomotion, and SWTac, a novel event-based visuotactile sensor with an actively vibrated elastomer. The event camera is mechanically decoupled from vibrations by a spring isolation mechanism, enabling high-quality tactile imaging of both dynamic and stationary objects. For algorithm design, we propose an IMU-guided temporal filter to enhance imaging consistency, improving MSNR by 24%. Moreover, we systematically optimize SWTac with vibration parameters, event camera settings and elastomer properties. Motivated by asymmetric edge features, we also implement contact surface estimation by U-Net. Experimental validation demonstrates SWTac's 0.2 mm texture resolution, 98% stone classification accuracy, and 0.15 N force estimation error, while SandWorm demonstrates versatile locomotion (up to 12.5 mm/s) in challenging terrains, successfully executes pipeline dredging and subsurface exploration in complex granular media (observed 90% success rate). Field experiments further confirm the system's practical performance.

