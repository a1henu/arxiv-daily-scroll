---
layout: default
title: Understanding and Improving UMAP with Geometric and Topological Priors: The JORC-UMAP Algorithm
---

# Understanding and Improving UMAP with Geometric and Topological Priors: The JORC-UMAP Algorithm
**arXiv**：[2601.16552v1](https://arxiv.org/abs/2601.16552) · [PDF](https://arxiv.org/pdf/2601.16552.pdf)  
**作者**：Xiaobin Li, Run Zhang  

**一句话要点**：提出JORC-UMAP算法，通过几何与拓扑先验改进UMAP以解决拓扑撕裂和结构塌陷问题。

**关键词**：非线性降维, UMAP改进, 几何先验, 拓扑先验, 数据可视化, 流形学习

## 3 点简述
- 核心问题：UMAP基于局部欧氏距离假设，难以捕捉内在流形几何，导致拓扑撕裂和结构塌陷。
- 方法要点：引入Ollivier-Ricci曲率作为几何先验，结合Jaccard相似性作为拓扑先验，优化k近邻图构建。
- 实验或效果：在合成和真实数据集上，JORC-UMAP减少撕裂和塌陷，提升SVM准确率和三元组保持分数，保持计算效率。

## 摘要（原文）

> Nonlinear dimensionality reduction techniques, particularly UMAP, are widely used for visualizing high-dimensional data. However, UMAP's local Euclidean distance assumption often fails to capture intrinsic manifold geometry, leading to topological tearing and structural collapse. We identify UMAP's sensitivity to the k-nearest neighbor graph as a key cause. To address this, we introduce Ollivier-Ricci curvature as a geometric prior, reinforcing edges at geometric bottlenecks and reducing redundant links. Since curvature estimation is noise-sensitive, we also incorporate a topological prior using Jaccard similarity to ensure neighborhood consistency. The resulting method, JORC-UMAP, better distinguishes true manifold structure from spurious connections. Experiments on synthetic and real-world datasets show that JORC-UMAP reduces tearing and collapse more effectively than standard UMAP and other DR methods, as measured by SVM accuracy and triplet preservation scores, while maintaining computational efficiency. This work offers a geometry-aware enhancement to UMAP for more faithful data visualization.

