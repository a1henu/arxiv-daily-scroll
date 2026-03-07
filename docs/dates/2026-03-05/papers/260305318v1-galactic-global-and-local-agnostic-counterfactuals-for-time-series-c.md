---
layout: default
title: GALACTIC: Global and Local Agnostic Counterfactuals for Time-series Clustering
---

# GALACTIC: Global and Local Agnostic Counterfactuals for Time-series Clustering
**arXiv**：[2603.05318v1](https://arxiv.org/abs/2603.05318) · [PDF](https://arxiv.org/pdf/2603.05318.pdf)  
**作者**：Christos Fragkathoulas, Eleni Psaroudaki, Themis Palpanas, Evaggelia Pitoura  

**一句话要点**：提出GALACTIC框架，通过局部和全局反事实解释统一解释无监督时间序列聚类。

**关键词**：时间序列聚类, 反事实解释, 无监督学习, 最小描述长度, 可解释性

## 3 点简述
- 现有方法无法识别跨聚类边界的转变，反事实解释多限于监督场景。
- GALACTIC结合局部扰动生成和全局代表性选择，基于最小描述长度优化。
- 在UCR Archive上验证，GALACTIC产生更稀疏局部解释和更简洁全局摘要。

## 摘要（原文）

> Time-series clustering is a fundamental tool for pattern discovery, yet existing explainability methods, primarily based on feature attribution or metadata, fail to identify the transitions that move an instance across cluster boundaries. While Counterfactual Explanations (CEs) identify the minimal temporal perturbations required to alter the prediction of a model, they have been mostly confined to supervised settings. This paper introduces GALACTIC, the first unified framework to bridge local and global counterfactual explainability for unsupervised time-series clustering. At instance level (local), GALACTIC generates perturbations via a cluster-aware optimization objective that respects the target and underlying cluster assignments. At cluster level (global), to mitigate cognitive load and enhance interpretability, we formulate a representative CE selection problem. We propose a Minimum Description Length (MDL) objective to extract a non-redundant summary of global explanations that characterize the transitions between clusters. We prove that our MDL objective is supermodular, which allows the corresponding MDL reduction to be framed as a monotone submodular set function. This enables an efficient greedy selection algorithm with provable $(1-1/e)$ approximation guarantees. Extensive experimental evaluation on the UCR Archive demonstrates that GALACTIC produces significantly sparser local CEs and more concise global summaries than state-of-the-art baselines adapted for our problem, offering the first unified approach for interpreting clustered time-series through counterfactuals.

