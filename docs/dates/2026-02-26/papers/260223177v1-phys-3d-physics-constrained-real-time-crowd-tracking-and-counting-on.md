---
layout: default
title: Phys-3D: Physics-Constrained Real-Time Crowd Tracking and Counting on Railway Platforms
---

# Phys-3D: Physics-Constrained Real-Time Crowd Tracking and Counting on Railway Platforms
**arXiv**：[2602.23177v1](https://arxiv.org/abs/2602.23177) · [PDF](https://arxiv.org/pdf/2602.23177.pdf)  
**作者**：Bin Zeng, Johannes Künzel, Anna Hilsmann, Peter Eisert  

**一句话要点**：提出Phys-3D框架，通过物理约束3D运动建模解决铁路平台实时人群计数中的遮挡和相机运动挑战。

**关键词**：人群计数, 物理约束跟踪, 3D运动建模, 铁路平台安全, 实时检测, 遮挡处理

## 3 点简述
- 核心问题：铁路平台人群计数因密集遮挡、相机运动和透视失真而困难，现有方法在动态条件下不可靠。
- 方法要点：结合YOLOv11m检测器、EfficientNet-B0外观编码和物理约束卡尔曼模型，实现实时检测、外观和3D运动推理。
- 实验或效果：在MOT-RPCH数据集上计数误差降至2.97%，验证了在安全和容量管理中的鲁棒性。

## 摘要（原文）

> Accurate, real-time crowd counting on railway platforms is essential for safety and capacity management. We propose to use a single camera mounted in a train, scanning the platform while arriving. While hardware constraints are simple, counting remains challenging due to dense occlusions, camera motion, and perspective distortions during train arrivals. Most existing tracking-by-detection approaches assume static cameras or ignore physical consistency in motion modeling, leading to unreliable counting under dynamic conditions. We propose a physics-constrained tracking framework that unifies detection, appearance, and 3D motion reasoning in a real-time pipeline. Our approach integrates a transfer-learned YOLOv11m detector with EfficientNet-B0 appearance encoding within DeepSORT, while introducing a physics-constrained Kalman model (Phys-3D) that enforces physically plausible 3D motion dynamics through pinhole geometry. To address counting brittleness under occlusions, we implement a virtual counting band with persistence. On our platform benchmark, MOT-RailwayPlatformCrowdHead Dataset(MOT-RPCH), our method reduces counting error to 2.97%, demonstrating robust performance despite motion and occlusions. Our results show that incorporating first-principles geometry and motion priors enables reliable crowd counting in safety-critical transportation scenarios, facilitating effective train scheduling and platform safety management.

