---
layout: default
title: Blind Deconvolution in Astronomy: How Does a Standalone U-Net Perform?
---

# Blind Deconvolution in Astronomy: How Does a Standalone U-Net Perform?
**arXiv**：[2601.08666v1](https://arxiv.org/abs/2601.08666) · [PDF](https://arxiv.org/pdf/2601.08666.pdf)  
**作者**：Jean-Eric Campagne  

**一句话要点**：评估U-Net在天文图像盲去卷积中的独立性能与泛化能力

**关键词**：盲去卷积, U-Net架构, 天文图像处理, 深度学习, 泛化评估

## 3 点简述
- 研究U-Net能否独立完成天文图像盲去卷积，无需点扩散函数或噪声先验知识
- 使用GalSim模拟真实观测数据，训练U-Net模型并评估其性能随训练数据量变化
- U-Net在低信噪比条件下优于经典Tikhonov方法，并展现出良好的泛化能力

## 摘要（原文）

> Aims: This study investigates whether a U-Net architecture can perform standalone end-to-end blind deconvolution of astronomical images without any prior knowledge of the Point Spread Function (PSF) or noise characteristics. Our goal is to evaluate its performance against the number of training images, classical Tikhonov deconvolution and to assess its generalization capability under varying seeing conditions and noise levels.
>   Methods: Realistic astronomical observations are simulated using the GalSim toolkit, incorporating random transformations, PSF convolution (accounting for both optical and atmospheric effects), and Gaussian white noise. A U-Net model is trained using a Mean Square Error (MSE) loss function on datasets of varying sizes, up to 40,000 images of size 48x48 from the COSMOS Real Galaxy Dataset. Performance is evaluated using PSNR, SSIM, and cosine similarity metrics, with the latter employed in a two-model framework to assess solution stability.
>   Results: The U-Net model demonstrates effectiveness in blind deconvolution, with performance improving consistently as the training dataset size increases, saturating beyond 5,000 images. Cosine similarity analysis reveals convergence between independently trained models, indicating stable solutions. Remarkably, the U-Net outperforms the oracle-like Tikhonov method in challenging conditions (low PSNR/medium SSIM). The model also generalizes well to unseen seeing and noise conditions, although optimal performance is achieved when training parameters include validation conditions. Experiments on synthetic $C^α$ images further support the hypothesis that the U-Net learns a geometry-adaptive harmonic basis, akin to sparse representations observed in denoising tasks. These results align with recent mathematical insights into its adaptive learning capabilities.

