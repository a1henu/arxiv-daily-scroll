---
layout: default
title: Integrated YOLOP Perception and Lyapunov-based Control for Autonomous Mobile Robot Navigation on Track
---

# Integrated YOLOP Perception and Lyapunov-based Control for Autonomous Mobile Robot Navigation on Track
**arXiv**：[2512.01608v1](https://arxiv.org/abs/2512.01608) · [PDF](https://arxiv.org/pdf/2512.01608.pdf)  
**作者**：Mo Chen  

**一句话要点**：提出集成YOLOP感知与李雅普诺夫控制框架，实现非完整移动机器人在轨道上的实时自主导航。

**关键词**：自主导航, 视觉感知, 李雅普诺夫控制, 非完整机器人, 实时系统, 轨道跟踪

## 3 点简述
- 核心问题：非完整移动机器人在动态、部分感知轨道场景中，缺乏高精度地图或全球定位下的稳定导航。
- 方法要点：通过2D-3D投影、重采样和多项式拟合重建车道中心线，结合李雅普诺夫稳定性设计控制器，确保误差有界和渐近收敛。
- 实验或效果：嵌入式平台真实实验验证了系统保真度、实时性、轨迹平滑性和闭环稳定性。

## 摘要（原文）

> This work presents a real-time autonomous track navigation framework for nonholonomic differential-drive mobile robots by jointly integrating multi-task visual perception and a provably stable tracking controller. The perception pipeline reconstructs lane centerlines using 2D-to-3D camera projection, arc-length based uniform point resampling, and cubic polynomial fitting solved via robust QR least-squares optimization. The controller regulates robot linear and angular velocities through a Lyapunov-stability grounded design, ensuring bounded error dynamics and asymptotic convergence of position and heading deviations even in dynamic and partially perceived lane scenarios, without relying on HD prior maps or global satellite localization. Real-world experiments on embedded platforms verify system fidelity, real-time execution, trajectory smoothness, and closed-loop stability for reliable autonomous navigation.

