---
layout: default
title: Accurate and Efficient Surface Reconstruction from Point Clouds via Geometry-Aware Local Adaptation
---

# Accurate and Efficient Surface Reconstruction from Point Clouds via Geometry-Aware Local Adaptation
**arXiv**：[2511.08233v1](https://arxiv.org/abs/2511.08233) · [PDF](https://arxiv.org/pdf/2511.08233.pdf)  
**作者**：Eito Ogawa, Taiga Hayami, Hiroshi Watanabe  

**一句话要点**：提出基于曲率自适应调节局部区域的方法，以提高点云表面重建的精度和效率。

**关键词**：点云表面重建, 局部区域自适应, 曲率估计, 深度学习, 几何复杂度

## 3 点简述
- 核心问题：现有方法局部区域固定，难以适应几何复杂度变化。
- 方法要点：根据点云曲率自适应调整局部区域的间距和大小。
- 实验或效果：未知，但声称改进重建精度和效率。

## 摘要（原文）

> Point cloud surface reconstruction has improved in accuracy with advances in deep learning, enabling applications such as infrastructure inspection. Recent approaches that reconstruct from small local regions rather than entire point clouds have attracted attention for their strong generalization capability. However, prior work typically places local regions uniformly and keeps their size fixed, limiting adaptability to variations in geometric complexity. In this study, we propose a method that improves reconstruction accuracy and efficiency by adaptively modulating the spacing and size of local regions based on the curvature of the input point cloud.

