---
layout: default
title: Hybrid Offline-Online Reinforcement Learning for Sensorless, High-Precision Force Regulation in Surgical Robotic Grasping
---

# Hybrid Offline-Online Reinforcement Learning for Sensorless, High-Precision Force Regulation in Surgical Robotic Grasping
**arXiv**：[2602.23870v1](https://arxiv.org/abs/2602.23870) · [PDF](https://arxiv.org/pdf/2602.23870.pdf)  
**作者**：Edoardo Fazzari, Omar Mohamed, Khalfan Hableel, Hamdan Alhadhrami, Cesare Stefanini  

**一句话要点**：提出混合离线-在线强化学习框架，实现手术机器人抓取中无传感器的高精度力调节。

**关键词**：手术机器人, 力调节, 强化学习, 无传感器控制, 数字孪生, 仿真到现实迁移

## 3 点简述
- 核心问题：肌腱驱动手术器械中，电机动力学、传动柔顺性、摩擦和远端机械的非线性耦合限制了精确抓取力调节。
- 方法要点：结合物理一致建模与三阶段强化学习，包括离线策略学习和在线精炼，无需远端传感。
- 实验或效果：仿真中力误差低于1%，硬件实验平均误差低于4%，验证了仿真到现实的迁移能力。

## 摘要（原文）

> Precise grasp force regulation in tendon-driven surgical instruments is fundamentally limited by nonlinear coupling between motor dynamics, transmission compliance, friction, and distal mechanics. Existing solutions typically rely on distal force sensing or analytical compensation, increasing hardware complexity or degrading performance under dynamic motion. We present a sensorless control framework that combines physics-consistent modeling and hybrid reinforcement learning to achieve high-precision distal force regulation in a proximally actuated surgical end-effector. We develop a first-principles digital twin of the da Vinci Xi grasping mechanism that captures coupled electrical, transmission, and jaw dynamics within a unified differential-algebraic formulation. To safely learn control policies in this stiff and highly nonlinear system, we introduce a three-stage pipeline:(i)a receding-horizon CMA-ES oracle that generates dynamically feasible expert trajectories,(ii)fully offline policy learning via Implicit Q-Learning to ensure stable initialization without unsafe exploration, and (iii)online refinement using TD3 for adaptation to on-policy dynamics. The resulting policy directly maps proximal measurements to motor voltages and requires no distal sensing. In simulation, the controller maintains grasp force within 1% of the desired reference during multi-harmonic jaw motion. Hardware experiments demonstrate average force errors below 4% across diverse trajectories, validating sim-to-real transfer. The learned policy contains approximately 71k param and executes at kH rates, enabling real-time deployment. These results demonstrate that high-fidelity modeling combined with structured offline-online RL can recover precise distal force behavior without additional sensing, offering a scalable and mechanically compatible solution for surgical robotic manipulation.

