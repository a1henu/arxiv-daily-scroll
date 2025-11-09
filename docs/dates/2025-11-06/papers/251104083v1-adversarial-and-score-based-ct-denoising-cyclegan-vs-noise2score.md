---
layout: default
title: Adversarial and Score-Based CT Denoising: CycleGAN vs Noise2Score
---

# Adversarial and Score-Based CT Denoising: CycleGAN vs Noise2Score
**arXiv**：[2511.04083v1](https://arxiv.org/abs/2511.04083) · [PDF](https://arxiv.org/pdf/2511.04083.pdf)  
**作者**：Abu Hanif Muhammad Syarubany  

**一句话要点**：比较CycleGAN与Noise2Score在无配对自监督CT图像去噪中的性能

**关键词**：CT图像去噪, 无配对学习, 自监督学习, CycleGAN, Noise2Score, 图像质量评估

## 3 点简述
- 研究无配对和自监督CT图像去噪问题，评估训练数据高效方法
- 采用CycleGAN残差翻译器和Noise2Score分数匹配去噪器进行对比
- CycleGAN在PSNR/SSIM上表现最佳，Noise2Score在噪声严重时增益显著

## 摘要（原文）

> We study CT image denoising in the unpaired and self-supervised regimes by
> evaluating two strong, training-data-efficient paradigms: a CycleGAN-based
> residual translator and a Noise2Score (N2S) score-matching denoiser. Under a
> common evaluation protocol, a configuration sweep identifies a simple standard
> U-Net backbone within CycleGAN (lambda_cycle = 30, lambda_iden = 2, ngf = ndf =
> 64) as the most reliable setting; we then train it to convergence with a longer
> schedule. The selected CycleGAN improves the noisy input from 34.66 dB / 0.9234
> SSIM to 38.913 dB / 0.971 SSIM and attains an estimated score of 1.9441 and an
> unseen-set (Kaggle leaderboard) score of 1.9343. Noise2Score, while slightly
> behind in absolute PSNR / SSIM, achieves large gains over very noisy inputs,
> highlighting its utility when clean pairs are unavailable. Overall, CycleGAN
> offers the strongest final image quality, whereas Noise2Score provides a robust
> pair-free alternative with competitive performance. Source code is available at
> https://github.com/hanifsyarubany/CT-Scan-Image-Denoising-using-CycleGAN-and-Noise2Score.

