---
layout: default
title: Selfi: Self Improving Reconstruction Engine via 3D Geometric Feature Alignment
---

# Selfi: Self Improving Reconstruction Engine via 3D Geometric Feature Alignment
**arXiv**：[2512.08930v1](https://arxiv.org/abs/2512.08930) · [PDF](https://arxiv.org/pdf/2512.08930.pdf)  
**作者**：Youming Deng, Songyou Peng, Junyi Zhang, Kathryn Heal, Tiancheng Sun, John Flynn, Steve Marschner, Lucy Chai  

**一句话要点**：提出Selfi通过特征对齐提升3D重建，改进VGGT的几何一致性以优化新视角合成和相机姿态估计。

**关键词**：新视角合成, 3D重建, 特征对齐, 相机姿态估计, 蒸馏训练, 几何一致性

## 3 点简述
- 核心问题：VGGT等视觉基础模型缺乏显式多视角几何一致性，影响3D重建质量。
- 方法要点：使用重投影一致性损失训练轻量特征适配器，将VGGT输出蒸馏到几何对齐特征空间。
- 实验或效果：在NVS和相机姿态估计任务中实现最先进性能，验证特征对齐对下游3D推理的益处。

## 摘要（原文）

> Novel View Synthesis (NVS) has traditionally relied on models with explicit 3D inductive biases combined with known camera parameters from Structure-from-Motion (SfM) beforehand. Recent vision foundation models like VGGT take an orthogonal approach -- 3D knowledge is gained implicitly through training data and loss objectives, enabling feed-forward prediction of both camera parameters and 3D representations directly from a set of uncalibrated images. While flexible, VGGT features lack explicit multi-view geometric consistency, and we find that improving such 3D feature consistency benefits both NVS and pose estimation tasks. We introduce Selfi, a self-improving 3D reconstruction pipeline via feature alignment, transforming a VGGT backbone into a high-fidelity 3D reconstruction engine by leveraging its own outputs as pseudo-ground-truth. Specifically, we train a lightweight feature adapter using a reprojection-based consistency loss, which distills VGGT outputs into a new geometrically-aligned feature space that captures spatial proximity in 3D. This enables state-of-the-art performance in both NVS and camera pose estimation, demonstrating that feature alignment is a highly beneficial step for downstream 3D reasoning.

