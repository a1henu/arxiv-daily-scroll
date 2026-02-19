---
layout: default
title: Neighborhood Stability as a Measure of Nearest Neighbor Searchability
---

# Neighborhood Stability as a Measure of Nearest Neighbor Searchability
**arXiv**：[2602.16673v1](https://arxiv.org/abs/2602.16673) · [PDF](https://arxiv.org/pdf/2602.16673.pdf)  
**作者**：Thomas Vecchiato, Sebastian Bruch  

**一句话要点**：提出邻域稳定性度量以评估聚类近似最近邻搜索的适用性

**关键词**：近似最近邻搜索, 聚类分析, 邻域稳定性, 高维数据, 搜索性评估

## 3 点简述
- 核心问题：缺乏分析工具评估聚类近似最近邻搜索对数据集的适用性
- 方法要点：定义聚类邻域稳定性度量和点邻域稳定性度量，基于最近邻关系而非距离
- 实验或效果：度量预测搜索准确性，适用于多种距离函数如内积

## 摘要（原文）

> Clustering-based Approximate Nearest Neighbor Search (ANNS) organizes a set of points into partitions, and searches only a few of them to find the nearest neighbors of a query. Despite its popularity, there are virtually no analytical tools to determine the suitability of clustering-based ANNS for a given dataset -- what we call "searchability." To address that gap, we present two measures for flat clusterings of high-dimensional points in Euclidean space. First is Clustering-Neighborhood Stability Measure (clustering-NSM), an internal measure of clustering quality -- a function of a clustering of a dataset -- that we show to be predictive of ANNS accuracy. The second, Point-Neighborhood Stability Measure (point-NSM), is a measure of clusterability -- a function of the dataset itself -- that is predictive of clustering-NSM. The two together allow us to determine whether a dataset is searchable by clustering-based ANNS given only the data points. Importantly, both are functions of nearest neighbor relationships between points, not distances, making them applicable to various distance functions including inner product.

