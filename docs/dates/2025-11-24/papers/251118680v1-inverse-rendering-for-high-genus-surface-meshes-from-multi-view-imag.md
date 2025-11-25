---
layout: default
title: Inverse Rendering for High-Genus Surface Meshes from Multi-View Images
---

# Inverse Rendering for High-Genus Surface Meshes from Multi-View Images
**arXiv**：[2511.18680v1](https://arxiv.org/abs/2511.18680) · [PDF](https://arxiv.org/pdf/2511.18680.pdf)  
**作者**：Xiang Gao, Xinmu Wang, Xiaolong Wu, Jiazhi Li, Jingyu Shi, Yu Guo, Yuanpeng Liu, Xiyun Song, Heather Yu, Zongfang Lin, Xianfeng David Gu  

**一句话要点**：提出拓扑感知逆渲染方法以重建高亏格表面网格

**关键词**：逆渲染, 高亏格表面, 网格重建, 拓扑优化, 多视图图像

## 3 点简述
- 现有逆渲染方法在高亏格表面易丢失拓扑特征，低亏格表面过度平滑
- 采用自适应V循环重网格和重参数化Adam优化器，增强拓扑与几何感知
- 实验显示在Chamfer距离和体积IoU上优于现有方法，提升表面细节

## 摘要（原文）

> We present a topology-informed inverse rendering approach for reconstructing high-genus surface meshes from multi-view images. Compared to 3D representations like voxels and point clouds, mesh-based representations are preferred as they enable the application of differential geometry theory and are optimized for modern graphics pipelines. However, existing inverse rendering methods often fail catastrophically on high-genus surfaces, leading to the loss of key topological features, and tend to oversmooth low-genus surfaces, resulting in the loss of surface details. This failure stems from their overreliance on Adam-based optimizers, which can lead to vanishing and exploding gradients. To overcome these challenges, we introduce an adaptive V-cycle remeshing scheme in conjunction with a re-parametrized Adam optimizer to enhance topological and geometric awareness. By periodically coarsening and refining the deforming mesh, our method informs mesh vertices of their current topology and geometry before optimization, mitigating gradient issues while preserving essential topological features. Additionally, we enforce topological consistency by constructing topological primitives with genus numbers that match those of ground truth using Gauss-Bonnet theorem. Experimental results demonstrate that our inverse rendering approach outperforms the current state-of-the-art method, achieving significant improvements in Chamfer Distance and Volume IoU, particularly for high-genus surfaces, while also enhancing surface details for low-genus surfaces.

