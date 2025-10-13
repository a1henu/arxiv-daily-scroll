---
layout: default
title: GL-DT: Multi-UAV Detection and Tracking with Global-Local Integration
---

# GL-DT: Multi-UAV Detection and Tracking with Global-Local Integration
**arXiv**：[2510.09092v1](https://arxiv.org/abs/2510.09092) · [PDF](https://arxiv.org/pdf/2510.09092.pdf)  
**作者**：Juanqin Liu, Leonardo Plotegher, Eloy Roura, Shaoming He  
**一句话要点**：提出GL-DT框架以解决无人机多目标检测与跟踪中的小目标和轨迹中断问题

**关键词**：多目标跟踪, 无人机检测, 时空特征融合, 小目标检测, 轨迹连续性

## 3 点简述
- 核心问题：复杂背景、小目标和频繁遮挡导致检测精度低和轨迹不连续
- 方法要点：采用时空特征融合和全局-局部协作检测，结合JPTrack算法减少ID切换
- 实验或效果：显著提升跟踪连续性和稳定性，同时保持实时性能

## 摘要（原文）

> The extensive application of unmanned aerial vehicles (UAVs) in military
> reconnaissance, environmental monitoring, and related domains has created an
> urgent need for accurate and efficient multi-object tracking (MOT)
> technologies, which are also essential for UAV situational awareness. However,
> complex backgrounds, small-scale targets, and frequent occlusions and
> interactions continue to challenge existing methods in terms of detection
> accuracy and trajectory continuity. To address these issues, this paper
> proposes the Global-Local Detection and Tracking (GL-DT) framework. It employs
> a Spatio-Temporal Feature Fusion (STFF) module to jointly model motion and
> appearance features, combined with a global-local collaborative detection
> strategy, effectively enhancing small-target detection. Building upon this, the
> JPTrack tracking algorithm is introduced to mitigate common issues such as ID
> switches and trajectory fragmentation. Experimental results demonstrate that
> the proposed approach significantly improves the continuity and stability of
> MOT while maintaining real-time performance, providing strong support for the
> advancement of UAV detection and tracking technologies.

