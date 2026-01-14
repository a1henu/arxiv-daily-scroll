---
layout: default
title: Translating Light-Sheet Microscopy Images to Virtual H&E Using CycleGAN
---

# Translating Light-Sheet Microscopy Images to Virtual H&E Using CycleGAN
**arXiv**：[2601.08776v1](https://arxiv.org/abs/2601.08776) · [PDF](https://arxiv.org/pdf/2601.08776.pdf)  
**作者**：Yanhua Zhao  

**一句话要点**：提出CycleGAN方法将荧光显微镜图像转换为虚拟H&E染色图像，以辅助病理学分析

**关键词**：图像到图像转换, CycleGAN, 荧光显微镜, 虚拟H&E染色, 病理学分析

## 3 点简述
- 核心问题：荧光显微镜与H&E染色图像格式不同，阻碍信息整合与病理学解读
- 方法要点：使用CycleGAN实现无配对图像转换，结合多通道荧光生成伪H&E图像
- 实验或效果：模型生成逼真伪H&E图像，保留形态结构并模拟H&E颜色特征

## 摘要（原文）

> Histopathology analysis relies on Hematoxylin and Eosin (H&E) staining, but fluorescence microscopy offers complementary information. Converting fluorescence images to H&E-like appearance can aid interpretation and integration with standard workflows. We present a Cycle-Consistent Adversarial Network (CycleGAN) approach for unpaired image-to-image translation from multi-channel fluorescence microscopy to pseudo H&E stained histopathology images. The method combines C01 and C02 fluorescence channels into RGB and learns a bidirectional mapping between fluorescence and H&E domains without paired training data. The architecture uses ResNet-based generators with residual blocks and PatchGAN discriminators, trained with adversarial, cycle-consistency, and identity losses. Experiments on fluorescence microscopy datasets show the model generates realistic pseudo H&E images that preserve morphological structures while adopting H&E-like color characteristics. This enables visualization of fluorescence data in a format familiar to pathologists and supports integration with existing H&E-based analysis pipelines.

