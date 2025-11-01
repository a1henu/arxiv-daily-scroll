---
layout: default
title: Masked Diffusion Captioning for Visual Feature Learning
---

# Masked Diffusion Captioning for Visual Feature Learning
**arXiv**：[2510.26799v1](https://arxiv.org/abs/2510.26799) · [PDF](https://arxiv.org/pdf/2510.26799.pdf)  
**作者**：Chao Feng, Zihao Wei, Andrew Owens  

**一句话要点**：提出掩码扩散字幕方法以学习视觉特征，用于下游视觉任务

**关键词**：掩码扩散字幕, 视觉特征学习, 图像字幕, 扩散模型, 线性探测

## 3 点简述
- 核心问题：如何高效学习视觉特征，减少对辅助目标的依赖
- 方法要点：使用图像条件掩码扩散语言模型，随机掩码文本并重构原文本
- 实验或效果：线性探测实验显示特征与自回归和对比方法竞争

## 摘要（原文）

> We learn visual features by captioning images with an image-conditioned
> masked diffusion language model, a formulation we call masked diffusion
> captioning (MDC). During training, text tokens in each image-caption pair are
> masked at a randomly chosen ratio, and a decoder conditioned on visual features
> is trained to reconstruct the original text. After training, the learned visual
> features can be applied to downstream vision tasks. Unlike autoregressive
> captioning, the strength of the visual learning signal in MDC does not depend
> on each token's position in the sequence, reducing the need for auxiliary
> objectives. Linear probing experiments across a variety of academic-scale
> models and datasets show that the learned visual features are competitive with
> those produced by autoregressive and contrastive approaches.

