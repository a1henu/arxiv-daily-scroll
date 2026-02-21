---
layout: default
title: A Multi-modal Detection System for Infrastructure-based Freight Signal Priority
---

# A Multi-modal Detection System for Infrastructure-based Freight Signal Priority
**arXiv**：[2602.17252v1](https://arxiv.org/abs/2602.17252) · [PDF](https://arxiv.org/pdf/2602.17252.pdf)  
**作者**：Ziyan Zhang, Chuheng Wei, Xuanpeng Zhao, Siyan Li, Will Snyder, Mike Stas, Peng Hao, Kanok Boriboonsomsin, Guoyuan Wu  

**一句话要点**：提出基于基础设施的多模态货运车辆检测系统以支持货运信号优先控制

**关键词**：多模态检测, 货运信号优先, 激光雷达, 卡尔曼滤波, 基础设施感知

## 3 点简述
- 核心问题：货运车辆在信号交叉口需要可靠检测与运动估计以实现有效信号优先控制
- 方法要点：集成激光雷达与摄像头，采用混合传感架构，结合聚类与深度学习检测及卡尔曼滤波跟踪
- 实验或效果：现场评估显示系统能高时空分辨率可靠监测货运车辆运动，为实际部署提供见解

## 摘要（原文）

> Freight vehicles approaching signalized intersections require reliable detection and motion estimation to support infrastructure-based Freight Signal Priority (FSP). Accurate and timely perception of vehicle type, position, and speed is essential for enabling effective priority control strategies. This paper presents the design, deployment, and evaluation of an infrastructure-based multi-modal freight vehicle detection system integrating LiDAR and camera sensors. A hybrid sensing architecture is adopted, consisting of an intersection-mounted subsystem and a midblock subsystem, connected via wireless communication for synchronized data transmission. The perception pipeline incorporates both clustering-based and deep learning-based detection methods with Kalman filter tracking to achieve stable real-time performance. LiDAR measurements are registered into geodetic reference frames to support lane-level localization and consistent vehicle tracking. Field evaluations demonstrate that the system can reliably monitor freight vehicle movements at high spatio-temporal resolution. The design and deployment provide practical insights for developing infrastructure-based sensing systems to support FSP applications.

