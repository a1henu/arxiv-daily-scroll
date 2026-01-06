---
layout: default
title: Improved Accuracy for Private Continual Cardinality Estimation in Fully Dynamic Streams via Matrix Factorization
---

# Improved Accuracy for Private Continual Cardinality Estimation in Fully Dynamic Streams via Matrix Factorization
**arXiv**：[2601.02257v1](https://arxiv.org/abs/2601.02257) · [PDF](https://arxiv.org/pdf/2601.02257.pdf)  
**作者**：Joel Daniel Andersson, Palak Jain, Satchit Sivakumar  

**一句话要点**：通过矩阵分解改进全动态流中私有持续基数估计的准确性

**关键词**：差分隐私, 流数据, 基数估计, 矩阵分解, 持续观察模型, 敏感度分析

## 3 点简述
- 研究全动态持续观察模型下的差分隐私统计，处理插入和删除更新的流数据
- 通过分析差异流的ℓp敏感度向量，改进基数估计的误差界
- 在理论和实证上展示对去重计数、度直方图和三角形计数等问题的准确性提升

## 摘要（原文）

> We study differentially-private statistics in the fully dynamic continual observation model, where many updates can arrive at each time step and updates to a stream can involve both insertions and deletions of an item. Earlier work (e.g., Jain et al., NeurIPS 2023 for counting distinct elements; Raskhodnikova & Steiner, PODS 2025 for triangle counting with edge updates) reduced the respective cardinality estimation problem to continual counting on the difference stream associated with the true function values on the input stream. In such reductions, a change in the original stream can cause many changes in the difference stream, this poses a challenge for applying private continual counting algorithms to obtain optimal error bounds. We improve the accuracy of several such reductions by studying the associated $\ell_p$-sensitivity vectors of the resulting difference streams and isolating their properties.
>   We demonstrate that our framework gives improved bounds for counting distinct elements, estimating degree histograms, and estimating triangle counts (under a slightly relaxed privacy model), thus offering a general approach to private continual cardinality estimation in streaming settings. Our improved accuracy stems from tight analysis of known factorization mechanisms for the counting matrix in this setting; the key technical challenge is arguing that one can use state-of-the-art factorizations for sensitivity vector sets with the properties we isolate. Empirically and analytically, we demonstrate that our improved error bounds offer a substantial improvement in accuracy for cardinality estimation problems over a large range of parameters.

