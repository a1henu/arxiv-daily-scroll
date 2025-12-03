---
layout: default
title: TrackNetV5: Residual-Driven Spatio-Temporal Refinement and Motion Direction Decoupling for Fast Object Tracking
---

# TrackNetV5: Residual-Driven Spatio-Temporal Refinement and Motion Direction Decoupling for Fast Object Tracking
**arXiv**：[2512.02789v1](https://arxiv.org/abs/2512.02789) · [PDF](https://arxiv.org/pdf/2512.02789.pdf)  
**作者**：Tang Haonan, Chen Yanjun, Jiang Lezhi  

**一句话要点**：提出TrackNetV5，通过运动方向解耦和残差驱动时空细化，提升快速小目标跟踪性能。

**关键词**：快速目标跟踪, 运动方向解耦, 残差驱动细化, 时空上下文, Transformer模块, 小物体跟踪

## 3 点简述
- 核心问题：现有TrackNet版本在遮挡和运动方向模糊方面存在局限，影响跟踪精度。
- 方法要点：引入运动方向解耦模块编码轨迹方向，并采用残差驱动时空细化头恢复遮挡目标。
- 实验或效果：在TrackNetV2数据集上达到新SOTA，F1分数0.9859，精度0.9733，计算开销仅增3.7%。

## 摘要（原文）

> The TrackNet series has established a strong baseline for fast-moving small object tracking in sports. However, existing iterations face significant limitations: V1-V3 struggle with occlusions due to a reliance on purely visual cues, while TrackNetV4, despite introducing motion inputs, suffers from directional ambiguity as its absolute difference method discards motion polarity. To overcome these bottlenecks, we propose TrackNetV5, a robust architecture integrating two novel mechanisms. First, to recover lost directional priors, we introduce the Motion Direction Decoupling (MDD) module. Unlike V4, MDD decomposes temporal dynamics into signed polarity fields, explicitly encoding both movement occurrence and trajectory direction. Second, we propose the Residual-Driven Spatio-Temporal Refinement (R-STR) head. Operating on a coarse-to-fine paradigm, this Transformer-based module leverages factorized spatio-temporal contexts to estimate a corrective residual, effectively recovering occluded targets. Extensive experiments on the TrackNetV2 dataset demonstrate that TrackNetV5 achieves a new state-of-the-art F1-score of 0.9859 and an accuracy of 0.9733, significantly outperforming previous versions. Notably, this performance leap is achieved with a marginal 3.7% increase in FLOPs compared to V4, maintaining real-time inference capabilities while delivering superior tracking precision.

