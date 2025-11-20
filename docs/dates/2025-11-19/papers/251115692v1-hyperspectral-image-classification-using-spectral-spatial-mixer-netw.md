---
layout: default
title: Hyperspectral Image Classification using Spectral-Spatial Mixer Network
---

# Hyperspectral Image Classification using Spectral-Spatial Mixer Network
**arXiv**：[2511.15692v1](https://arxiv.org/abs/2511.15692) · [PDF](https://arxiv.org/pdf/2511.15692.pdf)  
**作者**：Mohammed Q. Alkhatib  

**一句话要点**：提出SS-MixNet以解决高光谱图像分类问题，使用光谱-空间混合网络提升精度。

**关键词**：高光谱图像分类, 光谱-空间特征提取, 轻量级深度学习模型, 注意力机制, 有限监督学习

## 3 点简述
- 核心问题：高光谱图像分类在有限标注数据下如何实现高精度和鲁棒性。
- 方法要点：结合3D卷积提取局部特征，并行MLP混合块捕获光谱和空间长程依赖。
- 实验或效果：在QUH数据集上仅用1%标注数据，准确率达95.68%和93.86%。

## 摘要（原文）

> This paper introduces SS-MixNet, a lightweight and effective deep learning model for hyperspectral image (HSI) classification. The architecture integrates 3D convolutional layers for local spectral-spatial feature extraction with two parallel MLP-style mixer blocks that capture long-range dependencies in spectral and spatial dimensions. A depthwise convolution-based attention mechanism is employed to enhance discriminative capability with minimal computational overhead. The model is evaluated on the QUH-Tangdaowan and QUH-Qingyun datasets using only 1% of labeled data for training and validation. SS-MixNet achieves the highest performance among compared methods, including 2D-CNN, 3D-CNN, IP-SWIN, SimPoolFormer, and HybridKAN, reaching 95.68% and 93.86% overall accuracy on the Tangdaowan and Qingyun datasets, respectively. The results, supported by quantitative metrics and classification maps, confirm the model's effectiveness in delivering accurate and robust predictions with limited supervision. The code will be made publicly available at: https://github.com/mqalkhatib/SS-MixNet

