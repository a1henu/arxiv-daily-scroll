---
layout: default
title: ODD-SEC: Onboard Drone Detection with a Spinning Event Camera
---

# ODD-SEC: Onboard Drone Detection with a Spinning Event Camera
**arXiv**：[2603.06265v1](https://arxiv.org/abs/2603.06265) · [PDF](https://arxiv.org/pdf/2603.06265.pdf)  
**作者**：Kuan Dai, Hongxin Zhang, Sheng Zhong, Yi Zhou  

**一句话要点**：提出基于旋转事件相机的实时无人机检测系统，用于移动载体部署

**关键词**：事件相机, 无人机检测, 移动载体, 实时系统, 轻量神经网络, 360度视野

## 3 点简述
- 核心问题：现有事件相机方案假设静态相机，限制了在移动载体上的应用
- 方法要点：设计无需运动补偿的图像式事件表示和轻量神经网络，实现高效时空学习
- 实验或效果：在Jetson Orin NX上实时运行，室外实验平均角度误差低于2°

## 摘要（原文）

> The rapid proliferation of drones requires balancing innovation with regulation. To address security and privacy concerns, techniques for drone detection have attracted significant attention.Passive solutions, such as frame camera-based systems, offer versatility and energy efficiency under typical conditions but are fundamentally constrained by their operational principles in scenarios involving fast-moving targets or adverse illumination.Inspired by biological vision, event cameras asynchronously detect per-pixel brightness changes, offering high dynamic range and microsecond-level responsiveness that make them uniquely suited for drone detection in conditions beyond the reach of conventional frame-based cameras.However, the design of most existing event-based solutions assumes a static camera, greatly limiting their applicability to moving carriers--such as quadrupedal robots or unmanned ground vehicles--during field operations.In this paper, we introduce a real-time drone detection system designed for deployment on moving carriers. The system utilizes a spinning event-based camera, providing a 360° horizontal field of view and enabling bearing estimation of detected drones. A key contribution is a novel image-like event representation that operates without motion compensation, coupled with a lightweight neural network architecture for efficient spatiotemporal learning. Implemented on an onboard Jetson Orin NX, the system can operate in real time. Outdoor experimental results validate reliable detection with a mean angular error below 2° under challenging conditions, underscoring its suitability for real-world surveillance applications. We will open-source our complete pipeline to support future research.

