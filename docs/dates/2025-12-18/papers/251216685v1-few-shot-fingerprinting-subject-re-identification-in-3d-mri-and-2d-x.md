---
layout: default
title: Few-Shot Fingerprinting Subject Re-Identification in 3D-MRI and 2D-X-Ray
---

# Few-Shot Fingerprinting Subject Re-Identification in 3D-MRI and 2D-X-Ray
**arXiv**：[2512.16685v1](https://arxiv.org/abs/2512.16685) · [PDF](https://arxiv.org/pdf/2512.16685.pdf)  
**作者**：Gonçalo Gaspar Alves, Shekoufeh Gorgi Zadeh, Andreas Husch, Ben Bausch  

**一句话要点**：提出基于指纹识别的少样本主体重识别方法，解决多数据集合并时的数据泄露问题，应用于3D-MRI和2D-X射线图像。

**关键词**：主体重识别, 指纹识别, 少样本学习, 医学图像分析, 三元组损失

## 3 点简述
- 核心问题：多开源数据集合并时，同一主体重复出现导致数据泄露，模型性能被高估。
- 方法要点：使用ResNet-50和三元组边界损失，将主体图像映射到潜在空间特定区域进行指纹识别。
- 实验或效果：在ChestXray-14和BraTS-2021数据集上，少样本场景下Mean-Recall-@-K得分高达99.10%和98.86%。

## 摘要（原文）

> Combining open-source datasets can introduce data leakage if the same subject appears in multiple sets, leading to inflated model performance. To address this, we explore subject fingerprinting, mapping all images of a subject to a distinct region in latent space, to enable subject re-identification via similarity matching. Using a ResNet-50 trained with triplet margin loss, we evaluate few-shot fingerprinting on 3D MRI and 2D X-ray data in both standard (20-way 1-shot) and challenging (1000-way 1-shot) scenarios. The model achieves high Mean- Recall-@-K scores: 99.10% (20-way 1-shot) and 90.06% (500-way 5-shot) on ChestXray-14; 99.20% (20-way 1-shot) and 98.86% (100-way 3-shot) on BraTS- 2021.

