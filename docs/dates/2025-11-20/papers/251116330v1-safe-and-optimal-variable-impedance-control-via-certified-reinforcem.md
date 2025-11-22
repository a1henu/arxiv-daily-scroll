---
layout: default
title: Safe and Optimal Variable Impedance Control via Certified Reinforcement Learning
---

# Safe and Optimal Variable Impedance Control via Certified Reinforcement Learning
**arXiv**：[2511.16330v1](https://arxiv.org/abs/2511.16330) · [PDF](https://arxiv.org/pdf/2511.16330.pdf)  
**作者**：Shreyas Kumar, Ravi Prakash  

**一句话要点**：提出认证高斯流形采样以解决机器人变阻抗控制中的不稳定问题

**关键词**：强化学习, 变阻抗控制, 李雅普诺夫稳定, 机器人控制, 认证学习

## 3 点简述
- 核心问题：模型无关强化学习在变阻抗控制中易导致不稳定和不安全探索
- 方法要点：通过采样稳定增益流形，保证李雅普诺夫稳定性和执行器可行性
- 实验或效果：在仿真和真实机器人上验证了有界跟踪误差和可靠性

## 摘要（原文）

> Reinforcement learning (RL) offers a powerful approach for robots to learn complex, collaborative skills by combining Dynamic Movement Primitives (DMPs) for motion and Variable Impedance Control (VIC) for compliant interaction. However, this model-free paradigm often risks instability and unsafe exploration due to the time-varying nature of impedance gains. This work introduces Certified Gaussian Manifold Sampling (C-GMS), a novel trajectory-centric RL framework that learns combined DMP and VIC policies while guaranteeing Lyapunov stability and actuator feasibility by construction. Our approach reframes policy exploration as sampling from a mathematically defined manifold of stable gain schedules. This ensures every policy rollout is guaranteed to be stable and physically realizable, thereby eliminating the need for reward penalties or post-hoc validation. Furthermore, we provide a theoretical guarantee that our approach ensures bounded tracking error even in the presence of bounded model errors and deployment-time uncertainties. We demonstrate the effectiveness of C-GMS in simulation and verify its efficacy on a real robot, paving the way for reliable autonomous interaction in complex environments.

