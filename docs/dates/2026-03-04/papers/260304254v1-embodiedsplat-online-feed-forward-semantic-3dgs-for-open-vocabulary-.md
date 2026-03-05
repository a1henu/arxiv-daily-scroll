---
layout: default
title: EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding
---

# EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding
**arXiv**：[2603.04254v1](https://arxiv.org/abs/2603.04254) · [PDF](https://arxiv.org/pdf/2603.04254.pdf)  
**作者**：Seungjun Lee, Zihan Wang, Yunsong Wang, Gim Hee Lee  

**一句话要点**：提出EmbodiedSplat实现在线前馈语义3DGS，用于开放词汇3D场景理解

**关键词**：3D高斯溅射, 开放词汇理解, 在线重建, 语义嵌入, CLIP特征, 几何感知

## 3 点简述
- 核心问题：现有开放词汇3DGS方法通常限于离线或逐场景优化，难以支持在线实时3D重建与语义理解。
- 方法要点：设计在线稀疏系数场与CLIP全局码本，将2D CLIP嵌入绑定到3D高斯，并通过3D U-Net聚合点云生成几何感知特征。
- 实验或效果：在ScanNet等室内数据集上验证了方法的有效性和效率，支持近实时3D语义重建。

## 摘要（原文）

> Understanding a 3D scene immediately with its exploration is essential for embodied tasks, where an agent must construct and comprehend the 3D scene in an online and nearly real-time manner. In this study, we propose EmbodiedSplat, an online feed-forward 3DGS for open-vocabulary scene understanding that enables simultaneous online 3D reconstruction and 3D semantic understanding from the streaming images. Unlike existing open-vocabulary 3DGS methods which are typically restricted to either offline or per-scene optimization setting, our objectives are two-fold: 1) Reconstructs the semantic-embedded 3DGS of the entire scene from over 300 streaming images in an online manner. 2) Highly generalizable to novel scenes with feed-forward design and supports nearly real-time 3D semantic reconstruction when combined with real-time 2D models. To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while minimizing memory consumption and preserving the full semantic generalizability of CLIP. Furthermore, we generate 3D geometric-aware CLIP features by aggregating the partial point cloud of 3DGS through 3D U-Net to compensate the 3D geometric prior to 2D-oriented language embeddings. Extensive experiments on diverse indoor datasets, including ScanNet, ScanNet++, and Replica, demonstrate both the effectiveness and efficiency of our method. Check out our project page in https://0nandon.github.io/EmbodiedSplat/.

