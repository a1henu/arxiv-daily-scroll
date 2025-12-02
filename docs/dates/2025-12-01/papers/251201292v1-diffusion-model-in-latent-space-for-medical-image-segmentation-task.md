---
layout: default
title: Diffusion Model in Latent Space for Medical Image Segmentation Task
---

# Diffusion Model in Latent Space for Medical Image Segmentation Task
**arXiv**：[2512.01292v1](https://arxiv.org/abs/2512.01292) · [PDF](https://arxiv.org/pdf/2512.01292.pdf)  
**作者**：Huynh Trinh Ngoc, Toan Nguyen Hai, Ba Luong Son, Long Tran Quoc  

**一句话要点**：提出MedSegLatDiff，结合VAE与潜在扩散模型以高效生成医学图像分割的多样掩码。

**关键词**：医学图像分割, 潜在扩散模型, 变分自编码器, 不确定性建模, 置信度图, 小结构保留

## 3 点简述
- 医学图像分割需处理不确定性，传统方法仅输出单一掩码，无法模拟多医生协作。
- 方法使用VAE压缩输入至潜在空间，结合扩散模型生成多样分割，并改进损失函数以保留微小结构。
- 在皮肤病变、息肉和肺结节数据集上评估，达到先进性能，同时提供置信度图增强可解释性。

## 摘要（原文）

> Medical image segmentation is crucial for clinical diagnosis and treatment planning. Traditional methods typically produce a single segmentation mask, failing to capture inherent uncertainty. Recent generative models enable the creation of multiple plausible masks per image, mimicking the collaborative interpretation of several clinicians. However, these approaches remain computationally heavy. We propose MedSegLatDiff, a diffusion based framework that combines a variational autoencoder (VAE) with a latent diffusion model for efficient medical image segmentation. The VAE compresses the input into a low dimensional latent space, reducing noise and accelerating training, while the diffusion process operates directly in this compact representation. We further replace the conventional MSE loss with weighted cross entropy in the VAE mask reconstruction path to better preserve tiny structures such as small nodules. MedSegLatDiff is evaluated on ISIC-2018 (skin lesions), CVC-Clinic (polyps), and LIDC-IDRI (lung nodules). It achieves state of the art or highly competitive Dice and IoU scores while simultaneously generating diverse segmentation hypotheses and confidence maps. This provides enhanced interpretability and reliability compared to deterministic baselines, making the model particularly suitable for clinical deployment.

