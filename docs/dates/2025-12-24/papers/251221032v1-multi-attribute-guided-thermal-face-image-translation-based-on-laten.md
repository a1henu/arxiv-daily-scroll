---
layout: default
title: Multi-Attribute guided Thermal Face Image Translation based on Latent Diffusion Model
---

# Multi-Attribute guided Thermal Face Image Translation based on Latent Diffusion Model
**arXiv**：[2512.21032v1](https://arxiv.org/abs/2512.21032) · [PDF](https://arxiv.org/pdf/2512.21032.pdf)  
**作者**：Mingshu Cai, Osamu Yoshie, Yuya Ieiri  

**一句话要点**：提出基于潜在扩散模型的多属性引导热成像人脸图像转换方法，以提升异质人脸识别性能。

**关键词**：异质人脸识别, 潜在扩散模型, 多属性引导, 热成像图像转换, 跨模态特征建模

## 3 点简述
- 核心问题：可见光人脸识别模型在红外图像上性能下降，现有生成方法存在特征丢失和失真。
- 方法要点：结合多属性分类器提取关键面部属性，并引入Self-attn Mamba模块增强跨模态特征全局建模。
- 实验或效果：在两个基准数据集上实现图像质量和身份保持的先进性能，推理速度显著提升。

## 摘要（原文）

> Modern surveillance systems increasingly rely on multi-wavelength sensors and deep neural networks to recognize faces in infrared images captured at night. However, most facial recognition models are trained on visible light datasets, leading to substantial performance degradation on infrared inputs due to significant domain shifts. Early feature-based methods for infrared face recognition proved ineffective, prompting researchers to adopt generative approaches that convert infrared images into visible light images for improved recognition. This paradigm, known as Heterogeneous Face Recognition (HFR), faces challenges such as model and modality discrepancies, leading to distortion and feature loss in generated images. To address these limitations, this paper introduces a novel latent diffusion-based model designed to generate high-quality visible face images from thermal inputs while preserving critical identity features. A multi-attribute classifier is incorporated to extract key facial attributes from visible images, mitigating feature loss during infrared-to-visible image restoration. Additionally, we propose the Self-attn Mamba module, which enhances global modeling of cross-modal features and significantly improves inference speed. Experimental results on two benchmark datasets demonstrate the superiority of our approach, achieving state-of-the-art performance in both image quality and identity preservation.

