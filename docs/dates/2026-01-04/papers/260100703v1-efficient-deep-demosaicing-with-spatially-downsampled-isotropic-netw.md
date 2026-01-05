---
layout: default
title: Efficient Deep Demosaicing with Spatially Downsampled Isotropic Networks
---

# Efficient Deep Demosaicing with Spatially Downsampled Isotropic Networks
**arXiv**：[2601.00703v1](https://arxiv.org/abs/2601.00703) · [PDF](https://arxiv.org/pdf/2601.00703.pdf)  
**作者**：Cory Fan, Wenchao Zhang  

**一句话要点**：提出空间下采样各向同性网络以提升移动平台去马赛克效率与性能

**关键词**：图像去马赛克, 各向同性网络, 空间下采样, 移动计算, 联合去马赛克与去噪

## 3 点简述
- 核心问题：移动平台去马赛克中，传统各向同性网络计算成本高，限制应用。
- 方法要点：通过空间下采样设计轻量全卷积网络，提升计算效率与性能。
- 实验或效果：JD3Net在多种去马赛克和联合任务中表现优异，验证下采样有效性。

## 摘要（原文）

> In digital imaging, image demosaicing is a crucial first step which recovers the RGB information from a color filter array (CFA). Oftentimes, deep learning is utilized to perform image demosaicing. Given that most modern digital imaging applications occur on mobile platforms, applying deep learning to demosaicing requires lightweight and efficient networks. Isotropic networks, also known as residual-in-residual networks, have been often employed for image demosaicing and joint-demosaicing-and-denoising (JDD). Most demosaicing isotropic networks avoid spatial downsampling entirely, and thus are often prohibitively expensive computationally for mobile applications. Contrary to previous isotropic network designs, this paper claims that spatial downsampling to a signficant degree can improve the efficiency and performance of isotropic networks. To validate this claim, we design simple fully convolutional networks with and without downsampling using a mathematical architecture design technique adapted from DeepMAD, and find that downsampling improves empirical performance. Additionally, empirical testing of the downsampled variant, JD3Net, of our fully convolutional networks reveals strong empirical performance on a variety of image demosaicing and JDD tasks.

