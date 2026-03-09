---
layout: default
title: OpenHEART: Opening Heterogeneous Articulated Objects with a Legged Manipulator
---

# OpenHEART: Opening Heterogeneous Articulated Objects with a Legged Manipulator
**arXiv**：[2603.05830v1](https://arxiv.org/abs/2603.05830) · [PDF](https://arxiv.org/pdf/2603.05830.pdf)  
**作者**：Seonghyeon Lim, Hyeonwoo Lee, Seunghyun Lee, I Made Aswin Nahrendra, Hyun Myung  

**一句话要点**：提出OpenHEART框架，通过SAFE和ArtIEst方法，实现腿式机器人高效打开异构铰接物体。

**关键词**：腿式机器人操作, 异构铰接物体, 样本高效强化学习, 几何特征提取, 自适应感知融合

## 3 点简述
- 核心问题：腿式机器人操作异构铰接物体（如门、抽屉）时，因物体类型多样和机器人动力学复杂，现有强化学习方法样本效率低。
- 方法要点：引入SAFE编码手柄和面板几何为低维表示，提升跨域泛化；ArtIEst自适应融合本体与外感信息，估计物体开启方向和运动范围。
- 实验或效果：在仿真和真实机器人系统中部署，成功操作多种异构铰接物体，视频展示于项目网站。

## 摘要（原文）

> Legged manipulators offer high mobility and versatile manipulation. However, robust interaction with heterogeneous articulated objects, such as doors, drawers, and cabinets, remains challenging because of the diverse articulation types of the objects and the complex dynamics of the legged robot. Existing reinforcement learning (RL)-based approaches often rely on high-dimensional sensory inputs, leading to sample inefficiency. In this paper, we propose a robust and sample-efficient framework for opening heterogeneous articulated objects with a legged manipulator. In particular, we propose Sampling-based Abstracted Feature Extraction (SAFE), which encodes handle and panel geometry into a compact low-dimensional representation, improving cross-domain generalization. Additionally, Articulation Information Estimator (ArtIEst) is introduced to adaptively mix proprioception with exteroception to estimate opening direction and range of motion for each object. The proposed framework was deployed to manipulate various heterogeneous articulated objects in simulation and real-world robot systems. Videos can be found on the project website: https://openheart-icra.github.io/OpenHEART/

