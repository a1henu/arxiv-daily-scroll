---
layout: default
title: VecSet-Edit: Unleashing Pre-trained LRM for Mesh Editing from Single Image
---

# VecSet-Edit: Unleashing Pre-trained LRM for Mesh Editing from Single Image
**arXiv**：[2602.04349v1](https://arxiv.org/abs/2602.04349) · [PDF](https://arxiv.org/pdf/2602.04349.pdf)  
**作者**：Teng-Fang Hsiao, Bo-Kai Ruan, Yu-Lun Liu, Hong-Han Shuai  

**一句话要点**：提出VecSet-Edit，利用预训练LRM从单图像编辑3D网格

**关键词**：3D网格编辑, 单图像重建, 令牌化表示, 注意力机制, 纹理烘焙

## 3 点简述
- 核心问题：现有方法依赖体素或多视图，网格编辑分辨率低且需3D掩码
- 方法要点：基于VecSet令牌空间分析，引入掩码引导令牌播种和注意力对齐令牌门控
- 实验或效果：通过漂移感知令牌剪枝和细节保留纹理烘焙，提升编辑精度与保真度

## 摘要（原文）

> 3D editing has emerged as a critical research area to provide users with flexible control over 3D assets. While current editing approaches predominantly focus on 3D Gaussian Splatting or multi-view images, the direct editing of 3D meshes remains underexplored. Prior attempts, such as VoxHammer, rely on voxel-based representations that suffer from limited resolution and necessitate labor-intensive 3D mask. To address these limitations, we propose \textbf{VecSet-Edit}, the first pipeline that leverages the high-fidelity VecSet Large Reconstruction Model (LRM) as a backbone for mesh editing. Our approach is grounded on a analysis of the spatial properties in VecSet tokens, revealing that token subsets govern distinct geometric regions. Based on this insight, we introduce Mask-guided Token Seeding and Attention-aligned Token Gating strategies to precisely localize target regions using only 2D image conditions. Also, considering the difference between VecSet diffusion process versus voxel we design a Drift-aware Token Pruning to reject geometric outliers during the denoising process. Finally, our Detail-preserving Texture Baking module ensures that we not only preserve the geometric details of original mesh but also the textural information. More details can be found in our project page: https://github.com/BlueDyee/VecSet-Edit/tree/main

