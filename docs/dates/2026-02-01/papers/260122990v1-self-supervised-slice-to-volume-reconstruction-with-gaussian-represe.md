---
layout: default
title: Self-Supervised Slice-to-Volume Reconstruction with Gaussian Representations for Fetal MRI
---

# Self-Supervised Slice-to-Volume Reconstruction with Gaussian Representations for Fetal MRI
**arXiv**：[2601.22990v1](https://arxiv.org/abs/2601.22990) · [PDF](https://arxiv.org/pdf/2601.22990.pdf)  
**作者**：Yinsong Wang, Thomas Fletcher, Xinzhe Luo, Aine Travers Dineen, Rhodri Cusack, Chen Qin  

**一句话要点**：提出GaussianSVR自监督框架，使用高斯表示实现胎儿MRI切片到体积重建

**关键词**：切片到体积重建, 自监督学习, 高斯表示, 胎儿MRI, 多分辨率训练

## 3 点简述
- 核心问题：胎儿MRI中运动伪影切片重建3D体积耗时且依赖多正交堆栈，学习法需真实标签
- 方法要点：采用3D高斯表示高保真重建，模拟前向切片采集模型实现自监督训练，多分辨率策略优化
- 实验或效果：在胎儿MR体积重建上优于基线方法，代码将公开

## 摘要（原文）

> Reconstructing 3D fetal MR volumes from motion-corrupted stacks of 2D slices is a crucial and challenging task. Conventional slice-to-volume reconstruction (SVR) methods are time-consuming and require multiple orthogonal stacks for reconstruction. While learning-based SVR approaches have significantly reduced the time required at the inference stage, they heavily rely on ground truth information for training, which is inaccessible in practice. To address these challenges, we propose GaussianSVR, a self-supervised framework for slice-to-volume reconstruction. GaussianSVR represents the target volume using 3D Gaussian representations to achieve high-fidelity reconstruction. It leverages a simulated forward slice acquisition model to enable self-supervised training, alleviating the need for ground-truth volumes. Furthermore, to enhance both accuracy and efficiency, we introduce a multi-resolution training strategy that jointly optimizes Gaussian parameters and spatial transformations across different resolution levels. Experiments show that GaussianSVR outperforms the baseline methods on fetal MR volumetric reconstruction. Code will be available upon acceptance.

