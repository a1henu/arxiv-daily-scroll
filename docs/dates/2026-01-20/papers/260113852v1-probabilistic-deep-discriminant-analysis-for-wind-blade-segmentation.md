---
layout: default
title: Probabilistic Deep Discriminant Analysis for Wind Blade Segmentation
---

# Probabilistic Deep Discriminant Analysis for Wind Blade Segmentation
**arXiv**：[2601.13852v1](https://arxiv.org/abs/2601.13852) · [PDF](https://arxiv.org/pdf/2601.13852.pdf)  
**作者**：Raül Pérez-Gonzalo, Andreas Espersen, Antonio Agudo  

**一句话要点**：提出概率深度判别分析以解决风电叶片分割中的类别重叠问题

**关键词**：深度判别分析, 概率损失, 风电叶片分割, 图像分割, Fisher准则优化, 稳定训练

## 3 点简述
- 线性判别分析难以处理非线性可分数据，导致类别分离性不足
- 通过深度网络直接优化Fisher准则，引入稳定训练策略和概率损失，减少类内方差
- 在风电叶片分割任务中展示性能提升和一致性增强，首次应用于图像分割

## 摘要（原文）

> Linear discriminant analysis improves class separability but struggles with non-linearly separable data. To overcome this, we introduce Deep Discriminant Analysis (DDA), which directly optimizes the Fisher criterion utilizing deep networks. To ensure stable training and avoid computational instabilities, we incorporate signed between-class variance, bound outputs with a sigmoid function, and convert multiplicative relationships into additive ones. We present two stable DDA loss functions and augment them with a probability loss, resulting in Probabilistic DDA (PDDA). PDDA effectively minimizes class overlap in output distributions, producing highly confident predictions with reduced within-class variance. When applied to wind blade segmentation, PDDA showcases notable advances in performance and consistency, critical for wind energy maintenance. To our knowledge, this is the first application of DDA to image segmentation.

