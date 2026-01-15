---
layout: default
title: SpikeVAEDiff: Neural Spike-based Natural Visual Scene Reconstruction via VD-VAE and Versatile Diffusion
---

# SpikeVAEDiff: Neural Spike-based Natural Visual Scene Reconstruction via VD-VAE and Versatile Diffusion
**arXiv**：[2601.09213v1](https://arxiv.org/abs/2601.09213) · [PDF](https://arxiv.org/pdf/2601.09213.pdf)  
**作者**：Jialu Li, Taiyan Zhou  

**一句话要点**：提出SpikeVAEDiff框架，结合VD-VAE和Versatile Diffusion从神经尖峰数据重建自然视觉场景

**关键词**：神经尖峰解码, 视觉场景重建, 变分自编码器, 扩散模型, 脑区分析, 高分辨率图像生成

## 3 点简述
- 核心问题：从神经尖峰数据重建高分辨率、语义丰富的自然视觉场景，挑战在于解码神经活动。
- 方法要点：两阶段框架，先由VD-VAE生成低分辨率重建，再通过回归模型映射到CLIP特征，用Versatile Diffusion进行图像到图像精炼。
- 实验或效果：在Allen Visual Coding-Neuropixels数据集上评估，VISI脑区激活最显著，提升重建质量，优于基于fMRI的方法。

## 摘要（原文）

> Reconstructing natural visual scenes from neural activity is a key challenge in neuroscience and computer vision. We present SpikeVAEDiff, a novel two-stage framework that combines a Very Deep Variational Autoencoder (VDVAE) and the Versatile Diffusion model to generate high-resolution and semantically meaningful image reconstructions from neural spike data. In the first stage, VDVAE produces low-resolution preliminary reconstructions by mapping neural spike signals to latent representations. In the second stage, regression models map neural spike signals to CLIP-Vision and CLIP-Text features, enabling Versatile Diffusion to refine the images via image-to-image generation.
>   We evaluate our approach on the Allen Visual Coding-Neuropixels dataset and analyze different brain regions. Our results show that the VISI region exhibits the most prominent activation and plays a key role in reconstruction quality. We present both successful and unsuccessful reconstruction examples, reflecting the challenges of decoding neural activity. Compared with fMRI-based approaches, spike data provides superior temporal and spatial resolution. We further validate the effectiveness of the VDVAE model and conduct ablation studies demonstrating that data from specific brain regions significantly enhances reconstruction performance.

