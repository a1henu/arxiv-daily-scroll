---
layout: default
title: Learning Spatio-Temporal Feature Representations for Video-Based Gaze Estimation
---

# Learning Spatio-Temporal Feature Representations for Video-Based Gaze Estimation
**arXiv**：[2512.17673v1](https://arxiv.org/abs/2512.17673) · [PDF](https://arxiv.org/pdf/2512.17673.pdf)  
**作者**：Alexandre Personnic, Mihai Bâce  

**一句话要点**：提出ST-Gaze网络，结合CNN与注意力模块，优化视频中眼部和面部特征的时空融合，提升基于视频的视线估计性能。

**关键词**：视频视线估计, 时空特征表示, 注意力机制, CNN骨干网络, EVE数据集, 消融研究

## 3 点简述
- 核心问题：视频视线估计需同时建模帧内空间关系和帧间时间动态，现有方法性能受限。
- 方法要点：使用CNN骨干网络，集成通道注意力和自注意力模块，将融合特征作为空间序列处理，通过时空递归捕获上下文。
- 实验或效果：在EVE数据集上达到最先进性能，消融研究表明时空递归优于过早空间池化，增强鲁棒性。

## 摘要（原文）

> Video-based gaze estimation methods aim to capture the inherently temporal dynamics of human eye gaze from multiple image frames. However, since models must capture both spatial and temporal relationships, performance is limited by the feature representations within a frame but also between multiple frames. We propose the Spatio-Temporal Gaze Network (ST-Gaze), a model that combines a CNN backbone with dedicated channel attention and self-attention modules to fuse eye and face features optimally. The fused features are then treated as a spatial sequence, allowing for the capture of an intra-frame context, which is then propagated through time to model inter-frame dynamics. We evaluated our method on the EVE dataset and show that ST-Gaze achieves state-of-the-art performance both with and without person-specific adaptation. Additionally, our ablation study provides further insights into the model performance, showing that preserving and modelling intra-frame spatial context with our spatio-temporal recurrence is fundamentally superior to premature spatial pooling. As such, our results pave the way towards more robust video-based gaze estimation using commonly available cameras.

