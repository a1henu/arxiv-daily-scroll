---
layout: default
title: Scale-Cascaded Diffusion Models for Super-Resolution in Medical Imaging
---

# Scale-Cascaded Diffusion Models for Super-Resolution in Medical Imaging
**arXiv**：[2601.23201v1](https://arxiv.org/abs/2601.23201) · [PDF](https://arxiv.org/pdf/2601.23201.pdf)  
**作者**：Darshan Thaker, Mahmoud Mostapha, Radu Miron, Shihan Qiu, Mariappan Nadar  

**一句话要点**：提出尺度级联扩散模型以解决医学图像超分辨率中的多尺度重建问题

**关键词**：医学图像超分辨率, 扩散模型, 多尺度重建, 拉普拉斯金字塔, 感知质量提升, 推理时间优化

## 3 点简述
- 核心问题：现有扩散模型在医学图像超分辨率中忽略图像数据的层次尺度结构，通常使用单尺度先验。
- 方法要点：将图像分解为拉普拉斯金字塔尺度，为每个频带训练独立的扩散先验，并开发算法跨尺度渐进细化重建。
- 实验或效果：在脑、膝和前列腺MRI数据上评估，提升感知质量并减少推理时间，统一多尺度重建与扩散先验。

## 摘要（原文）

> Diffusion models have been increasingly used as strong generative priors for solving inverse problems such as super-resolution in medical imaging. However, these approaches typically utilize a diffusion prior trained at a single scale, ignoring the hierarchical scale structure of image data. In this work, we propose to decompose images into Laplacian pyramid scales and train separate diffusion priors for each frequency band. We then develop an algorithm to perform super-resolution that utilizes these priors to progressively refine reconstructions across different scales. Evaluated on brain, knee, and prostate MRI data, our approach both improves perceptual quality over baselines and reduces inference time through smaller coarse-scale networks. Our framework unifies multiscale reconstruction and diffusion priors for medical image super-resolution.

