---
layout: default
title: Decoupled MeanFlow: Turning Flow Models into Flow Maps for Accelerated Sampling
---

# Decoupled MeanFlow: Turning Flow Models into Flow Maps for Accelerated Sampling
**arXiv**：[2510.24474v1](https://arxiv.org/abs/2510.24474) · [PDF](https://arxiv.org/pdf/2510.24474.pdf)  
**作者**：Kyungmin Lee, Sihyun Yu, Jinwoo Shin  

**一句话要点**：提出解耦均值流方法，将流模型转换为流图模型以加速采样

**关键词**：流模型, 流图模型, 加速采样, 扩散变换器, 图像生成, 去噪生成模型

## 3 点简述
- 核心问题：去噪生成模型因离散化误差需多步采样，导致速度慢
- 方法要点：通过条件化扩散变换器最终块，无需修改架构即可转换流模型为流图模型
- 实验或效果：在ImageNet上实现1步FID 2.16，4步FID 1.51，推理速度提升超100倍

## 摘要（原文）

> Denoising generative models, such as diffusion and flow-based models, produce
> high-quality samples but require many denoising steps due to discretization
> error. Flow maps, which estimate the average velocity between timesteps,
> mitigate this error and enable faster sampling. However, their training
> typically demands architectural changes that limit compatibility with
> pretrained flow models. We introduce Decoupled MeanFlow, a simple decoding
> strategy that converts flow models into flow map models without architectural
> modifications. Our method conditions the final blocks of diffusion transformers
> on the subsequent timestep, allowing pretrained flow models to be directly
> repurposed as flow maps. Combined with enhanced training techniques, this
> design enables high-quality generation in as few as 1 to 4 steps. Notably, we
> find that training flow models and subsequently converting them is more
> efficient and effective than training flow maps from scratch. On ImageNet
> 256x256 and 512x512, our models attain 1-step FID of 2.16 and 2.12,
> respectively, surpassing prior art by a large margin. Furthermore, we achieve
> FID of 1.51 and 1.68 when increasing the steps to 4, which nearly matches the
> performance of flow models while delivering over 100x faster inference.

