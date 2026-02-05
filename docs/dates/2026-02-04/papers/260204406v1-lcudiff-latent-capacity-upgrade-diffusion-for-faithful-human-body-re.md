---
layout: default
title: LCUDiff: Latent Capacity Upgrade Diffusion for Faithful Human Body Restoration
---

# LCUDiff: Latent Capacity Upgrade Diffusion for Faithful Human Body Restoration
**arXiv**：[2602.04406v1](https://arxiv.org/abs/2602.04406) · [PDF](https://arxiv.org/pdf/2602.04406.pdf)  
**作者**：Jue Gong, Zihan Zhou, Jingkai Wang, Shu Li, Libo Liu, Jianliang Lan, Yulun Zhang  

**一句话要点**：提出LCUDiff框架，通过升级潜在空间至16通道以提升人体图像修复的保真度。

**关键词**：人体图像修复, 潜在扩散模型, 变分自编码器, 通道分裂蒸馏, 先验保持适应, 一步修复

## 3 点简述
- 现有方法在人体图像修复中保真度不足，变分自编码器成为瓶颈。
- LCUDiff采用通道分裂蒸馏和先验保持适应，升级潜在扩散模型至16通道。
- 实验显示在轻度退化下，该方法保真度高、伪影少，保持一步效率。

## 摘要（原文）

> Existing methods for restoring degraded human-centric images often struggle with insufficient fidelity, particularly in human body restoration (HBR). Recent diffusion-based restoration methods commonly adapt pre-trained text-to-image diffusion models, where the variational autoencoder (VAE) can significantly bottleneck restoration fidelity. We propose LCUDiff, a stable one-step framework that upgrades a pre-trained latent diffusion model from the 4-channel latent space to the 16-channel latent space. For VAE fine-tuning, channel splitting distillation (CSD) is used to keep the first four channels aligned with pre-trained priors while allocating the additional channels to effectively encode high-frequency details. We further design prior-preserving adaptation (PPA) to smoothly bridge the mismatch between 4-channel diffusion backbones and the higher-dimensional 16-channel latent. In addition, we propose a decoder router (DeR) for per-sample decoder routing using restoration-quality score annotations, which improves visual quality across diverse conditions. Experiments on synthetic and real-world datasets show competitive results with higher fidelity and fewer artifacts under mild degradations, while preserving one-step efficiency. The code and model will be at https://github.com/gobunu/LCUDiff.

