---
layout: default
title: Predefined-time One-Shot Cooperative Estimation, Guidance, and Control for Simultaneous Target Interception
---

# Predefined-time One-Shot Cooperative Estimation, Guidance, and Control for Simultaneous Target Interception
**arXiv**：[2601.07744v1](https://arxiv.org/abs/2601.07744) · [PDF](https://arxiv.org/pdf/2601.07744.pdf)  
**作者**：Lohitvel Gopikannan, Shashi Ranjan Kumar, Abhinav Sinha  

**一句话要点**：提出预定义时间一体化框架，解决异构传感下多拦截器协同同时拦截静止目标问题

**关键词**：协同拦截, 预定义时间控制, 分布式观测器, 时间协同, 自动驾驶仪, 滑模控制

## 3 点简述
- 核心问题：异构传感拓扑中部分拦截器无导引头，导致目标状态估计不完全可观测
- 方法要点：利用预定义时间分布式观测器和时间协同协议，确保估计与时间协同误差在指定时间内收敛
- 实验或效果：数值模拟验证了估计精度、协同拦截性能和自动驾驶仪响应，适用于多种交战几何

## 摘要（原文）

> This work develops a unified nonlinear estimation-guidance-control framework for cooperative simultaneous interception of a stationary target under a heterogeneous sensing topology, where sensing capabilities are non-uniform across interceptors. Specifically, only a subset of agents is instrumented with onboard seekers (informed/seeker-equipped agents), whereas the rest of them (seeker-less agents) acquire the information about the target indirectly via the informed agents and execute a distributed cooperative guidance for simultaneous target interception. To address the resulting partial observability, a predefined-time distributed observer is leveraged, guaranteeing convergence of the target state estimates for seeker-less agents through information exchange with seeker-equipped neighbors over a directed communication graph. Thereafter, an improved time-to-go estimate accounting for wide launch envelopes is utilized to design the distributed cooperative guidance commands. This estimate is coupled with a predefined-time consensus protocol, ensuring consensus in the agents' time-to-go values. The temporal upper bounds within which both observer error and time-to-go consensus error converge to zero can be prescribed as design parameters. Furthermore, the cooperative guidance commands are realized by means of an autopilot, wherein the interceptor is steered by canard actuation. The corresponding fin deflection commands are generated using a predefined-time convergent sliding mode control law. This enables the autopilot to precisely track the commanded lateral acceleration within a design-specified time, while maintaining non-singularity of the overall design. Theoretical guarantees are supported by numerical simulations across diverse engagement geometries, verifying the estimation accuracy, the cooperative interception performance, and the autopilot response using the proposed scheme.

