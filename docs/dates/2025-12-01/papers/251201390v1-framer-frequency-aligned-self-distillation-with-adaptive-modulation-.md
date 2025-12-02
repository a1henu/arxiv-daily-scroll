---
layout: default
title: FRAMER: Frequency-Aligned Self-Distillation with Adaptive Modulation Leveraging Diffusion Priors for Real-World Image Super-Resolution
---

# FRAMER: Frequency-Aligned Self-Distillation with Adaptive Modulation Leveraging Diffusion Priors for Real-World Image Super-Resolution
**arXiv**：[2512.01390v1](https://arxiv.org/abs/2512.01390) · [PDF](https://arxiv.org/pdf/2512.01390.pdf)  
**作者**：Seungho Choi, Jeahun Sung, Jihyong Oh  

**一句话要点**：提出FRAMER训练方案，利用扩散先验解决真实图像超分辨率中高频细节重建不足的问题。

**关键词**：真实图像超分辨率, 扩散模型, 自蒸馏, 频率对齐, 自适应调制, 对比学习

## 3 点简述
- 核心问题：扩散模型在真实图像超分辨率中因低频偏好和层次结构导致高频细节重建不足。
- 方法要点：通过频率对齐自蒸馏和自适应调制，利用最终层特征指导中间层，分解为低频/高频带进行对比损失优化。
- 实验或效果：在U-Net和DiT骨干上提升PSNR/SSIM和感知指标，消融实验验证最终层教师和随机层负样本的有效性。

## 摘要（原文）

> Real-image super-resolution (Real-ISR) seeks to recover HR images from LR inputs with mixed, unknown degradations. While diffusion models surpass GANs in perceptual quality, they under-reconstruct high-frequency (HF) details due to a low-frequency (LF) bias and a depth-wise "low-first, high-later" hierarchy. We introduce FRAMER, a plug-and-play training scheme that exploits diffusion priors without changing the backbone or inference. At each denoising step, the final-layer feature map teaches all intermediate layers. Teacher and student feature maps are decomposed into LF/HF bands via FFT masks to align supervision with the model's internal frequency hierarchy. For LF, an Intra Contrastive Loss (IntraCL) stabilizes globally shared structure. For HF, an Inter Contrastive Loss (InterCL) sharpens instance-specific details using random-layer and in-batch negatives. Two adaptive modulators, Frequency-based Adaptive Weight (FAW) and Frequency-based Alignment Modulation (FAM), reweight per-layer LF/HF signals and gate distillation by current similarity. Across U-Net and DiT backbones (e.g., Stable Diffusion 2, 3), FRAMER consistently improves PSNR/SSIM and perceptual metrics (LPIPS, NIQE, MANIQA, MUSIQ). Ablations validate the final-layer teacher and random-layer negatives.

