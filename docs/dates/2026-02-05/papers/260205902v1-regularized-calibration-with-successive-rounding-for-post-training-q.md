---
layout: default
title: Regularized Calibration with Successive Rounding for Post-Training Quantization
---

# Regularized Calibration with Successive Rounding for Post-Training Quantization
**arXiv**：[2602.05902v1](https://arxiv.org/abs/2602.05902) · [PDF](https://arxiv.org/pdf/2602.05902.pdf)  
**作者**：Seohyeon Cha, Huancheng Chen, Dongjun Kim, Haoran Zhang, Kevin Chan, Gustavo de Veciana, Haris Vikalo  

**一句话要点**：提出正则化校准与逐次舍入方法，以提升大语言模型后训练量化的性能与效率。

**关键词**：后训练量化, 大语言模型, 校准正则化, 逐次舍入, 有限搜索, 模型压缩

## 3 点简述
- 核心问题：后训练量化中量化目标和舍入过程对模型性能影响显著，需平衡量化质量与计算成本。
- 方法要点：通过对称与非对称校准的插值作为正则化，结合逐次舍入和有限搜索，增强对激活不匹配的鲁棒性。
- 实验或效果：在多种大语言模型、量化比特宽度和基准测试中，该方法持续改善困惑度和准确率，计算成本可控。

## 摘要（原文）

> Large language models (LLMs) deliver robust performance across diverse applications, yet their deployment often faces challenges due to the memory and latency costs of storing and accessing billions of parameters. Post-training quantization (PTQ) enables efficient inference by mapping pretrained weights to low-bit formats without retraining, but its effectiveness depends critically on both the quantization objective and the rounding procedure used to obtain low-bit weight representations. In this work, we show that interpolating between symmetric and asymmetric calibration acts as a form of regularization that preserves the standard quadratic structure used in PTQ while providing robustness to activation mismatch. Building on this perspective, we derive a simple successive rounding procedure that naturally incorporates asymmetric calibration, as well as a bounded-search extension that allows for an explicit trade-off between quantization quality and the compute cost. Experiments across multiple LLM families, quantization bit-widths, and benchmarks demonstrate that the proposed bounded search based on a regularized asymmetric calibration objective consistently improves perplexity and accuracy over PTQ baselines, while incurring only modest and controllable additional computational cost.

