---
layout: default
title: Align-cDAE: Alzheimer's Disease Progression Modeling with Attention-Aligned Conditional Diffusion Auto-Encoder
---

# Align-cDAE: Alzheimer's Disease Progression Modeling with Attention-Aligned Conditional Diffusion Auto-Encoder
**arXiv**：[2603.01552v1](https://arxiv.org/abs/2603.01552) · [PDF](https://arxiv.org/pdf/2603.01552.pdf)  
**作者**：Ayantika Das, Keerthi Ram, Mohanasankar Sivaprakasam  

**一句话要点**：提出Align-cDAE以解决阿尔茨海默病进展建模中多模态对齐与潜在空间结构化不足的问题

**关键词**：阿尔茨海默病进展建模, 条件扩散自编码器, 多模态对齐, 潜在空间结构化, 生成式人工智能, 神经影像分析

## 3 点简述
- 现有扩散模型未显式对齐非成像条件与图像特征，导致生成图像中进展相关区域调制不精确
- 引入注意力对齐目标函数，强制模型聚焦于进展相关变化区域，提升多模态信息整合
- 设计结构化潜在空间，分离进展条件与个体身份信息，实现更可控的解剖学精确图像生成

## 摘要（原文）

> Generative AI framework-based modeling and prediction of longitudinal human brain images offer an efficient mechanism to track neurodegenerative progression, essential for the assessment of diseases like Alzheimer's. Among the existing generative approaches, recent diffusion-based models have emerged as an effective alternative to generate disease progression images. Incorporating multi-modal and non-imaging attributes as conditional information into diffusion frameworks has been shown to improve controllability during such generations. However, existing methods do not explicitly ensure that information from non-imaging conditioning modalities is meaningfully aligned with image features to introduce desirable changes in the generated images, such as modulation of progression-specific regions. Further, more precise control over the generation process can be achieved by introducing progression-relevant structure into the internal representations of the model, lacking in the existing approaches. To address these limitations, we propose a diffusion autoencoder-based framework for disease progression modeling that explicitly enforces alignment between different modalities. The alignment is enforced by introducing an explicit objective function that enables the model to focus on the regions exhibiting progression-related changes. Further, we devise a mechanism to better structure the latent representational space of the diffusion auto-encoding framework. Specifically, we assign separate latent subspaces for integrating progression-related conditions and retaining subject-specific identity information, allowing better-controlled image generation. These results demonstrate that enforcing alignment and better structuring of the latent representational space of diffusion auto-encoding framework leads to more anatomically precise modeling of Alzheimer's disease progression.

