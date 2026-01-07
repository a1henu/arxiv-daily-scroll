---
layout: default
title: M-SEVIQ: A Multi-band Stereo Event Visual-Inertial Quadruped-based Dataset for Perception under Rapid Motion and Challenging Illumination
---

# M-SEVIQ: A Multi-band Stereo Event Visual-Inertial Quadruped-based Dataset for Perception under Rapid Motion and Challenging Illumination
**arXiv**：[2601.02777v1](https://arxiv.org/abs/2601.02777) · [PDF](https://arxiv.org/pdf/2601.02777.pdf)  
**作者**：Jingcheng Cao, Chaoran Xiong, Jianmin Song, Shang Yan, Jiachen Liu, Ling Pei  

**一句话要点**：提出M-SEVIQ数据集以解决四足机器人快速运动与挑战性光照下的感知问题

**关键词**：事件相机数据集, 立体视觉, 传感器融合, 四足机器人感知, 多模态视觉, 挑战性光照

## 3 点简述
- 核心问题：传统帧相机在快速运动和低光下易产生模糊图像，限制敏捷机器人感知
- 方法要点：使用立体事件相机、帧相机、IMU和关节编码器，采集多波段、多光照条件下的真实世界序列
- 实验或效果：提供超过30个序列及完整校准数据，支持传感器融合、语义分割和多模态视觉研究

## 摘要（原文）

> Agile locomotion in legged robots poses significant challenges for visual perception. Traditional frame-based cameras often fail in these scenarios for producing blurred images, particularly under low-light conditions. In contrast, event cameras capture changes in brightness asynchronously, offering low latency, high temporal resolution, and high dynamic range. These advantages make them suitable for robust perception during rapid motion and under challenging illumination. However, existing event camera datasets exhibit limitations in stereo configurations and multi-band sensing domains under various illumination conditions. To address this gap, we present M-SEVIQ, a multi-band stereo event visual and inertial quadruped dataset collected using a Unitree Go2 equipped with stereo event cameras, a frame-based camera, an inertial measurement unit (IMU), and joint encoders. This dataset contains more than 30 real-world sequences captured across different velocity levels, illumination wavelengths, and lighting conditions. In addition, comprehensive calibration data, including intrinsic, extrinsic, and temporal alignments, are provided to facilitate accurate sensor fusion and benchmarking. Our M-SEVIQ can be used to support research in agile robot perception, sensor fusion, semantic segmentation and multi-modal vision in challenging environments.

