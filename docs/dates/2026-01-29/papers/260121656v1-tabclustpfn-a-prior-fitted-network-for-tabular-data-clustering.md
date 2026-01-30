---
layout: default
title: TabClustPFN: A Prior-Fitted Network for Tabular Data Clustering
---

# TabClustPFN: A Prior-Fitted Network for Tabular Data Clustering
**arXiv**：[2601.21656v1](https://arxiv.org/abs/2601.21656) · [PDF](https://arxiv.org/pdf/2601.21656.pdf)  
**作者**：Tianqi Zhao, Guanyang Wang, Yan Shuo Tan, Qiong Zhang  

**一句话要点**：提出TabClustPFN以解决表格数据聚类中缺乏可迁移归纳偏置的挑战。

**关键词**：表格数据聚类, 先验拟合网络, 摊销贝叶斯推断, 异构特征处理, 无监督学习

## 3 点简述
- 核心问题：表格数据聚类因特征异构、数据生成机制多样和缺乏跨数据集归纳偏置而困难。
- 方法要点：基于先验拟合网络，通过摊销贝叶斯推断处理聚类分配和簇数，无需数据集特定训练。
- 实验或效果：在合成和真实基准上优于基线，展现强鲁棒性，支持异构特征和多样聚类结构。

## 摘要（原文）

> Clustering tabular data is a fundamental yet challenging problem due to heterogeneous feature types, diverse data-generating mechanisms, and the absence of transferable inductive biases across datasets. Prior-fitted networks (PFNs) have recently demonstrated strong generalization in supervised tabular learning by amortizing Bayesian inference under a broad synthetic prior. Extending this paradigm to clustering is nontrivial: clustering is unsupervised, admits a combinatorial and permutation-invariant output space, and requires inferring the number of clusters. We introduce TabClustPFN, a prior-fitted network for tabular data clustering that performs amortized Bayesian inference over both cluster assignments and cluster cardinality. Pretrained on synthetic datasets drawn from a flexible clustering prior, TabClustPFN clusters unseen datasets in a single forward pass, without dataset-specific retraining or hyperparameter tuning. The model naturally handles heterogeneous numerical and categorical features and adapts to a wide range of clustering structures. Experiments on synthetic data and curated real-world tabular benchmarks show that TabClustPFN outperforms classical, deep, and amortized clustering baselines, while exhibiting strong robustness in out-of-the-box exploratory settings. Code is available at https://github.com/Tianqi-Zhao/TabClustPFN.

