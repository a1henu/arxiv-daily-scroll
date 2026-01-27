---
layout: default
title: PRECISE: Reducing the Bias of LLM Evaluations Using Prediction-Powered Ranking Estimation
---

# PRECISE: Reducing the Bias of LLM Evaluations Using Prediction-Powered Ranking Estimation
**arXiv**：[2601.18777v1](https://arxiv.org/abs/2601.18777) · [PDF](https://arxiv.org/pdf/2601.18777.pdf)  
**作者**：Abhishek Divekar, Anirban Majumder  

**一句话要点**：提出PRECISE框架，结合少量人工标注与LLM判断，减少搜索系统评估中的LLM偏见。

**关键词**：LLM评估偏见, 预测驱动推理, 子实例标注, 搜索系统评估, 计算复杂度优化

## 3 点简述
- 核心问题：LLM作为自动评估器存在偏见，传统方法需大量人工标注，成本高。
- 方法要点：扩展预测驱动推理，整合子实例标注，降低计算复杂度至O(2^K)。
- 实验或效果：在检索数据集上验证，减少Precision@K方差，有效校正低资源设置下的LLM偏见。

## 摘要（原文）

> Evaluating the quality of search, ranking and RAG systems traditionally requires a significant number of human relevance annotations. In recent times, several deployed systems have explored the usage of Large Language Models (LLMs) as automated judges for this task while their inherent biases prevent direct use for metric estimation. We present a statistical framework extending Prediction-Powered Inference (PPI) that combines minimal human annotations with LLM judgments to produce reliable estimates of metrics which require sub-instance annotations. Our method requires as few as 100 human-annotated queries and 10,000 unlabeled examples, reducing annotation requirements significantly compared to traditional approaches. We formulate our proposed framework (PRECISE) for inference of relevance uplift for an LLM-based query reformulation application, extending PPI to sub-instance annotations at the query-document level. By reformulating the metric-integration space, we reduced the computational complexity from O(2^\|C\|) to O(2^K), where \|C\| represents corpus size (in order of millions). Detailed experiments across prominent retrieval datasets demonstrate that our method reduces the variance of estimates for the business-critical Precision@K metric, while effectively correcting for LLM bias in low-resource settings.

