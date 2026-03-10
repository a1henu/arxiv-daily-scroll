---
layout: default
title: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
---

# Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
**arXiv**：[2603.07939v1](https://arxiv.org/abs/2603.07939) · [PDF](https://arxiv.org/pdf/2603.07939.pdf)  
**作者**：Chenrui Zhang, Yiyuan Zhang, Yunfei Ye, Junkai Chen, Haozhe Wang, Cecilia Laschi  

**一句话要点**：提出轨迹驱动全局优化框架，统一建模水下欠驱动与软体机器人的结构-流体动力学参数。

**关键词**：水下机器人建模, 欠驱动机制, 软体机器人, 结构-流体动力学, 轨迹优化, 参数识别

## 3 点简述
- 核心问题：水下欠驱动与软体机器人建模需识别高维结构-流体参数，传统方法困难。
- 方法要点：基于CMA-ES，通过轨迹匹配同时优化内部弹性、阻尼和分布流体参数。
- 实验或效果：验证于欠驱动多体机制和章鱼软臂，实现高保真仿真，误差低于5%，无需手动调参。

## 摘要（原文）

> Underwater robots are widely deployed for ocean exploration and manipulation. Underactuated mechanisms are particularly advantageous in aquatic environments, as reducing actuator count lowers the risk of motor leakage while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated and soft robotic systems remains challenging because it requires identifying a high-dimensional set of internal structural and external hydrodynamic parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the proposed approach simultaneously identifies coupled internal elastic, damping, and distributed hydrodynamic parameters through trajectory-level matching between simulation and experimental motion. This enables high-fidelity reproduction of both underactuated mechanisms and compliant soft robotic systems in underwater environments. We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification of distributed hydrodynamic coefficients, with a normalized end effector position error below 5% across multiple trajectories, varying initial conditions, and both active-passive and fully passive configurations. The identified modeling strategy is then transferred to a single octopus-inspired soft arm, showing strong real-to-sim consistency without manual retuning. Finally, eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole body behavior without additional parameter calibration. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic modeling framework across underwater underactuated and soft robotic systems.

