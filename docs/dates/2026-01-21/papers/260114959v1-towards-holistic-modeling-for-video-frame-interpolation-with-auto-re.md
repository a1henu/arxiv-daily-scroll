---
layout: default
title: Towards Holistic Modeling for Video Frame Interpolation with Auto-regressive Diffusion Transformers
---

# Towards Holistic Modeling for Video Frame Interpolation with Auto-regressive Diffusion Transformers
**arXiv**：[2601.14959v1](https://arxiv.org/abs/2601.14959) · [PDF](https://arxiv.org/pdf/2601.14959.pdf)  
**作者**：Xinyu Peng, Han Li, Yuyang Huang, Ziyang Zheng, Yaoming Wang, Xin Chen, Wenrui Dai, Chenglin Li, Junni Zou, Hongkai Xiong  

**一句话要点**：提出LDF-VFI框架，通过自回归扩散变换器实现视频帧插值，解决长序列时间不一致性问题。

**关键词**：视频帧插值, 自回归扩散变换器, 长序列建模, 时间一致性, 高分辨率处理

## 3 点简述
- 现有方法处理视频为独立短片段，导致时间不一致和运动伪影。
- 采用自回归扩散变换器建模整个视频序列，引入跳跃连接采样策略减少误差累积。
- 在长序列基准测试中达到最先进性能，尤其在运动大场景下表现优异。

## 摘要（原文）

> Existing video frame interpolation (VFI) methods often adopt a frame-centric approach, processing videos as independent short segments (e.g., triplets), which leads to temporal inconsistencies and motion artifacts. To overcome this, we propose a holistic, video-centric paradigm named \textbf{L}ocal \textbf{D}iffusion \textbf{F}orcing for \textbf{V}ideo \textbf{F}rame \textbf{I}nterpolation (LDF-VFI). Our framework is built upon an auto-regressive diffusion transformer that models the entire video sequence to ensure long-range temporal coherence. To mitigate error accumulation inherent in auto-regressive generation, we introduce a novel skip-concatenate sampling strategy that effectively maintains temporal stability. Furthermore, LDF-VFI incorporates sparse, local attention and tiled VAE encoding, a combination that not only enables efficient processing of long sequences but also allows generalization to arbitrary spatial resolutions (e.g., 4K) at inference without retraining. An enhanced conditional VAE decoder, which leverages multi-scale features from the input video, further improves reconstruction fidelity. Empirically, LDF-VFI achieves state-of-the-art performance on challenging long-sequence benchmarks, demonstrating superior per-frame quality and temporal consistency, especially in scenes with large motion. The source code is available at https://github.com/xypeng9903/LDF-VFI.

