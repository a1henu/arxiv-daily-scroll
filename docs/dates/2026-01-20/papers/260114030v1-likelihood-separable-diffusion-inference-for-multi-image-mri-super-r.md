---
layout: default
title: Likelihood-Separable Diffusion Inference for Multi-Image MRI Super-Resolution
---

# Likelihood-Separable Diffusion Inference for Multi-Image MRI Super-Resolution
**arXiv**：[2601.14030v1](https://arxiv.org/abs/2601.14030) · [PDF](https://arxiv.org/pdf/2601.14030.pdf)  
**作者**：Samuel W. Remedios, Zhangxing Bian, Shuwen Wei, Aaron Carass, Jerry L. Prince, Blake E. Dewey  

**一句话要点**：提出似然可分离扩散推理方法，用于多图像MRI超分辨率重建

**关键词**：扩散模型, 多图像超分辨率, 磁共振成像, 后验采样, 似然可分离, 各向异性退化

## 3 点简述
- 针对多图像MRI超分辨率问题，扩散模型后验采样通常局限于单图像场景
- 基于DPS似然校正，实现跨独立测量的梯度可分离分解，无需联合算子或模型修改
- 在4×/8×/16×各向异性退化下，多图像方法显著优于单图像超分辨率，实现近各向同性重建

## 摘要（原文）

> Diffusion models are the current state-of-the-art for solving inverse problems in imaging. Their impressive generative capability allows them to approximate sampling from a prior distribution, which alongside a known likelihood function permits posterior sampling without retraining the model. While recent methods have made strides in advancing the accuracy of posterior sampling, the majority focuses on single-image inverse problems. However, for modalities such as magnetic resonance imaging (MRI), it is common to acquire multiple complementary measurements, each low-resolution along a different axis. In this work, we generalize common diffusion-based inverse single-image problem solvers for multi-image super-resolution (MISR) MRI. We show that the DPS likelihood correction allows an exactly-separable gradient decomposition across independently acquired measurements, enabling MISR without constructing a joint operator, modifying the diffusion model, or increasing network function evaluations. We derive MISR versions of DPS, DMAP, DPPS, and diffusion-based PnP/ADMM, and demonstrate substantial gains over SISR across $4\times/8\times/16\times$ anisotropic degradations. Our results achieve state-of-the-art super-resolution of anisotropic MRI volumes and, critically, enable reconstruction of near-isotropic anatomy from routine 2D multi-slice acquisitions, which are otherwise highly degraded in orthogonal views.

