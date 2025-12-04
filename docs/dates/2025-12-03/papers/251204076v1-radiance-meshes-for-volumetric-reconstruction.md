---
layout: default
title: Radiance Meshes for Volumetric Reconstruction
---

# Radiance Meshes for Volumetric Reconstruction
**arXiv**：[2512.04076v1](https://arxiv.org/abs/2512.04076) · [PDF](https://arxiv.org/pdf/2512.04076.pdf)  
**作者**：Alexander Mai, Trevor Hedstrom, George Kopanas, Janne Kontkanen, Falko Kuester, Jonathan T. Barron  

**一句话要点**：提出辐射网格技术，利用Delaunay四面体化实现高质量实时视图合成

**关键词**：辐射场表示, Delaunay四面体化, 实时渲染, 视图合成, 体积重建, 网格提取

## 3 点简述
- 核心问题：传统辐射场表示在渲染速度和质量上存在限制，难以在消费硬件上实时应用
- 方法要点：基于Delaunay四面体化构建恒定密度四面体网格，结合Zip-NeRF风格骨干网络处理拓扑变化
- 实验或效果：在多种平台上实现比现有方法更快的渲染速度，支持高质量实时视图合成和多种应用

## 摘要（原文）

> We introduce radiance meshes, a technique for representing radiance fields with constant density tetrahedral cells produced with a Delaunay tetrahedralization. Unlike a Voronoi diagram, a Delaunay tetrahedralization yields simple triangles that are natively supported by existing hardware. As such, our model is able to perform exact and fast volume rendering using both rasterization and ray-tracing. We introduce a new rasterization method that achieves faster rendering speeds than all prior radiance field representations (assuming an equivalent number of primitives and resolution) across a variety of platforms. Optimizing the positions of Delaunay vertices introduces topological discontinuities (edge flips). To solve this, we use a Zip-NeRF-style backbone which allows us to express a smoothly varying field even when the topology changes. Our rendering method exactly evaluates the volume rendering equation and enables high quality, real-time view synthesis on standard consumer hardware. Our tetrahedral meshes also lend themselves to a variety of exciting applications including fisheye lens distortion, physics-based simulation, editing, and mesh extraction.

