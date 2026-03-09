---
layout: default
title: TempoSyncDiff: Distilled Temporally-Consistent Diffusion for Low-Latency Audio-Driven Talking Head Generation
---

# TempoSyncDiff: Distilled Temporally-Consistent Diffusion for Low-Latency Audio-Driven Talking Head Generation
**arXiv**：[2603.06057v1](https://arxiv.org/abs/2603.06057) · [PDF](https://arxiv.org/pdf/2603.06057.pdf)  
**作者**：Soumya Mazumdar, Vineet Kumar Rakesh  

**一句话要点**：提出TempoSyncDiff蒸馏框架以解决音频驱动说话头生成中的高延迟与时间不稳定问题

**关键词**：说话头生成, 扩散模型, 蒸馏训练, 时间一致性, 音频驱动, 边缘计算

## 3 点简述
- 核心问题：扩散模型在说话头生成中存在高推理延迟、时间不稳定如闪烁和身份漂移，以及音频-视觉对齐不完美
- 方法要点：采用教师-学生蒸馏，通过身份锚定、时间正则化和音素音频条件化，实现少步推理以提升稳定性和效率
- 实验或效果：在LRS3数据集上评估，蒸馏模型能保持教师重建行为，同时显著降低延迟，支持边缘部署可行性

## 摘要（原文）

> Diffusion models have recently advanced photorealistic human synthesis, although practical talking-head generation (THG) remains constrained by high inference latency, temporal instability such as flicker and identity drift, and imperfect audio-visual alignment under challenging speech conditions. This paper introduces TempoSyncDiff, a reference-conditioned latent diffusion framework that explores few-step inference for efficient audio-driven talking-head generation. The approach adopts a teacher-student distillation formulation in which a diffusion teacher trained with a standard noise prediction objective guides a lightweight student denoiser capable of operating with significantly fewer inference steps to improve generation stability. The framework incorporates identity anchoring and temporal regularization designed to mitigate identity drift and frame-to-frame flicker during synthesis, while viseme-based audio conditioning provides coarse lip motion control. Experiments on the LRS3 dataset report denoising-stage component-level metrics relative to VAE reconstructions and preliminary latency characterization, including CPU-only and edge computing measurements and feasibility estimates for edge deployment. The results suggest that distilled diffusion models can retain much of the reconstruction behaviour of a stronger teacher while enabling substantially lower latency inference. The study is positioned as an initial step toward practical diffusion-based talking-head generation under constrained computational settings. GitHub: https://mazumdarsoumya.github.io/TempoSyncDiff

