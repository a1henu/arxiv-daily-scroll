---
layout: default
title: Biomechanically Accurate Gait Analysis: A 3d Human Reconstruction Framework for Markerless Estimation of Gait Parameters
---

# Biomechanically Accurate Gait Analysis: A 3d Human Reconstruction Framework for Markerless Estimation of Gait Parameters
**arXiv**：[2603.02499v1](https://arxiv.org/abs/2603.02499) · [PDF](https://arxiv.org/pdf/2603.02499.pdf)  
**作者**：Akila Pemasiri, Ethan Goan, Glen Lichtwark, Robert Schuster, Luke Kelly, Clinton Fookes  

**一句话要点**：提出基于3D人体重建的无标记步态分析框架，用于生物力学可解释的步态参数估计

**关键词**：步态分析, 3D人体重建, 无标记估计, 生物力学, 运动捕捉, OpenSim集成

## 3 点简述
- 核心问题：传统基于关键点的方法在步态分析中缺乏生物力学可解释性，难以替代标记式运动捕捉系统。
- 方法要点：从视频数据重建3D人体，提取类似运动捕捉的生物力学标记，并集成到OpenSim中进行关节运动学估计。
- 实验或效果：与标记式参考数据对比，时空和运动学步态参数显示强一致性，相比仅姿态估计方法有显著改进。

## 摘要（原文）

> This paper presents a biomechanically interpretable framework for gait analysis using 3D human reconstruction from video data. Unlike conventional keypoint based approaches, the proposed method extracts biomechanically meaningful markers analogous to motion capture systems and integrates them within OpenSim for joint kinematic estimation. To evaluate performance, both spatiotemporal and kinematic gait parameters were analysed against reference marker-based data. Results indicate strong agreement with marker-based measurements, with considerable improvements when compared with pose-estimation methods alone. The proposed framework offers a scalable, markerless, and interpretable approach for accurate gait assessment, supporting broader clinical and real world deployment of vision based biomechanics

