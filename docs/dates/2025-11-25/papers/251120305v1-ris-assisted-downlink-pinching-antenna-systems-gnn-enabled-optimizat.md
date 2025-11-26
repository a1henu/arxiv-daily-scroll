---
layout: default
title: RIS-Assisted Downlink Pinching-Antenna Systems: GNN-Enabled Optimization Approaches
---

# RIS-Assisted Downlink Pinching-Antenna Systems: GNN-Enabled Optimization Approaches
**arXiv**：[2511.20305v1](https://arxiv.org/abs/2511.20305) · [PDF](https://arxiv.org/pdf/2511.20305.pdf)  
**作者**：Changpeng He, Yang Lu, Yanqing Xu, Chong-Yung Chi, Bo Ai, Arumugam Nallanathan  

**一句话要点**：提出基于图神经网络的优化方法，用于RIS辅助多用户下行链路捏合天线系统。

**关键词**：可重构智能表面, 捏合天线系统, 图神经网络, 和速率优化, 能效优化, 多用户下行链路

## 3 点简述
- 研究RIS与捏合天线系统集成对无线通信的影响，聚焦和速率与能效最大化问题。
- 设计三阶段图神经网络，学习天线位置、RIS相位和波束成形，结合凸优化策略。
- 数值实验验证方法有效性，展示泛化能力、性能可靠性和实时适用性。

## 摘要（原文）

> This paper investigates a reconfigurable intelligent surface (RIS)-assisted multi-waveguide pinching-antenna (PA) system (PASS) for multi-user downlink information transmission, motivated by the unknown impact of the integration of emerging PASS and RIS on wireless communications. First, we formulate sum rate (SR) and energy efficiency (EE) maximization problems in a unified framework, subject to constraints on the movable region of PAs, total power budget, and tunable phase of RIS elements. Then, by leveraging a graph-structured topology of the RIS-assisted PASS, a novel three-stage graph neural network (GNN) is proposed, which learns PA positions based on user locations, and RIS phase shifts according to composite channel conditions at the first two stages, respectively, and finally determines beamforming vectors. Specifically, the proposed GNN is achieved through unsupervised training, together with three implementation strategies for its integration with convex optimization, thus offering trade-offs between inference time and solution optimality. Extensive numerical results are provided to validate the effectiveness of the proposed GNN, and to support its unique attributes of viable generalization capability, good performance reliability, and real-time applicability. Moreover, the impact of key parameters on RIS-assisted PASS is illustrated and analyzed.

