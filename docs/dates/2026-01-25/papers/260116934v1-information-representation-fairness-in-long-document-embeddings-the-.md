---
layout: default
title: Information Representation Fairness in Long-Document Embeddings: The Peculiar Interaction of Positional and Language Bias
---

# Information Representation Fairness in Long-Document Embeddings: The Peculiar Interaction of Positional and Language Bias
**arXiv**：[2601.16934v1](https://arxiv.org/abs/2601.16934) · [PDF](https://arxiv.org/pdf/2601.16934.pdf)  
**作者**：Elias Schuhmacher, Andrianos Michail, Juri Opitz, Rico Sennrich, Simon Clematide  

**一句话要点**：提出基于排列的评估框架和注意力校准方法，以解决长文档嵌入中的位置和语言偏差问题。

**关键词**：长文档嵌入, 位置偏差, 语言偏差, 注意力校准, 评估框架, 可发现性

## 3 点简述
- 核心问题：现有嵌入模型在长文档中表现出系统性的位置和语言偏差，导致早期和高资源语言段被过度代表。
- 方法要点：引入基于排列的评估框架量化偏差，并提出推理时注意力校准方法，以更均匀地分配注意力。
- 实验或效果：评估显示校准方法提高了后期段的可发现性，框架和代码已开源。

## 摘要（原文）

> To be discoverable in an embedding-based search process, each part of a document should be reflected in its embedding representation. To quantify any potential reflection biases, we introduce a permutation-based evaluation framework. With this, we observe that state-of-the-art embedding models exhibit systematic positional and language biases when documents are longer and consist of multiple segments. Specifically, early segments and segments in higher-resource languages like English are over-represented, while later segments and segments in lower-resource languages are marginalized. In our further analysis, we find that the positional bias stems from front-loaded attention distributions in pooling-token embeddings, where early tokens receive more attention. To mitigate this issue, we introduce an inference-time attention calibration method that redistributes attention more evenly across document positions, increasing discoverabiltiy of later segments. Our evaluation framework and attention calibration is available at https://github.com/impresso/fair-sentence-transformers

