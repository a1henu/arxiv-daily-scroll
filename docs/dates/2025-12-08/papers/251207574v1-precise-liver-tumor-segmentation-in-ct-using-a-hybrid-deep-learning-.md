---
layout: default
title: Precise Liver Tumor Segmentation in CT Using a Hybrid Deep Learning-Radiomics Framework
---

# Precise Liver Tumor Segmentation in CT Using a Hybrid Deep Learning-Radiomics Framework
**arXiv**：[2512.07574v1](https://arxiv.org/abs/2512.07574) · [PDF](https://arxiv.org/pdf/2512.07574.pdf)  
**作者**：Xuecheng Li, Weikuan Jia, Komildzhon Sharipov, Alimov Ruslan, Lutfuloev Mazbutdzhon, Ismoilov Shuhratjon, Yuanjie Zheng  

**一句话要点**：提出混合深度学习-放射组学框架以解决CT中肝脏肿瘤精确分割问题

**关键词**：肝脏肿瘤分割, 深度学习, 放射组学, CT图像处理, 注意力机制, 3D CNN

## 3 点简述
- 核心问题：CT图像中肝脏肿瘤自动分割因低对比度、边界模糊和结构干扰而复杂
- 方法要点：结合注意力增强级联U-Net、放射组学特征筛选和3D CNN细化进行联合分割
- 实验或效果：通过多阶段处理提升分割精度，减少假阳性，实现三维轮廓平滑

## 摘要（原文）

> Accurate three-dimensional delineation of liver tumors on contrast-enhanced CT is a prerequisite for treatment planning, navigation and response assessment, yet manual contouring is slow, observer-dependent and difficult to standardise across centres. Automatic segmentation is complicated by low lesion-parenchyma contrast, blurred or incomplete boundaries, heterogeneous enhancement patterns, and confounding structures such as vessels and adjacent organs. We propose a hybrid framework that couples an attention-enhanced cascaded U-Net with handcrafted radiomics and voxel-wise 3D CNN refinement for joint liver and liver-tumor segmentation. First, a 2.5D two-stage network with a densely connected encoder, sub-pixel convolution decoders and multi-scale attention gates produces initial liver and tumor probability maps from short stacks of axial slices. Inter-slice temporal consistency is then enforced by a simple three-slice refinement rule along the cranio-caudal direction, which restores thin and tiny lesions while suppressing isolated noise. Next, 728 radiomic descriptors spanning intensity, texture, shape, boundary and wavelet feature groups are extracted from candidate lesions and reduced to 20 stable, highly informative features via multi-strategy feature selection; a random forest classifier uses these features to reject false-positive regions. Finally, a compact 3D patch-based CNN derived from AlexNet operates in a narrow band around the tumor boundary to perform voxel-level relabelling and contour smoothing.

