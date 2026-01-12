---
layout: default
title: Kidney Cancer Detection Using 3D-Based Latent Diffusion Models
---

# Kidney Cancer Detection Using 3D-Based Latent Diffusion Models
**arXiv**：[2601.05852v1](https://arxiv.org/abs/2601.05852) · [PDF](https://arxiv.org/pdf/2601.05852.pdf)  
**作者**：Jen Dusseljee, Sarah de Boer, Alessa Hering  

**一句话要点**：提出基于3D潜在扩散的弱监督方法，用于增强CT中的肾脏异常检测。

**关键词**：3D医学图像分析, 潜在扩散模型, 弱监督学习, 肾脏异常检测, 生成对抗网络, CT图像处理

## 3 点简述
- 核心问题：在仅使用病例级伪标签的弱监督下，从3D腹部CT中检测肾脏异常。
- 方法要点：结合DDPM、DDIM和VQ-GAN，直接在图像体积上操作，避免切片级处理。
- 实验或效果：基准测试显示，该方法虽未超越全监督基线，但验证了3D潜在扩散在弱监督异常检测中的可行性。

## 摘要（原文）

> In this work, we present a novel latent diffusion-based pipeline for 3D kidney anomaly detection on contrast-enhanced abdominal CT. The method combines Denoising Diffusion Probabilistic Models (DDPMs), Denoising Diffusion Implicit Models (DDIMs), and Vector-Quantized Generative Adversarial Networks (VQ-GANs). Unlike prior slice-wise approaches, our method operates directly on an image volume and leverages weak supervision with only case-level pseudo-labels. We benchmark our approach against state-of-the-art supervised segmentation and detection models. This study demonstrates the feasibility and promise of 3D latent diffusion for weakly supervised anomaly detection. While the current results do not yet match supervised baselines, they reveal key directions for improving reconstruction fidelity and lesion localization. Our findings provide an important step toward annotation-efficient, generative modeling of complex abdominal anatomy.

