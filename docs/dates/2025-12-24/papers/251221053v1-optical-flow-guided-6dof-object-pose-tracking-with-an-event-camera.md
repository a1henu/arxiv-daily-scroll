---
layout: default
title: Optical Flow-Guided 6DoF Object Pose Tracking with an Event Camera
---

# Optical Flow-Guided 6DoF Object Pose Tracking with an Event Camera
**arXiv**：[2512.21053v1](https://arxiv.org/abs/2512.21053) · [PDF](https://arxiv.org/pdf/2512.21053.pdf)  
**作者**：Zibin Liu, Banglei Guan, Yang Shang, Shunkun Liang, Zhenbao Yu, Qifeng Yu  

**一句话要点**：提出光流引导的6自由度物体姿态跟踪方法，利用事件相机解决传统相机在动态场景中的挑战。

**关键词**：事件相机, 6自由度姿态跟踪, 光流引导, 混合特征提取, 物体运动表征

## 3 点简述
- 核心问题：传统相机在物体姿态跟踪中面临运动模糊、噪声、遮挡和光照变化等挑战，影响精度和鲁棒性。
- 方法要点：采用2D-3D混合特征提取策略，通过光流关联角点和边缘，迭代优化6自由度姿态以实现连续跟踪。
- 实验或效果：在模拟和真实事件数据上验证，方法在准确性和鲁棒性上优于基于事件的最先进方法。

## 摘要（原文）

> Object pose tracking is one of the pivotal technologies in multimedia, attracting ever-growing attention in recent years. Existing methods employing traditional cameras encounter numerous challenges such as motion blur, sensor noise, partial occlusion, and changing lighting conditions. The emerging bio-inspired sensors, particularly event cameras, possess advantages such as high dynamic range and low latency, which hold the potential to address the aforementioned challenges. In this work, we present an optical flow-guided 6DoF object pose tracking method with an event camera. A 2D-3D hybrid feature extraction strategy is firstly utilized to detect corners and edges from events and object models, which characterizes object motion precisely. Then, we search for the optical flow of corners by maximizing the event-associated probability within a spatio-temporal window, and establish the correlation between corners and edges guided by optical flow. Furthermore, by minimizing the distances between corners and edges, the 6DoF object pose is iteratively optimized to achieve continuous pose tracking. Experimental results of both simulated and real events demonstrate that our methods outperform event-based state-of-the-art methods in terms of both accuracy and robustness.

