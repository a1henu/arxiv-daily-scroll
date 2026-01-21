---
layout: default
title: Generalizing Abstention for Noise-Robust Learning in Medical Image Segmentation
---

# Generalizing Abstention for Noise-Robust Learning in Medical Image Segmentation
**arXiv**：[2601.14039v1](https://arxiv.org/abs/2601.14039) · [PDF](https://arxiv.org/pdf/2601.14039.pdf)  
**作者**：Wesam Moustafa, Hossam Elsafty, Helen Schneider, Lorenz Sparrenberg, Rafet Sifa  

**一句话要点**：提出通用弃权框架以增强医学图像分割中的噪声鲁棒性

**关键词**：医学图像分割, 标签噪声, 弃权机制, 噪声鲁棒学习, 损失函数增强

## 3 点简述
- 核心问题：医学图像分割中标签噪声导致模型过拟合，降低泛化性能。
- 方法要点：引入模块化弃权框架，包含正则化项和自动调参算法，增强损失函数噪声鲁棒性。
- 实验或效果：在CaDIS和DSAD数据集上，新方法在高噪声水平下显著优于基线。

## 摘要（原文）

> Label noise is a critical problem in medical image segmentation, often arising from the inherent difficulty of manual annotation. Models trained on noisy data are prone to overfitting, which degrades their generalization performance. While a number of methods and strategies have been proposed to mitigate noisy labels in the segmentation domain, this area remains largely under-explored. The abstention mechanism has proven effective in classification tasks by enhancing the capabilities of Cross Entropy, yet its potential in segmentation remains unverified. In this paper, we address this gap by introducing a universal and modular abstention framework capable of enhancing the noise-robustness of a diverse range of loss functions. Our framework improves upon prior work with two key components: an informed regularization term to guide abstention behaviour, and a more flexible power-law-based auto-tuning algorithm for the abstention penalty. We demonstrate the framework's versatility by systematically integrating it with three distinct loss functions to create three novel, noise-robust variants: GAC, SAC, and ADS. Experiments on the CaDIS and DSAD medical datasets show our methods consistently and significantly outperform their non-abstaining baselines, especially under high noise levels. This work establishes that enabling models to selectively ignore corrupted samples is a powerful and generalizable strategy for building more reliable segmentation models. Our code is publicly available at https://github.com/wemous/abstention-for-segmentation.

