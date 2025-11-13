---
layout: default
title: WDT-MD: Wavelet Diffusion Transformers for Microaneurysm Detection in Fundus Images
---

# WDT-MD: Wavelet Diffusion Transformers for Microaneurysm Detection in Fundus Images
**arXiv**：[2511.08987v1](https://arxiv.org/abs/2511.08987) · [PDF](https://arxiv.org/pdf/2511.08987.pdf)  
**作者**：Yifei Sun, Yuzhi He, Junhao Jia, Jinhong Wang, Ruiquan Ge, Changmiao Wang, Hongxia Xu  

**一句话要点**：提出WDT-MD框架以解决眼底图像中微动脉瘤检测的挑战

**关键词**：微动脉瘤检测, 扩散模型, 小波分析, Transformer架构, 眼底图像分析, 异常检测

## 3 点简述
- 核心问题：扩散模型在微动脉瘤检测中存在身份映射、高假阳性及正常特征重建不佳问题
- 方法要点：结合噪声编码条件、伪正常模式合成及小波扩散Transformer架构
- 实验或效果：在IDRiD和e-ophtha数据集上优于现有方法，提升像素级和图像级检测性能

## 摘要（原文）

> Microaneurysms (MAs), the earliest pathognomonic signs of Diabetic Retinopathy (DR), present as sub-60 $μm$ lesions in fundus images with highly variable photometric and morphological characteristics, rendering manual screening not only labor-intensive but inherently error-prone. While diffusion-based anomaly detection has emerged as a promising approach for automated MA screening, its clinical application is hindered by three fundamental limitations. First, these models often fall prey to "identity mapping", where they inadvertently replicate the input image. Second, they struggle to distinguish MAs from other anomalies, leading to high false positives. Third, their suboptimal reconstruction of normal features hampers overall performance. To address these challenges, we propose a Wavelet Diffusion Transformer framework for MA Detection (WDT-MD), which features three key innovations: a noise-encoded image conditioning mechanism to avoid "identity mapping" by perturbing image conditions during training; pseudo-normal pattern synthesis via inpainting to introduce pixel-level supervision, enabling discrimination between MAs and other anomalies; and a wavelet diffusion Transformer architecture that combines the global modeling capability of diffusion Transformers with multi-scale wavelet analysis to enhance reconstruction of normal retinal features. Comprehensive experiments on the IDRiD and e-ophtha MA datasets demonstrate that WDT-MD outperforms state-of-the-art methods in both pixel-level and image-level MA detection. This advancement holds significant promise for improving early DR screening.

