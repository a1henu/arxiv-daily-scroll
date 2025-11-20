---
layout: default
title: Evaluating Low-Light Image Enhancement Across Multiple Intensity Levels
---

# Evaluating Low-Light Image Enhancement Across Multiple Intensity Levels
**arXiv**：[2511.15496v1](https://arxiv.org/abs/2511.15496) · [PDF](https://arxiv.org/pdf/2511.15496.pdf)  
**作者**：Maria Pilligua, David Serrano-Lozano, Pai Peng, Ramon Baldrich, Michael S. Brown, Javier Vazquez-Corral  

**一句话要点**：提出多光照低光数据集以评估图像增强方法在不同光照强度下的性能

**关键词**：低光图像增强, 多光照数据集, 性能评估, PSNR改进, 鲁棒性增强

## 3 点简述
- 核心问题：现有低光增强方法依赖单一光照配对数据，缺乏对多光照强度性能的评估。
- 方法要点：引入MILL数据集，包含多光照强度图像，用于全面评估增强算法。
- 实验或效果：基准测试显示性能波动，改进方法在PSNR上获得显著提升。

## 摘要（原文）

> Imaging in low-light environments is challenging due to reduced scene radiance, which leads to elevated sensor noise and reduced color saturation. Most learning-based low-light enhancement methods rely on paired training data captured under a single low-light condition and a well-lit reference. The lack of radiance diversity limits our understanding of how enhancement techniques perform across varying illumination intensities. We introduce the Multi-Illumination Low-Light (MILL) dataset, containing images captured at diverse light intensities under controlled conditions with fixed camera settings and precise illuminance measurements. MILL enables comprehensive evaluation of enhancement algorithms across variable lighting conditions. We benchmark several state-of-the-art methods and reveal significant performance variations across intensity levels. Leveraging the unique multi-illumination structure of our dataset, we propose improvements that enhance robustness across diverse illumination scenarios. Our modifications achieve up to 10 dB PSNR improvement for DSLR and 2 dB for the smartphone on Full HD images.

