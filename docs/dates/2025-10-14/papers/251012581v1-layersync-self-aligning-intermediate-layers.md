---
layout: default
title: LayerSync: Self-aligning Intermediate Layers
---

# LayerSync: Self-aligning Intermediate Layers
**arXiv**：[2510.12581v1](https://arxiv.org/abs/2510.12581) · [PDF](https://arxiv.org/pdf/2510.12581.pdf)  
**作者**：Yasaman Haghighi, Bastien van Delft, Mariam Hassan, Alexandre Alahi  

**一句话要点**：提出LayerSync自对齐中间层方法，提升扩散模型生成质量与训练效率。

**关键词**：扩散模型, 中间层正则化, 自对齐学习, 多模态生成, 训练加速

## 3 点简述
- 核心问题：扩散模型中间层表示质量不均，影响生成质量与训练效率。
- 方法要点：利用语义丰富层指导弱层，无需外部监督，作为即插即用正则项。
- 实验或效果：在图像生成中加速训练8.75倍，提升质量23.6%，适用于多模态。

## 摘要（原文）

> We propose LayerSync, a domain-agnostic approach for improving the generation
> quality and the training efficiency of diffusion models. Prior studies have
> highlighted the connection between the quality of generation and the
> representations learned by diffusion models, showing that external guidance on
> model intermediate representations accelerates training. We reconceptualize
> this paradigm by regularizing diffusion models with their own intermediate
> representations. Building on the observation that representation quality varies
> across diffusion model layers, we show that the most semantically rich
> representations can act as an intrinsic guidance for weaker ones, reducing the
> need for external supervision. Our approach, LayerSync, is a self-sufficient,
> plug-and-play regularizer term with no overhead on diffusion model training and
> generalizes beyond the visual domain to other modalities. LayerSync requires no
> pretrained models nor additional data. We extensively evaluate the method on
> image generation and demonstrate its applicability to other domains such as
> audio, video, and motion generation. We show that it consistently improves the
> generation quality and the training efficiency. For example, we speed up the
> training of flow-based transformer by over 8.75x on ImageNet dataset and
> improved the generation quality by 23.6%. The code is available at
> https://github.com/vita-epfl/LayerSync.

