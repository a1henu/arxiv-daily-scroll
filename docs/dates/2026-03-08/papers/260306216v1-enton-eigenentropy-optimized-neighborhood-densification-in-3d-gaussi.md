---
layout: default
title: EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting
---

# EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting
**arXiv**：[2603.06216v1](https://arxiv.org/abs/2603.06216) · [PDF](https://arxiv.org/pdf/2603.06216.pdf)  
**作者**：Miriam Jäger, Boris Jutzi  

**一句话要点**：提出EntON方法，通过特征熵优化邻域密度化，提升3D高斯溅射的几何精度与渲染质量。

**关键词**：3D高斯溅射, 几何重建, 特征熵优化, 密度化策略, 交替优化, 渲染质量

## 3 点简述
- 核心问题：标准3D高斯溅射中高斯中心与物体几何对齐不佳，而表面重建方法常牺牲光度精度。
- 方法要点：引入特征熵量化局部结构秩序，结合交替优化框架，优先在低熵区域密度化以捕捉细节。
- 实验或效果：在DTU和TUM2TWIN数据集上，几何精度提升达33%，渲染质量提升达7%，高斯数量减少达50%。

## 摘要（原文）

> We present a novel Eigenentropy-optimized neighboorhood densification strategy EntON in 3D Gaussian Splatting (3DGS) for geometrically accurate and high-quality rendered 3D reconstruction. While standard 3DGS produces Gaussians whose centers and surfaces are poorly aligned with the underlying object geometry, surface-focused reconstruction methods frequently sacrifice photometric accuracy. In contrast to the conventional densification strategy, which relies on the magnitude of the view-space position gradient, our approach introduces a geometry-aware strategy to guide adaptive splitting and pruning. Specifically, we compute the 3D shape feature Eigenentropy from the eigenvalues of the covariance matrix in the k-nearest neighborhood of each Gaussian center, which quantifies the local structural order. These Eigenentropy values are integrated into an alternating optimization framework: During the optimization process, the algorithm alternates between (i) standard gradient-based densification, which refines regions via view-space gradients, and (ii) Eigenentropy-aware densification, which preferentially densifies Gaussians in low-Eigenentropy (ordered, flat) neighborhoods to better capture fine geometric details on the object surface, and prunes those in high-Eigenentropy (disordered, spherical) regions. We provide quantitative and qualitative evaluations on two benchmark datasets: small-scale DTU dataset and large-scale TUM2TWIN dataset, covering man-made objects and urban scenes. Experiments demonstrate that our Eigenentropy-aware alternating densification strategy improves geometric accuracy by up to 33% and rendering quality by up to 7%, while reducing the number of Gaussians by up to 50% and training time by up to 23%. Overall, EnTON achieves a favorable balance between geometric accuracy, rendering quality and efficiency by avoiding unnecessary scene expansion.

