---
layout: default
title: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
---

# A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
**arXiv**：[2602.05855v1](https://arxiv.org/abs/2602.05855) · [PDF](https://arxiv.org/pdf/2602.05855.pdf)  
**作者**：Dennis Bank, Joost Cordes, Thomas Seel, Simon F. G. Ehlers  

**一句话要点**：提出混合自编码器框架，融合激光雷达与深度数据，提升人形机器人非结构化环境中的地形感知鲁棒性。

**关键词**：地形感知, 多模态融合, 混合自编码器, 人形机器人, 高度图生成

## 3 点简述
- 核心问题：传统单传感器系统在人形机器人非结构化环境地形感知中可靠性不足。
- 方法要点：采用混合编码器-解码器结构，结合CNN提取空间特征与GRU保持时间一致性，融合多模态数据。
- 实验或效果：多模态融合比单传感器配置提升重建精度7.2%-9.9%，时间上下文集成减少建图漂移。

## 摘要（原文）

> Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments. While traditional systems often rely on manually engineered, single-sensor pipelines, this paper presents a learning-based framework that uses an intermediate, robot-centric heightmap representation. A hybrid Encoder-Decoder Structure (EDS) is introduced, utilizing a Convolutional Neural Network (CNN) for spatial feature extraction fused with a Gated Recurrent Unit (GRU) core for temporal consistency. The architecture integrates multimodal data from an Intel RealSense depth camera, a LIVOX MID-360 LiDAR processed via efficient spherical projection, and an onboard IMU. Quantitative results demonstrate that multimodal fusion improves reconstruction accuracy by 7.2% over depth-only and 9.9% over LiDAR-only configurations. Furthermore, the integration of a 3.2 s temporal context reduces mapping drift.

