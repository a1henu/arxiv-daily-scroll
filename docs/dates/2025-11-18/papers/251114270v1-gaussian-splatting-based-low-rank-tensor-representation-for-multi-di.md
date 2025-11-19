---
layout: default
title: Gaussian Splatting-based Low-Rank Tensor Representation for Multi-Dimensional Image Recovery
---

# Gaussian Splatting-based Low-Rank Tensor Representation for Multi-Dimensional Image Recovery
**arXiv**：[2511.14270v1](https://arxiv.org/abs/2511.14270) · [PDF](https://arxiv.org/pdf/2511.14270.pdf)  
**作者**：Yiming Zeng, Xi-Le Zhao, Wei-Hao Wu, Teng-Yu Ji, Chao Wang  

**一句话要点**：提出GSLR框架以解决多维图像恢复中局部高频信息捕获不足问题

**关键词**：多维图像恢复, 高斯泼溅, 低秩张量表示, 局部高频信息, 无监督学习

## 3 点简述
- t-SVD方法在表示多维图像时，潜在张量近似粗糙且变换矩阵固定，无法精确捕获局部高频信息
- GSLR使用2D和1D高斯泼溅分别生成潜在张量和变换矩阵，实现紧凑连续的多维图像表示
- 实验表明GSLR在多维图像恢复中优于现有方法，尤其在局部高频信息捕获方面表现突出

## 摘要（原文）

> Tensor singular value decomposition (t-SVD) is a promising tool for multi-dimensional image representation, which decomposes a multi-dimensional image into a latent tensor and an accompanying transform matrix. However, two critical limitations of t-SVD methods persist: (1) the approximation of the latent tensor (e.g., tensor factorizations) is coarse and fails to accurately capture spatial local high-frequency information; (2) The transform matrix is composed of fixed basis atoms (e.g., complex exponential atoms in DFT and cosine atoms in DCT) and cannot precisely capture local high-frequency information along the mode-3 fibers. To address these two limitations, we propose a Gaussian Splatting-based Low-rank tensor Representation (GSLR) framework, which compactly and continuously represents multi-dimensional images. Specifically, we leverage tailored 2D Gaussian splatting and 1D Gaussian splatting to generate the latent tensor and transform matrix, respectively. The 2D and 1D Gaussian splatting are indispensable and complementary under this representation framework, which enjoys a powerful representation capability, especially for local high-frequency information. To evaluate the representation ability of the proposed GSLR, we develop an unsupervised GSLR-based multi-dimensional image recovery model. Extensive experiments on multi-dimensional image recovery demonstrate that GSLR consistently outperforms state-of-the-art methods, particularly in capturing local high-frequency information.

