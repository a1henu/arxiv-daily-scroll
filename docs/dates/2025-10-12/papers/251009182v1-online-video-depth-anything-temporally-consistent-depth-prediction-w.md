---
layout: default
title: Online Video Depth Anything: Temporally-Consistent Depth Prediction with Low Memory Consumption
---

# Online Video Depth Anything: Temporally-Consistent Depth Prediction with Low Memory Consumption
**arXiv**：[2510.09182v1](https://arxiv.org/abs/2510.09182) · [PDF](https://arxiv.org/pdf/2510.09182.pdf)  
**作者**：Johann-Friedrich Feiden, Tim Küchler, Denis Zavadski, Bogdan Savchynskyy, Carsten Rother  
**一句话要点**：提出在线视频深度估计方法oVDA，实现低内存消耗和时序一致性深度预测。
**关键词**：在线视频深度估计, 时序一致性, 低内存消耗, 边缘设备部署, 潜在特征缓存, 帧掩码训练

## 3 点简述
- 核心问题：现有视频深度估计方法依赖批处理，无法在线实时应用。
- 方法要点：借鉴大语言模型技术，缓存潜在特征并掩码训练帧。
- 实验效果：在精度和VRAM使用上优于其他在线方法，边缘设备可达20 FPS。

## 摘要（原文）

> Depth estimation from monocular video has become a key component of many
> real-world computer vision systems. Recently, Video Depth Anything (VDA) has
> demonstrated strong performance on long video sequences. However, it relies on
> batch-processing which prohibits its use in an online setting. In this work, we
> overcome this limitation and introduce online VDA (oVDA). The key innovation is
> to employ techniques from Large Language Models (LLMs), namely, caching latent
> features during inference and masking frames at training. Our oVDA method
> outperforms all competing online video depth estimation methods in both
> accuracy and VRAM usage. Low VRAM usage is particularly important for
> deployment on edge devices. We demonstrate that oVDA runs at 42 FPS on an
> NVIDIA A100 and at 20 FPS on an NVIDIA Jetson edge device. We will release
> both, code and compilation scripts, making oVDA easy to deploy on low-power
> hardware.

