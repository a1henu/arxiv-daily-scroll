---
layout: default
title: TokenSeg: Efficient 3D Medical Image Segmentation via Hierarchical Visual Token Compression
---

# TokenSeg: Efficient 3D Medical Image Segmentation via Hierarchical Visual Token Compression
**arXiv**：[2601.04519v1](https://arxiv.org/abs/2601.04519) · [PDF](https://arxiv.org/pdf/2601.04519.pdf)  
**作者**：Sen Zeng, Hong Zhou, Zheng Zhu, Yang Liu  

**一句话要点**：提出TokenSeg框架，通过分层视觉令牌压缩实现高效3D医学图像分割。

**关键词**：3D医学图像分割, 视觉令牌压缩, 边界感知, 稀疏表示, 高效计算

## 3 点简述
- 核心问题：3D医学图像分割计算量大，存在冗余处理。
- 方法要点：设计多尺度分层编码器、边界感知令牌化器和稀疏到密集解码器。
- 实验或效果：在乳腺癌DCE-MRI数据集上达到94.49% Dice，降低GPU内存和推理延迟。

## 摘要（原文）

> Three-dimensional medical image segmentation is a fundamental yet computationally demanding task due to the cubic growth of voxel processing and the redundant computation on homogeneous regions. To address these limitations, we propose \textbf{TokenSeg}, a boundary-aware sparse token representation framework for efficient 3D medical volume segmentation. Specifically, (1) we design a \emph{multi-scale hierarchical encoder} that extracts 400 candidate tokens across four resolution levels to capture both global anatomical context and fine boundary details; (2) we introduce a \emph{boundary-aware tokenizer} that combines VQ-VAE quantization with importance scoring to select 100 salient tokens, over 60\% of which lie near tumor boundaries; and (3) we develop a \emph{sparse-to-dense decoder} that reconstructs full-resolution masks through token reprojection, progressive upsampling, and skip connections. Extensive experiments on a 3D breast DCE-MRI dataset comprising 960 cases demonstrate that TokenSeg achieves state-of-the-art performance with 94.49\% Dice and 89.61\% IoU, while reducing GPU memory and inference latency by 64\% and 68\%, respectively. To verify the generalization capability, our evaluations on MSD cardiac and brain MRI benchmark datasets demonstrate that TokenSeg consistently delivers optimal performance across heterogeneous anatomical structures. These results highlight the effectiveness of anatomically informed sparse representation for accurate and efficient 3D medical image segmentation.

