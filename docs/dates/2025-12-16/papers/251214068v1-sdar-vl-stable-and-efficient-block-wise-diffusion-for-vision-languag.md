---
layout: default
title: SDAR-VL: Stable and Efficient Block-wise Diffusion for Vision-Language Understanding
---

# SDAR-VL: Stable and Efficient Block-wise Diffusion for Vision-Language Understanding
**arXiv**：[2512.14068v1](https://arxiv.org/abs/2512.14068) · [PDF](https://arxiv.org/pdf/2512.14068.pdf)  
**作者**：Shuang Cheng, Yuhua Jiang, Zineng Zhou, Dawei Liu, Wang Tao, Linfeng Zhang, Biqing Qi, Bowen Zhou  

**一句话要点**：提出SDAR-VL框架，以稳定高效块状扩散提升视觉语言理解性能

**关键词**：块状离散扩散, 视觉语言理解, 训练稳定性, 噪声调度, 掩码策略, 多模态模型

## 3 点简述
- 核心问题：块状离散扩散训练成本高、收敛慢且不稳定，落后于自回归基线
- 方法要点：集成异步块状噪声调度、有效掩码比率缩放和渐进Beta噪声课程
- 实验或效果：在21个基准测试中提升效率、稳定性和性能，匹配或超越强基线

## 摘要（原文）

> Block-wise discrete diffusion offers an attractive balance between parallel generation and causal dependency modeling, making it a promising backbone for vision-language modeling. However, its practical adoption has been limited by high training cost, slow convergence, and instability, which have so far kept it behind strong autoregressive (AR) baselines. We present \textbf{SDAR-VL}, the first systematic application of block-wise discrete diffusion to large-scale vision-language understanding (VLU), together with an \emph{integrated framework for efficient and stable training}. This framework unifies three components: (1) \textbf{Asynchronous Block-wise Noise Scheduling} to diversify supervision within each batch; (2) \textbf{Effective Mask Ratio Scaling} for unbiased loss normalization under stochastic masking; and (3) a \textbf{Progressive Beta Noise Curriculum} that increases effective mask coverage while preserving corruption diversity. Experiments on 21 single-image, multi-image, and video benchmarks show that SDAR-VL consistently improves \emph{training efficiency}, \emph{convergence stability}, and \emph{task performance} over conventional block diffusion. On this evaluation suite, SDAR-VL sets a new state of the art among diffusion-based vision-language models and, under matched settings, matches or surpasses strong AR baselines such as LLaVA-OneVision as well as the global diffusion baseline LLaDA-V, establishing block-wise diffusion as a practical backbone for VLU.

