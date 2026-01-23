---
layout: default
title: ProGiDiff: Prompt-Guided Diffusion-Based Medical Image Segmentation
---

# ProGiDiff: Prompt-Guided Diffusion-Based Medical Image Segmentation
**arXiv**：[2601.16060v1](https://arxiv.org/abs/2601.16060) · [PDF](https://arxiv.org/pdf/2601.16060.pdf)  
**作者**：Yuan Lin, Murong Xu, Marc Hölle, Chinmay Prabhakar, Andreas Maier, Vasileios Belagiannis, Bjoern Menze, Suprosanna Shit  

**一句话要点**：提出ProGiDiff框架，利用预训练扩散模型和提示引导实现医学图像分割

**关键词**：医学图像分割, 扩散模型, 提示引导, 多类分割, 跨模态适应

## 3 点简述
- 现有医学图像分割方法多为确定性，缺乏多提案估计和自然语言提示交互能力
- 采用ControlNet风格条件机制，结合自定义编码器，引导扩散模型输出分割掩码
- 在CT器官分割实验中表现优异，支持多类分割和跨模态少样本适应

## 摘要（原文）

> Widely adopted medical image segmentation methods, although efficient, are primarily deterministic and remain poorly amenable to natural language prompts. Thus, they lack the capability to estimate multiple proposals, human interaction, and cross-modality adaptation. Recently, text-to-image diffusion models have shown potential to bridge the gap. However, training them from scratch requires a large dataset-a limitation for medical image segmentation. Furthermore, they are often limited to binary segmentation and cannot be conditioned on a natural language prompt. To this end, we propose a novel framework called ProGiDiff that leverages existing image generation models for medical image segmentation purposes. Specifically, we propose a ControlNet-style conditioning mechanism with a custom encoder, suitable for image conditioning, to steer a pre-trained diffusion model to output segmentation masks. It naturally extends to a multi-class setting simply by prompting the target organ. Our experiment on organ segmentation from CT images demonstrates strong performance compared to previous methods and could greatly benefit from an expert-in-the-loop setting to leverage multiple proposals. Importantly, we demonstrate that the learned conditioning mechanism can be easily transferred through low-rank, few-shot adaptation to segment MR images.

