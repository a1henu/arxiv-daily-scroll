---
layout: default
title: Missing At Random as Covariate Shift: Correcting Bias in Iterative Imputation
---

# Missing At Random as Covariate Shift: Correcting Bias in Iterative Imputation
**arXiv**：[2602.06713v1](https://arxiv.org/abs/2602.06713) · [PDF](https://arxiv.org/pdf/2602.06713.pdf)  
**作者**：Luke Shannon, Song Liu, Katarzyna Reluga  

**一句话要点**：提出基于协变量偏移重要性加权的迭代插补算法以纠正缺失数据偏差

**关键词**：缺失数据插补, 协变量偏移, 重要性加权, 迭代插补算法, 分布偏差纠正

## 3 点简述
- 核心问题：缺失数据插补中的协变量偏移导致分布偏差，影响下游机器学习性能
- 方法要点：推导理论有效的重要性权重，联合估计权重与插补模型以纠正偏差
- 实验或效果：在基准数据集上，相比未加权方法，均方根误差和Wasserstein距离分别降低达7%和20%

## 摘要（原文）

> Accurate imputation of missing data is critical to downstream machine learning performance. We formulate missing data imputation as a risk minimisation problem, which highlights a covariate shift between the observed and unobserved data distributions. This covariate shift induced bias is not accounted for by popular imputation methods and leads to suboptimal performance. In this paper, we derive theoretically valid importance weights that correct for the induced distributional bias. Furthermore, we propose a novel imputation algorithm that jointly estimates both the importance weights and imputation models, enabling bias correction throughout the imputation process. Empirical results across benchmark datasets show reductions in root mean squared error and Wasserstein distance of up to 7% and 20%, respectively, compared to otherwise identical unweighted methods.

