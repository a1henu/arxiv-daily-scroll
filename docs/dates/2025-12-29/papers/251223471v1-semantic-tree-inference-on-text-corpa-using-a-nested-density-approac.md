---
layout: default
title: Semantic Tree Inference on Text Corpa using a Nested Density Approach together with Large Language Model Embeddings
---

# Semantic Tree Inference on Text Corpa using a Nested Density Approach together with Large Language Model Embeddings
**arXiv**：[2512.23471v1](https://arxiv.org/abs/2512.23471) · [PDF](https://arxiv.org/pdf/2512.23471.pdf)  
**作者**：Thomas Haschka, Joseph Bakarji  

**一句话要点**：提出嵌套密度聚类方法，结合大语言模型嵌入，从文本语料中推断语义树结构。

**关键词**：语义树推断, 嵌套密度聚类, 大语言模型嵌入, 文本分类, 层次结构, 数据驱动发现

## 3 点简述
- 核心问题：大语言模型嵌入虽能存储和检索语义相似文本，但文本语料的全局语义关系结构常不透明。
- 方法要点：通过逐步放松密度标准，在嵌入空间中从密集簇合并为扩散簇，构建层次树以捕获语义关系。
- 实验或效果：应用于科学摘要、20新闻组和IMDB电影评论数据集，展示跨领域鲁棒性和数据驱动发现能力。

## 摘要（原文）

> Semantic text classification has undergone significant advances in recent years due to the rise of large language models (LLMs) and their high dimensional embeddings. While LLM-embeddings are frequently used to store and retrieve text by semantic similarity in vector databases, the global structure semantic relationships in text corpora often remains opaque. Herein we propose a nested density clustering approach, to infer hierarchical trees of semantically related texts. The method starts by identifying texts of strong semantic similarity as it searches for dense clusters in LLM embedding space. As the density criterion is gradually relaxed, these dense clusters merge into more diffuse clusters, until the whole dataset is represented by a single cluster - the root of the tree. By embedding dense clusters into increasingly diffuse ones, we construct a tree structure that captures hierarchical semantic relationships among texts. We outline how this approach can be used to classify textual data for abstracts of scientific abstracts as a case study. This enables the data-driven discovery research areas and their subfields without predefined categories. To evaluate the general applicability of the method, we further apply it to established benchmark datasets such as the 20 News- groups and IMDB 50k Movie Reviews, demonstrating its robustness across domains. Finally we discuss possible applications on scientometrics, topic evolution, highlighting how nested density trees can reveal semantic structure and evolution in textual datasets.

