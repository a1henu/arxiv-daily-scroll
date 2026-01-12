---
layout: default
title: Towards Generalized Multi-Image Editing for Unified Multimodal Models
---

# Towards Generalized Multi-Image Editing for Unified Multimodal Models
**arXiv**：[2601.05572v1](https://arxiv.org/abs/2601.05572) · [PDF](https://arxiv.org/pdf/2601.05572.pdf)  
**作者**：Pengcheng Xu, Peng Tang, Donghao Luo, Xiaobin Hu, Weichu Cui, Qingdong He, Zhennan Chen, Jiangning Zhang, Charles Ling, Boyu Wang  

**一句话要点**：提出可扩展多图像编辑框架以提升统一多模态模型在视觉一致性和泛化能力上的表现

**关键词**：多图像编辑, 统一多模态模型, 潜在分离器, 正弦索引编码, 视觉一致性, 泛化能力

## 3 点简述
- 核心问题：统一多模态模型在多图像编辑中难以保持视觉一致性和区分图像细节
- 方法要点：引入可学习潜在分离器和正弦索引编码以明确区分图像身份并支持可变输入数量
- 实验或效果：通过高保真基准测试验证了在语义一致性、视觉保真度和跨图像集成方面的改进

## 摘要（原文）

> Unified Multimodal Models (UMMs) integrate multimodal understanding and generation, yet they are limited to maintaining visual consistency and disambiguating visual cues when referencing details across multiple input images. In this work, we propose a scalable multi-image editing framework for UMMs that explicitly distinguishes image identities and generalizes to variable input counts. Algorithmically, we introduce two innovations: 1) The learnable latent separators explicitly differentiate each reference image in the latent space, enabling accurate and disentangled conditioning. 2) The sinusoidal index encoding assigns visual tokens from the same image a continuous sinusoidal index embedding, which provides explicit image identity while allowing generalization and extrapolation on a variable number of inputs. To facilitate training and evaluation, we establish a high-fidelity benchmark using an inverse dataset construction methodology to guarantee artifact-free, achievable outputs. Experiments show clear improvements in semantic consistency, visual fidelity, and cross-image integration over prior baselines on diverse multi-image editing tasks, validating our advantages on consistency and generalization ability.

