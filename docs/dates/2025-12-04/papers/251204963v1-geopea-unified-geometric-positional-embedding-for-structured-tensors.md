---
layout: default
title: GeoPE:A Unified Geometric Positional Embedding for Structured Tensors
---

# GeoPE:A Unified Geometric Positional Embedding for Structured Tensors
**arXiv**：[2512.04963v1](https://arxiv.org/abs/2512.04963) · [PDF](https://arxiv.org/pdf/2512.04963.pdf)  
**作者**：Yupu Yao, Bowen Yang  

**一句话要点**：提出GeoPE以解决Vision Transformers中2D空间拓扑破坏问题，通过四元数扩展旋转到3D欧几里得空间。

**关键词**：几何位置嵌入, Vision Transformers, 四元数旋转, 空间拓扑, 图像分类, 3D语义分割

## 3 点简述
- 核心问题：标准Vision Transformers将2D图像展平为1D序列，破坏空间拓扑，导致空间距离与序列邻近性混淆。
- 方法要点：使用四元数在3D欧几里得空间中扩展旋转，通过李代数几何平均构建统一旋转算子，实现几何耦合编码。
- 实验或效果：在图像分类、目标检测和3D语义分割实验中，GeoPE优于现有2D RoPE变体，显著增强形状偏差。

## 摘要（原文）

> Standard Vision Transformers flatten 2D images into 1D sequences, disrupting the natural spatial topology. While Rotary Positional Embedding (RoPE) excels in 1D, it inherits this limitation, often treating spatially distant patches (e.g., at row edges) as sequence neighbors. Existing 2D approaches typically treat spatial axes independently, failing to decouple this false sequential proximity from true spatial distance. To restore the 2D spatial manifold, we introduce Geometric Positional Embedding (GeoPE), a framework that extends rotations to 3D Euclidean space using quaternions. To overcome non-commutativity and ensure symmetry, GeoPE constructs a unified rotational operator by computing the geometric mean in the Lie algebra. This creates a geometrically coupled encoding that effectively separates spatial dimensions. Extensive experiments on image classification, object detection, and 3D semantic segmentation demonstrate that GeoPE consistently outperforms existing 2D RoPE variants and significantly enhances shape bias, confirming its ability to capture true geometric structure.

