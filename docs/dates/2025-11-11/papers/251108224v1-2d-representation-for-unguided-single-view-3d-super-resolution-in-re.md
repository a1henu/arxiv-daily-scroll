---
layout: default
title: 2D Representation for Unguided Single-View 3D Super-Resolution in Real-Time
---

# 2D Representation for Unguided Single-View 3D Super-Resolution in Real-Time
**arXiv**：[2511.08224v1](https://arxiv.org/abs/2511.08224) · [PDF](https://arxiv.org/pdf/2511.08224.pdf)  
**作者**：Ignasi Mas, Ivan Huerta, Ramon Morros, Javier Ruiz-Hidalgo  

**一句话要点**：提出2Dto3D-SR框架，实现无高分辨率RGB引导的实时单视图3D超分辨率。

**关键词**：3D超分辨率, 单视图重建, 2D表示, 实时处理, 几何编码, 轻量模型

## 3 点简述
- 核心问题：单视图3D超分辨率需高分辨率RGB引导，复杂且不实用。
- 方法要点：将3D数据编码为2D表示，直接应用2D超分辨率架构。
- 实验效果：Swin Transformer版精度领先，Vision Mamba版实时高效。

## 摘要（原文）

> We introduce 2Dto3D-SR, a versatile framework for real-time single-view 3D super-resolution that eliminates the need for high-resolution RGB guidance. Our framework encodes 3D data from a single viewpoint into a structured 2D representation, enabling the direct application of existing 2D image super-resolution architectures. We utilize the Projected Normalized Coordinate Code (PNCC) to represent 3D geometry from a visible surface as a regular image, thereby circumventing the complexities of 3D point-based or RGB-guided methods. This design supports lightweight and fast models adaptable to various deployment environments. We evaluate 2Dto3D-SR with two implementations: one using Swin Transformers for high accuracy, and another using Vision Mamba for high efficiency. Experiments show the Swin Transformer model achieves state-of-the-art accuracy on standard benchmarks, while the Vision Mamba model delivers competitive results at real-time speeds. This establishes our geometry-guided pipeline as a surprisingly simple yet viable and practical solution for real-world scenarios, especially where high-resolution RGB data is inaccessible.

