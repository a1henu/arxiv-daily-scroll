---
layout: default
title: UEOF: A Benchmark Dataset for Underwater Event-Based Optical Flow
---

# UEOF: A Benchmark Dataset for Underwater Event-Based Optical Flow
**arXiv**：[2601.10054v1](https://arxiv.org/abs/2601.10054) · [PDF](https://arxiv.org/pdf/2601.10054.pdf)  
**作者**：Nick Truong, Pritam P. Karmokar, William J. Beksi  

**一句话要点**：提出首个合成水下事件光流基准数据集UEOF，以解决水下光学挑战下事件相机光流评估问题。

**关键词**：水下成像, 事件相机, 光流估计, 合成数据集, 基准测试, 光线追踪

## 3 点简述
- 核心问题：水下成像因光衰减、散射和模糊导致标准相机性能受限，且缺乏事件相机光流真实数据。
- 方法要点：基于物理光线追踪RGBD序列，通过视频到事件管道生成合成水下事件数据流，包含密集光流、深度和相机运动真值。
- 实验或效果：基准测试了先进学习型和模型型光流方法，评估水下光传输对事件形成和运动估计的影响，为算法开发提供新基线。

## 摘要（原文）

> Underwater imaging is fundamentally challenging due to wavelength-dependent light attenuation, strong scattering from suspended particles, turbidity-induced blur, and non-uniform illumination. These effects impair standard cameras and make ground-truth motion nearly impossible to obtain. On the other hand, event cameras offer microsecond resolution and high dynamic range. Nonetheless, progress on investigating event cameras for underwater environments has been limited due to the lack of datasets that pair realistic underwater optics with accurate optical flow. To address this problem, we introduce the first synthetic underwater benchmark dataset for event-based optical flow derived from physically-based ray-traced RGBD sequences. Using a modern video-to-event pipeline applied to rendered underwater videos, we produce realistic event data streams with dense ground-truth flow, depth, and camera motion. Moreover, we benchmark state-of-the-art learning-based and model-based optical flow prediction methods to understand how underwater light transport affects event formation and motion estimation accuracy. Our dataset establishes a new baseline for future development and evaluation of underwater event-based perception algorithms. The source code and dataset for this project are publicly available at https://robotic-vision-lab.github.io/ueof.

