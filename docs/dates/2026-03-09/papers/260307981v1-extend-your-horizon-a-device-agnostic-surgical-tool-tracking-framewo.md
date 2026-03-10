---
layout: default
title: Extend Your Horizon: A Device-Agnostic Surgical Tool Tracking Framework with Multi-View Optimization for Augmented Reality
---

# Extend Your Horizon: A Device-Agnostic Surgical Tool Tracking Framework with Multi-View Optimization for Augmented Reality
**arXiv**：[2603.07981v1](https://arxiv.org/abs/2603.07981) · [PDF](https://arxiv.org/pdf/2603.07981.pdf)  
**作者**：Jiaming Zhang, Mingxu Liu, Hongchao Shu, Ruixing Liang, Yihao Liu, Ojas Taskar, Amir Kheradmand, Mehran Armand, Alejandro Martin-Gomez  

**一句话要点**：提出多传感器融合框架以解决手术工具在遮挡环境下的跟踪问题

**关键词**：手术工具跟踪, 多传感器融合, 动态场景图, 增强现实可视化, 遮挡鲁棒性

## 3 点简述
- 核心问题：手术导航中工具跟踪易受遮挡影响，传统方法依赖清晰视线难以维持
- 方法要点：融合多传感器数据于动态场景图，实时评估跟踪可靠性并优化多视图
- 实验或效果：实验显示在遮挡下增强AR可视化的一致性和鲁棒性

## 摘要（原文）

> Surgical navigation provides real-time guidance by estimating the pose of patient anatomy and surgical instruments to visualize relevant intraoperative information. In conventional systems, instruments are typically tracked using fiducial markers and stationary optical tracking systems (OTS). Augmented reality (AR) has further enabled intuitive visualization and motivated tracking using sensors embedded in head-mounted displays (HMDs). However, most existing approaches rely on a clear line of sight, which is difficult to maintain in dynamic operating room environments due to frequent occlusions caused by equipment, surgical tools, and personnel. This work introduces a framework for tracking surgical instruments under occlusion by fusing multiple sensing modalities within a dynamic scene graph representation. The proposed approach integrates tracking systems with different accuracy levels and motion characteristics while estimating tracking reliability in real time. Experimental results demonstrate improved robustness and enhanced consistency of AR visualization in the presence of occlusions.

