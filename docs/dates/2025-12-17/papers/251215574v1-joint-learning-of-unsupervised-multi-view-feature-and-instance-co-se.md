---
layout: default
title: Joint Learning of Unsupervised Multi-view Feature and Instance Co-selection with Cross-view Imputation
---

# Joint Learning of Unsupervised Multi-view Feature and Instance Co-selection with Cross-view Imputation
**arXiv**：[2512.15574v1](https://arxiv.org/abs/2512.15574) · [PDF](https://arxiv.org/pdf/2512.15574.pdf)  
**作者**：Yuxin Cai, Yanyong Huang, Jinyuan Chang, Dongjie Wang, Tianrui Li, Xiaoyi Jiang  

**一句话要点**：提出JUICE方法以解决无标签不完整多视图数据的特征与实例协同选择问题

**关键词**：多视图学习, 特征选择, 实例选择, 缺失数据插补, 无监督学习

## 3 点简述
- 核心问题：现有方法独立处理缺失数据插补与协同选择，忽略交互作用，且简单合并视图限制效果
- 方法要点：在统一框架中联合学习缺失数据重建与协同选择，利用跨视图邻域信息优化插补
- 实验或效果：广泛实验显示JUICE优于现有先进方法，提升特征与实例选择代表性

## 摘要（原文）

> Feature and instance co-selection, which aims to reduce both feature dimensionality and sample size by identifying the most informative features and instances, has attracted considerable attention in recent years. However, when dealing with unlabeled incomplete multi-view data, where some samples are missing in certain views, existing methods typically first impute the missing data and then concatenate all views into a single dataset for subsequent co-selection. Such a strategy treats co-selection and missing data imputation as two independent processes, overlooking potential interactions between them. The inter-sample relationships gleaned from co-selection can aid imputation, which in turn enhances co-selection performance. Additionally, simply merging multi-view data fails to capture the complementary information among views, ultimately limiting co-selection effectiveness. To address these issues, we propose a novel co-selection method, termed Joint learning of Unsupervised multI-view feature and instance Co-selection with cross-viEw imputation (JUICE). JUICE first reconstructs incomplete multi-view data using available observations, bringing missing data recovery and feature and instance co-selection together in a unified framework. Then, JUICE leverages cross-view neighborhood information to learn inter-sample relationships and further refine the imputation of missing values during reconstruction. This enables the selection of more representative features and instances. Extensive experiments demonstrate that JUICE outperforms state-of-the-art methods.

