---
layout: default
title: Semi-Supervised Mixture Models under the Concept of Missing at Radom with Margin Confidence and Aranda Ordaz Function
---

# Semi-Supervised Mixture Models under the Concept of Missing at Radom with Margin Confidence and Aranda Ordaz Function
**arXiv**：[2601.14631v1](https://arxiv.org/abs/2601.14631) · [PDF](https://arxiv.org/pdf/2601.14631.pdf)  
**作者**：Jinyang Liao, Ziyang Lyu  

**一句话要点**：提出基于缺失随机机制的半监督高斯混合模型，通过边界置信度和Aranda Ordaz函数建模缺失概率以缓解偏差。

**关键词**：半监督学习, 高斯混合模型, 缺失随机机制, 边界置信度, Aranda Ordaz函数, ECM算法

## 3 点简述
- 核心问题：在缺失随机机制下，忽略缺失机制会导致半监督学习中的偏差，影响分类性能。
- 方法要点：使用边界置信度量化分类不确定性，结合Aranda Ordaz函数灵活建模不确定性与缺失概率的非对称关系。
- 实验或效果：开发ECM算法联合估计参数，通过贝叶斯分类器填补缺失标签，在大量缺失标签的现实场景中提升分类鲁棒性。

## 摘要（原文）

> This paper presents a semi-supervised learning framework for Gaussian mixture modelling under a Missing at Random (MAR) mechanism. The method explicitly parameterizes the missingness mechanism by modelling the probability of missingness as a function of classification uncertainty. To quantify classification uncertainty, we introduce margin confidence and incorporate the Aranda Ordaz (AO) link function to flexibly capture the asymmetric relationships between uncertainty and missing probability. Based on this formulation, we develop an efficient Expectation Conditional Maximization (ECM) algorithm that jointly estimates all parameters appearing in both the Gaussian mixture model (GMM) and the missingness mechanism, and subsequently imputes the missing labels by a Bayesian classifier derived from the fitted mixture model. This method effectively alleviates the bias induced by ignoring the missingness mechanism while enhancing the robustness of semi-supervised learning. The resulting uncertainty-aware framework delivers reliable classification performance in realistic MAR scenarios with substantial proportions of missing labels.

