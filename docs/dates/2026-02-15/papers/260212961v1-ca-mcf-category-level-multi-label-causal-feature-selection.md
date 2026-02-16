---
layout: default
title: Ca-MCF: Category-level Multi-label Causal Feature selection
---

# Ca-MCF: Category-level Multi-label Causal Feature selection
**arXiv**：[2602.12961v1](https://arxiv.org/abs/2602.12961) · [PDF](https://arxiv.org/pdf/2602.12961.pdf)  
**作者**：Wanfu Gao, Yanan Wang, Yonghao Li  

**一句话要点**：提出Ca-MCF方法以解决多标签因果特征选择中忽略类别级因果机制的问题

**关键词**：多标签学习, 因果特征选择, 类别级建模, 马尔可夫毯, 互信息, 特征降维

## 3 点简述
- 当前多标签因果特征选择方法在标签层面操作，忽视类别级因果机制。
- Ca-MCF通过标签类别扁平化和基于解释竞争的恢复机制，精确建模因果结构。
- 在七个真实数据集上实验显示，Ca-MCF在预测准确性和特征降维方面优于基准方法。

## 摘要（原文）

> Multi-label causal feature selection has attracted extensive attention in recent years. However, current methods primarily operate at the label level, treating each label variable as a monolithic entity and overlooking the fine-grained causal mechanisms unique to individual categories. To address this, we propose a Category-level Multi-label Causal Feature selection method named Ca-MCF. Ca-MCF utilizes label category flattening to decompose label variables into specific category nodes, enabling precise modeling of causal structures within the label space. Furthermore, we introduce an explanatory competition-based category-aware recovery mechanism that leverages the proposed Specific Category-Specific Mutual Information (SCSMI) and Distinct Category-Specific Mutual Information (DCSMI) to salvage causal features obscured by label correlations. The method also incorporates structural symmetry checks and cross-dimensional redundancy removal to ensure the robustness and compactness of the identified Markov Blankets. Extensive experiments across seven real-world datasets demonstrate that Ca-MCF significantly outperforms state-of-the-art benchmarks, achieving superior predictive accuracy with reduced feature dimensionality.

