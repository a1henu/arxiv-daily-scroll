---
layout: default
title: Switchcodec: Adaptive residual-expert sparse quantization for high-fidelity neural audio coding
---

# Switchcodec: Adaptive residual-expert sparse quantization for high-fidelity neural audio coding
**arXiv**：[2601.20362v1](https://arxiv.org/abs/2601.20362) · [PDF](https://arxiv.org/pdf/2601.20362.pdf)  
**作者**：Xiangbo Wang, Wenbin Jiang, Jin Wang, Yubo You, Sheng Fang, Fei Wen  

**一句话要点**：提出SwitchCodec，基于残差专家向量量化，实现高保真神经音频编码的自适应多比特率压缩。

**关键词**：神经音频编码, 残差专家向量量化, 自适应量化, 高保真压缩, 多比特率操作

## 3 点简述
- 核心问题：固定码本数量的残差向量量化在音频内容变异性大时效率低下，尤其对简单或复杂信号。
- 方法要点：结合共享量化器和动态路由的专家量化器，根据输入音频激活，解耦比特率与码本容量。
- 实验或效果：在客观指标和主观听测中超越现有基线，支持无需重训练的多比特率操作。

## 摘要（原文）

> Recent neural audio compression models often rely on residual vector quantization for high-fidelity coding, but using a fixed number of per-frame codebooks is suboptimal for the wide variability of audio content-especially for signals that are either very simple or highly complex. To address this limitation, we propose SwitchCodec, a neural audio codec based on Residual Experts Vector Quantization (REVQ). REVQ combines a shared quantizer with dynamically routed expert quantizers that are activated according to the input audio, decoupling bitrate from codebook capacity and improving compression efficiency. This design ensures full training and utilization of each quantizer. In addition, a variable-bitrate mechanism adjusts the number of active expert quantizers at inference, enabling multi-bitrate operation without retraining. Experiments demonstrate that SwitchCodec surpasses existing baselines on both objective metrics and subjective listening tests.

