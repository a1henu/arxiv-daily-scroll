---
layout: default
title: Enhancing User Throughput in Multi-panel mmWave Radio Access Networks for Beam-based MU-MIMO Using a DRL Method
---

# Enhancing User Throughput in Multi-panel mmWave Radio Access Networks for Beam-based MU-MIMO Using a DRL Method
**arXiv**：[2603.02745v1](https://arxiv.org/abs/2603.02745) · [PDF](https://arxiv.org/pdf/2603.02745.pdf)  
**作者**：Ramin Hashemi, Vismika Ranasinghe, Teemu Veijalainen, Petteri Kela, Risto Wichman  

**一句话要点**：提出基于深度强化学习的自适应波束管理方法，以提升多面板毫米波MU-MIMO网络中的用户吞吐量。

**关键词**：毫米波通信, 多用户MIMO, 深度强化学习, 波束管理, 吞吐量优化, 延迟降低

## 3 点简述
- 核心问题：毫米波MU-MIMO系统因动态波束选择复杂，面临吞吐量优化和延迟最小化的挑战。
- 方法要点：利用深度强化学习建模为马尔可夫决策过程，结合波束间互相关、RSRP和统计信息动态调整波束。
- 实验或效果：相比基线，吞吐量提升达16%，延迟降低3-7倍。

## 摘要（原文）

> Millimeter-wave (mmWave) communication systems, particularly those leveraging multi-user multiple-input and multiple-output (MU-MIMO) with hybrid beamforming, face challenges in optimizing user throughput and minimizing latency due to the high complexity of dynamic beam selection and management. This paper introduces a deep reinforcement learning (DRL) approach for enhancing user throughput in multi-panel mmWave radio access networks in a practical network setup. Our DRL-based formulation utilizes an adaptive beam management strategy that models the interaction between the communication agent and its environment as a Markov decision process (MDP), optimizing beam selection based on real-time observations. The proposed framework exploits spatial domain (SD) characteristics by incorporating the cross-correlation between the beams in different antenna panels, the measured reference signal received power (RSRP), and the beam usage statistics to dynamically adjust beamforming decisions. As a result, the spectral efficiency is improved and end-to-end latency is reduced. The numerical results demonstrate an increase in throughput of up to 16% and a reduction in latency by factors 3-7x compared to baseline (legacy beam management).

