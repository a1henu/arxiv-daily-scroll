---
layout: default
title: Blind Deconvolution for Color Images Using Normalized Quaternion Kernels
---

# Blind Deconvolution for Color Images Using Normalized Quaternion Kernels
**arXiv**：[2511.17253v1](https://arxiv.org/abs/2511.17253) · [PDF](https://arxiv.org/pdf/2511.17253.pdf)  
**作者**：Yuming Yang, Michael K. Ng, Zhigang Jia, Wei Wang  

**一句话要点**：提出归一化四元数核方法以解决彩色图像盲去卷积问题

**关键词**：彩色图像盲去卷积, 四元数核, 归一化卷积, 颜色通道关系, 图像去模糊

## 3 点简述
- 核心问题：彩色图像盲去卷积中忽略颜色通道间关系，导致去模糊效果不佳。
- 方法要点：设计四元数保真项，利用四元数卷积核建模颜色通道间未知依赖关系。
- 实验或效果：在真实模糊彩色图像数据集上验证，有效去除伪影并显著提升去模糊效果。

## 摘要（原文）

> In this work, we address the challenging problem of blind deconvolution for color images. Existing methods often convert color images to grayscale or process each color channel separately, which overlooking the relationships between color channels. To handle this issue, we formulate a novel quaternion fidelity term designed specifically for color image blind deconvolution. This fidelity term leverages the properties of quaternion convolution kernel, which consists of four kernels: one that functions similarly to a non-negative convolution kernel to capture the overall blur, and three additional convolution kernels without constraints corresponding to red, green and blue channels respectively model their unknown interdependencies. In order to preserve image intensity, we propose to use the normalized quaternion kernel in the blind deconvolution process. Extensive experiments on real datasets of blurred color images show that the proposed method effectively removes artifacts and significantly improves deblurring effect, demonstrating its potential as a powerful tool for color image deconvolution.

