---
layout: default
title: Streaming Autoregressive Video Generation via Diagonal Distillation
---

# Streaming Autoregressive Video Generation via Diagonal Distillation
**arXiv**：[2603.09488v1](https://arxiv.org/abs/2603.09488) · [PDF](https://arxiv.org/pdf/2603.09488.pdf)  
**作者**：Jinxiu Liu, Xuanming Liu, Kangfu Mei, Yandong Wen, Ming-HsuanYang, Weiyang Liu  

**一句话要点**：提出对角蒸馏方法以解决视频流生成中的时序依赖与误差累积问题

**关键词**：视频生成, 自回归模型, 蒸馏训练, 时序依赖, 实时流媒体, 光流建模

## 3 点简述
- 核心问题：现有视频蒸馏方法忽视时序依赖，导致运动不连贯和长序列误差累积
- 方法要点：采用非对称生成策略，早期块多步处理，后期块少步继承，结合隐式光流建模
- 实验或效果：实现31 FPS的5秒视频生成，速度提升277.3倍，保持高质量运动

## 摘要（原文）

> Large pretrained diffusion models have significantly enhanced the quality of generated videos, and yet their use in real-time streaming remains limited. Autoregressive models offer a natural framework for sequential frame synthesis but require heavy computation to achieve high fidelity. Diffusion distillation can compress these models into efficient few-step variants, but existing video distillation approaches largely adapt image-specific methods that neglect temporal dependencies. These techniques often excel in image generation but underperform in video synthesis, exhibiting reduced motion coherence, error accumulation over long sequences, and a latency-quality trade-off. We identify two factors that result in these limitations: insufficient utilization of temporal context during step reduction and implicit prediction of subsequent noise levels in next-chunk prediction (i.e., exposure bias). To address these issues, we propose Diagonal Distillation, which operates orthogonally to existing approaches and better exploits temporal information across both video chunks and denoising steps. Central to our approach is an asymmetric generation strategy: more steps early, fewer steps later. This design allows later chunks to inherit rich appearance information from thoroughly processed early chunks, while using partially denoised chunks as conditional inputs for subsequent synthesis. By aligning the implicit prediction of subsequent noise levels during chunk generation with the actual inference conditions, our approach mitigates error propagation and reduces oversaturation in long-range sequences. We further incorporate implicit optical flow modeling to preserve motion quality under strict step constraints. Our method generates a 5-second video in 2.61 seconds (up to 31 FPS), achieving a 277.3x speedup over the undistilled model.

