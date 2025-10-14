---
layout: default
title: ContextGen: Contextual Layout Anchoring for Identity-Consistent Multi-Instance Generation
---

# ContextGen: Contextual Layout Anchoring for Identity-Consistent Multi-Instance Generation
**arXiv**：[2510.11000v1](https://arxiv.org/abs/2510.11000) · [PDF](https://arxiv.org/pdf/2510.11000.pdf)  
**作者**：Ruihang Xu, Dewei Zhou, Fan Ma, Yi Yang  

**一句话要点**：提出ContextGen框架以解决多实例图像生成中的布局控制和身份一致性问题

**关键词**：多实例图像生成, 扩散变换器, 布局控制, 身份一致性, 注意力机制, 数据集构建

## 3 点简述
- 核心问题：扩散模型在多实例生成中难以精确控制对象布局和保持多个不同主体的身份一致性
- 方法要点：引入Contextual Layout Anchoring机制和Identity Consistency Attention机制，结合布局和参考图像指导生成
- 实验或效果：在控制精度、身份保真度和视觉质量上优于现有方法，并构建了IMIG-100K数据集

## 摘要（原文）

> Multi-instance image generation (MIG) remains a significant challenge for
> modern diffusion models due to key limitations in achieving precise control
> over object layout and preserving the identity of multiple distinct subjects.
> To address these limitations, we introduce ContextGen, a novel Diffusion
> Transformer framework for multi-instance generation that is guided by both
> layout and reference images. Our approach integrates two key technical
> contributions: a Contextual Layout Anchoring (CLA) mechanism that incorporates
> the composite layout image into the generation context to robustly anchor the
> objects in their desired positions, and Identity Consistency Attention (ICA),
> an innovative attention mechanism that leverages contextual reference images to
> ensure the identity consistency of multiple instances. Recognizing the lack of
> large-scale, hierarchically-structured datasets for this task, we introduce
> IMIG-100K, the first dataset with detailed layout and identity annotations.
> Extensive experiments demonstrate that ContextGen sets a new state-of-the-art,
> outperforming existing methods in control precision, identity fidelity, and
> overall visual quality.

