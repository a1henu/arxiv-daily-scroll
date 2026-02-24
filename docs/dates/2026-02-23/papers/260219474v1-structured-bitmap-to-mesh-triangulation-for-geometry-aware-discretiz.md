---
layout: default
title: Structured Bitmap-to-Mesh Triangulation for Geometry-Aware Discretization of Image-Derived Domains
---

# Structured Bitmap-to-Mesh Triangulation for Geometry-Aware Discretization of Image-Derived Domains
**arXiv**：[2602.19474v1](https://arxiv.org/abs/2602.19474) · [PDF](https://arxiv.org/pdf/2602.19474.pdf)  
**作者**：Wei Feng, Haiyong Zheng  

**一句话要点**：提出基于模板的三角化框架，用于图像衍生域的几何感知离散化，以稳定偏微分方程求解。

**关键词**：图像衍生域离散化, 模板驱动三角化, 几何感知网格生成, 偏微分方程求解, 并行计算

## 3 点简述
- 核心问题：传统约束Delaunay三角化在图像衍生域中可能导致全局连接更新，影响稳定性和并行性。
- 方法要点：通过局部边界相交配置分类，生成有限符号查找表，仅重三角化边界相交的三角形，保持基网格。
- 实验或效果：在椭圆和抛物型偏微分方程等应用中，减少细长元素，提高边界附近的几何保真度。

## 摘要（原文）

> We propose a template-driven triangulation framework that embeds raster- or segmentation-derived boundaries into a regular triangular grid for stable PDE discretization on image-derived domains. Unlike constrained Delaunay triangulation (CDT), which may trigger global connectivity updates, our method retriangulates only triangles intersected by the boundary, preserves the base mesh, and supports synchronization-free parallel execution. To ensure determinism and scalability, we classify all local boundary-intersection configurations up to discrete equivalence and triangle symmetries, yielding a finite symbolic lookup table that maps each case to a conflict-free retriangulation template. We prove that the resulting mesh is closed, has bounded angles, and is compatible with cotangent-based discretizations and standard finite element methods. Experiments on elliptic and parabolic PDEs, signal interpolation, and structural metrics show fewer sliver elements, more regular triangles, and improved geometric fidelity near complex boundaries. The framework is well suited for real-time geometric analysis and physically based simulation over image-derived domains.

