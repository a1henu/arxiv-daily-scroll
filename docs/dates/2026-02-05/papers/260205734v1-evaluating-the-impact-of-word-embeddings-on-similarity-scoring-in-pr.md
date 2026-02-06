---
layout: default
title: Evaluating the impact of word embeddings on similarity scoring in practical information retrieval
---

# Evaluating the impact of word embeddings on similarity scoring in practical information retrieval
**arXiv**：[2602.05734v1](https://arxiv.org/abs/2602.05734) · [PDF](https://arxiv.org/pdf/2602.05734.pdf)  
**作者**：Niall McCarroll, Kevin Curran, Eugene McNamee, Angela Clist, Andrew Brammer  

**一句话要点**：评估词嵌入对信息检索相似性评分的影响，提出结合WMD与GloVe的方法提升准确性

**关键词**：信息检索, 词嵌入, 词移距离, 相似性评分, 语义表示, 自然语言处理

## 3 点简述
- 核心问题：传统基于词嵌入质心的相似性度量在信息检索中可能不足，需更精确捕捉查询与语句的语义关联
- 方法要点：采用词移距离模型，通过计算查询与语句中单个词的距离来评估相似性，结合预训练词嵌入如GloVe
- 实验或效果：在排名查询和响应语句上，WMD+GloVe组合显著优于Doc2Vec和LSA等先进模型，实现领域无关的便携解决方案

## 摘要（原文）

> Search behaviour is characterised using synonymy and polysemy as users often want to search information based on meaning. Semantic representation strategies represent a move towards richer associative connections that can adequately capture this complex usage of language. Vector Space Modelling (VSM) and neural word embeddings play a crucial role in modern machine learning and Natural Language Processing (NLP) pipelines. Embeddings use distributional semantics to represent words, sentences, paragraphs or entire documents as vectors in high dimensional spaces. This can be leveraged by Information Retrieval (IR) systems to exploit the semantic relatedness between queries and answers.
>   This paper evaluates an alternative approach to measuring query statement similarity that moves away from the common similarity measure of centroids of neural word embeddings. Motivated by the Word Movers Distance (WMD) model, similarity is evaluated using the distance between individual words of queries and statements. Results from ranked query and response statements demonstrate significant gains in accuracy using the combined approach of similarity ranking through WMD with the word embedding techniques. The top performing WMD + GloVe combination outperforms all other state-of-the-art retrieval models including Doc2Vec and the baseline LSA model. Along with the significant gains in performance of similarity ranking through WMD, we conclude that the use of pre-trained word embeddings, trained on vast amounts of data, result in domain agnostic language processing solutions that are portable to diverse business use-cases.

