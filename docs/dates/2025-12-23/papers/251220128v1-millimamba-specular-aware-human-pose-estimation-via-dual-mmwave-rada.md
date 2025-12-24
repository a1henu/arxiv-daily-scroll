---
layout: default
title: milliMamba: Specular-Aware Human Pose Estimation via Dual mmWave Radar with Multi-Frame Mamba Fusion
---

# milliMamba: Specular-Aware Human Pose Estimation via Dual mmWave Radar with Multi-Frame Mamba Fusion
**arXiv**：[2512.20128v1](https://arxiv.org/abs/2512.20128) · [PDF](https://arxiv.org/pdf/2512.20128.pdf)  
**作者**：Niraj Prakash Kini, Shiau-Rung Tsai, Guan-Hsun Lin, Wen-Hsiao Peng, Ching-Wen Ma, Jenq-Neng Hwang  

**一句话要点**：提出milliMamba框架，通过双毫米波雷达与多帧Mamba融合解决镜面反射下的人体姿态估计问题

**关键词**：毫米波雷达, 人体姿态估计, 镜面反射, 时空建模, Mamba架构, 多帧融合

## 3 点简述
- 毫米波雷达用于人体姿态估计面临镜面反射导致的信号稀疏问题
- 采用Cross-View Fusion Mamba编码器和Spatio-Temporal-Cross Attention解码器联合建模时空依赖
- 在TransHuPR和HuPR数据集上分别超过基线11.0 AP和14.6 AP

## 摘要（原文）

> Millimeter-wave radar offers a privacy-preserving and lighting-invariant alternative to RGB sensors for Human Pose Estimation (HPE) task. However, the radar signals are often sparse due to specular reflection, making the extraction of robust features from radar signals highly challenging. To address this, we present milliMamba, a radar-based 2D human pose estimation framework that jointly models spatio-temporal dependencies across both the feature extraction and decoding stages. Specifically, given the high dimensionality of radar inputs, we adopt a Cross-View Fusion Mamba encoder to efficiently extract spatio-temporal features from longer sequences with linear complexity. A Spatio-Temporal-Cross Attention decoder then predicts joint coordinates across multiple frames. Together, this spatio-temporal modeling pipeline enables the model to leverage contextual cues from neighboring frames and joints to infer missing joints caused by specular reflections. To reinforce motion smoothness, we incorporate a velocity loss alongside the standard keypoint loss during training. Experiments on the TransHuPR and HuPR datasets demonstrate that our method achieves significant performance improvements, exceeding the baselines by 11.0 AP and 14.6 AP, respectively, while maintaining reasonable complexity. Code: https://github.com/NYCU-MAPL/milliMamba

