---
layout: default
title: BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model
---

# BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model
**arXiv**：[2602.22596v1](https://arxiv.org/abs/2602.22596) · [PDF](https://arxiv.org/pdf/2602.22596.pdf)  
**作者**：Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz  

**一句话要点**：提出BetterScene方法，通过表示对齐增强稀疏照片下的新视角合成质量

**关键词**：新视角合成, 扩散模型, 3D高斯泼溅, 表示对齐, 稀疏视图

## 3 点简述
- 核心问题：现有方法依赖预训练扩散先验，仅微调UNet模块，导致细节不一致和伪影
- 方法要点：引入时间等变正则化和视觉基础模型对齐表示，优化VAE模块以提升表示一致性
- 实验或效果：在DL3DV-10K数据集上评估，优于先进方法，生成连续、无伪影、一致的新视角

## 摘要（原文）

> We present BetterScene, an approach to enhance novel view synthesis (NVS) quality for diverse real-world scenes using extremely sparse, unconstrained photos. BetterScene leverages the production-ready Stable Video Diffusion (SVD) model pretrained on billions of frames as a strong backbone, aiming to mitigate artifacts and recover view-consistent details at inference time. Conventional methods have developed similar diffusion-based solutions to address these challenges of novel view synthesis. Despite significant improvements, these methods typically rely on off-the-shelf pretrained diffusion priors and fine-tune only the UNet module while keeping other components frozen, which still leads to inconsistent details and artifacts even when incorporating geometry-aware regularizations like depth or semantic conditions. To address this, we investigate the latent space of the diffusion model and introduce two components: (1) temporal equivariance regularization and (2) vision foundation model-aligned representation, both applied to the variational autoencoder (VAE) module within the SVD pipeline. BetterScene integrates a feed-forward 3D Gaussian Splatting (3DGS) model to render features as inputs for the SVD enhancer and generate continuous, artifact-free, consistent novel views. We evaluate on the challenging DL3DV-10K dataset and demonstrate superior performance compared to state-of-the-art methods.

