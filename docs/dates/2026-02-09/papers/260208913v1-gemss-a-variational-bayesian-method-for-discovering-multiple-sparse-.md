---
layout: default
title: GEMSS: A Variational Bayesian Method for Discovering Multiple Sparse Solutions in Classification and Regression Problems
---

# GEMSS: A Variational Bayesian Method for Discovering Multiple Sparse Solutions in Classification and Regression Problems
**arXiv**：[2602.08913v1](https://arxiv.org/abs/2602.08913) · [PDF](https://arxiv.org/pdf/2602.08913.pdf)  
**作者**：Kateřina Henclová, Václav Šmídl  

**一句话要点**：提出GEMSS变分贝叶斯框架以在分类和回归问题中发现多个稀疏解

**关键词**：变分贝叶斯, 稀疏解发现, 特征选择, 多模态后验, 高维数据, Python包

## 3 点简述
- 核心问题：在欠定和高相关场景中，传统方法仅提供单一稀疏解，难以揭示多个同等有效的特征组合。
- 方法要点：采用结构化尖峰-平板先验、高斯混合近似后验和Jaccard惩罚，通过随机梯度下降优化整个解集合。
- 实验或效果：在128个合成实验中验证，可处理高维数据、小样本、连续目标、缺失数据，对类别不平衡和高斯噪声鲁棒。

## 摘要（原文）

> Selecting interpretable feature sets in underdetermined ($n \ll p$) and highly correlated regimes constitutes a fundamental challenge in data science, particularly when analyzing physical measurements. In such settings, multiple distinct sparse subsets may explain the response equally well. Identifying these alternatives is crucial for generating domain-specific insights into the underlying mechanisms, yet conventional methods typically isolate a single solution, obscuring the full spectrum of plausible explanations.
>   We present GEMSS (Gaussian Ensemble for Multiple Sparse Solutions), a variational Bayesian framework specifically designed to simultaneously discover multiple, diverse sparse feature combinations. The method employs a structured spike-and-slab prior for sparsity, a mixture of Gaussians to approximate the intractable multimodal posterior, and a Jaccard-based penalty to further control solution diversity. Unlike sequential greedy approaches, GEMSS optimizes the entire ensemble of solutions within a single objective function via stochastic gradient descent.
>   The method is validated on a comprehensive benchmark comprising 128 synthetic experiments across classification and regression tasks. Results demonstrate that GEMSS scales effectively to high-dimensional settings ($p=5000$) with sample size as small as $n = 50$, generalizes seamlessly to continuous targets, handles missing data natively, and exhibits remarkable robustness to class imbalance and Gaussian noise.
>   GEMSS is available as a Python package 'gemss' at PyPI. The full GitHub repository at https://github.com/kat-er-ina/gemss/ also includes a free, easy-to-use application suitable for non-coders.

