---
layout: default
title: LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation
---

# LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation
**arXiv**：[2601.19675v1](https://arxiv.org/abs/2601.19675) · [PDF](https://arxiv.org/pdf/2601.19675.pdf)  
**作者**：Hongyaoxing Gu, Lijuan Hu, Liye Yu, Haowei Li, Fangfang Liu  

**一句话要点**：提出LoPRo算法以增强低秩量化，通过块置换旋转提升残差矩阵量化精度，无需微调。

**关键词**：后训练量化, 低秩量化, 块置换旋转, Walsh-Hadamard变换, 混合精度分解, 模型压缩

## 3 点简述
- 核心问题：低比特量化中残差矩阵量化困难，导致精度下降。
- 方法要点：应用块置换和Walsh-Hadamard变换旋转列，并基于R1SVD进行混合精度低秩分解。
- 实验或效果：在2/3比特量化中超越无微调方法，在LLaMA和Mixtral模型上实现高精度与加速。

## 摘要（原文）

> Post-training quantization (PTQ) enables effective model compression while preserving relatively high accuracy. Current weight-only PTQ methods primarily focus on the challenging sub-3-bit regime, where approaches often suffer significant accuracy degradation, typically requiring fine-tuning to achieve competitive performance. In this work, we revisit the fundamental characteristics of weight quantization and analyze the challenges in quantizing the residual matrix under low-rank approximation. We propose LoPRo, a novel fine-tuning-free PTQ algorithm that enhances residual matrix quantization by applying block-wise permutation and Walsh-Hadamard transformations to rotate columns of similar importance, while explicitly preserving the quantization accuracy of the most salient column blocks. Furthermore, we introduce a mixed-precision fast low-rank decomposition based on rank-1 sketch (R1SVD) to further minimize quantization costs. Experiments demonstrate that LoPRo outperforms existing fine-tuning-free PTQ methods at both 2-bit and 3-bit quantization, achieving accuracy comparable to fine-tuning baselines. Specifically, LoPRo achieves state-of-the-art quantization accuracy on LLaMA-2 and LLaMA-3 series models while delivering up to a 4$\times$ speedup. In the MoE model Mixtral-8x7B, LoPRo completes quantization within 2.5 hours, simultaneously reducing perplexity by 0.4$\downarrow$ and improving accuracy by 8\%$\uparrow$. Moreover, compared to other low-rank quantization methods, LoPRo achieves superior accuracy with a significantly lower rank, while maintaining high inference efficiency and minimal additional latency.

