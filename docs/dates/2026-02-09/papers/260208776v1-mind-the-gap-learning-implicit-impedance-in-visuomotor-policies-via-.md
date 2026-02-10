---
layout: default
title: Mind the Gap: Learning Implicit Impedance in Visuomotor Policies via Intent-Execution Mismatch
---

# Mind the Gap: Learning Implicit Impedance in Visuomotor Policies via Intent-Execution Mismatch
**arXiv**：[2602.08776v1](https://arxiv.org/abs/2602.08776) · [PDF](https://arxiv.org/pdf/2602.08776.pdf)  
**作者**：Cuijie Xu, Shurui Zheng, Zihao Su, Yuanfan Xu, Tinghao Yi, Xudong Zhang, Jian Wang, Yu Wang, Jinchen Yu  

**一句话要点**：提出基于意图-执行不匹配的双状态条件框架，实现低成本硬件上的隐式阻抗控制与系统辨识。

**关键词**：遥操作, 行为克隆, 隐式阻抗控制, 系统辨识, 轨迹修复, 低成本硬件

## 3 点简述
- 核心问题：遥操作中标准行为克隆忽略人类补偿机制，导致无法处理硬件缺陷如延迟和接触刚度。
- 方法要点：通过意图克隆学习虚拟平衡点，利用不匹配历史进行隐式系统辨识，并采用轨迹修复确保连续控制。
- 实验或效果：在无传感器低成本双手机器人上验证，相比执行克隆，该方法在接触丰富操作和动态跟踪任务中实现鲁棒成功。

## 摘要（原文）

> Teleoperation inherently relies on the human operator acting as a closed-loop controller to actively compensate for hardware imperfections, including latency, mechanical friction, and lack of explicit force feedback. Standard Behavior Cloning (BC), by mimicking the robot's executed trajectory, fundamentally ignores this compensatory mechanism. In this work, we propose a Dual-State Conditioning framework that shifts the learning objective to "Intent Cloning" (master command). We posit that the Intent-Execution Mismatch, the discrepancy between master command and slave response, is not noise, but a critical signal that physically encodes implicit interaction forces and algorithmically reveals the operator's strategy for overcoming system dynamics. By predicting the master intent, our policy learns to generate a "virtual equilibrium point", effectively realizing implicit impedance control. Furthermore, by explicitly conditioning on the history of this mismatch, the model performs implicit system identification, perceiving tracking errors as external forces to close the control loop. To bridge the temporal gap caused by inference latency, we further formulate the policy as a trajectory inpainter to ensure continuous control. We validate our approach on a sensorless, low-cost bi-manual setup. Empirical results across tasks requiring contact-rich manipulation and dynamic tracking reveal a decisive gap: while standard execution-cloning fails due to the inability to overcome contact stiffness and tracking lag, our mismatch-aware approach achieves robust success. This presents a minimalist behavior cloning framework for low-cost hardware, enabling force perception and dynamic compensation without relying on explicit force sensing. Videos are available on the \href{https://xucj98.github.io/mind-the-gap-page/}{project page}.

