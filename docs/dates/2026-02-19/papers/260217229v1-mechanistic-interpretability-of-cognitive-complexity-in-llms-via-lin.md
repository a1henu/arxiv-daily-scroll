---
layout: default
title: Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom's Taxonomy
---

# Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom's Taxonomy
**arXiv**：[2602.17229v1](https://arxiv.org/abs/2602.17229) · [PDF](https://arxiv.org/pdf/2602.17229.pdf)  
**作者**：Bianca Raimondi, Maurizio Gabbrielli  

**一句话要点**：通过线性探测分析LLM中基于布鲁姆分类法的认知复杂度内部表示

**关键词**：大语言模型, 可解释性, 线性探测, 布鲁姆分类法, 认知复杂度, 内部表示

## 3 点简述
- 研究LLM内部如何编码认知复杂度，使用布鲁姆分类法作为层次框架
- 通过分析高维激活向量，探究不同认知水平是否在残差流中线性可分
- 线性分类器平均准确率达95%，表明认知水平在线性子空间中可访问

## 摘要（原文）

> The black-box nature of Large Language Models necessitates novel evaluation frameworks that transcend surface-level performance metrics. This study investigates the internal neural representations of cognitive complexity using Bloom's Taxonomy as a hierarchical lens. By analyzing high-dimensional activation vectors from different LLMs, we probe whether different cognitive levels, ranging from basic recall (Remember) to abstract synthesis (Create), are linearly separable within the model's residual streams. Our results demonstrate that linear classifiers achieve approximately 95% mean accuracy across all Bloom levels, providing strong evidence that cognitive level is encoded in a linearly accessible subspace of the model's representations. These findings provide evidence that the model resolves the cognitive difficulty of a prompt early in the forward pass, with representations becoming increasingly separable across layers.

