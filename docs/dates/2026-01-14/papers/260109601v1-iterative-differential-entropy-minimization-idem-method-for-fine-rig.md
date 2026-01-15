---
layout: default
title: Iterative Differential Entropy Minimization (IDEM) method for fine rigid pairwise 3D Point Cloud Registration: A Focus on the Metric
---

# Iterative Differential Entropy Minimization (IDEM) method for fine rigid pairwise 3D Point Cloud Registration: A Focus on the Metric
**arXiv**：[2601.09601v1](https://arxiv.org/abs/2601.09601) · [PDF](https://arxiv.org/pdf/2601.09601.pdf)  
**作者**：Emmanuele Barberi, Felice Sfravara, Filippo Cucinotta  

**一句话要点**：提出基于微分熵的IDEM方法以解决点云配准中密度差异、噪声和部分重叠问题

**关键词**：点云配准, 微分熵, 刚性配准, 优化方法, 3D计算机视觉

## 3 点简述
- 传统点云配准方法如ICP依赖欧氏距离，对密度差异、噪声和部分重叠敏感，需预处理或固定参考点云。
- IDEM方法引入微分熵作为目标函数，不依赖固定点云选择，在优化中显示清晰最小值对应最佳对齐。
- 实验表明IDEM在密度差异、噪声、孔洞和部分重叠场景下优于RMSE、Chamfer距离和Hausdorff距离。

## 摘要（原文）

> Point cloud registration is a central theme in computer vision, with alignment algorithms continuously improving for greater robustness. Commonly used methods evaluate Euclidean distances between point clouds and minimize an objective function, such as Root Mean Square Error (RMSE). However, these approaches are most effective when the point clouds are well-prealigned and issues such as differences in density, noise, holes, and limited overlap can compromise the results. Traditional methods, such as Iterative Closest Point (ICP), require choosing one point cloud as fixed, since Euclidean distances lack commutativity. When only one point cloud has issues, adjustments can be made, but in real scenarios, both point clouds may be affected, often necessitating preprocessing. The authors introduce a novel differential entropy-based metric, designed to serve as the objective function within an optimization framework for fine rigid pairwise 3D point cloud registration, denoted as Iterative Differential Entropy Minimization (IDEM). This metric does not depend on the choice of a fixed point cloud and, during transformations, reveals a clear minimum corresponding to the best alignment. Multiple case studies are conducted, and the results are compared with those obtained using RMSE, Chamfer distance, and Hausdorff distance. The proposed metric proves effective even with density differences, noise, holes, and partial overlap, where RMSE does not always yield optimal alignment.

