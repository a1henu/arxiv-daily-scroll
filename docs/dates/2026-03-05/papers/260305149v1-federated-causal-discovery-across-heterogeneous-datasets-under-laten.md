---
layout: default
title: Federated Causal Discovery Across Heterogeneous Datasets under Latent Confounding
---

# Federated Causal Discovery Across Heterogeneous Datasets under Latent Confounding
**arXiv**：[2603.05149v1](https://arxiv.org/abs/2603.05149) · [PDF](https://arxiv.org/pdf/2603.05149.pdf)  
**作者**：Maximilian Hahn, Alina Zajak, Dominik Heider, Adèle Helena Ribeiro  

**一句话要点**：提出fedCI-IOD以解决分布式异构数据集下隐私保护与潜在混杂的因果发现问题

**关键词**：联邦学习, 因果发现, 条件独立性检验, 异构数据集, 隐私保护, 潜在混杂

## 3 点简述
- 核心问题：数据隐私与跨站点异质性限制传统因果发现方法，需处理变量集不同、站点效应和混合类型数据
- 方法要点：基于联邦条件独立性检验fedCI，通过联邦IRLS估计广义线性模型参数，扩展为fedCI-IOD算法
- 实验或效果：联邦聚合证据提升统计功效，性能接近全池化分析，缓解本地样本量小导致的伪影

## 摘要（原文）

> Causal discovery across multiple datasets is often constrained by data privacy regulations and cross-site heterogeneity, limiting the use of conventional methods that require a single, centralized dataset. To address these challenges, we introduce fedCI, a federated conditional independence test that rigorously handles heterogeneous datasets with non-identical sets of variables, site-specific effects, and mixed variable types, including continuous, ordinal, binary, and categorical variables. At its core, fedCI uses a federated Iteratively Reweighted Least Squares (IRLS) procedure to estimate the parameters of generalized linear models underlying likelihood-ratio tests for conditional independence. Building on this, we develop fedCI-IOD, a federated extension of the Integration of Overlapping Datasets (IOD) algorithm, that replaces its meta-analysis strategy and enables, for the fist time, federated causal discovery under latent confounding across distributed and heterogeneous datasets. By aggregating evidence federatively, fedCI-IOD not only preserves privacy but also substantially enhances statistical power, achieving performance comparable to fully pooled analyses and mitigating artifacts from low local sample sizes. Our tools are publicly available as the fedCI Python package, a privacy-preserving R implementation of IOD, and a web application for the fedCI-IOD pipeline, providing versatile, user-friendly solutions for federated conditional independence testing and causal discovery.

