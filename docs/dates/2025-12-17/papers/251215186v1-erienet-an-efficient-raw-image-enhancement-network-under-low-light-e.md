---
layout: default
title: ERIENet: An Efficient RAW Image Enhancement Network under Low-Light Environment
---

# ERIENet: An Efficient RAW Image Enhancement Network under Low-Light Environment
**arXiv**：[2512.15186v1](https://arxiv.org/abs/2512.15186) · [PDF](https://arxiv.org/pdf/2512.15186.pdf)  
**作者**：Jianan Wang, Yang Hong, Hesong Li, Tao Wang, Songrong Liu, Ying Fu  

**一句话要点**：提出ERIENet以高效增强低光RAW图像，通过并行多尺度处理和绿通道引导提升性能与速度。

**关键词**：RAW图像增强, 低光环境, 并行多尺度处理, 绿通道引导, 实时处理, 轻量模型

## 3 点简述
- 现有方法多尺度处理顺序进行，导致模型笨重且速度慢，忽略RAW图像绿通道优势。
- 采用并行多尺度架构和通道感知残差密集块，结合绿通道引导分支，以低计算成本提升重建质量。
- 实验显示在低光数据集上优于先进方法，4K图像处理速度超过146 FPS，实现高效实时增强。

## 摘要（原文）

> RAW images have shown superior performance than sRGB images in many image processing tasks, especially for low-light image enhancement. However, most existing methods for RAW-based low-light enhancement usually sequentially process multi-scale information, which makes it difficult to achieve lightweight models and high processing speeds. Besides, they usually ignore the green channel superiority of RAW images, and fail to achieve better reconstruction performance with good use of green channel information. In this work, we propose an efficient RAW Image Enhancement Network (ERIENet), which parallelly processes multi-scale information with efficient convolution modules, and takes advantage of rich information in green channels to guide the reconstruction of images. Firstly, we introduce an efficient multi-scale fully-parallel architecture with a novel channel-aware residual dense block to extract feature maps, which reduces computational costs and achieves real-time processing speed. Secondly, we introduce a green channel guidance branch to exploit the rich information within the green channels of the input RAW image. It increases the quality of reconstruction results with few parameters and computations. Experiments on commonly used low-light image enhancement datasets show that ERIENet outperforms state-of-the-art methods in enhancing low-light RAW images with higher effiency. It also achieves an optimal speed of over 146 frame-per-second (FPS) for 4K-resolution images on a single NVIDIA GeForce RTX 3090 with 24G memory.

