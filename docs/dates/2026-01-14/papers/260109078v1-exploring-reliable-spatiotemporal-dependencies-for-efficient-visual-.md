---
layout: default
title: Exploring Reliable Spatiotemporal Dependencies for Efficient Visual Tracking
---

# Exploring Reliable Spatiotemporal Dependencies for Efficient Visual Tracking
**arXiv**：[2601.09078v1](https://arxiv.org/abs/2601.09078) · [PDF](https://arxiv.org/pdf/2601.09078.pdf)  
**作者**：Junze Shi, Yang Yu, Jian Shi, Haibo Luo  

**一句话要点**：提出STDTrack框架，通过可靠时空依赖提升轻量跟踪器性能，实现实时高效跟踪。

**关键词**：轻量目标跟踪, 时空依赖建模, 多帧信息融合, 实时跟踪, Transformer架构, 视频采样策略

## 3 点简述
- 现有轻量跟踪器训练时稀疏采样，未能充分利用视频时空信息，限制性能提升。
- STDTrack引入密集采样、时空传播令牌和多帧信息融合模块，增强特征提取与状态表示。
- 在多个基准测试中达到先进水平，在GOT-10k上媲美高性能非实时跟踪器，同时保持高帧率。

## 摘要（原文）

> Recent advances in transformer-based lightweight object tracking have established new standards across benchmarks, leveraging the global receptive field and powerful feature extraction capabilities of attention mechanisms. Despite these achievements, existing methods universally employ sparse sampling during training--utilizing only one template and one search image per sequence--which fails to comprehensively explore spatiotemporal information in videos. This limitation constrains performance and cause the gap between lightweight and high-performance trackers. To bridge this divide while maintaining real-time efficiency, we propose STDTrack, a framework that pioneers the integration of reliable spatiotemporal dependencies into lightweight trackers. Our approach implements dense video sampling to maximize spatiotemporal information utilization. We introduce a temporally propagating spatiotemporal token to guide per-frame feature extraction. To ensure comprehensive target state representation, we disign the Multi-frame Information Fusion Module (MFIFM), which augments current dependencies using historical context. The MFIFM operates on features stored in our constructed Spatiotemporal Token Maintainer (STM), where a quality-based update mechanism ensures information reliability. Considering the scale variation among tracking targets, we develop a multi-scale prediction head to dynamically adapt to objects of different sizes. Extensive experiments demonstrate state-of-the-art results across six benchmarks. Notably, on GOT-10k, STDTrack rivals certain high-performance non-real-time trackers (e.g., MixFormer) while operating at 192 FPS(GPU) and 41 FPS(CPU).

