---
layout: default
title: FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time
---

# FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time
**arXiv**：[2601.05738v1](https://arxiv.org/abs/2601.05738) · [PDF](https://arxiv.org/pdf/2601.05738.pdf)  
**作者**：Christopher Thirgood, Oscar Mendez, Erin Ling, Jon Storey, Simon Hadfield  

**一句话要点**：提出FeatureSLAM，实时SLAM系统结合3D高斯泼溅与特征光栅化，提升跟踪与建图精度并支持开放集分割。

**关键词**：实时SLAM, 3D高斯泼溅, 特征光栅化, 开放集分割, 视觉基础模型, 语义建图

## 3 点简述
- 核心问题：传统SLAM系统依赖RGB-D输入，语义信息有限，影响跟踪稳定性和下游任务扩展。
- 方法要点：集成密集特征光栅化到3D高斯泼溅中，利用视觉基础模型增强语义，实现实时跟踪与特征丰富建图。
- 实验或效果：在标准基准测试中，姿态误差降低9%，建图精度提高8%，跟踪性能媲美先进系统，支持开放集分割。

## 摘要（原文）

> We present a real-time tracking SLAM system that unifies efficient camera tracking with photorealistic feature-enriched mapping using 3D Gaussian Splatting (3DGS). Our main contribution is integrating dense feature rasterization into the novel-view synthesis, aligned with a visual foundation model. This yields strong semantics, going beyond basic RGB-D input, aiding both tracking and mapping accuracy. Unlike previous semantic SLAM approaches (which embed pre-defined class labels) FeatureSLAM enables entirely new downstream tasks via free-viewpoint, open-set segmentation. Across standard benchmarks, our method achieves real-time tracking, on par with state-of-the-art systems while improving tracking stability and map fidelity without prohibitive compute. Quantitatively, we obtain 9\% lower pose error and 8\% higher mapping accuracy compared to recent fixed-set SLAM baselines. Our results confirm that real-time feature-embedded SLAM, is not only valuable for enabling new downstream applications. It also improves the performance of the underlying tracking and mapping subsystems, providing semantic and language masking results that are on-par with offline 3DGS models, alongside state-of-the-art tracking, depth and RGB rendering.

