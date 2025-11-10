---
layout: default
title: Tunable Passivity Control for Centralized Multiport Networked Systems
---

# Tunable Passivity Control for Centralized Multiport Networked Systems
**arXiv**：[2511.05026v1](https://arxiv.org/abs/2511.05026) · [PDF](https://arxiv.org/pdf/2511.05026.pdf)  
**作者**：Xingyuan Zhou, Peter Paik, S. Farokh Atashzar  

**一句话要点**：提出可调集中最优无源性控制框架，以增强集中式多端口网络系统的稳定性。

**关键词**：集中式多端口网络系统, 无源性控制, 稳定性分析, 最优控制, 网络系统仿真

## 3 点简述
- 核心问题：集中式多端口网络系统因网络非理想因素影响稳定性，传统无源性方法灵活性不足。
- 方法要点：采用集中无源性观测器和最优控制器，按需分配耗散，确保严格无源性和L2稳定性。
- 实验或效果：仿真显示在时变延迟下提升性能，放宽远程节点最小相位和无源性假设。

## 摘要（原文）

> Centralized Multiport Networked Dynamic (CMND) systems have emerged as a key
> architecture with applications in several complex network systems, such as
> multilateral telerobotics and multi-agent control. These systems consist of a
> hub node/subsystem connecting with multiple remote nodes/subsystems via a
> networked architecture. One challenge for this system is stability, which can
> be affected by non-ideal network artifacts. Conventional passivity-based
> approaches can stabilize the system under specialized applications like
> small-scale networked systems. However, those conventional passive stabilizers
> have several restrictions, such as distributing compensation across subsystems
> in a decentralized manner, limiting flexibility, and, at the same time, relying
> on the restrictive assumptions of node passivity. This paper synthesizes a
> centralized optimal passivity-based stabilization framework for CMND systems.
> It consists of a centralized passivity observer monitoring overall energy flow
> and an optimal passivity controller that distributes the just-needed
> dissipation among various nodes, guaranteeing strict passivity and, thus, L2
> stability. The proposed data-driven model-free approach, i.e., Tunable
> Centralized Optimal Passivity Control (TCoPC), optimizes total performance
> based on the prescribed dissipation distribution strategy while ensuring
> stability. The controller can put high dissipation loads on some sub-networks
> while relaxing the dissipation on other nodes. Simulation results demonstrate
> the proposed frameworks performance in a complex task under different
> time-varying delay scenarios while relaxing the remote nodes minimum phase and
> passivity assumption, enhancing the scalability and generalizability.

