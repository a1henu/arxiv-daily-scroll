---
layout: default
title: ROSE: Reordered SparseGPT for More Accurate One-Shot Large Language Models Pruning
---

# ROSE: Reordered SparseGPT for More Accurate One-Shot Large Language Models Pruning
**arXiv**：[2603.05878v1](https://arxiv.org/abs/2603.05878) · [PDF](https://arxiv.org/pdf/2603.05878.pdf)  
**作者**：Mingluo Su, Huan Wang  

**一句话要点**：提出ROSE方法，通过重排序优化SparseGPT框架，提升大语言模型剪枝精度。

**关键词**：大语言模型剪枝, 稀疏化优化, 二阶梯度, 自适应重排序, 模型压缩

## 3 点简述
- 核心问题：SparseGPT预定义剪枝顺序在权重呈列模式时导致性能下降。
- 方法要点：基于潜在剪枝误差进行两级重排序，自适应识别列层。
- 实验或效果：在LLaMA2/3、Mistral等模型上超越SparseGPT及其他剪枝方法。

## 摘要（原文）

> Pruning is widely recognized as an effective method for reducing the parameters of large language models (LLMs), potentially leading to more efficient deployment and inference. One classic and prominent path of LLM one-shot pruning is to leverage second-order gradients (i.e., Hessian), represented by the pioneering work SparseGPT. However, the predefined left-to-right pruning order in SparseGPT leads to suboptimal performance when the weights exhibit columnar patterns. This paper studies the effect of pruning order under the SparseGPT framework. The analyses lead us to propose ROSE, a reordered SparseGPT method that prioritizes weights with larger potential pruning errors to be pruned earlier. ROSE first performs pre-pruning to identify candidate weights for removal, and estimates both column and block pruning loss. Subsequently, two-level reordering is performed: columns within each block are reordered in descending order of column loss, while blocks are reordered based on block loss. We introduce the relative range of block loss as a metric to identify columnar layers, enabling adaptive reordering across the entire model. Substantial empirical results on prevalent LLMs (LLaMA2-7B/13B/70B, LLaMA3-8B, Mistral-7B) demonstrate that ROSE surpasses the original SparseGPT and other counterpart pruning methods. Our code is available at https://github.com/mingluo-su/ROSE.

