---
layout: default
title: Selecting Hyperparameters for Tree-Boosting
---

# Selecting Hyperparameters for Tree-Boosting
**arXiv**：[2602.05786v1](https://arxiv.org/abs/2602.05786) · [PDF](https://arxiv.org/pdf/2602.05786.pdf)  
**作者**：Floris Jan Koster, Fabio Sigrist  

**一句话要点**：比较树提升超参数优化方法，发现SMAC方法表现最优

**关键词**：树提升, 超参数优化, SMAC方法, 表格数据, 机器学习调优

## 3 点简述
- 核心问题：树提升模型在表格数据中的样本外精度高度依赖超参数设置
- 方法要点：实证比较随机网格搜索、TPE、GP-BO、Hyperband、SMAC和全网格搜索等方法
- 实验或效果：基于59个数据集，SMAC方法显著优于其他方法，并得出超参数调优的关键观察

## 摘要（原文）

> Tree-boosting is a widely used machine learning technique for tabular data. However, its out-of-sample accuracy is critically dependent on multiple hyperparameters. In this article, we empirically compare several popular methods for hyperparameter optimization for tree-boosting including random grid search, the tree-structured Parzen estimator (TPE), Gaussian-process-based Bayesian optimization (GP-BO), Hyperband, the sequential model-based algorithm configuration (SMAC) method, and deterministic full grid search using $59$ regression and classification data sets. We find that the SMAC method clearly outperforms all the other considered methods. We further observe that (i) a relatively large number of trials larger than $100$ is required for accurate tuning, (ii) using default values for hyperparameters yields very inaccurate models, (iii) all considered hyperparameters can have a material effect on the accuracy of tree-boosting, i.e., there is no small set of hyperparameters that is more important than others, and (iv) choosing the number of boosting iterations using early stopping yields more accurate results compared to including it in the search space for regression tasks.

