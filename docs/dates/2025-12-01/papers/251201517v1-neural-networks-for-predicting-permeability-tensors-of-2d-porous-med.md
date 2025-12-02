---
layout: default
title: Neural Networks for Predicting Permeability Tensors of 2D Porous Media: Comparison of Convolution- and Transformer-based Architectures
---

# Neural Networks for Predicting Permeability Tensors of 2D Porous Media: Comparison of Convolution- and Transformer-based Architectures
**arXiv**：[2512.01517v1](https://arxiv.org/abs/2512.01517) · [PDF](https://arxiv.org/pdf/2512.01517.pdf)  
**作者**：Sigurd Vargdal, Paula Reis, Henrik Andersen Sveinsson, Gaute Linga  

**一句话要点**：比较卷积与Transformer架构，基于二维孔隙图像预测渗透率张量

**关键词**：渗透率预测, 孔隙介质, 深度学习, 卷积神经网络, 视觉Transformer, 图像分析

## 3 点简述
- 核心问题：传统渗透率预测方法耗时或简化，需高效替代方案。
- 方法要点：使用ResNet、ViT和ConvNeXt模型，结合数据增强等技术提升泛化。
- 实验效果：ConvNeXt-Small在测试集上R²达0.99460，优于其他模型。

## 摘要（原文）

> Permeability is a central concept in the macroscopic description of flow through porous media, with applications spanning from oil recovery to hydrology. Traditional methods for determining the permeability tensor involving flow simulations or experiments can be time consuming and resource-intensive, while analytical methods, e.g., based on the Kozeny-Carman equation, may be too simplistic for accurate prediction based on pore-scale features. In this work, we explore deep learning as a more efficient alternative for predicting the permeability tensor based on two-dimensional binary images of porous media, segmented into solid ($1$) and void ($0$) regions. We generate a dataset of 24,000 synthetic random periodic porous media samples with specified porosity and characteristic length scale. Using Lattice-Boltzmann simulations, we compute the permeability tensor for flow through these samples with values spanning three orders of magnitude. We evaluate three families of image-based deep learning models: ResNet (ResNet-$50$ and ResNet-$101$), Vision Transformers (ViT-T$16$ and ViT-S$16$) and ConvNeXt (Tiny and Small). To improve model generalisation, we employ techniques such as weight decay, learning rate scheduling, and data augmentation. The effect of data augmentation and dataset size on model performance is studied, and we find that they generally increase the accuracy of permeability predictions. We also show that ConvNeXt and ResNet converge faster than ViT and degrade in performance if trained for too long. ConvNeXt-Small achieved the highest $R^2$ score of $0.99460$ on $4,000$ unseen test samples. These findings underscore the potential to use image-based neural networks to predict permeability tensors accurately.

