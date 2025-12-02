---
layout: default
title: Q2D2: A Geometry-Aware Audio Codec Leveraging Two-Dimensional Quantization
---

# Q2D2: A Geometry-Aware Audio Codec Leveraging Two-Dimensional Quantization
**arXiv**：[2512.01537v1](https://arxiv.org/abs/2512.01537) · [PDF](https://arxiv.org/pdf/2512.01537.pdf)  
**作者**：Tal Shuster, Eliya Nachmani  

**一句话要点**：提出Q2D2量化方案以提升神经音频编解码器的压缩效率和表示学习能力。

**关键词**：神经音频编解码, 二维量化, 几何感知, 码本利用率, 压缩效率, 语音重建

## 3 点简述
- 核心问题：传统量化方法如RVQ、VQ和FSQ限制潜在空间几何结构，导致特征相关性捕获不足、码本利用率低和令牌率低效。
- 方法要点：Q2D2将特征对投影到结构化二维网格（如六边形、菱形或矩形）并量化到最近网格值，形成隐式码本，码本大小与传统方法相当。
- 实验或效果：在语音领域实验中，Q2D2在客观和主观重建指标上达到竞争或优越性能，同时保持低令牌率和高码本利用率。

## 摘要（原文）

> Recent neural audio codecs have achieved impressive reconstruction quality, typically relying on quantization methods such as Residual Vector Quantization (RVQ), Vector Quantization (VQ) and Finite Scalar Quantization (FSQ). However, these quantization techniques limit the geometric structure of the latent space, make it harder to capture correlations between features leading to inefficiency in representation learning, codebook utilization and token rate. In this paper we introduce Two Dimensional Quantization (Q2D2), a quantization scheme in which feature pairs are projected onto structured 2D grids such as hexagonal, rhombic, or rectangular tiling and quantized to the nearest grid values, yielding an implicit codebook defined by the product of grid levels, with codebook sizes comparable to conventional methods. Despite its simple geometric formulation, Q2D2 improves audio compression efficiency, with low token rates and high codebook utilization while maintaining state of the art reconstruction quality. Specifically, Q2D2 achieves competitive to superior performance in various objective and subjective reconstruction metrics, across extensive experiments in speech domain compared to state of the art models. Comprehensive ablation studies further confirm the effectiveness of our design choices.

