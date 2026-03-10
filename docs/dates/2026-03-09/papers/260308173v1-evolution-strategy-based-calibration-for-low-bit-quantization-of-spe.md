---
layout: default
title: Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models
---

# Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models
**arXiv**：[2603.08173v1](https://arxiv.org/abs/2603.08173) · [PDF](https://arxiv.org/pdf/2603.08173.pdf)  
**作者**：Lucas Rakotoarivony  

**一句话要点**：提出基于进化策略的校准方法ESC，以解决语音模型低比特量化中的激活范围校准问题。

**关键词**：语音模型量化, 进化策略校准, 低比特量化, 激活范围优化, 后训练量化

## 3 点简述
- 核心问题：语音信号激活范围大，标准校准技术导致信息丢失，影响量化性能。
- 方法要点：将激活缩放建模为优化问题，采用基于进化策略的两步局部-全局方案求解。
- 实验或效果：ESC在INT8量化下保持性能无损，INT4量化下实现近无损，结合PTQ方法进一步减少精度损失。

## 摘要（原文）

> Quantization has become essential for the efficient deployment of speech processing systems. Although widely studied, most existing quantization methods were developed for vision and NLP architectures, while the specific challenges of audio signals remain largely overlooked. In particular, we show that audio activations can exhibit large calibration ranges, leading to significant information loss when standard calibration techniques are applied. To address this, we propose ESC, an Evolution Strategy-based Calibration method that formulates activation scaling as an optimization problem and solves it using a two-step local-global scheme driven by an evolution strategy. ESC enables unaltered performance under full INT8 quantization and is the first calibration method to achieve near-lossless performance for full INT4 quantization across multiple speech tasks. Integrating ESC with PTQ methods further reduces performance loss, achieving a 1% relative accuracy degradation on the AST model.

