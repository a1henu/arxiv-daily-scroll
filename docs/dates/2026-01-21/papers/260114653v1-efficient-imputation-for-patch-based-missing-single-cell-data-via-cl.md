---
layout: default
title: Efficient Imputation for Patch-based Missing Single-cell Data via Cluster-regularized Optimal Transport
---

# Efficient Imputation for Patch-based Missing Single-cell Data via Cluster-regularized Optimal Transport
**arXiv**：[2601.14653v1](https://arxiv.org/abs/2601.14653) · [PDF](https://arxiv.org/pdf/2601.14653.pdf)  
**作者**：Yuyu Liu, Jiannan Yang, Ziyang Yu, Weishen Pan, Fei Wang, Tengfei Ma  

**一句话要点**：提出CROT算法，基于最优传输处理单细胞数据中的块状缺失问题

**关键词**：单细胞数据插补, 最优传输, 聚类正则化, 块状缺失处理, 高效算法

## 3 点简述
- 核心问题：单细胞测序数据存在块状缺失，传统方法难以处理大规模缺失情况
- 方法要点：利用最优传输结合聚类正则化，有效捕捉数据底层结构
- 实验或效果：在保持高精度的同时显著减少运行时间，适用于大规模数据集

## 摘要（原文）

> Missing data in single-cell sequencing datasets poses significant challenges for extracting meaningful biological insights. However, existing imputation approaches, which often assume uniformity and data completeness, struggle to address cases with large patches of missing data. In this paper, we present CROT, an optimal transport-based imputation algorithm designed to handle patch-based missing data in tabular formats. Our approach effectively captures the underlying data structure in the presence of significant missingness. Notably, it achieves superior imputation accuracy while significantly reducing runtime, demonstrating its scalability and efficiency for large-scale datasets. This work introduces a robust solution for imputation in heterogeneous, high-dimensional datasets with structured data absence, addressing critical challenges in both biological and clinical data analysis. Our code is available at Anomalous Github.

