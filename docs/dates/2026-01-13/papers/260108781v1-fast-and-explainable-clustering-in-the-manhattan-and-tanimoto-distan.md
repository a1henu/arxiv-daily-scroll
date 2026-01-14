---
layout: default
title: Fast and explainable clustering in the Manhattan and Tanimoto distance
---

# Fast and explainable clustering in the Manhattan and Tanimoto distance
**arXiv**：[2601.08781v1](https://arxiv.org/abs/2601.08781) · [PDF](https://arxiv.org/pdf/2601.08781.pdf)  
**作者**：Stefan Güttel, Kaustubh Roy  

**一句话要点**：扩展CLASSIX算法至曼哈顿与Tanimoto距离，实现快速可解释聚类

**关键词**：聚类算法, 距离度量, 可解释性, 性能优化, 化学指纹分析

## 3 点简述
- 核心问题：原始CLASSIX算法仅支持欧氏距离，限制了其在其他距离度量下的应用。
- 方法要点：使用数据向量范数排序并结合三角不等式，针对Tanimoto距离采用更锐利的交集不等式优化性能。
- 实验或效果：在化学指纹基准测试中，新算法比Taylor-Butina快约30倍，比DBSCAN快约80倍，且聚类质量更高。

## 摘要（原文）

> The CLASSIX algorithm is a fast and explainable approach to data clustering. In its original form, this algorithm exploits the sorting of the data points by their first principal component to truncate the search for nearby data points, with nearness being defined in terms of the Euclidean distance. Here we extend CLASSIX to other distance metrics, including the Manhattan distance and the Tanimoto distance. Instead of principal components, we use an appropriate norm of the data vectors as the sorting criterion, combined with the triangle inequality for search termination. In the case of Tanimoto distance, a provably sharper intersection inequality is used to further boost the performance of the new algorithm. On a real-world chemical fingerprint benchmark, CLASSIX Tanimoto is about 30 times faster than the Taylor--Butina algorithm, and about 80 times faster than DBSCAN, while computing higher-quality clusters in both cases.

