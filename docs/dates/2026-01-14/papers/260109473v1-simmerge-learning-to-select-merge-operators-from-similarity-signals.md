---
layout: default
title: SimMerge: Learning to Select Merge Operators from Similarity Signals
---

# SimMerge: Learning to Select Merge Operators from Similarity Signals
**arXiv**：[2601.09473v1](https://arxiv.org/abs/2601.09473) · [PDF](https://arxiv.org/pdf/2601.09473.pdf)  
**作者**：Oliver Bolton, Aakanksha, Arash Ahmadian, Sara Hooker, Marzieh Fadaee, Beyza Ermis  

**一句话要点**：提出SimMerge方法，通过模型相似性信号预测最佳合并操作，以解决大规模模型合并中的选择难题。

**关键词**：模型合并, 大语言模型, 相似性预测, 合并操作符选择, 多任务学习, 可扩展模型组合

## 3 点简述
- 核心问题：模型合并需选择合适操作符、模型和顺序，传统方法依赖昂贵搜索。
- 方法要点：利用无标签探针计算功能与结构特征，预测合并性能，避免评估循环。
- 实验或效果：在7B和111B参数LLM上超越标准合并性能，支持动态扩展任务和模型。

## 摘要（原文）

> Model merging enables multiple large language models (LLMs) to be combined into a single model while preserving performance. This makes it a valuable tool in LLM development, offering a competitive alternative to multi-task training. However, merging can be difficult at scale, as successful merging requires choosing the right merge operator, selecting the right models, and merging them in the right order. This often leads researchers to run expensive merge-and-evaluate searches to select the best merge. In this work, we provide an alternative by introducing \simmerge{}, \emph{a predictive merge-selection method} that selects the best merge using inexpensive, task-agnostic similarity signals between models. From a small set of unlabeled probes, we compute functional and structural features and use them to predict the performance of a given 2-way merge. Using these predictions, \simmerge{} selects the best merge operator, the subset of models to merge, and the merge order, eliminating the expensive merge-and-evaluate loop. We demonstrate that we surpass standard merge-operator performance on 2-way merges of 7B-parameter LLMs, and that \simmerge{} generalizes to multi-way merges and 111B-parameter LLM merges without retraining. Additionally, we present a bandit variant that supports adding new tasks, models, and operators on the fly. Our results suggest that learning how to merge is a practical route to scalable model composition when checkpoint catalogs are large and evaluation budgets are tight.

