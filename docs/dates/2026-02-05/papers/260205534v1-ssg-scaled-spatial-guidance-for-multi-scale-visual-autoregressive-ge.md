---
layout: default
title: SSG: Scaled Spatial Guidance for Multi-Scale Visual Autoregressive Generation
---

# SSG: Scaled Spatial Guidance for Multi-Scale Visual Autoregressive Generation
**arXiv**：[2602.05534v1](https://arxiv.org/abs/2602.05534) · [PDF](https://arxiv.org/pdf/2602.05534.pdf)  
**作者**：Youngwoo Shin, Jiwan Hur, Junmo Kim  

**一句话要点**：提出SSG以解决视觉自回归模型在推理时层次漂移问题，提升图像生成质量。

**关键词**：视觉自回归生成, 多尺度图像合成, 推理时指导, 频率域处理, 语义残差, 层次漂移缓解

## 3 点简述
- 核心问题：视觉自回归模型在推理时因容量限制和误差累积导致层次漂移，偏离粗到细生成特性。
- 方法要点：基于信息论视角，提出SSG，通过频率域处理DSE隔离语义残差，作为无训练推理指导。
- 实验或效果：SSG在多种VAR模型中提升保真度和多样性，保持低延迟，代码已开源。

## 摘要（原文）

> Visual autoregressive (VAR) models generate images through next-scale prediction, naturally achieving coarse-to-fine, fast, high-fidelity synthesis mirroring human perception. In practice, this hierarchy can drift at inference time, as limited capacity and accumulated error cause the model to deviate from its coarse-to-fine nature. We revisit this limitation from an information-theoretic perspective and deduce that ensuring each scale contributes high-frequency content not explained by earlier scales mitigates the train-inference discrepancy. With this insight, we propose Scaled Spatial Guidance (SSG), training-free, inference-time guidance that steers generation toward the intended hierarchy while maintaining global coherence. SSG emphasizes target high-frequency signals, defined as the semantic residual, isolated from a coarser prior. To obtain this prior, we leverage a principled frequency-domain procedure, Discrete Spatial Enhancement (DSE), which is devised to sharpen and better isolate the semantic residual through frequency-aware construction. SSG applies broadly across VAR models leveraging discrete visual tokens, regardless of tokenization design or conditioning modality. Experiments demonstrate SSG yields consistent gains in fidelity and diversity while preserving low latency, revealing untapped efficiency in coarse-to-fine image generation. Code is available at https://github.com/Youngwoo-git/SSG.

