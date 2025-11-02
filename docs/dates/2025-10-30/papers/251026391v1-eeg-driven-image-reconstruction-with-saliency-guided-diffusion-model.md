---
layout: default
title: EEG-Driven Image Reconstruction with Saliency-Guided Diffusion Models
---

# EEG-Driven Image Reconstruction with Saliency-Guided Diffusion Models
**arXiv**：[2510.26391v1](https://arxiv.org/abs/2510.26391) · [PDF](https://arxiv.org/pdf/2510.26391.pdf)  
**作者**：Igor Abramov, Ilya Makarov  

**一句话要点**：提出双条件框架结合EEG嵌入与空间显著图，以提升EEG驱动图像重建的保真度和语义一致性。

**关键词**：EEG图像重建, 扩散模型, 空间显著图, 神经解码, 低秩适应

## 3 点简述
- 现有EEG驱动图像重建方法忽视空间注意机制，导致保真度和语义一致性受限。
- 采用ATM提取EEG特征，LoRA微调Stable Diffusion 2.1，并集成ControlNet分支进行空间控制。
- 在THINGS-EEG数据集上评估，显著改善图像特征质量，并与人类视觉注意高度对齐。

## 摘要（原文）

> Existing EEG-driven image reconstruction methods often overlook spatial
> attention mechanisms, limiting fidelity and semantic coherence. To address
> this, we propose a dual-conditioning framework that combines EEG embeddings
> with spatial saliency maps to enhance image generation. Our approach leverages
> the Adaptive Thinking Mapper (ATM) for EEG feature extraction and fine-tunes
> Stable Diffusion 2.1 via Low-Rank Adaptation (LoRA) to align neural signals
> with visual semantics, while a ControlNet branch conditions generation on
> saliency maps for spatial control. Evaluated on THINGS-EEG, our method achieves
> a significant improvement in the quality of low- and high-level image features
> over existing approaches. Simultaneously, strongly aligning with human visual
> attention. The results demonstrate that attentional priors resolve EEG
> ambiguities, enabling high-fidelity reconstructions with applications in
> medical diagnostics and neuroadaptive interfaces, advancing neural decoding
> through efficient adaptation of pre-trained diffusion models.

