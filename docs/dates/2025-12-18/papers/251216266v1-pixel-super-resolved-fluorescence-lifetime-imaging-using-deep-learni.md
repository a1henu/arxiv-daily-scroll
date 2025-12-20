---
layout: default
title: Pixel Super-Resolved Fluorescence Lifetime Imaging Using Deep Learning
---

# Pixel Super-Resolved Fluorescence Lifetime Imaging Using Deep Learning
**arXiv**：[2512.16266v1](https://arxiv.org/abs/2512.16266) · [PDF](https://arxiv.org/pdf/2512.16266.pdf)  
**作者**：Paloma Casteleiro Costa, Parnian Ghapandar Kashani, Xuhui Liu, Alexander Chen, Ary Portes, Julien Bec, Laura Marcu, Aydogan Ozcan  

**一句话要点**：提出基于深度学习的像素超分辨率框架FLIM_PSR_k，以提升荧光寿命成像的空间分辨率和速度。

**关键词**：荧光寿命成像, 像素超分辨率, 条件生成对抗网络, 深度学习, 图像重建, 生物医学成像

## 3 点简述
- 核心问题：荧光寿命成像受限于长像素停留时间和低信噪比，导致分辨率与速度权衡严格。
- 方法要点：使用条件生成对抗网络实现多通道像素超分辨率，从大像素数据重建高分辨率图像。
- 实验或效果：在患者肿瘤组织样本上验证，实现5倍超分辨率因子，显著提升图像质量和空间带宽积。

## 摘要（原文）

> Fluorescence lifetime imaging microscopy (FLIM) is a powerful quantitative technique that provides metabolic and molecular contrast, offering strong translational potential for label-free, real-time diagnostics. However, its clinical adoption remains limited by long pixel dwell times and low signal-to-noise ratio (SNR), which impose a stricter resolution-speed trade-off than conventional optical imaging approaches. Here, we introduce FLIM_PSR_k, a deep learning-based multi-channel pixel super-resolution (PSR) framework that reconstructs high-resolution FLIM images from data acquired with up to a 5-fold increased pixel size. The model is trained using the conditional generative adversarial network (cGAN) framework, which, compared to diffusion model-based alternatives, delivers a more robust PSR reconstruction with substantially shorter inference times, a crucial advantage for practical deployment. FLIM_PSR_k not only enables faster image acquisition but can also alleviate SNR limitations in autofluorescence-based FLIM. Blind testing on held-out patient-derived tumor tissue samples demonstrates that FLIM_PSR_k reliably achieves a super-resolution factor of k = 5, resulting in a 25-fold increase in the space-bandwidth product of the output images and revealing fine architectural features lost in lower-resolution inputs, with statistically significant improvements across various image quality metrics. By increasing FLIM's effective spatial resolution, FLIM_PSR_k advances lifetime imaging toward faster, higher-resolution, and hardware-flexible implementations compatible with low-numerical-aperture and miniaturized platforms, better positioning FLIM for translational applications.

