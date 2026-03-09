---
layout: default
title: SuperSuit: An Isomorphic Bimodal Interface for Scalable Mobile Manipulation
---

# SuperSuit: An Isomorphic Bimodal Interface for Scalable Mobile Manipulation
**arXiv**：[2603.06280v1](https://arxiv.org/abs/2603.06280) · [PDF](https://arxiv.org/pdf/2603.06280.pdf)  
**作者**：Tongqing Chen, Hang Wu, Jiasen Wang, Xiaotao Li, Zhu Jin, Lu Fang  

**一句话要点**：提出SuperSuit双模态框架，通过共享运动学接口解决移动机械臂长时程演示数据采集瓶颈。

**关键词**：移动机械臂, 数据采集, 双模态接口, 运动学表示, 长时程任务, 可穿戴设备

## 3 点简述
- 核心问题：移动机械臂需协调SE(2)运动与精确操作，现有遥操作和可穿戴接口数据采集效率低。
- 方法要点：采用双模态（遥操作和主动演示）共享运动学接口，映射人类步进为连续基座速度，使用同构可穿戴臂。
- 实验或效果：主动模式演示吞吐量比遥操作基线高2.6倍，数据混合后策略性能可比，随主动数据量增加性能单调提升。

## 摘要（原文）

> High-quality, long-horizon demonstrations are essential for embodied AI, yet acquiring such data for tightly coupled wheeled mobile manipulators remains a fundamental bottleneck. Unlike fixed-base systems, mobile manipulators require continuous coordination between $SE(2)$ locomotion and precise manipulation, exposing limitations in existing teleoperation and wearable interfaces. We present \textbf{SuperSuit}, a bimodal data acquisition framework that supports both robot-in-the-loop teleoperation and active demonstration under a shared kinematic interface. Both modalities produce structurally identical joint-space trajectories, enabling direct data mixing without modifying downstream policies. For locomotion, SuperSuit maps natural human stepping to continuous planar base velocities, eliminating discrete command switches. For manipulation, it employs a strictly isomorphic wearable arm in both modes, while policy training is formulated in a shift-invariant delta-joint representation to mitigate calibration offsets and structural compliance without inverse kinematics. Real-world experiments on long-horizon mobile manipulation tasks show 2.6$\times$ higher demonstration throughput in active mode compared to a teleoperation baseline, comparable policy performance when substituting teleoperation data with active demonstrations at fixed dataset size, and monotonic performance improvement as active data volume increases. These results indicate that consistent kinematic representations across collection modalities enable scalable data acquisition for long-horizon mobile manipulation.

