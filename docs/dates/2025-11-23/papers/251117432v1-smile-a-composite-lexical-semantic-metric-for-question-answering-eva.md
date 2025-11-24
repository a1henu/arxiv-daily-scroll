---
layout: default
title: SMILE: A Composite Lexical-Semantic Metric for Question-Answering Evaluation
---

# SMILE: A Composite Lexical-Semantic Metric for Question-Answering Evaluation
**arXiv**：[2511.17432v1](https://arxiv.org/abs/2511.17432) · [PDF](https://arxiv.org/pdf/2511.17432.pdf)  
**作者**：Shrikant Kendre, Austin Xu, Honglu Zhou, Michael Ryoo, Shafiq Joty, Juan Carlos Niebles  

**一句话要点**：提出SMILE复合指标，结合词法和语义评估以改进问答系统评价。

**关键词**：问答系统评估, 语义相似度, 词法匹配, 复合指标, 轻量计算

## 3 点简述
- 传统问答评估指标依赖n-gram，忽略深层语义理解，导致评估不准确。
- SMILE融合句子级和关键词级语义，并保留词法匹配，平衡精确性与相关性。
- 在文本、图像和视频QA任务中，SMILE与人类判断高度相关，且计算轻量。

## 摘要（原文）

> Traditional evaluation metrics for textual and visual question answering, like ROUGE, METEOR, and Exact Match (EM), focus heavily on n-gram based lexical similarity, often missing the deeper semantic understanding needed for accurate assessment. While measures like BERTScore and MoverScore leverage contextual embeddings to address this limitation, they lack flexibility in balancing sentence-level and keyword-level semantics and ignore lexical similarity, which remains important. Large Language Model (LLM) based evaluators, though powerful, come with drawbacks like high costs, bias, inconsistency, and hallucinations. To address these issues, we introduce SMILE: Semantic Metric Integrating Lexical Exactness, a novel approach that combines sentence-level semantic understanding with keyword-level semantic understanding and easy keyword matching. This composite method balances lexical precision and semantic relevance, offering a comprehensive evaluation. Extensive benchmarks across text, image, and video QA tasks show SMILE is highly correlated with human judgments and computationally lightweight, bridging the gap between lexical and semantic evaluation.

