---
layout: default
title: Topeax -- An Improved Clustering Topic Model with Density Peak Detection and Lexical-Semantic Term Importance
---

# Topeax -- An Improved Clustering Topic Model with Density Peak Detection and Lexical-Semantic Term Importance
**arXiv**：[2601.21465v1](https://arxiv.org/abs/2601.21465) · [PDF](https://arxiv.org/pdf/2601.21465.pdf)  
**作者**：Márton Kardos  

**一句话要点**：提出Topeax以改进聚类主题模型，通过密度峰值检测和词义-语义术语重要性提升聚类发现与描述质量。

**关键词**：主题建模, 文本聚类, 密度峰值检测, 术语重要性评估, 语义距离, 超参数稳定性

## 3 点简述
- 核心问题：Top2Vec和BERTopic在发现自然聚类和估计术语重要性时存在不可靠性，如对样本大小和超参数敏感，导致主题不连贯。
- 方法要点：Topeax利用密度估计峰值自动确定聚类数量，并融合词频和语义距离来评估术语重要性，以生成高质量主题关键词。
- 实验或效果：Topeax在聚类恢复和描述方面优于Top2Vec和BERTopic，且对样本大小和超参数变化表现出更稳定的行为。

## 摘要（原文）

> Text clustering is today the most popular paradigm for topic modelling, both in academia and industry. Despite clustering topic models' apparent success, we identify a number of issues in Top2Vec and BERTopic, which remain largely unsolved. Firstly, these approaches are unreliable at discovering natural clusters in corpora, due to extreme sensitivity to sample size and hyperparameters, the default values of which result in suboptimal behaviour. Secondly, when estimating term importance, BERTopic ignores the semantic distance of keywords to topic vectors, while Top2Vec ignores word counts in the corpus. This results in, on the one hand, less coherent topics due to the presence of stop words and junk words, and lack of variety and trust on the other. In this paper, I introduce a new approach, \textbf{Topeax}, which discovers the number of clusters from peaks in density estimates, and combines lexical and semantic indices of term importance to gain high-quality topic keywords. Topeax is demonstrated to be better at both cluster recovery and cluster description than Top2Vec and BERTopic, while also exhibiting less erratic behaviour in response to changing sample size and hyperparameters.

