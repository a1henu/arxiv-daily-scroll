---
layout: default
title: Zero-shot Synthetic Video Realism Enhancement via Structure-aware Denoising
---

# Zero-shot Synthetic Video Realism Enhancement via Structure-aware Denoising
**arXiv**：[2511.14719v1](https://arxiv.org/abs/2511.14719) · [PDF](https://arxiv.org/pdf/2511.14719.pdf)  
**作者**：Yifan Wang, Liya Ji, Zhanghan Ke, Harry Yang, Ser-Nam Lim, Qifeng Chen  

**一句话要点**：提出零样本结构感知去噪方法以增强合成视频真实感

**关键词**：合成视频增强, 零样本学习, 结构感知去噪, 扩散模型, 视频真实感

## 3 点简述
- 核心问题：合成视频缺乏真实感，需在零样本下提升视觉质量。
- 方法要点：基于扩散模型，利用深度、语义和边缘图引导去噪过程。
- 实验效果：在结构一致性和真实感方面优于现有基线方法。

## 摘要（原文）

> We propose an approach to enhancing synthetic video realism, which can re-render synthetic videos from a simulator in photorealistic fashion. Our realism enhancement approach is a zero-shot framework that focuses on preserving the multi-level structures from synthetic videos into the enhanced one in both spatial and temporal domains, built upon a diffusion video foundational model without further fine-tuning. Specifically, we incorporate an effective modification to have the generation/denoising process conditioned on estimated structure-aware information from the synthetic video, such as depth maps, semantic maps, and edge maps, by an auxiliary model, rather than extracting the information from a simulator. This guidance ensures that the enhanced videos are consistent with the original synthetic video at both the structural and semantic levels. Our approach is a simple yet general and powerful approach to enhancing synthetic video realism: we show that our approach outperforms existing baselines in structural consistency with the original video while maintaining state-of-the-art photorealism quality in our experiments.

