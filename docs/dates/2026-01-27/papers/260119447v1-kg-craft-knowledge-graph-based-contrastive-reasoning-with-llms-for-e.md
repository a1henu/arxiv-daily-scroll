---
layout: default
title: KG-CRAFT: Knowledge Graph-based Contrastive Reasoning with LLMs for Enhancing Automated Fact-checking
---

# KG-CRAFT: Knowledge Graph-based Contrastive Reasoning with LLMs for Enhancing Automated Fact-checking
**arXiv**：[2601.19447v1](https://arxiv.org/abs/2601.19447) · [PDF](https://arxiv.org/pdf/2601.19447.pdf)  
**作者**：Vítor N. Lourenço, Aline Paes, Tillman Weyde, Audrey Depeige, Mohnish Dubey  

**一句话要点**：提出KG-CRAFT方法，基于知识图谱的对比推理增强LLMs的自动事实核查能力。

**关键词**：自动事实核查, 知识图谱, 对比推理, 大语言模型, 声明验证

## 3 点简述
- 核心问题：自动事实核查中，如何有效利用知识源提升声明的真实性验证准确性。
- 方法要点：构建知识图谱，生成对比性问题引导LLMs提取证据，合成摘要进行真实性评估。
- 实验或效果：在LIAR-RAW和RAWFC数据集上实现最优预测性能，验证了方法的有效性。

## 摘要（原文）

> Claim verification is a core component of automated fact-checking systems, aimed at determining the truthfulness of a statement by assessing it against reliable evidence sources such as documents or knowledge bases. This work presents KG-CRAFT, a method that improves automatic claim verification by leveraging large language models (LLMs) augmented with contrastive questions grounded in a knowledge graph. KG-CRAFT first constructs a knowledge graph from claims and associated reports, then formulates contextually relevant contrastive questions based on the knowledge graph structure. These questions guide the distillation of evidence-based reports, which are synthesised into a concise summary that is used for veracity assessment by LLMs. Extensive evaluations on two real-world datasets (LIAR-RAW and RAWFC) demonstrate that our method achieves a new state-of-the-art in predictive performance. Comprehensive analyses validate in detail the effectiveness of our knowledge graph-based contrastive reasoning approach in improving LLMs' fact-checking capabilities.

