---
layout: default
title: NeuralSSD: A Neural Solver for Signed Distance Surface Reconstruction
---

# NeuralSSD: A Neural Solver for Signed Distance Surface Reconstruction
**arXiv**：[2511.14283v1](https://arxiv.org/abs/2511.14283) · [PDF](https://arxiv.org/pdf/2511.14283.pdf)  
**作者**：Zi-Chen Xi, Jiahui Huang, Hao-Xiang Chen, Francis Williams, Qun-Ce Xu, Tai-Jiang Mu, Shi-Min Hu  

**一句话要点**：提出NeuralSSD方法以从点云数据重建高质量3D隐式表面

**关键词**：3D表面重建, 隐式表面, 点云处理, 神经Galerkin方法, 卷积网络, 能量方程优化

## 3 点简述
- 核心问题：现有隐式场参数化缺乏确保表面与输入点云紧密拟合的机制。
- 方法要点：基于神经Galerkin方法，引入新能量方程和卷积网络优化表面重建。
- 实验或效果：在ShapeNet等数据集上实现最先进的表面重建精度和泛化性。

## 摘要（原文）

> We proposed a generalized method, NeuralSSD, for reconstructing a 3D implicit surface from the widely-available point cloud data. NeuralSSD is a solver-based on the neural Galerkin method, aimed at reconstructing higher-quality and accurate surfaces from input point clouds. Implicit method is preferred due to its ability to accurately represent shapes and its robustness in handling topological changes. However, existing parameterizations of implicit fields lack explicit mechanisms to ensure a tight fit between the surface and input data. To address this, we propose a novel energy equation that balances the reliability of point cloud information. Additionally, we introduce a new convolutional network that learns three-dimensional information to achieve superior optimization results. This approach ensures that the reconstructed surface closely adheres to the raw input points and infers valuable inductive biases from point clouds, resulting in a highly accurate and stable surface reconstruction. NeuralSSD is evaluated on a variety of challenging datasets, including the ShapeNet and Matterport datasets, and achieves state-of-the-art results in terms of both surface reconstruction accuracy and generalizability.

