---
layout: default
title: Event-based Motion & Appearance Fusion for 6D Object Pose Tracking
---

# Event-based Motion & Appearance Fusion for 6D Object Pose Tracking
**arXiv**：[2603.08264v1](https://arxiv.org/abs/2603.08264) · [PDF](https://arxiv.org/pdf/2603.08264.pdf)  
**作者**：Zhichao Li, Chiara Bartolozzi, Lorenzo Natale, Arren Glover  

**一句话要点**：提出基于事件与外观融合的6D物体姿态跟踪方法，以应对高速动态场景

**关键词**：事件相机, 6D姿态跟踪, 姿态传播, 姿态校正, 动态场景, 光流

## 3 点简述
- 核心问题：传统RGB-D相机在高速动态环境中易受运动模糊和帧率限制，事件相机的高时间分辨率可弥补此缺陷
- 方法要点：结合事件光流获取6D速度进行姿态传播，并采用基于模板的局部姿态校正模块进行修正
- 实验或效果：无学习方法性能与先进算法相当，在快速移动物体上表现更优，适用于高动态场景

## 摘要（原文）

> Object pose tracking is a fundamental and essential task for robotics to perform tasks in the home and industrial settings. The most commonly used sensors to do so are RGB-D cameras, which can hit limitations in highly dynamic environments due to motion blur and frame-rate constraints. Event cameras have remarkable features such as high temporal resolution and low latency, which make them a potentially ideal vision sensors for object pose tracking at high speed. Even so, there are still only few works on 6D pose tracking with event cameras. In this work, we take advantage of the high temporal resolution and propose a method that uses both a propagation step fused with a pose correction strategy. Specifically, we use 6D object velocity obtained from event-based optical flow for pose propagation, after which, a template-based local pose correction module is utilized for pose correction. Our learning-free method has comparable performance to the state-of-the-art algorithms, and in some cases out performs them for fast-moving objects. The results indicate the potential for using event cameras in highly-dynamic scenarios where the use of deep network approaches are limited by low update rates.

