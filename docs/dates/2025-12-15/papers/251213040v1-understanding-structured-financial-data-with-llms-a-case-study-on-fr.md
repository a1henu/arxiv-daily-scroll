---
layout: default
title: Understanding Structured Financial Data with LLMs: A Case Study on Fraud Detection
---

# Understanding Structured Financial Data with LLMs: A Case Study on Fraud Detection
**arXiv**：[2512.13040v1](https://arxiv.org/abs/2512.13040) · [PDF](https://arxiv.org/pdf/2512.13040.pdf)  
**作者**：Xuwei Tan, Yao Ma, Xueru Zhang  

**一句话要点**：提出FinFRE-RAG方法，通过特征缩减和检索增强学习提升LLMs在金融欺诈检测中的性能与可解释性。

**关键词**：金融欺诈检测, 大型语言模型, 特征缩减, 检索增强生成, 表格数据理解, 可解释性

## 3 点简述
- 核心问题：LLMs直接应用于表格欺诈检测时性能差，因特征多、类别不平衡和缺乏上下文信息。
- 方法要点：采用两阶段方法，先重要性引导特征缩减序列化，再检索增强上下文学习。
- 实验或效果：在四个公共数据集上显著提升F1/MCC，接近表格基线并提供可解释理由。

## 摘要（原文）

> Detecting fraud in financial transactions typically relies on tabular models that demand heavy feature engineering to handle high-dimensional data and offer limited interpretability, making it difficult for humans to understand predictions. Large Language Models (LLMs), in contrast, can produce human-readable explanations and facilitate feature analysis, potentially reducing the manual workload of fraud analysts and informing system refinements. However, they perform poorly when applied directly to tabular fraud detection due to the difficulty of reasoning over many features, the extreme class imbalance, and the absence of contextual information. To bridge this gap, we introduce FinFRE-RAG, a two-stage approach that applies importance-guided feature reduction to serialize a compact subset of numeric/categorical attributes into natural language and performs retrieval-augmented in-context learning over label-aware, instance-level exemplars. Across four public fraud datasets and three families of open-weight LLMs, FinFRE-RAG substantially improves F1/MCC over direct prompting and is competitive with strong tabular baselines in several settings. Although these LLMs still lag behind specialized classifiers, they narrow the performance gap and provide interpretable rationales, highlighting their value as assistive tools in fraud analysis.

