---
layout: default
title: The Pictorial Cortex: Zero-Shot Cross-Subject fMRI-to-Image Reconstruction via Compositional Latent Modeling
---

# The Pictorial Cortex: Zero-Shot Cross-Subject fMRI-to-Image Reconstruction via Compositional Latent Modeling
**arXiv**：[2601.15071v1](https://arxiv.org/abs/2601.15071) · [PDF](https://arxiv.org/pdf/2601.15071.pdf)  
**作者**：Jingyang Huo, Yikai Wang, Yanwei Fu, Jianfeng Feng  

**一句话要点**：提出PictorialCortex，通过组合潜在建模实现零样本跨被试fMRI到图像重建

**关键词**：fMRI到图像重建, 零样本学习, 组合潜在建模, 跨被试解码, 扩散模型, 神经影像数据集

## 3 点简述
- 核心问题：fMRI响应因个体差异导致跨被试图像重建困难，需零样本方法。
- 方法要点：使用组合潜在空间建模fMRI活动，分解主体、数据集和试验相关变异性。
- 实验或效果：在UniCortex-fMRI数据集上验证，提升零样本跨被试视觉重建性能。

## 摘要（原文）

> Decoding visual experiences from human brain activity remains a central challenge at the intersection of neuroscience, neuroimaging, and artificial intelligence. A critical obstacle is the inherent variability of cortical responses: neural activity elicited by the same visual stimulus differs across individuals and trials due to anatomical, functional, cognitive, and experimental factors, making fMRI-to-image reconstruction non-injective. In this paper, we tackle a challenging yet practically meaningful problem: zero-shot cross-subject fMRI-to-image reconstruction, where the visual experience of a previously unseen individual must be reconstructed without subject-specific training. To enable principled evaluation, we present a unified cortical-surface dataset -- UniCortex-fMRI, assembled from multiple visual-stimulus fMRI datasets to provide broad coverage of subjects and stimuli. Our UniCortex-fMRI is particularly processed by standardized data formats to make it possible to explore this possibility in the zero-shot scenario of cross-subject fMRI-to-image reconstruction. To tackle the modeling challenge, we propose PictorialCortex, which models fMRI activity using a compositional latent formulation that structures stimulus-driven representations under subject-, dataset-, and trial-related variability. PictorialCortex operates in a universal cortical latent space and implements this formulation through a latent factorization-composition module, reinforced by paired factorization and re-factorizing consistency regularization. During inference, surrogate latents synthesized under multiple seen-subject conditions are aggregated to guide diffusion-based image synthesis for unseen subjects. Extensive experiments show that PictorialCortex improves zero-shot cross-subject visual reconstruction, highlighting the benefits of compositional latent modeling and multi-dataset training.

