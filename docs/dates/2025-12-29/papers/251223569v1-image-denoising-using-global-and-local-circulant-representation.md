---
layout: default
title: Image Denoising Using Global and Local Circulant Representation
---

# Image Denoising Using Global and Local Circulant Representation
**arXiv**：[2512.23569v1](https://arxiv.org/abs/2512.23569) · [PDF](https://arxiv.org/pdf/2512.23569.pdf)  
**作者**：Zhaoming Kong, Xiaowei Yang, Jiahuan Zhang  

**一句话要点**：提出Haar-tSVD方法，结合全局与局部循环表示进行图像去噪

**关键词**：图像去噪, 循环表示, 张量奇异值分解, Haar变换, 自适应噪声估计

## 3 点简述
- 核心问题：图像去噪需高效平衡速度与性能，传统方法依赖局部基学习。
- 方法要点：基于PCA与Haar变换的理论连接，利用t-SVD投影捕获全局和局部相关性。
- 实验或效果：在多种数据集上验证了方法的效率和有效性，并集成深度学习增强性能。

## 摘要（原文）

> The proliferation of imaging devices and countless image data generated every day impose an increasingly high demand on efficient and effective image denoising. In this paper, we establish a theoretical connection between principal component analysis (PCA) and the Haar transform under circulant representation, and present a computationally simple denoising algorithm. The proposed method, termed Haar-tSVD, exploits a unified tensor singular value decomposition (t-SVD) projection combined with Haar transform to efficiently capture global and local patch correlations. Haar-tSVD operates as a one-step, parallelizable plug-and-play denoiser that eliminates the need for learning local bases, thereby striking a balance between denoising speed and performance. Besides, an adaptive noise estimation scheme is introduced to improve robustness according to eigenvalue analysis of the circulant structure. To further enhance the performance under severe noise conditions, we integrate deep neural networks with Haar-tSVD based on the established Haar-PCA relationship. Experimental results on various denoising datasets demonstrate the efficiency and effectiveness of proposed method for noise removal. Our code is publicly available at https://github.com/ZhaomingKong/Haar-tSVD.

