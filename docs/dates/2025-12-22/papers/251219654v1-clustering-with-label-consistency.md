---
layout: default
title: Clustering with Label Consistency
---

# Clustering with Label Consistency
**arXiv**：[2512.19654v1](https://arxiv.org/abs/2512.19654) · [PDF](https://arxiv.org/pdf/2512.19654.pdf)  
**作者**：Diptarka Chakraborty, Hendrik Fichtenberger, Bernhard Haeupler, Silvio Lattanzi, Ashkan Norouzi-Fard, Ola Svensson  

**一句话要点**：提出标签一致性度量聚类算法，解决传统方法忽略点标签稳定性的问题。

**关键词**：度量聚类, 标签一致性, k-center问题, k-median问题, 近似算法

## 3 点简述
- 核心问题：传统度量聚类算法关注聚类中心稳定性，但忽视点标签（点分配到命名集合）的稳定性，这在现实应用中至关重要。
- 方法要点：引入新的标签一致性概念，基于连续解之间的标签距离，设计针对k-center和k-median问题的近似算法。
- 实验或效果：未知，论文未提供具体实验细节或效果数据。

## 摘要（原文）

> Designing efficient, effective, and consistent metric clustering algorithms is a significant challenge attracting growing attention. Traditional approaches focus on the stability of cluster centers; unfortunately, this neglects the real-world need for stable point labels, i.e., stable assignments of points to named sets (clusters). In this paper, we address this gap by initiating the study of label-consistent metric clustering. We first introduce a new notion of consistency, measuring the label distance between two consecutive solutions. Then, armed with this new definition, we design new consistent approximation algorithms for the classical $k$-center and $k$-median problems.

