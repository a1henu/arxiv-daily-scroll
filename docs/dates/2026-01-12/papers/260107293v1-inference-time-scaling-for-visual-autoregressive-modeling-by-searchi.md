---
layout: default
title: Inference-Time Scaling for Visual AutoRegressive modeling by Searching Representative Samples
---

# Inference-Time Scaling for Visual AutoRegressive modeling by Searching Representative Samples
**arXiv**：[2601.07293v1](https://arxiv.org/abs/2601.07293) · [PDF](https://arxiv.org/pdf/2601.07293.pdf)  
**作者**：Weidong Tang, Xinyan Wan, Siyu Li, Xiumei Wang  

**一句话要点**：提出VAR-Scaling框架，通过搜索代表性样本实现视觉自回归模型的推理时缩放。

**关键词**：视觉自回归建模, 推理时缩放, 核密度估计, 混合采样策略, 离散潜在空间

## 3 点简述
- 核心问题：离散潜在空间阻碍VQ视觉自回归模型的推理时缩放路径搜索。
- 方法要点：使用核密度估计映射采样空间，结合Top-k和Random-k混合采样策略优化样本质量。
- 实验或效果：在类条件和文本到图像任务中显著提升推理过程质量。

## 摘要（原文）

> While inference-time scaling has significantly enhanced generative quality in large language and diffusion models, its application to vector-quantized (VQ) visual autoregressive modeling (VAR) remains unexplored. We introduce VAR-Scaling, the first general framework for inference-time scaling in VAR, addressing the critical challenge of discrete latent spaces that prohibit continuous path search. We find that VAR scales exhibit two distinct pattern types: general patterns and specific patterns, where later-stage specific patterns conditionally optimize early-stage general patterns. To overcome the discrete latent space barrier in VQ models, we map sampling spaces to quasi-continuous feature spaces via kernel density estimation (KDE), where high-density samples approximate stable, high-quality solutions. This transformation enables effective navigation of sampling distributions. We propose a density-adaptive hybrid sampling strategy: Top-k sampling focuses on high-density regions to preserve quality near distribution modes, while Random-k sampling explores low-density areas to maintain diversity and prevent premature convergence. Consequently, VAR-Scaling optimizes sample fidelity at critical scales to enhance output quality. Experiments in class-conditional and text-to-image evaluations demonstrate significant improvements in inference process. The code is available at https://github.com/WD7ang/VAR-Scaling.

