---
layout: default
title: Comparative Study of CNN Architectures for Binary Classification of Horses and Motorcycles in the VOC 2008 Dataset
---

# Comparative Study of CNN Architectures for Binary Classification of Horses and Motorcycles in the VOC 2008 Dataset
**arXiv**：[2511.04344v1](https://arxiv.org/abs/2511.04344) · [PDF](https://arxiv.org/pdf/2511.04344.pdf)  
**作者**：Muhammad Annas Shaikh, Hamza Zaman, Arbaz Asif  

**一句话要点**：比较九种CNN架构在VOC 2008数据集上对马和摩托车的二分类性能

**关键词**：二分类, 类别不平衡, 数据增强, 卷积神经网络, 平均精度, VOC 2008数据集

## 3 点简述
- 核心问题：VOC 2008数据集中马和摩托车二分类存在显著类别不平衡问题。
- 方法要点：采用少数类数据增强技术缓解不平衡，评估ResNet-50等九种架构。
- 实验或效果：ConvNeXt-Tiny在平均精度上表现最佳，数据增强提升少数类检测。

## 摘要（原文）

> This paper presents a comprehensive evaluation of nine convolutional neural
> network architectures for binary classification of horses and motorcycles in
> the VOC 2008 dataset. We address the significant class imbalance problem by
> implementing minority-class augmentation techniques. Our experiments compare
> modern architectures including ResNet-50, ConvNeXt-Tiny, DenseNet-121, and
> Vision Transformer across multiple performance metrics. Results demonstrate
> substantial performance variations, with ConvNeXt-Tiny achieving the highest
> Average Precision (AP) of 95.53% for horse detection and 89.12% for motorcycle
> detection. We observe that data augmentation significantly improves minority
> class detection, particularly benefiting deeper architectures. This study
> provides insights into architecture selection for imbalanced binary
> classification tasks and quantifies the impact of data augmentation strategies
> in mitigating class imbalance issues in object detection.

