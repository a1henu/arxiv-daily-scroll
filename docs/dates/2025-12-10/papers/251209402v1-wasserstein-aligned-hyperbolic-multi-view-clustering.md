---
layout: default
title: Wasserstein-Aligned Hyperbolic Multi-View Clustering
---

# Wasserstein-Aligned Hyperbolic Multi-View Clustering
**arXiv**：[2512.09402v1](https://arxiv.org/abs/2512.09402) · [PDF](https://arxiv.org/pdf/2512.09402.pdf)  
**作者**：Rui Wang, Yuting Jiang, Xiaoqing Luo, Xiao-Jun Wu, Nicu Sebe, Ziheng Chen  

**一句话要点**：提出Wasserstein对齐双曲多视图聚类框架以解决多视图数据全局语义一致性问题

**关键词**：多视图聚类, 双曲表示, Wasserstein距离, 语义对齐, Lorentz流形, 全局一致性

## 3 点简述
- 多视图聚类中现有双曲表示方法忽视全局语义一致性，易受视图特定信息干扰
- 利用视图特定双曲编码器嵌入Lorentz流形，引入双曲切片Wasserstein距离对齐跨视图分布
- 在多个基准数据集上实现最先进的聚类性能，验证了方法的有效性

## 摘要（原文）

> Multi-view clustering (MVC) aims to uncover the latent structure of multi-view data by learning view-common and view-specific information. Although recent studies have explored hyperbolic representations for better tackling the representation gap between different views, they focus primarily on instance-level alignment and neglect global semantic consistency, rendering them vulnerable to view-specific information (\textit{e.g.}, noise and cross-view discrepancies). To this end, this paper proposes a novel Wasserstein-Aligned Hyperbolic (WAH) framework for multi-view clustering. Specifically, our method exploits a view-specific hyperbolic encoder for each view to embed features into the Lorentz manifold for hierarchical semantic modeling. Whereafter, a global semantic loss based on the hyperbolic sliced-Wasserstein distance is introduced to align manifold distributions across views. This is followed by soft cluster assignments to encourage cross-view semantic consistency. Extensive experiments on multiple benchmarking datasets show that our method can achieve SOTA clustering performance.

