---
layout: default
title: A Single-Parameter Factor-Graph Image Prior
---

# A Single-Parameter Factor-Graph Image Prior
**arXiv**：[2601.08749v1](https://arxiv.org/abs/2601.08749) · [PDF](https://arxiv.org/pdf/2601.08749.pdf)  
**作者**：Tianyang Wang, Ender Konukoglu, Hans-Andrea Loeliger  

**一句话要点**：提出基于单参数因子图的图像先验模型，用于图像去噪和对比度增强。

**关键词**：图像先验模型, 因子图, 高斯消息传递, 图像去噪, 对比度增强

## 3 点简述
- 核心问题：构建自适应图像先验模型以处理图像局部平滑性。
- 方法要点：采用因子图与未知参数正态先验，结合共轭梯度与高斯消息传递迭代计算。
- 实验或效果：在去噪和对比度增强应用中验证模型与算法的有效性。

## 摘要（原文）

> We propose a novel piecewise smooth image model with piecewise constant local parameters that are automatically adapted to each image. Technically, the model is formulated in terms of factor graphs with NUP (normal with unknown parameters) priors, and the pertinent computations amount to iterations of conjugate-gradient steps and Gaussian message passing. The proposed model and algorithms are demonstrated with applications to denoising and contrast enhancement.

