---
layout: default
title: CanvasMAR: Improving Masked Autoregressive Video Generation With Canvas
---

# CanvasMAR: Improving Masked Autoregressive Video Generation With Canvas
**arXiv**：[2510.13669v1](https://arxiv.org/abs/2510.13669) · [PDF](https://arxiv.org/pdf/2510.13669.pdf)  
**作者**：Zian Li, Muhan Zhang  

**一句话要点**：提出CanvasMAR以解决视频掩码自回归生成中的慢启动和误差累积问题

**关键词**：视频生成, 掩码自回归模型, 画布机制, 无分类器引导, 误差累积, 慢启动问题

## 3 点简述
- 视频掩码自回归模型存在慢启动和时空误差累积问题
- 引入画布机制提供全局结构，结合组合式无分类器引导和噪声增强
- 在BAIR和Kinetics-600基准上实现高质量视频生成，减少自回归步骤

## 摘要（原文）

> Masked autoregressive models (MAR) have recently emerged as a powerful
> paradigm for image and video generation, combining the flexibility of masked
> modeling with the potential of continuous tokenizer. However, video MAR models
> suffer from two major limitations: the slow-start problem, caused by the lack
> of a structured global prior at early sampling stages, and error accumulation
> across the autoregression in both spatial and temporal dimensions. In this
> work, we propose CanvasMAR, a novel video MAR model that mitigates these issues
> by introducing a canvas mechanism--a blurred, global prediction of the next
> frame, used as the starting point for masked generation. The canvas provides
> global structure early in sampling, enabling faster and more coherent frame
> synthesis. Furthermore, we introduce compositional classifier-free guidance
> that jointly enlarges spatial (canvas) and temporal conditioning, and employ
> noise-based canvas augmentation to enhance robustness. Experiments on the BAIR
> and Kinetics-600 benchmarks demonstrate that CanvasMAR produces high-quality
> videos with fewer autoregressive steps. Our approach achieves remarkable
> performance among autoregressive models on Kinetics-600 dataset and rivals
> diffusion-based methods.

