---
layout: default
title: Encoding Biomechanical Energy Margin into Passivity-based Synchronization for Networked Telerobotic Systems
---

# Encoding Biomechanical Energy Margin into Passivity-based Synchronization for Networked Telerobotic Systems
**arXiv**：[2511.04994v1](https://arxiv.org/abs/2511.04994) · [PDF](https://arxiv.org/pdf/2511.04994.pdf)  
**作者**：Xingyuan Zhou, Peter Paik, S. Farokh Atashzar  

**一句话要点**：提出TBPS2同步器以解决网络遥操作机器人位置失同步问题

**关键词**：网络遥操作机器人, 生物力学感知, 被动同步, 位置跟踪, 系统稳定性, 时延控制

## 3 点简述
- 核心问题：网络延迟和非被动行为导致位置失同步，影响稳定性和跟踪精度
- 方法要点：设计两端口生物力学感知被动同步器，优化同步并减少保守激活
- 实验或效果：通过网格模拟和系统实验，在多种延迟和环境下验证性能优于现有方案

## 摘要（原文）

> Maintaining system stability and accurate position tracking is imperative in
> networked robotic systems, particularly for haptics-enabled human-robot
> interaction. Recent literature has integrated human biomechanics into the
> stabilizers implemented for teleoperation, enhancing force preservation while
> guaranteeing convergence and safety. However, position desynchronization due to
> imperfect communication and non-passive behaviors remains a challenge. This
> paper proposes a two-port biomechanics-aware passivity-based synchronizer and
> stabilizer, referred to as TBPS2. This stabilizer optimizes position
> synchronization by leveraging human biomechanics while reducing the
> stabilizer's conservatism in its activation. We provide the mathematical design
> synthesis of the stabilizer and the proof of stability. We also conducted a
> series of grid simulations and systematic experiments, comparing their
> performance with that of state-of-the-art solutions under varying time delays
> and environmental conditions.

