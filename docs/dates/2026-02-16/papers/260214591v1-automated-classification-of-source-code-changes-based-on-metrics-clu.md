---
layout: default
title: Automated Classification of Source Code Changes Based on Metrics Clustering in the Software Development Process
---

# Automated Classification of Source Code Changes Based on Metrics Clustering in the Software Development Process
**arXiv**：[2602.14591v1](https://arxiv.org/abs/2602.14591) · [PDF](https://arxiv.org/pdf/2602.14591.pdf)  
**作者**：Evgenii Kniazev  

**一句话要点**：提出基于度量聚类自动分类源代码变更的方法，以加速软件开发中的代码审查过程。

**关键词**：源代码变更分类, 度量聚类, k-means算法, 代码审查自动化, 软件工程

## 3 点简述
- 核心问题：软件开发中手动分类源代码变更耗时，需自动化方法提高效率。
- 方法要点：使用k-means算法和余弦相似度对11个代码度量进行聚类，专家映射聚类到预定义类别。
- 实验或效果：在五个软件系统验证，分类纯度约0.75，熵约0.37，显著减少审查时间。

## 摘要（原文）

> This paper presents an automated method for classifying source code changes during the software development process based on clustering of change metrics. The method consists of two steps: clustering of metric vectors computed for each code change, followed by expert mapping of the resulting clusters to predefined change classes. The distribution of changes into clusters is performed automatically, while the mapping of clusters to classes is carried out by an expert. Automation of the distribution step substantially reduces the time required for code change review. The k-means algorithm with a cosine similarity measure between metric vectors is used for clustering. Eleven source code metrics are employed, covering lines of code, cyclomatic complexity, file counts, interface changes, and structural changes. The method was validated on five software systems, including two open-source projects (Subversion and NHibernate), and demonstrated classification purity of P_C = 0.75 +/- 0.05 and entropy of E_C = 0.37 +/- 0.06 at a significance level of 0.05.

