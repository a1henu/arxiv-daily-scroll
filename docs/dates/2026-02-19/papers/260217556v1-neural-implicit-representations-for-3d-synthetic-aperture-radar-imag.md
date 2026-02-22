---
layout: default
title: Neural Implicit Representations for 3D Synthetic Aperture Radar Imaging
---

# Neural Implicit Representations for 3D Synthetic Aperture Radar Imaging
**arXiv**：[2602.17556v1](https://arxiv.org/abs/2602.17556) · [PDF](https://arxiv.org/pdf/2602.17556.pdf)  
**作者**：Nithin Sugavanam, Emre Ertin  

**一句话要点**：提出神经隐式表示以解决3D合成孔径雷达成像中的稀疏数据重建问题

**关键词**：合成孔径雷达, 神经隐式表示, 3D成像, 表面散射建模, 有符号距离函数

## 3 点简述
- 核心问题：SAR测量数据在傅里叶域稀疏，导致重建图像存在显著伪影。
- 方法要点：使用神经结构建模表面散射，学习有符号距离函数表示物体表面。
- 实验或效果：在单车辆和多车辆场景的实测与模拟数据上验证模型有效性。

## 摘要（原文）

> Synthetic aperture radar (SAR) is a tomographic sensor that measures 2D slices of the 3D spatial Fourier transform of the scene. In many operational scenarios, the measured set of 2D slices does not fill the 3D space in the Fourier domain, resulting in significant artifacts in the reconstructed imagery. Traditionally, simple priors, such as sparsity in the image domain, are used to regularize the inverse problem. In this paper, we review our recent work that achieves state-of-the-art results in 3D SAR imaging employing neural structures to model the surface scattering that dominates SAR returns. These neural structures encode the surface of the objects in the form of a signed distance function learned from the sparse scattering data. Since estimating a smooth surface from a sparse and noisy point cloud is an ill-posed problem, we regularize the surface estimation by sampling points from the implicit surface representation during the training step. We demonstrate the model's ability to represent target scattering using measured and simulated data from single vehicles and a larger scene with a large number of vehicles. We conclude with future research directions calling for methods to learn complex-valued neural representations to enable synthesizing new collections from the volumetric neural implicit representation.

