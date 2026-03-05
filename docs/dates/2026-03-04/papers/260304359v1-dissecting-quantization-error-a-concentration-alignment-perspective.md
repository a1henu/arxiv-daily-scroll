---
layout: default
title: Dissecting Quantization Error: A Concentration-Alignment Perspective
---

# Dissecting Quantization Error: A Concentration-Alignment Perspective
**arXiv**：[2603.04359v1](https://arxiv.org/abs/2603.04359) · [PDF](https://arxiv.org/pdf/2603.04359.pdf)  
**作者**：Marco Federici, Boris van Breugel, Paul Whatmough, Markus Nagel  

**一句话要点**：提出块级集中对齐变换以优化大模型量化误差，提升4位精度性能。

**关键词**：量化误差分析, 集中对齐变换, 大模型量化, 信噪比优化, 4位精度

## 3 点简述
- 量化误差分析：基于信噪比分解为权重与激活的集中度和对齐度。
- 方法创新：引入块级集中对齐变换，联合优化集中度和对齐度以最大化信噪比。
- 实验验证：在多个大语言模型上，4位量化性能优于或匹配现有变换方法。

## 摘要（原文）

> Quantization can drastically increase the efficiency of large language and vision models, but typically incurs an accuracy drop. Recently, function-preserving transforms (e.g. rotations, Hadamard transform, channel-wise scaling) have been successfully applied to reduce post-training quantization error, yet a principled explanation remains elusive. We analyze linear-layer quantization via the signal-to-quantization-noise ratio (SQNR), showing that for uniform integer quantization at a fixed bit width, SQNR decomposes into (i) the concentration of weights and activations (capturing spread and outliers), and (ii) the alignment of their dominant variation directions. This reveals an actionable insight: beyond concentration - the focus of most prior transforms (e.g. rotations or Hadamard) - improving alignment between weight and activation can further reduce quantization error. Motivated by this, we introduce block Concentration-Alignment Transforms (CAT), a lightweight linear transformation that uses a covariance estimate from a small calibration set to jointly improve concentration and alignment, approximately maximizing SQNR. Experiments across several LLMs show that CAT consistently matches or outperforms prior transform-based quantization methods at 4-bit precision, confirming the insights gained in our framework.

