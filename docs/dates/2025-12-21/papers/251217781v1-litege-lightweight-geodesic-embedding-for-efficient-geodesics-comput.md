---
layout: default
title: LiteGE: Lightweight Geodesic Embedding for Efficient Geodesics Computation and Non-Isometric Shape Correspondence
---

# LiteGE: Lightweight Geodesic Embedding for Efficient Geodesics Computation and Non-Isometric Shape Correspondence
**arXiv**：[2512.17781v1](https://arxiv.org/abs/2512.17781) · [PDF](https://arxiv.org/pdf/2512.17781.pdf)  
**作者**：Yohanes Yudhi Adikusuma, Qixing Huang, Ying He  

**一句话要点**：提出LiteGE轻量级方法，通过PCA处理UDF样本构建紧凑描述符，以高效计算测地距离并支持非等距形状对应。

**关键词**：轻量级测地嵌入, 无符号距离场, PCA降维, 形状对应, 稀疏点云处理, 高效计算

## 3 点简述
- 核心问题：现有基于学习的方法依赖大型3D骨干网络，导致高内存和延迟，限制在交互或资源受限场景中的应用。
- 方法要点：使用PCA对信息体素处的无符号距离场样本进行降维，构建类别感知的轻量级形状描述符，无需高容量网络。
- 实验或效果：在稀疏点云（如300点）上保持鲁棒性，相比现有神经方法内存和推理时间减少高达300倍，非等距形状匹配速度提升高达1000倍。

## 摘要（原文）

> Computing geodesic distances on 3D surfaces is fundamental to many tasks in 3D vision and geometry processing, with deep connections to tasks such as shape correspondence. Recent learning-based methods achieve strong performance but rely on large 3D backbones, leading to high memory usage and latency, which limit their use in interactive or resource-constrained settings. We introduce LiteGE, a lightweight approach that constructs compact, category-aware shape descriptors by applying PCA to unsigned distance field (UDFs) samples at informative voxels. This descriptor is efficient to compute and removes the need for high-capacity networks. LiteGE remains robust on sparse point clouds, supporting inputs with as few as 300 points, where prior methods fail. Extensive experiments show that LiteGE reduces memory usage and inference time by up to 300$\times$ compared to existing neural approaches. In addition, by exploiting the intrinsic relationship between geodesic distance and shape correspondence, LiteGE enables fast and accurate shape matching. Our method achieves up to 1000$\times$ speedup over state-of-the-art mesh-based approaches while maintaining comparable accuracy on non-isometric shape pairs, including evaluations on point-cloud inputs.

