---
layout: default
title: Matching of SAR and optical images based on transformation to shared modality
---

# Matching of SAR and optical images based on transformation to shared modality
**arXiv**：[2602.12515v1](https://arxiv.org/abs/2602.12515) · [PDF](https://arxiv.org/pdf/2602.12515.pdf)  
**作者**：Alexey Borisov, Evgeny Myasnikov, Vladislav Myasnikov  

**一句话要点**：提出基于共享模态转换的方法以解决SAR与光学图像匹配难题

**关键词**：SAR图像匹配, 光学图像匹配, 模态转换, RoMa模型, 遥感图像处理

## 3 点简述
- 核心问题：SAR与光学图像因物理原理差异导致匹配困难
- 方法要点：将图像转换至共享模态，满足通道数相等、相似性高、特征保留条件
- 实验或效果：在MultiSenGE数据集上优于传统方法，支持预训练模型直接应用

## 摘要（原文）

> Significant differences in optical images and Synthetic Aperture Radar (SAR) images are caused by fundamental differences in the physical principles underlying their acquisition by Earth remote sensing platforms. These differences make precise image matching (co-registration) of these two types of images difficult. In this paper, we propose a new approach to image matching of optical and SAR images, which is based on transforming the images to a new modality. The new image modality is common to both optical and SAR images and satisfies the following conditions. First, the transformed images must have an equal pre-defined number of channels. Second, the transformed and co-registered images must be as similar as possible. Third, the transformed images must be non-degenerate, meaning they must preserve the significant features of the original images. To further match images transformed to this shared modality, we train the RoMa image matching model, which is one of the leading solutions for matching of regular digital photographs. We evaluated the proposed approach on the publicly available MultiSenGE dataset containing both optical and SAR images. We demonstrated its superiority over alternative approaches based on image translation between original modalities and various feature matching algorithms. The proposed solution not only provides better quality of matching, but is also more versatile. It enables the use of ready-made RoMa and DeDoDe models, pre-trained for regular images, without retraining for a new modality, while maintaining high-quality matching of optical and SAR images.

