---
layout: default
title: An Intuitionistic Fuzzy Logic Driven UNet architecture: Application to Brain Image segmentation
---

# An Intuitionistic Fuzzy Logic Driven UNet architecture: Application to Brain Image segmentation
**arXiv**：[2602.04227v1](https://arxiv.org/abs/2602.04227) · [PDF](https://arxiv.org/pdf/2602.04227.pdf)  
**作者**：Hanuman Verma, Kiho Im, Pranabesh Maji, Akshansh Gupta  

**一句话要点**：提出IF-UNet以解决脑图像分割中的不确定性，结合直觉模糊逻辑增强UNet。

**关键词**：脑图像分割, 直觉模糊逻辑, UNet架构, 医学图像处理, 不确定性处理

## 3 点简述
- 核心问题：脑MRI图像分割因部分容积效应和边界模糊导致不确定性处理困难。
- 方法要点：将直觉模糊逻辑融入UNet，通过隶属度、非隶属度和犹豫度处理输入数据。
- 实验或效果：在IBSR数据集上评估，IF-UNet在准确率、Dice系数和IoU上提升分割质量。

## 摘要（原文）

> Accurate segmentation of MRI brain images is essential for image analysis, diagnosis of neuro-logical disorders and medical image computing. In the deep learning approach, the convolutional neural networks (CNNs), especially UNet, are widely applied in medical image segmentation. However, it is difficult to deal with uncertainty due to the partial volume effect in brain images. To overcome this limitation, we propose an enhanced framework, named UNet with intuitionistic fuzzy logic (IF-UNet), which incorporates intuitionistic fuzzy logic into UNet. The model processes input data in terms of membership, nonmembership, and hesitation degrees, allowing it to better address tissue ambiguity resulting from partial volume effects and boundary uncertainties. The proposed architecture is evaluated on the Internet Brain Segmentation Repository (IBSR) dataset, and its performance is computed using accuracy, Dice coefficient, and intersection over union (IoU). Experimental results confirm that IF-UNet improves segmentation quality with handling uncertainty in brain images.

