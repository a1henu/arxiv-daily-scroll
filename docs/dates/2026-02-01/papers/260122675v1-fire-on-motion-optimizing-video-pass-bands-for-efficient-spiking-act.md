---
layout: default
title: Fire on Motion: Optimizing Video Pass-bands for Efficient Spiking Action Recognition
---

# Fire on Motion: Optimizing Video Pass-bands for Efficient Spiking Action Recognition
**arXiv**：[2601.22675v1](https://arxiv.org/abs/2601.22675) · [PDF](https://arxiv.org/pdf/2601.22675.pdf)  
**作者**：Shuhan Ye, Yuanbin Qian, Yi Yu, Chong Wang, Yuqi Xie, Jiazhen Xu, Kun Wang, Xudong Jiang  

**一句话要点**：提出Pass-Bands Optimizer以优化脉冲神经网络在视频动作识别中的时域通带

**关键词**：脉冲神经网络, 视频动作识别, 时域通带优化, 运动信息增强, 轻量模块

## 3 点简述
- 核心问题：脉冲神经网络在动态视频任务中表现不佳，因标准脉冲动态作为时域低通滤波器，强调静态内容而衰减运动信息。
- 方法要点：引入Pass-Bands Optimizer，通过两个可学习参数和轻量一致性约束，优化时域通带以聚焦任务相关运动频带。
- 实验或效果：在UCF101上提升超过10个百分点，在多模态动作识别和弱监督视频异常检测中均取得显著增益。

## 摘要（原文）

> Spiking neural networks (SNNs) have gained traction in vision due to their energy efficiency, bio-plausibility, and inherent temporal processing. Yet, despite this temporal capacity, most progress concentrates on static image benchmarks, and SNNs still underperform on dynamic video tasks compared to artificial neural networks (ANNs). In this work, we diagnose a fundamental pass-band mismatch: Standard spiking dynamics behave as a temporal low pass that emphasizes static content while attenuating motion bearing bands, where task relevant information concentrates in dynamic tasks. This phenomenon explains why SNNs can approach ANNs on static tasks yet fall behind on tasks that demand richer temporal understanding.To remedy this, we propose the Pass-Bands Optimizer (PBO), a plug-and-play module that optimizes the temporal pass-band toward task-relevant motion bands. PBO introduces only two learnable parameters, and a lightweight consistency constraint that preserves semantics and boundaries, incurring negligible computational overhead and requires no architectural changes. PBO deliberately suppresses static components that contribute little to discrimination, effectively high passing the stream so that spiking activity concentrates on motion bearing content. On UCF101, PBO yields over ten percentage points improvement. On more complex multi-modal action recognition and weakly supervised video anomaly detection, PBO delivers consistent and significant gains, offering a new perspective for SNN based video processing and understanding.

