---
layout: default
title: Covariance Descriptors Meet General Vision Encoders: Riemannian Deep Learning for Medical Image Classification
---

# Covariance Descriptors Meet General Vision Encoders: Riemannian Deep Learning for Medical Image Classification
**arXiv**：[2511.04190v1](https://arxiv.org/abs/2511.04190) · [PDF](https://arxiv.org/pdf/2511.04190.pdf)  
**作者**：Josef Mayr, Anna Reithmeir, Maxime Di Folco, Julia A. Schnabel  

**一句话要点**：提出结合协方差描述符与通用视觉编码器，提升医学图像分类性能

**关键词**：协方差描述符, 通用视觉编码器, SPDNet, 医学图像分类, Riemannian深度学习

## 3 点简述
- 核心问题：协方差描述符在医学图像中应用不足，需验证其有效性
- 方法要点：从预训练GVE提取特征构建协方差描述符，并评估SPDNet分类网络
- 实验或效果：在MedMNIST数据集上，GVE特征协方差描述符优于手工特征，SPDNet结合DINOv2表现最佳

## 摘要（原文）

> Covariance descriptors capture second-order statistics of image features.
> They have shown strong performance in general computer vision tasks, but remain
> underexplored in medical imaging. We investigate their effectiveness for both
> conventional and learning-based medical image classification, with a particular
> focus on SPDNet, a classification network specifically designed for symmetric
> positive definite (SPD) matrices. We propose constructing covariance
> descriptors from features extracted by pre-trained general vision encoders
> (GVEs) and comparing them with handcrafted descriptors. Two GVEs - DINOv2 and
> MedSAM - are evaluated across eleven binary and multi-class datasets from the
> MedMNSIT benchmark. Our results show that covariance descriptors derived from
> GVE features consistently outperform those derived from handcrafted features.
> Moreover, SPDNet yields superior performance to state-of-the-art methods when
> combined with DINOv2 features. Our findings highlight the potential of
> combining covariance descriptors with powerful pretrained vision encoders for
> medical image analysis.

