---
layout: default
title: Selecting Hyperparameters for Tree-Boosting
---

# Selecting Hyperparameters for Tree-Boosting
**arXiv**：[2602.05786v1](https://arxiv.org/abs/2602.05786) · [PDF](https://arxiv.org/pdf/2602.05786.pdf)  
**作者**：Floris Jan Koster, Fabio Sigrist  

**一句话要点**：比较树提升超参数优化方法，发现SMAC方法表现最佳

**关键词**：树提升, 超参数优化, SMAC, 机器学习, 回归分类

## 3 点简述
- 核心问题：树提升模型超参数对样本外精度有重要影响，需有效优化
- 方法要点：实证比较随机网格搜索、TPE、GP-BO、Hyperband、SMAC和全网格搜索
- 实验或效果：基于59个数据集，SMAC方法优于其他方法，需大量试验且默认值不准确

## 摘要（原文）

> Tree-boosting is a widely used machine learning technique for tabular data. However, its out-of-sample accuracy is critically dependent on multiple hyperparameters. In this article, we empirically compare several popular methods for hyperparameter optimization for tree-boosting including random grid search, the tree-structured Parzen estimator (TPE), Gaussian-process-based Bayesian optimization (GP-BO), Hyperband, the sequential model-based algorithm configuration (SMAC) method, and deterministic full grid search using $59$ regression and classification data sets. We find that the SMAC method clearly outperforms all the other considered methods. We further observe that (i) a relatively large number of trials larger than $100$ is required for accurate tuning, (ii) using default values for hyperparameters yields very inaccurate models, (iii) all considered hyperparameters can have a material effect on the accuracy of tree-boosting, i.e., there is no small set of hyperparameters that is more important than others, and (iv) choosing the number of boosting iterations using early stopping yields more accurate results compared to including it in the search space for regression tasks.

