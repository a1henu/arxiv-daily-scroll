---
layout: default
title: Near-Field Perception for Safety Enhancement of Autonomous Mobile Robots in Manufacturing Environments
---

# Near-Field Perception for Safety Enhancement of Autonomous Mobile Robots in Manufacturing Environments
**arXiv**：[2512.13561v1](https://arxiv.org/abs/2512.13561) · [PDF](https://arxiv.org/pdf/2512.13561.pdf)  
**作者**：Li-Wei Shih, Ruo-Syuan Mei, Jesse Heidrich, Hui-Ping Wang, Joel Hooton, Joshua Solomon, Jorge Arinez, Guangze Li, Chenhui Shao  

**一句话要点**：提出三层近场感知框架以增强制造环境中自主移动机器人的安全性

**关键词**：近场感知, 自主移动机器人, 制造环境安全, 光间断检测, 光位移测量, 嵌入式AI

## 3 点简述
- 核心问题：传统测距传感器难以检测机器人基座附近的小物体，影响AMR安全操作。
- 方法要点：采用光间断检测、光位移测量和基于计算机视觉的对象检测，实现快速障碍感知、高度估计和语义分类。
- 实验或效果：在Raspberry Pi 5上实时运行，帧率达25或50fps，平衡精度、计算和成本，提升AMR安全性。

## 摘要（原文）

> Near-field perception is essential for the safe operation of autonomous mobile robots (AMRs) in manufacturing environments. Conventional ranging sensors such as light detection and ranging (LiDAR) and ultrasonic devices provide broad situational awareness but often fail to detect small objects near the robot base. To address this limitation, this paper presents a three-tier near-field perception framework. The first approach employs light-discontinuity detection, which projects a laser stripe across the near-field zone and identifies interruptions in the stripe to perform fast, binary cutoff sensing for obstacle presence. The second approach utilizes light-displacement measurement to estimate object height by analyzing the geometric displacement of a projected stripe in the camera image, which provides quantitative obstacle height information with minimal computational overhead. The third approach employs a computer vision-based object detection model on embedded AI hardware to classify objects, enabling semantic perception and context-aware safety decisions. All methods are implemented on a Raspberry Pi 5 system, achieving real-time performance at 25 or 50 frames per second. Experimental evaluation and comparative analysis demonstrate that the proposed hierarchy balances precision, computation, and cost, thereby providing a scalable perception solution for enabling safe operations of AMRs in manufacturing environments.

