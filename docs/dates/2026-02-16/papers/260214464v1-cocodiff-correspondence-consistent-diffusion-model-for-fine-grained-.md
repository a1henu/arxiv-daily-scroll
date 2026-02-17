---
layout: default
title: CoCoDiff: Correspondence-Consistent Diffusion Model for Fine-grained Style Transfer
---

# CoCoDiff: Correspondence-Consistent Diffusion Model for Fine-grained Style Transfer
**arXiv**：[2602.14464v1](https://arxiv.org/abs/2602.14464) · [PDF](https://arxiv.org/pdf/2602.14464.pdf)  
**作者**：Wenbo Nie, Zixiang Li, Renshuai Tao, Bin Wu, Yunchao Wei, Yao Zhao  

**一句话要点**：提出CoCoDiff以解决细粒度风格迁移中的语义对应问题

**关键词**：风格迁移, 扩散模型, 语义对应, 无训练框架, 细粒度处理

## 3 点简述
- 核心问题：现有方法在全局风格迁移中忽视区域和像素级语义对应，导致内容一致性不足。
- 方法要点：利用预训练扩散模型，通过像素级语义对应模块和循环一致性模块实现无训练、低成本的细粒度风格迁移。
- 实验或效果：无需额外训练或标注，在视觉质量和量化指标上达到先进水平，优于依赖额外训练的方法。

## 摘要（原文）

> Transferring visual style between images while preserving semantic correspondence between similar objects remains a central challenge in computer vision. While existing methods have made great strides, most of them operate at global level but overlook region-wise and even pixel-wise semantic correspondence. To address this, we propose CoCoDiff, a novel training-free and low-cost style transfer framework that leverages pretrained latent diffusion models to achieve fine-grained, semantically consistent stylization. We identify that correspondence cues within generative diffusion models are under-explored and that content consistency across semantically matched regions is often neglected. CoCoDiff introduces a pixel-wise semantic correspondence module that mines intermediate diffusion features to construct a dense alignment map between content and style images. Furthermore, a cycle-consistency module then enforces structural and perceptual alignment across iterations, yielding object and region level stylization that preserves geometry and detail. Despite requiring no additional training or supervision, CoCoDiff delivers state-of-the-art visual quality and strong quantitative results, outperforming methods that rely on extra training or annotations.

