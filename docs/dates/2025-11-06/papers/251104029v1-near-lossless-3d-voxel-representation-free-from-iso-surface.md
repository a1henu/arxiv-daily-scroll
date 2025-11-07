---
layout: default
title: Near-Lossless 3D Voxel Representation Free from Iso-surface
---

# Near-Lossless 3D Voxel Representation Free from Iso-surface
**arXiv**：[2511.04029v1](https://arxiv.org/abs/2511.04029) · [PDF](https://arxiv.org/pdf/2511.04029.pdf)  
**作者**：Yihao Luo, Xianglong He, Chuanyu Pan, Yiwen Chen, Jiaqi Wu, Yangguang Li, Wanli Ouyang, Yuanming Hu, Guang Yang, ChoonHwai Yap  

**一句话要点**：提出Faithful Contouring以解决3D网格表示中几何保真度不足的问题

**关键词**：3D体素表示, 几何保真, 稀疏表示, 形状重建, 等值面自由

## 3 点简述
- 现有基于等值面的体素表示依赖水密化或渲染优化，损害几何精度
- Faithful Contouring为稀疏体素表示，无需场函数转换或等值面提取，支持高分辨率
- 实验显示，在表示和重建任务中，误差显著降低，保真度优于基线方法

## 摘要（原文）

> Accurate and efficient voxelized representations of 3D meshes are the
> foundation of 3D reconstruction and generation. However, existing
> representations based on iso-surface heavily rely on water-tightening or
> rendering optimization, which inevitably compromise geometric fidelity. We
> propose Faithful Contouring, a sparse voxelized representation that supports
> 2048+ resolutions for arbitrary meshes, requiring neither converting meshes to
> field functions nor extracting the isosurface during remeshing. It achieves
> near-lossless fidelity by preserving sharpness and internal structures, even
> for challenging cases with complex geometry and topology. The proposed method
> also shows flexibility for texturing, manipulation, and editing. Beyond
> representation, we design a dual-mode autoencoder for Faithful Contouring,
> enabling scalable and detail-preserving shape reconstruction. Extensive
> experiments show that Faithful Contouring surpasses existing methods in
> accuracy and efficiency for both representation and reconstruction. For direct
> representation, it achieves distance errors at the $10^{-5}$ level; for mesh
> reconstruction, it yields a 93\% reduction in Chamfer Distance and a 35\%
> improvement in F-score over strong baselines, confirming superior fidelity as a
> representation for 3D learning tasks.

