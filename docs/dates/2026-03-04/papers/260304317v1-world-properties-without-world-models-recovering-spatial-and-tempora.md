---
layout: default
title: World Properties without World Models: Recovering Spatial and Temporal Structure from Co-occurrence Statistics in Static Word Embeddings
---

# World Properties without World Models: Recovering Spatial and Temporal Structure from Co-occurrence Statistics in Static Word Embeddings
**arXiv**：[2603.04317v1](https://arxiv.org/abs/2603.04317) · [PDF](https://arxiv.org/pdf/2603.04317.pdf)  
**作者**：Elan Barenholtz  

**一句话要点**：通过静态词嵌入的共现统计恢复空间与时间结构，挑战世界模型必要性

**关键词**：静态词嵌入, 共现统计, 线性探针, 空间结构恢复, 时间结构恢复, 岭回归

## 3 点简述
- 核心问题：线性探针从LLM隐藏状态恢复地理和时序变量是否证明世界模型存在？
- 方法要点：应用岭回归探针到GloVe和Word2Vec静态嵌入，分析共现统计中的结构。
- 实验或效果：城市坐标R²达0.71-0.87，出生年份R²为0.48-0.52，依赖词汇梯度如国名和气候词。

## 摘要（原文）

> Recent work interprets the linear recoverability of geographic and temporal variables from large language model (LLM) hidden states as evidence for world-like internal representations. We test a simpler possibility: that much of the relevant structure is already latent in text itself. Applying the same class of ridge regression probes to static co-occurrence-based embeddings (GloVe and Word2Vec), we find substantial recoverable geographic signal and weaker but reliable temporal signal, with held-out R^2 values of 0.71-0.87 for city coordinates and 0.48-0.52 for historical birth years. Semantic-neighbor analyses and targeted subspace ablations show that these signals depend strongly on interpretable lexical gradients, especially country names and climate-related vocabulary. These findings suggest that ordinary word co-occurrence preserves richer spatial, temporal, and environmental structure than is often assumed, revealing a remarkable and underappreciated capacity of simple static embeddings to preserve world-shaped structure from text alone. Linear probe recoverability alone therefore does not establish a representational move beyond text.

