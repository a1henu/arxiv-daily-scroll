---
layout: default
title: Carousel: A High-Resolution Dataset for Multi-Target Automatic Image Cropping
---

# Carousel: A High-Resolution Dataset for Multi-Target Automatic Image Cropping
**arXiv**：[2511.04680v1](https://arxiv.org/abs/2511.04680) · [PDF](https://arxiv.org/pdf/2511.04680.pdf)  
**作者**：Rafe Loya, Andrew Hamara, Benjamin Estell, Benjamin Kilpatrick, Andrew C. Freeman  

**一句话要点**：提出Carousel数据集以解决多目标自动图像裁剪问题

**关键词**：自动图像裁剪, 多目标裁剪, 高分辨率数据集, 图像分割, 美学评估

## 3 点简述
- 核心问题：自动图像裁剪需生成多个美观且不同的裁剪区域，现有方法多聚焦单裁剪
- 方法要点：引入高分辨率数据集，结合图像分割算法作为预处理步骤
- 实验或效果：评估多个单裁剪模型，数据集包含277张图像和人类标注

## 摘要（原文）

> Automatic image cropping is a method for maximizing the human-perceived
> quality of cropped regions in photographs. Although several works have proposed
> techniques for producing singular crops, little work has addressed the problem
> of producing multiple, distinct crops with aesthetic appeal. In this paper, we
> motivate the problem with a discussion on modern social media applications,
> introduce a dataset of 277 relevant images and human labels, and evaluate the
> efficacy of several single-crop models with an image partitioning algorithm as
> a pre-processing step. The dataset is available at
> https://github.com/RafeLoya/carousel.

