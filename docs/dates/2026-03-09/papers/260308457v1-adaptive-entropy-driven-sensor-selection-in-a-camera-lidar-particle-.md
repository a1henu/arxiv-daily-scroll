---
layout: default
title: Adaptive Entropy-Driven Sensor Selection in a Camera-LiDAR Particle Filter for Single-Vessel Tracking
---

# Adaptive Entropy-Driven Sensor Selection in a Camera-LiDAR Particle Filter for Single-Vessel Tracking
**arXiv**：[2603.08457v1](https://arxiv.org/abs/2603.08457) · [PDF](https://arxiv.org/pdf/2603.08457.pdf)  
**作者**：Andrei Starodubov, Yaqub Aris Prabowo, Andreas Hadjipieris, Ioannis Kyriakides, Roberto Galeazzi  

**一句话要点**：提出基于信息增益的自适应传感器选择粒子滤波方法，用于固定平台单船跟踪，以应对相机与LiDAR的模态退化问题。

**关键词**：传感器融合, 粒子滤波, 自适应感知, 海事跟踪, 信息增益, 多模态退化

## 3 点简述
- 核心问题：固定海岸平台单船跟踪中，相机受光照和视觉杂波影响，LiDAR性能随距离和间歇返回下降。
- 方法要点：采用异构多传感器融合粒子滤波，引入信息增益（熵减）自适应感知策略，动态选择最优传感器配置。
- 实验或效果：在真实海事部署中验证，自适应策略通过切换模态实现精度与连续性的平衡，优于单一传感器或全传感器配置。

## 摘要（原文）

> Robust single-vessel tracking from fixed coastal platforms is hindered by modality-specific degradations: cameras suffer from illumination and visual clutter, while LiDAR performance drops with range and intermittent returns. We present a heterogeneous multi-sensor fusion particle-filter tracker that incorporates an information-gain (entropy-reduction) adaptive sensing policy to select the most informative configuration at each fusion time bin. The approach is validated in a real maritime deployment at the CMMI Smart Marina Testbed (Ayia Napa Marina, Cyprus), using a shore-mounted 3D LiDAR and an elevated fixed camera to track a rigid inflatable boat with onboard GNSS ground truth. We compare LiDAR-only, camera-only, all-sensors, and adaptive configurations. Results show LiDAR dominates near-field accuracy, the camera sustains longer-range coverage when LiDAR becomes unavailable, and the adaptive policy achieves a favorable accuracy-continuity trade-off by switching modalities based on information gain. By avoiding continuous multi-stream processing, the adaptive configuration provides a practical baseline for resilient and resource-aware maritime surveillance.

