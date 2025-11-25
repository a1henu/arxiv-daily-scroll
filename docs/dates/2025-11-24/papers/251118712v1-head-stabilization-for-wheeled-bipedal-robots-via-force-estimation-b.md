---
layout: default
title: Head Stabilization for Wheeled Bipedal Robots via Force-Estimation-Based Admittance Control
---

# Head Stabilization for Wheeled Bipedal Robots via Force-Estimation-Based Admittance Control
**arXiv**：[2511.18712v1](https://arxiv.org/abs/2511.18712) · [PDF](https://arxiv.org/pdf/2511.18712.pdf)  
**作者**：Tianyu Wang, Chunxiang Yan, Xuanhong Liao, Tao Zhang, Ping Wang, Cong Wen, Dingchuan Liu, Haowen Yu, Ximin Lyu  

**一句话要点**：提出基于力估计的导纳控制以解决轮式双足机器人头部在不平地形中的稳定性问题

**关键词**：轮式双足机器人, 头部稳定性, 力估计, 导纳控制, 地形适应性, 仿真实验

## 3 点简述
- 核心问题：轮式双足机器人在不平地形中头部不稳定，影响传感器精度和载荷安全
- 方法要点：开发基于模型的接地力估计方法，并应用导纳控制算法增强地形适应性
- 实验或效果：仿真实验验证了力估计器的实时性能和机器人在不平地形中的鲁棒性

## 摘要（原文）

> Wheeled bipedal robots are emerging as flexible platforms for field exploration. However, head instability induced by uneven terrain can degrade the accuracy of onboard sensors or damage fragile payloads. Existing research primarily focuses on stabilizing the mobile platform but overlooks active stabilization of the head in the world frame, resulting in vertical oscillations that undermine overall stability. To address this challenge, we developed a model-based ground force estimation method for our 6-degree-of-freedom wheeled bipedal robot. Leveraging these force estimates, we implemented an admittance control algorithm to enhance terrain adaptability. Simulation experiments validated the real-time performance of the force estimator and the robot's robustness when traversing uneven terrain.

