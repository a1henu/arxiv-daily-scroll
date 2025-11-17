---
layout: default
title: MPCGNet: A Multiscale Feature Extraction and Progressive Feature Aggregation Network Using Coupling Gates for Polyp Segmentation
---

# MPCGNet: A Multiscale Feature Extraction and Progressive Feature Aggregation Network Using Coupling Gates for Polyp Segmentation
**arXiv**：[2511.11032v1](https://arxiv.org/abs/2511.11032) · [PDF](https://arxiv.org/pdf/2511.11032.pdf)  
**作者**：Wei Wang, Feng Jiang, Xin Wang  

**一句话要点**：提出MPCGNet网络，使用耦合门解决息肉分割中的噪声和边界模糊问题。

**关键词**：息肉分割, 多尺度特征提取, 耦合门, 特征聚合, 窗口交叉注意力, 医学图像分割

## 3 点简述
- 核心问题：息肉分割面临小息肉易漏检、边界模糊和图像噪声干扰。
- 方法要点：引入耦合门模块，包括多尺度特征提取、窗口交叉注意力和解码器特征聚合。
- 实验或效果：在ETIS-LaribPolypDB和CVC-ColonDB数据集上mDice分数优于其他网络。

## 摘要（原文）

> Automatic segmentation methods of polyps is crucial for assisting doctors in colorectal polyp screening and cancer diagnosis. Despite the progress made by existing methods, polyp segmentation faces several challenges: (1) small-sized polyps are prone to being missed during identification, (2) the boundaries between polyps and the surrounding environment are often ambiguous, (3) noise in colonoscopy images, caused by uneven lighting and other factors, affects segmentation results. To address these challenges, this paper introduces coupling gates as components in specific modules to filter noise and perform feature importance selection. Three modules are proposed: the coupling gates multiscale feature extraction (CGMFE) module, which effectively extracts local features and suppresses noise; the windows cross attention (WCAD) decoder module, which restores details after capturing the precise location of polyps; and the decoder feature aggregation (DFA) module, which progressively aggregates features, further extracts them, and performs feature importance selection to reduce the loss of small-sized polyps. Experimental results demonstrate that MPCGNet outperforms recent networks, with mDice scores 2.20% and 0.68% higher than the second-best network on the ETIS-LaribPolypDB and CVC-ColonDB datasets, respectively.

