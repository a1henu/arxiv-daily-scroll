---
layout: default
title: Robust Variational Model Based Tailored UNet: Leveraging Edge Detector and Mean Curvature for Improved Image Segmentation
---

# Robust Variational Model Based Tailored UNet: Leveraging Edge Detector and Mean Curvature for Improved Image Segmentation
**arXiv**：[2512.07590v1](https://arxiv.org/abs/2512.07590) · [PDF](https://arxiv.org/pdf/2512.07590.pdf)  
**作者**：Kaili Qi, Zhongyi Huang, Wenli Yang  

**一句话要点**：提出鲁棒变分模型定制UNet，结合边缘检测与平均曲率以改进噪声图像分割

**关键词**：图像分割, 变分模型, 深度学习, 边缘检测, 平均曲率, 噪声图像处理

## 3 点简述
- 针对噪声图像边界模糊或断裂的分割挑战，提出混合框架VM_TUNet。
- 集成变分方法与深度学习，引入物理先验、边缘检测和平均曲率项。
- 在三个基准数据集上实验，性能与计算效率平衡，优于纯CNN模型。

## 摘要（原文）

> To address the challenge of segmenting noisy images with blurred or fragmented boundaries, this paper presents a robust version of Variational Model Based Tailored UNet (VM_TUNet), a hybrid framework that integrates variational methods with deep learning. The proposed approach incorporates physical priors, an edge detector and a mean curvature term, into a modified Cahn-Hilliard equation, aiming to combine the interpretability and boundary-smoothing advantages of variational partial differential equations (PDEs) with the strong representational ability of deep neural networks. The architecture consists of two collaborative modules: an F module, which conducts efficient frequency domain preprocessing to alleviate poor local minima, and a T module, which ensures accurate and stable local computations, backed by a stability estimate. Extensive experiments on three benchmark datasets indicate that the proposed method achieves a balanced trade-off between performance and computational efficiency, which yields competitive quantitative results and improved visual quality compared to pure convolutional neural network (CNN) based models, while achieving performance close to that of transformer-based method with reasonable computational expense.

