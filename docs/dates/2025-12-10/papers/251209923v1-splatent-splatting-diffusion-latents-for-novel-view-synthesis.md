---
layout: default
title: Splatent: Splatting Diffusion Latents for Novel View Synthesis
---

# Splatent: Splatting Diffusion Latents for Novel View Synthesis
**arXiv**：[2512.09923v1](https://arxiv.org/abs/2512.09923) · [PDF](https://arxiv.org/pdf/2512.09923.pdf)  
**作者**：Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  

**一句话要点**：提出Splatent框架，通过多视图注意力在VAE潜在空间中增强3D高斯泼溅以实现高质量新视角合成

**关键词**：新视角合成, 3D高斯泼溅, 扩散模型, VAE潜在空间, 多视图注意力, 稀疏视图重建

## 3 点简述
- 核心问题：VAE潜在空间缺乏多视图一致性，导致3D重建中纹理模糊和细节缺失
- 方法要点：在VAE潜在空间中对3D高斯泼溅进行扩散增强，利用多视图注意力从输入视图恢复细节
- 实验或效果：在多个基准测试中达到最先进水平，与现有前馈框架集成提升细节保留

## 摘要（原文）

> Radiance field representations have recently been explored in the latent space of VAEs that are commonly used by diffusion models. This direction offers efficient rendering and seamless integration with diffusion-based pipelines. However, these methods face a fundamental limitation: The VAE latent space lacks multi-view consistency, leading to blurred textures and missing details during 3D reconstruction. Existing approaches attempt to address this by fine-tuning the VAE, at the cost of reconstruction quality, or by relying on pre-trained diffusion models to recover fine-grained details, at the risk of some hallucinations. We present Splatent, a diffusion-based enhancement framework designed to operate on top of 3D Gaussian Splatting (3DGS) in the latent space of VAEs. Our key insight departs from the conventional 3D-centric view: rather than reconstructing fine-grained details in 3D space, we recover them in 2D from input views through multi-view attention mechanisms. This approach preserves the reconstruction quality of pretrained VAEs while achieving faithful detail recovery. Evaluated across multiple benchmarks, Splatent establishes a new state-of-the-art for VAE latent radiance field reconstruction. We further demonstrate that integrating our method with existing feed-forward frameworks, consistently improves detail preservation, opening new possibilities for high-quality sparse-view 3D reconstruction.

