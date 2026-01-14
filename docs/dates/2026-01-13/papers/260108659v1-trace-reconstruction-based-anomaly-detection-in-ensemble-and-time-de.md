---
layout: default
title: TRACE: Reconstruction-Based Anomaly Detection in Ensemble and Time-Dependent Simulations
---

# TRACE: Reconstruction-Based Anomaly Detection in Ensemble and Time-Dependent Simulations
**arXiv**：[2601.08659v1](https://arxiv.org/abs/2601.08659) · [PDF](https://arxiv.org/pdf/2601.08659.pdf)  
**作者**：Hamid Gadirov, Martijn Westra, Steffen Frey  

**一句话要点**：提出基于重建的异常检测方法，用于参数化卡门涡街模拟的集合和时间依赖数据

**关键词**：异常检测, 卷积自编码器, 时间依赖模拟, 卡门涡街, 重建误差

## 3 点简述
- 核心问题：高维时间依赖模拟数据中复杂时空动态导致异常检测困难
- 方法要点：比较2D和3D卷积自编码器，2D检测单帧空间异常，3D利用时空上下文检测运动模式
- 实验或效果：3D模型减少时间冗余检测，重建误差受质量空间分布影响

## 摘要（原文）

> Detecting anomalies in high-dimensional, time-dependent simulation data is challenging due to complex spatial and temporal dynamics. We study reconstruction-based anomaly detection for ensemble data from parameterized Kármán vortex street simulations using convolutional autoencoders. We compare a 2D autoencoder operating on individual frames with a 3D autoencoder that processes short temporal stacks. The 2D model identifies localized spatial irregularities in single time steps, while the 3D model exploits spatio-temporal context to detect anomalous motion patterns and reduces redundant detections across time. We further evaluate volumetric time-dependent data and find that reconstruction errors are strongly influenced by the spatial distribution of mass, with highly concentrated regions yielding larger errors than dispersed configurations. Our results highlight the importance of temporal context for robust anomaly detection in dynamic simulations.

