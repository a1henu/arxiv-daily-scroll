---
layout: default
title: Mano: Restriking Manifold Optimization for LLM Training
---

# Mano: Restriking Manifold Optimization for LLM Training
**arXiv**：[2601.23000v1](https://arxiv.org/abs/2601.23000) · [PDF](https://arxiv.org/pdf/2601.23000.pdf)  
**作者**：Yufei Gu, Zeke Xie  

**一句话要点**：提出Mano优化器，通过流形优化解决LLM训练中AdamW和Muon的局限性。

**关键词**：大语言模型训练, 流形优化, 优化器设计, 计算效率, 参数优化

## 3 点简述
- 核心问题：LLM训练成本高，现有优化器如AdamW忽略结构属性，Muon丢失曲率信息。
- 方法要点：创新地将动量投影到参数切空间，并约束在旋转斜流形上，实现高效优化。
- 实验或效果：在LLaMA和Qwen3模型上，Mano性能优于AdamW和Muon，内存和计算复杂度更低。

## 摘要（原文）

> While large language models (LLMs) have emerged as a significant advancement in artificial intelligence, the hardware and computational costs for training LLMs are also significantly burdensome. Among the state-of-the-art optimizers, AdamW relies on diagonal curvature estimates and ignores structural properties, while Muon applies global spectral normalization at the expense of losing curvature information. In this study, we restriked manifold optimization methods for training LLMs, which may address both optimizers' limitations, while conventional manifold optimization methods have been largely overlooked due to the poor performance in large-scale model optimization. By innovatively projecting the momentum onto the tangent space of model parameters and constraining it on a rotational Oblique manifold, we propose a novel, powerful, and efficient optimizer **Mano** that is the first to bridge the performance gap between manifold optimization and modern optimizers. Extensive experiments on the LLaMA and Qwen3 models demonstrate that Mano consistently and significantly outperforms AdamW and Muon even with less memory consumption and computational complexity, respectively, suggesting an expanded Pareto frontier in terms of space and time efficiency.

