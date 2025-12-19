---
layout: default
title: Enhanced 3D Shape Analysis via Information Geometry
---

# Enhanced 3D Shape Analysis via Information Geometry
**arXiv**：[2512.16213v1](https://arxiv.org/abs/2512.16213) · [PDF](https://arxiv.org/pdf/2512.16213.pdf)  
**作者**：Amit Vishwakarma, K. S. Subrahamanian Moosath  

**一句话要点**：提出基于信息几何的改进对称KL散度，以稳定比较三维点云形状。

**关键词**：三维点云分析, 信息几何, 高斯混合模型, KL散度, 形状比较, 统计流形

## 3 点简述
- 三维点云比较面临无结构性和几何复杂性挑战，传统度量如Hausdorff距离易受异常值影响。
- 将点云建模为高斯混合模型，证明其构成统计流形，并设计有理论上界的改进对称KL散度。
- 在人体姿态和动物形状数据集上实验，MSKL提供稳定单调值，优于传统距离和现有KL近似。

## 摘要（原文）

> Three-dimensional point clouds provide highly accurate digital representations of objects, essential for applications in computer graphics, photogrammetry, computer vision, and robotics. However, comparing point clouds faces significant challenges due to their unstructured nature and the complex geometry of the surfaces they represent. Traditional geometric metrics such as Hausdorff and Chamfer distances often fail to capture global statistical structure and exhibit sensitivity to outliers, while existing Kullback-Leibler (KL) divergence approximations for Gaussian Mixture Models can produce unbounded or numerically unstable values. This paper introduces an information geometric framework for 3D point cloud shape analysis by representing point clouds as Gaussian Mixture Models (GMMs) on a statistical manifold. We prove that the space of GMMs forms a statistical manifold and propose the Modified Symmetric Kullback-Leibler (MSKL) divergence with theoretically guaranteed upper and lower bounds, ensuring numerical stability for all GMM comparisons. Through comprehensive experiments on human pose discrimination (MPI-FAUST dataset) and animal shape comparison (G-PCD dataset), we demonstrate that MSKL provides stable and monotonically varying values that directly reflect geometric variation, outperforming traditional distances and existing KL approximations.

