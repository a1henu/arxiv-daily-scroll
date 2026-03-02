---
layout: default
title: GRAIL: Post-hoc Compensation by Linear Reconstruction for Compressed Networks
---

# GRAIL: Post-hoc Compensation by Linear Reconstruction for Compressed Networks
**arXiv**：[2602.23795v1](https://arxiv.org/abs/2602.23795) · [PDF](https://arxiv.org/pdf/2602.23795.pdf)  
**作者**：Wenwu Tang, Dong Wang, Lothar Thiele, Olga Saukh  

**一句话要点**：提出GRAIL方法，通过线性重建补偿压缩网络，无需微调即可恢复精度

**关键词**：模型压缩, 后处理补偿, 线性重建, Gram矩阵, 零微调, 结构化剪枝

## 3 点简述
- 核心问题：结构化压缩后精度下降，但微调可能不切实际
- 方法要点：基于Gram矩阵和岭回归，线性重建隐藏表示并吸收到权重中
- 实验或效果：在ResNets、ViTs和LLMs上提升精度或困惑度，无需反向传播

## 摘要（原文）

> Structured deep model compression methods are hardware-friendly and substantially reduce memory and inference costs. However, under aggressive compression, the resulting accuracy degradation often necessitates post-compression finetuning, which can be impractical due to missing labeled data or high training cost. We propose post-hoc blockwise compensation, called GRAIL, a simple zero-finetuning step applied after model compression that restores each block's input-output behavior using a small calibration set. The method summarizes hidden activations via a Gram matrix and applies ridge regression to linearly reconstruct the original hidden representation from the reduced one. The resulting reconstruction map is absorbed into the downstream projection weights, while the upstream layer is compressed. The approach is selector-agnostic (Magnitude, Wanda, Gram-based selection, or folding), data-aware (requiring only a few forward passes without gradients or labels), and recovers classic pruning or folding when the Gram matrix is near identity, indicating weak inter-channel correlations. Across ResNets, ViTs, and decoder-only LLMs, GRAIL consistently improves accuracy or perplexity over data-free and data-aware pruning or folding baselines in practical compression regimes, with manageable overhead and no backpropagation. The code is available at https://github.com/TWWinde/GRAIL.

