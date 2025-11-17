---
layout: default
title: Unsupervised Segmentation of Micro-CT Scans of Polyurethane Structures By Combining Hidden-Markov-Random Fields and a U-Net
---

# Unsupervised Segmentation of Micro-CT Scans of Polyurethane Structures By Combining Hidden-Markov-Random Fields and a U-Net
**arXiv**：[2511.11378v1](https://arxiv.org/abs/2511.11378) · [PDF](https://arxiv.org/pdf/2511.11378.pdf)  
**作者**：Julian Grolig, Lars Griem, Michael Selzer, Hans-Ulrich Kauczor, Simon M. F. Triphan, Britta Nestler, Arnd Koeppe  

**一句话要点**：提出HMRF-UNet方法，用于无监督分割聚氨酯泡沫Micro-CT图像

**关键词**：无监督分割, 隐马尔可夫随机场, U-Net, Micro-CT图像, 聚氨酯泡沫

## 3 点简述
- 核心问题：无监督分割方法常速度慢且精度低，监督方法需大量标注数据
- 方法要点：结合隐马尔可夫随机场与U-Net，实现无监督学习与快速分割
- 实验或效果：在聚氨酯泡沫Micro-CT数据集上实现高精度分割，无需真实标签

## 摘要（原文）

> Extracting digital material representations from images is a necessary prerequisite for a quantitative analysis of material properties. Different segmentation approaches have been extensively studied in the past to achieve this task, but were often lacking accuracy or speed. With the advent of machine learning, supervised convolutional neural networks (CNNs) have achieved state-of-the-art performance for different segmentation tasks. However, these models are often trained in a supervised manner, which requires large labeled datasets. Unsupervised approaches do not require ground-truth data for learning, but suffer from long segmentation times and often worse segmentation accuracy. Hidden Markov Random Fields (HMRF) are an unsupervised segmentation approach that incorporates concepts of neighborhood and class distributions. We present a method that integrates HMRF theory and CNN segmentation, leveraging the advantages of both areas: unsupervised learning and fast segmentation times. We investigate the contribution of different neighborhood terms and components for the unsupervised HMRF loss. We demonstrate that the HMRF-UNet enables high segmentation accuracy without ground truth on a Micro-Computed Tomography ($μ$CT) image dataset of Polyurethane (PU) foam structures. Finally, we propose and demonstrate a pre-training strategy that considerably reduces the required amount of ground-truth data when training a segmentation model.

