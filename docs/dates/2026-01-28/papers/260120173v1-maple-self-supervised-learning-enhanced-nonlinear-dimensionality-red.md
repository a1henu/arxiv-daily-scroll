---
layout: default
title: MAPLE: Self-supervised Learning-Enhanced Nonlinear Dimensionality Reduction for Visual Analysis
---

# MAPLE: Self-supervised Learning-Enhanced Nonlinear Dimensionality Reduction for Visual Analysis
**arXiv**：[2601.20173v1](https://arxiv.org/abs/2601.20173) · [PDF](https://arxiv.org/pdf/2601.20173.pdf)  
**作者**：Zeyang Huang, Takanori Fujiwara, Angelos Chatzimparmpas, Wandrille Duchemin, Andreas Kerren  

**一句话要点**：提出MAPLE非线性降维方法，通过自监督学习增强UMAP的流形建模能力，适用于高维生物或图像数据。

**关键词**：非线性降维, 自监督学习, 流形建模, UMAP增强, 视觉分析, 高维数据

## 3 点简述
- 核心问题：UMAP在复杂流形结构和高簇内方差数据中建模不足，影响视觉分析效果。
- 方法要点：采用自监督学习和最大流形容量表示，压缩相似点方差并放大不相似点方差，以优化低维流形几何编码。
- 实验或效果：定性和定量评估显示，MAPLE比UMAP产生更清晰的视觉簇分离和更细的子簇分辨率，计算成本相当。

## 摘要（原文）

> We present a new nonlinear dimensionality reduction method, MAPLE, that enhances UMAP by improving manifold modeling. MAPLE employs a self-supervised learning approach to more efficiently encode low-dimensional manifold geometry. Central to this approach are maximum manifold capacity representations (MMCRs), which help untangle complex manifolds by compressing variances among locally similar data points while amplifying variance among dissimilar data points. This design is particularly effective for high-dimensional data with substantial intra-cluster variance and curved manifold structures, such as biological or image data. Our qualitative and quantitative evaluations demonstrate that MAPLE can produce clearer visual cluster separations and finer subcluster resolution than UMAP while maintaining comparable computational cost.

