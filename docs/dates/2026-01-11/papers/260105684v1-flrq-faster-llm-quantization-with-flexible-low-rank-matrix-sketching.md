---
layout: default
title: FLRQ: Faster LLM Quantization with Flexible Low-Rank Matrix Sketching
---

# FLRQ: Faster LLM Quantization with Flexible Low-Rank Matrix Sketching
**arXiv**：[2601.05684v1](https://arxiv.org/abs/2601.05684) · [PDF](https://arxiv.org/pdf/2601.05684.pdf)  
**作者**：Hongyaoxing Gul, Lijuan Hu, Shuzi Niu, Fangfang Liu  

**一句话要点**：提出FLRQ方法，通过灵活低秩矩阵草图快速优化大语言模型量化，提升效率与精度。

**关键词**：大语言模型量化, 低秩近似, 后训练量化, 矩阵草图, 量化误差优化, 算法效率

## 3 点简述
- 现有低秩后训练量化方法需昂贵微调，难以适应大模型不同层和数据，且计算开销大。
- FLRQ结合R1-FLR快速选择最优秩和BLC最小化量化误差，实现高效低秩近似与量化。
- 实验表明FLRQ在量化质量和算法效率上达到先进水平，具有强鲁棒性。

## 摘要（原文）

> Traditional post-training quantization (PTQ) is considered an effective approach to reduce model size and accelerate inference of large-scale language models (LLMs). However, existing low-rank PTQ methods require costly fine-tuning to determine a compromise rank for diverse data and layers in large models, failing to exploit their full potential. Additionally, the current SVD-based low-rank approximation compounds the computational overhead. In this work, we thoroughly analyze the varying effectiveness of low-rank approximation across different layers in representative models. Accordingly, we introduce \underline{F}lexible \underline{L}ow-\underline{R}ank \underline{Q}uantization (FLRQ), a novel solution designed to quickly identify the accuracy-optimal ranks and aggregate them to achieve minimal storage combinations. FLRQ comprises two powerful components, Rank1-Sketch-based Flexible Rank Selection (R1-FLR) and Best Low-rank Approximation under Clipping (BLC). R1-FLR applies the R1-Sketch with Gaussian projection for the fast low-rank approximation, enabling outlier-aware rank extraction for each layer. Meanwhile, BLC aims at minimizing the low-rank quantization error under the scaling and clipping strategy through an iterative method. FLRQ demonstrates strong effectiveness and robustness in comprehensive experiments, achieving state-of-the-art performance in both quantization quality and algorithm efficiency.

