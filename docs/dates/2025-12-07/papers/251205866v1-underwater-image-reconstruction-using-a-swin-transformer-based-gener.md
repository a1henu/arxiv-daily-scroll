---
layout: default
title: Underwater Image Reconstruction Using a Swin Transformer-Based Generator and PatchGAN Discriminator
---

# Underwater Image Reconstruction Using a Swin Transformer-Based Generator and PatchGAN Discriminator
**arXiv**：[2512.05866v1](https://arxiv.org/abs/2512.05866) · [PDF](https://arxiv.org/pdf/2512.05866.pdf)  
**作者**：Md. Mahbub Hasan Akash, Aria Tasnim Mridula, Sheekar Banerjee, Ishtiak Al Mamoon  

**一句话要点**：提出基于Swin Transformer生成器和PatchGAN判别器的GAN框架以解决水下图像重建问题

**关键词**：水下图像重建, Swin Transformer, 生成对抗网络, PatchGAN判别器, 全局依赖建模, 颜色校正

## 3 点简述
- 核心问题：水下成像因波长依赖吸收和散射导致颜色失真、低对比度和雾霾效应，传统方法受限于局部感受野和全局依赖建模不足
- 方法要点：采用U-Net结构集成Swin Transformer块作为生成器，捕获局部特征和长程依赖，结合PatchGAN判别器进行对抗训练以保留高频细节
- 实验或效果：在EUVP数据集上评估，PSNR达24.76 dB、SSIM达0.89，视觉结果有效恢复颜色平衡、提升对比度和减少雾霾

## 摘要（原文）

> Underwater imaging is essential for marine exploration, environmental monitoring, and infrastructure inspection. However, water causes severe image degradation through wavelength-dependent absorption and scattering, resulting in color distortion, low contrast, and haze effects. Traditional reconstruction methods and convolutional neural network-based approaches often fail to adequately address these challenges due to limited receptive fields and inability to model global dependencies. This paper presented a novel deep learning framework that integrated a Swin Transformer architecture within a generative adversarial network (GAN) for underwater image reconstruction. Our generator employed a U-Net structure with Swin Transformer blocks to capture both local features and long-range dependencies crucial for color correction across entire images. A PatchGAN discriminator provided adversarial training to ensure high-frequency detail preservation. We trained and evaluated our model on the EUVP dataset, which contains paired underwater images of varying quality. Quantitative results demonstrate stateof-the-art performance with PSNR of 24.76 dB and SSIM of 0.89, representing significant improvements over existing methods. Visual results showed effective color balance restoration, contrast improvement, and haze reduction. An ablation study confirms the superiority of our Swin Transformer designed over convolutional alternatives. The proposed method offers robust underwater image reconstruction suitable for various marine applications.

