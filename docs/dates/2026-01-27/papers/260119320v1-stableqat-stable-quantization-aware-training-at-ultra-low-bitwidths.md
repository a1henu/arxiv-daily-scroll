---
layout: default
title: StableQAT: Stable Quantization-Aware Training at Ultra-Low Bitwidths
---

# StableQAT: Stable Quantization-Aware Training at Ultra-Low Bitwidths
**arXiv**：[2601.19320v1](https://arxiv.org/abs/2601.19320) · [PDF](https://arxiv.org/pdf/2601.19320.pdf)  
**作者**：Tianyi Chen, Sihan Chen, Xiaoyi Qu, Dan Zhao, Ruomei Yan, Jongwoo Ko, Luming Liang, Pashmina Cameron  

**一句话要点**：提出StableQAT框架以解决超低位宽量化感知训练中的不稳定问题

**关键词**：量化感知训练, 超低位宽量化, 梯度替代, 训练稳定性, 离散傅里叶分析

## 3 点简述
- 核心问题：超低位宽量化感知训练常因梯度不匹配或不稳定导致优化困难
- 方法要点：基于舍入算子的离散傅里叶分析，设计轻量级理论替代梯度以稳定训练
- 实验或效果：在2-4位宽下实现稳定高效训练，提升性能与鲁棒性，训练开销可忽略

## 摘要（原文）

> Quantization-aware training (QAT) is essential for deploying large models under strict memory and latency constraints, yet achieving stable and robust optimization at ultra-low bitwidths remains challenging. Common approaches based on the straight-through estimator (STE) or soft quantizers often suffer from gradient mismatch, instability, or high computational overhead. As such, we propose StableQAT, a unified and efficient QAT framework that stabilizes training in ultra low-bit settings via a novel, lightweight, and theoretically grounded surrogate for backpropagation derived from a discrete Fourier analysis of the rounding operator. StableQAT strictly generalizes STE as the latter arises as a special case of our more expressive surrogate family, yielding smooth, bounded, and inexpensive gradients that improve QAT training performance and stability across various hyperparameter choices. In experiments, StableQAT exhibits stable and efficient QAT at 2-4 bit regimes, demonstrating improved training stability, robustness, and superior performance with negligible training overhead against standard QAT techniques. Our code is available at https://github.com/microsoft/StableQAT.

