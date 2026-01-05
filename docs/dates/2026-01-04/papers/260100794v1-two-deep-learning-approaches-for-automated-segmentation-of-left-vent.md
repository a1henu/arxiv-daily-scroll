---
layout: default
title: Two Deep Learning Approaches for Automated Segmentation of Left Ventricle in Cine Cardiac MRI
---

# Two Deep Learning Approaches for Automated Segmentation of Left Ventricle in Cine Cardiac MRI
**arXiv**：[2601.00794v1](https://arxiv.org/abs/2601.00794) · [PDF](https://arxiv.org/pdf/2601.00794.pdf)  
**作者**：Wenhui Chu, Nikolaos V. Tsekos  

**一句话要点**：提出LNU-Net和IBU-Net两种深度学习架构，用于短轴电影心脏MRI中的左心室自动分割。

**关键词**：左心室分割, 深度学习架构, 医学图像分割, U-Net变体, 归一化技术, 心脏MRI

## 3 点简述
- 核心问题：左心室分割对心脏图像临床量化与诊断至关重要，需从短轴电影MRI中精确分割。
- 方法要点：LNU-Net基于层归一化U-Net，IBU-Net结合实例和批量归一化，均采用下采样和上采样路径，并应用仿射变换和弹性变形进行数据处理。
- 实验或效果：在45名患者的805张MRI图像上评估，实验结果显示在Dice系数和平均垂直距离上优于其他先进方法。

## 摘要（原文）

> Left ventricle (LV) segmentation is critical for clinical quantification and diagnosis of cardiac images. In this work, we propose two novel deep learning architectures called LNU-Net and IBU-Net for left ventricle segmentation from short-axis cine MRI images. LNU-Net is derived from layer normalization (LN) U-Net architecture, while IBU-Net is derived from the instance-batch normalized (IB) U-Net for medical image segmentation. The architectures of LNU-Net and IBU-Net have a down-sampling path for feature extraction and an up-sampling path for precise localization. We use the original U-Net as the basic segmentation approach and compared it with our proposed architectures. Both LNU-Net and IBU-Net have left ventricle segmentation methods: LNU-Net applies layer normalization in each convolutional block, while IBU-Net incorporates instance and batch normalization together in the first convolutional block and passes its result to the next layer. Our method incorporates affine transformations and elastic deformations for image data processing. Our dataset that contains 805 MRI images regarding the left ventricle from 45 patients is used for evaluation. We experimentally evaluate the results of the proposed approaches outperforming the dice coefficient and the average perpendicular distance than other state-of-the-art approaches.

