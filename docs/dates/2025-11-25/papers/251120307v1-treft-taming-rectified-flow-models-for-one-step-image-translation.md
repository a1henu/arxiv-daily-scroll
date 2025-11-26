---
layout: default
title: TReFT: Taming Rectified Flow Models For One-Step Image Translation
---

# TReFT: Taming Rectified Flow Models For One-Step Image Translation
**arXiv**：[2511.20307v1](https://arxiv.org/abs/2511.20307) · [PDF](https://arxiv.org/pdf/2511.20307.pdf)  
**作者**：Shengqian Li, Ming Gao, Yi Liu, Zuzeng Lin, Feng Wang, Feng Dai  

**一句话要点**：提出TReFT方法以解决Rectified Flow模型在一步图像翻译中的收敛问题

**关键词**：图像翻译, Rectified Flow模型, 一步推理, 对抗训练, 实时应用

## 3 点简述
- Rectified Flow模型在图像翻译中依赖多步去噪，阻碍实时应用
- TReFT直接使用预训练模型的预测速度作为输出，实现一步推理
- 在SD3.5和FLUX等模型上微调，性能媲美SOTA且支持实时推理

## 摘要（原文）

> Rectified Flow (RF) models have advanced high-quality image and video synthesis via optimal transport theory. However, when applied to image-to-image translation, they still depend on costly multi-step denoising, hindering real-time applications. Although the recent adversarial training paradigm, CycleGAN-Turbo, works in pretrained diffusion models for one-step image translation, we find that directly applying it to RF models leads to severe convergence issues. In this paper, we analyze these challenges and propose TReFT, a novel method to Tame Rectified Flow models for one-step image Translation. Unlike previous works, TReFT directly uses the velocity predicted by pretrained DiT or UNet as output-a simple yet effective design that tackles the convergence issues under adversarial training with one-step inference. This design is mainly motivated by a novel observation that, near the end of the denoising process, the velocity predicted by pretrained RF models converges to the vector from origin to the final clean image, a property we further justify through theoretical analysis. When applying TReFT to large pretrained RF models such as SD3.5 and FLUX, we introduce memory-efficient latent cycle-consistency and identity losses during training, as well as lightweight architectural simplifications for faster inference. Pretrained RF models finetuned with TReFT achieve performance comparable to sota methods across multiple image translation datasets while enabling real-time inference.

