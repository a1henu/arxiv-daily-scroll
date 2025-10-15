---
layout: default
title: Multiplicative Loss for Enhancing Semantic Segmentation in Medical and Cellular Images
---

# Multiplicative Loss for Enhancing Semantic Segmentation in Medical and Cellular Images
**arXiv**：[2510.12258v1](https://arxiv.org/abs/2510.12258) · [PDF](https://arxiv.org/pdf/2510.12258.pdf)  
**作者**：Yuto Yokoi, Kazuhiro Hotta  

**一句话要点**：提出乘法损失函数以增强医学和细胞图像语义分割的鲁棒性

**关键词**：语义分割, 损失函数, 医学图像, 细胞图像, 数据稀缺, 梯度调制

## 3 点简述
- 医学图像数据稀缺，传统损失函数超参数敏感且性能不佳
- 乘法损失结合交叉熵和Dice损失，动态调整梯度以稳定优化
- 实验表明在数据稀缺场景下优于现有损失函数，无需超参数调优

## 摘要（原文）

> We propose two novel loss functions, Multiplicative Loss and
> Confidence-Adaptive Multiplicative Loss, for semantic segmentation in medical
> and cellular images. Although Cross Entropy and Dice Loss are widely used,
> their additive combination is sensitive to hyperparameters and often performs
> suboptimally, especially with limited data. Medical images suffer from data
> scarcity due to privacy, ethics, and costly annotations, requiring robust and
> efficient training objectives. Our Multiplicative Loss combines Cross Entropy
> and Dice losses multiplicatively, dynamically modulating gradients based on
> prediction confidence. This reduces penalties for confident correct predictions
> and amplifies gradients for incorrect overconfident ones, stabilizing
> optimization. Building on this, Confidence-Adaptive Multiplicative Loss applies
> a confidence-driven exponential scaling inspired by Focal Loss, integrating
> predicted probabilities and Dice coefficients to emphasize difficult samples.
> This enhances learning under extreme data scarcity by strengthening gradients
> when confidence is low. Experiments on cellular and medical segmentation
> benchmarks show our framework consistently outperforms tuned additive and
> existing loss functions, offering a simple, effective, and hyperparameter-free
> mechanism for robust segmentation under challenging data limitations.

