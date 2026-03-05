---
layout: default
title: Architecture and evaluation protocol for transformer-based visual object tracking in UAV applications
---

# Architecture and evaluation protocol for transformer-based visual object tracking in UAV applications
**arXiv**：[2603.03904v1](https://arxiv.org/abs/2603.03904) · [PDF](https://arxiv.org/pdf/2603.03904.pdf)  
**作者**：Augustin Borne, Pierre Notin, Christophe Hennequin, Sebastien Changey, Stephane Bazeille, Christophe Cudel, Franz Quint  

**一句话要点**：提出MATA架构与NT2F指标，以提升无人机视觉目标跟踪的鲁棒性与嵌入式实时性能。

**关键词**：无人机视觉跟踪, Transformer跟踪器, 嵌入式系统评估, 扩展卡尔曼滤波, 自运动补偿, NT2F指标

## 3 点简述
- 无人机目标跟踪面临平台动态、相机运动和资源限制的挑战，现有方法在复杂场景下鲁棒性不足或计算开销大。
- 提出MATA架构，结合基于Transformer的跟踪器与扩展卡尔曼滤波，集成自运动补偿和轨迹模型，增强跟踪稳定性。
- 引入硬件无关的嵌入式评估协议和NT2F指标，实验在无人机基准上显示成功率和NT2F提升，ROS 2实现验证实时性能。

## 摘要（原文）

> Object tracking from Unmanned Aerial Vehicles (UAVs) is challenged by platform dynamics, camera motion, and limited onboard resources. Existing visual trackers either lack robustness in complex scenarios or are too computationally demanding for real-time embedded use. We propose an Modular Asynchronous Tracking Architecture (MATA) that combines a transformer-based tracker with an Extended Kalman Filter, integrating ego-motion compensation from sparse optical flow and an object trajectory model. We further introduce a hardware-independent, embedded oriented evaluation protocol and a new metric called Normalized time to Failure (NT2F) to quantify how long a tracker can sustain a tracking sequence without external help. Experiments on UAV benchmarks, including an augmented UAV123 dataset with synthetic occlusions, show consistent improvements in Success and NT2F metrics across multiple tracking processing frequency. A ROS 2 implementation on a Nvidia Jetson AGX Orin confirms that the evaluation protocol more closely matches real-time performance on embedded systems.

