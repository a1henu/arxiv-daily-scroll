---
layout: default
title: Meta-D: Metadata-Aware Architectures for Brain Tumor Analysis and Missing-Modality Segmentation
---

# Meta-D: Metadata-Aware Architectures for Brain Tumor Analysis and Missing-Modality Segmentation
**arXiv**：[2603.04811v1](https://arxiv.org/abs/2603.04811) · [PDF](https://arxiv.org/pdf/2603.04811.pdf)  
**作者**：SangHyuk Kim, Daniel Haehn, Sumientra Rampersad  

**一句话要点**：提出Meta-D架构，利用MRI元数据提升脑肿瘤检测与缺失模态分割性能

**关键词**：脑肿瘤分析, 缺失模态分割, 元数据引导, 特征调制, Transformer注意力

## 3 点简述
- 核心问题：医学图像分析中，如何利用扫描元数据稳定特征表示并处理模态缺失。
- 方法要点：通过元数据动态调制卷积特征，并基于元数据的Transformer交叉注意力路由可用模态。
- 实验或效果：在2D检测中F1分数提升达2.62%，3D分割中Dice分数提升达5.12%，参数减少24.1%。

## 摘要（原文）

> We present Meta-D, an architecture that explicitly leverages categorical scanner metadata such as MRI sequence and plane orientation to guide feature extraction for brain tumor analysis. We aim to improve the performance of medical image deep learning pipelines by integrating explicit metadata to stabilize feature representations. We first evaluate this in 2D tumor detection, where injecting sequence (e.g., T1, T2) and plane (e.g., axial) metadata dynamically modulates convolutional features, yielding an absolute increase of up to 2.62% in F1-score over image-only baselines. Because metadata grounds feature extraction when data are available, we hypothesize it can serve as a robust anchor when data are missing. We apply this to 3D missing-modality tumor segmentation. Our Transformer Maximizer utilizes metadata-based cross-attention to isolate and route available modalities, ensuring the network focuses on valid slices. This targeted attention improves brain tumor segmentation Dice scores by up to 5.12% under extreme modality scarcity while reducing model parameters by 24.1%.

