---
layout: default
title: Scale Where It Matters: Training-Free Localized Scaling for Diffusion Models
---

# Scale Where It Matters: Training-Free Localized Scaling for Diffusion Models
**arXiv**：[2511.19917v1](https://arxiv.org/abs/2511.19917) · [PDF](https://arxiv.org/pdf/2511.19917.pdf)  
**作者**：Qin Ren, Yufei Wang, Lanqing Guo, Wen Zhang, Zhiwen Fan, Chenyu You  

**一句话要点**：提出LoTTS框架以解决扩散模型推理时全图缩放的低效问题

**关键词**：扩散模型, 测试时缩放, 局部优化, 注意力机制, 训练免费方法, 图像生成

## 3 点简述
- 核心问题：现有测试时缩放方法在全图操作，忽略图像质量空间异质性，导致计算浪费和局部缺陷修正不足
- 方法要点：通过对比注意力信号定位缺陷区域，并局部扰动和去噪以保持全局一致性
- 实验或效果：在SD2.1等模型上，LoTTS提升局部质量和全局保真度，同时GPU成本降低2-4倍

## 摘要（原文）

> Diffusion models have become the dominant paradigm in text-to-image generation, and test-time scaling (TTS) further improves quality by allocating more computation during inference. However, existing TTS methods operate at the full-image level, overlooking the fact that image quality is often spatially heterogeneous. This leads to unnecessary computation on already satisfactory regions and insufficient correction of localized defects. In this paper, we explore a new direction - Localized TTS - that adaptively resamples defective regions while preserving high-quality regions, thereby substantially reducing the search space. This paradigm poses two central challenges: accurately localizing defects and maintaining global consistency. We propose LoTTS, the first fully training-free framework for localized TTS. For defect localization, LoTTS contrasts cross- and self-attention signals under quality-aware prompts (e.g., high-quality vs. low-quality) to identify defective regions, and then refines them into coherent masks. For consistency, LoTTS perturbs only defective regions and denoises them locally, ensuring that corrections remain confined while the rest of the image remains undisturbed. Extensive experiments on SD2.1, SDXL, and FLUX demonstrate that LoTTS achieves state-of-the-art performance: it consistently improves both local quality and global fidelity, while reducing GPU cost by 2-4x compared to Best-of-N sampling. These findings establish localized TTS as a promising new direction for scaling diffusion models at inference time.

