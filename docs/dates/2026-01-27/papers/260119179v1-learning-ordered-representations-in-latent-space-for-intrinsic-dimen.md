---
layout: default
title: Learning Ordered Representations in Latent Space for Intrinsic Dimension Estimation via Principal Component Autoencoder
---

# Learning Ordered Representations in Latent Space for Intrinsic Dimension Estimation via Principal Component Autoencoder
**arXiv**：[2601.19179v1](https://arxiv.org/abs/2601.19179) · [PDF](https://arxiv.org/pdf/2601.19179.pdf)  
**作者**：Qipeng Zhan, Zhuoping Zhou, Zexuan Wang, Li Shen  

**一句话要点**：提出结合非均匀方差正则化和等距约束的自编码器框架，以在非线性降维中保持有序表示和方差保留。

**关键词**：自编码器, 非线性降维, 主成分分析, 有序表示, 方差正则化, 等距约束

## 3 点简述
- 核心问题：非线性自编码器难以像PCA那样保持有序表示和独立捕获剩余方差。
- 方法要点：集成非均匀方差正则化与等距约束，作为PCA的自然推广。
- 实验或效果：未知，但框架旨在保留PCA优势并适用于非线性任务。

## 摘要（原文）

> Autoencoders have long been considered a nonlinear extension of Principal Component Analysis (PCA). Prior studies have demonstrated that linear autoencoders (LAEs) can recover the ordered, axis-aligned principal components of PCA by incorporating non-uniform $\ell_2$ regularization or by adjusting the loss function. However, these approaches become insufficient in the nonlinear setting, as the remaining variance cannot be properly captured independently of the nonlinear mapping. In this work, we propose a novel autoencoder framework that integrates non-uniform variance regularization with an isometric constraint. This design serves as a natural generalization of PCA, enabling the model to preserve key advantages, such as ordered representations and variance retention, while remaining effective for nonlinear dimensionality reduction tasks.

