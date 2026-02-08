---
layout: default
title: Hybrid Gated Flow (HGF): Stabilizing 1.58-bit LLMs via Selective Low-Rank Correction
---

# Hybrid Gated Flow (HGF): Stabilizing 1.58-bit LLMs via Selective Low-Rank Correction
**arXiv**：[2602.05269v1](https://arxiv.org/abs/2602.05269) · [PDF](https://arxiv.org/pdf/2602.05269.pdf)  
**作者**：David Alejandro Trejo Pizzo  

**一句话要点**：提出混合门控流以稳定1.58位大语言模型，通过选择性低秩校正减少边缘部署中的内存墙问题。

**关键词**：大语言模型量化, 边缘设备部署, 低秩校正, 自适应门控, 模型稳定性, 内存墙优化

## 3 点简述
- 核心问题：1.58位量化技术显著降低内存占用，但导致困惑度下降20-25%，影响模型质量。
- 方法要点：采用双流架构，结合1.58位三元主干和由自适应门控制的低秩FP16校正路径，实现选择性校正。
- 实验或效果：在TinyStories数据集上，HGF 5.4验证损失为0.9306，相比BitNet恢复约55%质量差距，内存开销仅增加12-15%。

## 摘要（原文）

> The deployment of Large Language Models (LLMs) on edge devices is fundamentally constrained by the "Memory Wall" -- a hardware limitation where memory bandwidth, not compute, becomes the bottleneck. Recent 1.58-bit quantization techniques (e.g., BitNet b1.58) dramatically reduce memory footprint but typically incur a perplexity degradation of 20-25% compared to FP16 baselines. In this work, we introduce Hybrid Gated Flow (HGF), a dual-stream architecture that couples a 1.58-bit ternary backbone with a learnable, low-rank FP16 correction path controlled by adaptive gates.
>   Through extensive experiments on the TinyStories dataset across two training regimes (2500 and 3500 steps), we demonstrate that HGF 5.4 achieves a validation loss of 0.9306 compared to BitNet's 1.0294, recovering approximately 55% of the quality gap between pure ternary quantization and the FP16 baseline (0.8490). This recovery is achieved with only ~12-15% memory overhead beyond the ternary backbone.
>   Furthermore, we provide empirical evidence for an emergent phenomenon: quantization as structural regularization. While a full-precision differential attention baseline (Diff_Only) exhibited training instability with validation loss exceeding 1.68, the ternary-anchored HGF maintained robust convergence throughout training. Finally, we report preliminary results extending this architecture to 1.2B and 3B parameter models trained on SlimPajama and FineWeb-Edu. These larger-scale experiments confirm that the architectural stability and quality recovery observed in small-scale proxies scale linearly to production-grade language modeling regimes.

