---
layout: default
title: FUSE: A Flow-based Mapping Between Shapes
---

# FUSE: A Flow-based Mapping Between Shapes
**arXiv**：[2511.13431v1](https://arxiv.org/abs/2511.13431) · [PDF](https://arxiv.org/pdf/2511.13431.pdf)  
**作者**：Lorenzo Olearo, Giulio Viganò, Daniele Baieri, Filippo Maggioli, Simone Melzi  

**一句话要点**：提出基于流匹配的神经映射方法，实现高效跨表示3D形状匹配。

**关键词**：3D形状匹配, 流匹配模型, 可逆映射, 跨表示学习, UV映射

## 3 点简述
- 核心问题：3D形状间映射需高效处理点云、网格等多种表示。
- 方法要点：使用流模型构建可逆映射，从锚分布连续变换形状。
- 实验效果：在多个基准测试中实现高覆盖率和准确性。

## 摘要（原文）

> We introduce a novel neural representation for maps between 3D shapes based on flow-matching models, which is computationally efficient and supports cross-representation shape matching without large-scale training or data-driven procedures. 3D shapes are represented as the probability distribution induced by a continuous and invertible flow mapping from a fixed anchor distribution. Given a source and a target shape, the composition of the inverse flow (source to anchor) with the forward flow (anchor to target), we continuously map points between the two surfaces. By encoding the shapes with a pointwise task-tailored embedding, this construction provides an invertible and modality-agnostic representation of maps between shapes across point clouds, meshes, signed distance fields (SDFs), and volumetric data. The resulting representation consistently achieves high coverage and accuracy across diverse benchmarks and challenging settings in shape matching. Beyond shape matching, our framework shows promising results in other tasks, including UV mapping and registration of raw point cloud scans of human bodies.

