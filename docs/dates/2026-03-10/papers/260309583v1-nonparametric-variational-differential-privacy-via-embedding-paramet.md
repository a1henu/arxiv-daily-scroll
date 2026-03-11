---
layout: default
title: Nonparametric Variational Differential Privacy via Embedding Parameter Clipping
---

# Nonparametric Variational Differential Privacy via Embedding Parameter Clipping
**arXiv**：[2603.09583v1](https://arxiv.org/abs/2603.09583) · [PDF](https://arxiv.org/pdf/2603.09583.pdf)  
**作者**：Dina El Zein, Shashi Kumar, James Henderson  

**一句话要点**：提出嵌入参数裁剪方法以增强非参数变分差分隐私模型的隐私-效用权衡

**关键词**：非参数变分差分隐私, 嵌入参数裁剪, Rényi散度, 隐私-效用权衡, 语言模型隐私

## 3 点简述
- 核心问题：非参数变分差分隐私中潜在表示漂移导致隐私保障弱和训练不稳定
- 方法要点：基于Rényi散度上界最小化目标，推导后验参数的理论约束并实施裁剪
- 实验或效果：裁剪模型在多个下游任务中实现更紧隐私界限和更高性能

## 摘要（原文）

> The nonparametric variational information bottleneck (NVIB) provides the foundation for nonparametric variational differential privacy (NVDP), a framework for building privacy-preserving language models. However, the learned latent representations can drift into regions with high information content, leading to poor privacy guarantees, but also low utility due to numerical instability during training. In this work, we introduce a principled parameter clipping strategy to directly address this issue. Our method is mathematically derived from the objective of minimizing the Rényi Divergence (RD) upper bound, yielding specific, theoretically grounded constraints on the posterior mean, variance, and mixture weight parameters. We apply our technique to an NVIB based model and empirically compare it against an unconstrained baseline. Our findings demonstrate that the clipped model consistently achieves tighter RD bounds, implying stronger privacy, while simultaneously attaining higher performance on several downstream tasks. This work presents a simple yet effective method for improving the privacy-utility trade-off in variational models, making them more robust and practical.

