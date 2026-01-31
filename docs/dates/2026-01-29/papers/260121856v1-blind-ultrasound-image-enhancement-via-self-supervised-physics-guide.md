---
layout: default
title: Blind Ultrasound Image Enhancement via Self-Supervised Physics-Guided Degradation Modeling
---

# Blind Ultrasound Image Enhancement via Self-Supervised Physics-Guided Degradation Modeling
**arXiv**：[2601.21856v1](https://arxiv.org/abs/2601.21856) · [PDF](https://arxiv.org/pdf/2601.21856.pdf)  
**作者**：Shujaat Khan, Syed Muhammad Atif, Jaeyoung Huh, Syed Saad Azhar  

**一句话要点**：提出盲超声图像增强框架，通过自监督物理引导退化建模联合去卷积和去噪。

**关键词**：盲超声图像增强, 自监督学习, 物理引导退化建模, 联合去卷积去噪, Swin卷积U-Net, 非局部低秩去噪

## 3 点简述
- 核心问题：超声图像受乘性斑点、点扩散函数模糊和扫描器/操作者相关伪影影响，缺乏干净目标或已知退化模型。
- 方法要点：使用Swin卷积U-Net，基于物理引导退化模型自监督训练，合成输入通过高斯PSF卷积和噪声注入，目标通过非局部低秩去噪或原始图像获得。
- 实验或效果：在多个数据集上验证，PSNR/SSIM优于现有方法，在强噪声下提升显著，能恢复分辨率并提升分割性能。

## 摘要（原文）

> Ultrasound (US) interpretation is hampered by multiplicative speckle, acquisition blur from the point-spread function (PSF), and scanner- and operator-dependent artifacts. Supervised enhancement methods assume access to clean targets or known degradations; conditions rarely met in practice. We present a blind, self-supervised enhancement framework that jointly deconvolves and denoises B-mode images using a Swin Convolutional U-Net trained with a \emph{physics-guided} degradation model. From each training frame, we extract rotated/cropped patches and synthesize inputs by (i) convolving with a Gaussian PSF surrogate and (ii) injecting noise via either spatial additive Gaussian noise or complex Fourier-domain perturbations that emulate phase/magnitude distortions. For US scans, clean-like targets are obtained via non-local low-rank (NLLR) denoising, removing the need for ground truth; for natural images, the originals serve as targets. Trained and validated on UDIAT~B, JNU-IFM, and XPIE Set-P, and evaluated additionally on a 700-image PSFHS test set, the method achieves the highest PSNR/SSIM across Gaussian and speckle noise levels, with margins that widen under stronger corruption. Relative to MSANN, Restormer, and DnCNN, it typically preserves an extra $\sim$1--4\,dB PSNR and 0.05--0.15 SSIM in heavy Gaussian noise, and $\sim$2--5\,dB PSNR and 0.05--0.20 SSIM under severe speckle. Controlled PSF studies show reduced FWHM and higher peak gradients, evidence of resolution recovery without edge erosion. Used as a plug-and-play preprocessor, it consistently boosts Dice for fetal head and pubic symphysis segmentation. Overall, the approach offers a practical, assumption-light path to robust US enhancement that generalizes across datasets, scanners, and degradation types.

