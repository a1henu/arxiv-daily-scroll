---
layout: default
title: Physics-Guided Fusion for Robust 3D Tracking of Fast Moving Small Objects
---

# Physics-Guided Fusion for Robust 3D Tracking of Fast Moving Small Objects
**arXiv**：[2510.20126v1](https://arxiv.org/abs/2510.20126) · [PDF](https://arxiv.org/pdf/2510.20126.pdf)  
**作者**：Prithvi Raj Singh, Raju Gottumukkala, Anthony S. Maida, Alan B. Barhorst, Vijaya Gopu  

**一句话要点**：提出物理引导融合系统以解决快速移动小物体3D跟踪问题

**关键词**：3D物体跟踪, 快速移动小物体, 物理引导融合, 深度学习检测, RGB-D相机, 异常检测

## 3 点简述
- 核心问题：快速移动小物体检测与跟踪在RGB-D相机中仍具挑战性
- 方法要点：结合深度学习检测与基于物理的跟踪算法，集成运动方程
- 实验或效果：在自定义数据集上，平均位移误差比卡尔曼滤波器减少高达70%

## 摘要（原文）

> While computer vision has advanced considerably for general object detection
> and tracking, the specific problem of fast-moving tiny objects remains
> underexplored. This paper addresses the significant challenge of detecting and
> tracking rapidly moving small objects using an RGB-D camera. Our novel system
> combines deep learning-based detection with physics-based tracking to overcome
> the limitations of existing approaches. Our contributions include: (1) a
> comprehensive system design for object detection and tracking of fast-moving
> small objects in 3D space, (2) an innovative physics-based tracking algorithm
> that integrates kinematics motion equations to handle outliers and missed
> detections, and (3) an outlier detection and correction module that
> significantly improves tracking performance in challenging scenarios such as
> occlusions and rapid direction changes. We evaluated our proposed system on a
> custom racquetball dataset. Our evaluation shows our system surpassing kalman
> filter based trackers with up to 70\% less Average Displacement Error. Our
> system has significant applications for improving robot perception on
> autonomous platforms and demonstrates the effectiveness of combining
> physics-based models with deep learning approaches for real-time 3D detection
> and tracking of challenging small objects.

