---
layout: default
title: Differential Privacy Image Generation with Reconstruction Loss and Noise Injection Using an Error Feedback SGD
---

# Differential Privacy Image Generation with Reconstruction Loss and Noise Injection Using an Error Feedback SGD
**arXiv**：[2601.15061v1](https://arxiv.org/abs/2601.15061) · [PDF](https://arxiv.org/pdf/2601.15061.pdf)  
**作者**：Qiwei Ma, Jun Zhang  

**一句话要点**：提出基于误差反馈SGD的差分隐私图像生成框架，以提升隐私保护下的数据效用。

**关键词**：差分隐私, 图像生成, 误差反馈SGD, 重构损失, 噪声注入, 隐私保护机器学习

## 3 点简述
- 传统数据掩码技术在隐私保护机器学习中难以平衡隐私与数据效用。
- 引入误差反馈SGD、重构损失和噪声注入机制，优化生成过程。
- 在MNIST等基准测试中，相同隐私预算下实现更高质量的图像生成。

## 摘要（原文）

> Traditional data masking techniques such as anonymization cannot achieve the expected privacy protection while ensuring data utility for privacy-preserving machine learning. Synthetic data plays an increasingly important role as it generates a large number of training samples and prevents information leakage in real data. The existing methods suffer from the repeating trade-off processes between privacy and utility. We propose a novel framework for differential privacy generation, which employs an Error Feedback Stochastic Gradient Descent(EFSGD) method and introduces a reconstruction loss and noise injection mechanism into the training process. We generate images with higher quality and usability under the same privacy budget as the related work. Extensive experiments demonstrate the effectiveness and generalization of our proposed framework for both grayscale and RGB images. We achieve state-of-the-art results over almost all metrics on three benchmarks: MNIST, Fashion-MNIST, and CelebA.

