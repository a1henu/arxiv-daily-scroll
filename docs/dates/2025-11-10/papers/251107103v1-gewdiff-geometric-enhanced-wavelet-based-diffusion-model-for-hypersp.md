---
layout: default
title: GEWDiff: Geometric Enhanced Wavelet-based Diffusion Model for Hyperspectral Image Super-resolution
---

# GEWDiff: Geometric Enhanced Wavelet-based Diffusion Model for Hyperspectral Image Super-resolution
**arXiv**：[2511.07103v1](https://arxiv.org/abs/2511.07103) · [PDF](https://arxiv.org/pdf/2511.07103.pdf)  
**作者**：Sirui Wang, Jiang He, Natàlia Blasco Andreo, Xiao Xiang Zhu  

**一句话要点**：提出GEWDiff以解决高光谱图像超分辨率中的内存和几何结构问题

**关键词**：高光谱图像超分辨率, 扩散模型, 小波变换, 几何增强, 潜在空间压缩, 多级损失函数

## 3 点简述
- 高光谱图像高维内存密集，且生成模型缺乏对几何结构的理解
- 使用小波编码器和几何增强扩散过程，在潜在空间高效压缩并保持特征
- 实验显示在保真度、光谱精度和视觉真实感方面达到先进水平

## 摘要（原文）

> Improving the quality of hyperspectral images (HSIs), such as through
> super-resolution, is a crucial research area. However, generative modeling for
> HSIs presents several challenges. Due to their high spectral dimensionality,
> HSIs are too memory-intensive for direct input into conventional diffusion
> models. Furthermore, general generative models lack an understanding of the
> topological and geometric structures of ground objects in remote sensing
> imagery. In addition, most diffusion models optimize loss functions at the
> noise level, leading to a non-intuitive convergence behavior and suboptimal
> generation quality for complex data. To address these challenges, we propose a
> Geometric Enhanced Wavelet-based Diffusion Model (GEWDiff), a novel framework
> for reconstructing hyperspectral images at 4-times super-resolution. A
> wavelet-based encoder-decoder is introduced that efficiently compresses HSIs
> into a latent space while preserving spectral-spatial information. To avoid
> distortion during generation, we incorporate a geometry-enhanced diffusion
> process that preserves the geometric features. Furthermore, a multi-level loss
> function was designed to guide the diffusion process, promoting stable
> convergence and improved reconstruction fidelity. Our model demonstrated
> state-of-the-art results across multiple dimensions, including fidelity,
> spectral accuracy, visual realism, and clarity.

