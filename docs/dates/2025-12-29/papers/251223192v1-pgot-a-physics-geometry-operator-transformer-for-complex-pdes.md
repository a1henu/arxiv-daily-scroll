---
layout: default
title: PGOT: A Physics-Geometry Operator Transformer for Complex PDEs
---

# PGOT: A Physics-Geometry Operator Transformer for Complex PDEs
**arXiv**：[2512.23192v1](https://arxiv.org/abs/2512.23192) · [PDF](https://arxiv.org/pdf/2512.23192.pdf)  
**作者**：Zhuo Zhang, Xi Yang, Yuan Zhao, Canqun Yang  

**一句话要点**：提出PGOT以解决复杂几何下PDE建模中的几何混叠问题

**关键词**：偏微分方程建模, 几何感知Transformer, 多尺度几何编码, 空间自适应计算, 工业仿真

## 3 点简述
- 核心问题：Transformer建模大规模非结构化网格时，特征降维导致几何混叠，丢失物理边界信息。
- 方法要点：设计SpecGeo-Attention模块，通过物理切片-几何注入机制，显式保留多尺度几何特征，保持线性计算复杂度。
- 实验或效果：在四个标准基准测试中达到SOTA，并在翼型和汽车设计等工业任务中表现优异。

## 摘要（原文）

> While Transformers have demonstrated remarkable potential in modeling Partial Differential Equations (PDEs), modeling large-scale unstructured meshes with complex geometries remains a significant challenge. Existing efficient architectures often employ feature dimensionality reduction strategies, which inadvertently induces Geometric Aliasing, resulting in the loss of critical physical boundary information. To address this, we propose the Physics-Geometry Operator Transformer (PGOT), designed to reconstruct physical feature learning through explicit geometry awareness. Specifically, we propose Spectrum-Preserving Geometric Attention (SpecGeo-Attention). Utilizing a ``physics slicing-geometry injection" mechanism, this module incorporates multi-scale geometric encodings to explicitly preserve multi-scale geometric features while maintaining linear computational complexity $O(N)$. Furthermore, PGOT dynamically routes computations to low-order linear paths for smooth regions and high-order non-linear paths for shock waves and discontinuities based on spatial coordinates, enabling spatially adaptive and high-precision physical field modeling. PGOT achieves consistent state-of-the-art performance across four standard benchmarks and excels in large-scale industrial tasks including airfoil and car designs.

