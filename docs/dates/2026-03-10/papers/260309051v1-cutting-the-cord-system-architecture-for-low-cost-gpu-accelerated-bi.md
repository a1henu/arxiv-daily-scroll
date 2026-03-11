---
layout: default
title: Cutting the Cord: System Architecture for Low-Cost, GPU-Accelerated Bimanual Mobile Manipulation
---

# Cutting the Cord: System Architecture for Low-Cost, GPU-Accelerated Bimanual Mobile Manipulation
**arXiv**：[2603.09051v1](https://arxiv.org/abs/2603.09051) · [PDF](https://arxiv.org/pdf/2603.09051.pdf)  
**作者**：Artemis Shaw, Chen Liu, Justin Costa, Rane Gray, Alina Skowronek, Kevin Diaz, Nam Bui, Nikolaus Correll  

**一句话要点**：提出低成本双手机器人平台，集成GPU加速计算，用于无外部依赖的机器人研究。

**关键词**：双手机器人, 低成本机器人, GPU加速, 嵌入式自主, SLAM导航, 视觉操控

## 3 点简述
- 核心问题：开发低成本、高刚度、无外部依赖的双手机器人平台。
- 方法要点：优化机械设计、采用Tri-Bus电源拓扑、集成NVIDIA Jetson Orin Nano实现嵌入式自主。
- 实验或效果：平台支持远程操作、自主SLAM导航和视觉操控，成本低于1300美元。

## 摘要（原文）

> We present a bimanual mobile manipulator built on the open-source XLeRobot with integrated onboard compute for less than \$1300. Key contributions include: (1) optimized mechanical design maximizing stiffness-to-weight ratio, (2) a Tri-Bus power topology isolating compute from motor-induced voltage transients, and (3) embedded autonomy using NVIDIA Jetson Orin Nano for untethered operation. The platform enables teleoperation, autonomous SLAM navigation, and vision-based manipulation without external dependencies, providing a low-cost alternative for research and education in robotics and robot learning.

