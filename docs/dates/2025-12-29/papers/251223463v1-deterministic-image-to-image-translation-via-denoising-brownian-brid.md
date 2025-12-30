---
layout: default
title: Deterministic Image-to-Image Translation via Denoising Brownian Bridge Models with Dual Approximators
---

# Deterministic Image-to-Image Translation via Denoising Brownian Bridge Models with Dual Approximators
**arXiv**：[2512.23463v1](https://arxiv.org/abs/2512.23463) · [PDF](https://arxiv.org/pdf/2512.23463.pdf)  
**作者**：Bohan Xiao, Peiyong Wang, Qisheng He, Ming Dong  

**一句话要点**：提出基于去噪布朗桥与双近似器的确定性图像到图像翻译模型，以提升输出一致性和保真度。

**关键词**：图像到图像翻译, 确定性生成模型, 布朗桥模型, 去噪扩散模型, 图像超分辨率, 高保真生成

## 3 点简述
- 核心问题：确定性图像到图像翻译需保证输入到输出的高保真、低方差映射。
- 方法要点：利用布朗桥动态和双神经网络近似器（前向与反向过程）构建生成模型。
- 实验或效果：在图像生成和超分辨率基准测试中，相比随机和确定性基线，表现出更优的图像质量和保真度。

## 摘要（原文）

> Image-to-Image (I2I) translation involves converting an image from one domain to another. Deterministic I2I translation, such as in image super-resolution, extends this concept by guaranteeing that each input generates a consistent and predictable output, closely matching the ground truth (GT) with high fidelity. In this paper, we propose a denoising Brownian bridge model with dual approximators (Dual-approx Bridge), a novel generative model that exploits the Brownian bridge dynamics and two neural network-based approximators (one for forward and one for reverse process) to produce faithful output with negligible variance and high image quality in I2I translations. Our extensive experiments on benchmark datasets including image generation and super-resolution demonstrate the consistent and superior performance of Dual-approx Bridge in terms of image quality and faithfulness to GT when compared to both stochastic and deterministic baselines. Project page and code: https://github.com/bohan95/dual-app-bridge

