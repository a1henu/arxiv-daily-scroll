---
layout: default
title: Visual Model Checking: Graph-Based Inference of Visual Routines for Image Retrieval
---

# Visual Model Checking: Graph-Based Inference of Visual Routines for Image Retrieval
**arXiv**：[2602.17386v1](https://arxiv.org/abs/2602.17386) · [PDF](https://arxiv.org/pdf/2602.17386.pdf)  
**作者**：Adrià Molina, Oriol Ramos Terrades, Josep Lladós  

**一句话要点**：提出基于图验证与神经代码生成的视觉模型检查框架，以提升图像检索的可信度与可验证性。

**关键词**：图像检索, 形式验证, 图推理, 神经代码生成, 可解释性

## 3 点简述
- 核心问题：当前图像检索在处理复杂关系、对象组合或精确约束时存在不可靠性。
- 方法要点：结合图验证与神经代码生成，通过形式推理验证查询中的原子真值。
- 实验或效果：增强检索结果的透明度与可问责性，提升基于嵌入方法的性能。

## 摘要（原文）

> Information retrieval lies at the foundation of the modern digital industry. While natural language search has seen dramatic progress in recent years largely driven by embedding-based models and large-scale pretraining, the field still faces significant challenges. Specifically, queries that involve complex relationships, object compositions, or precise constraints such as identities, counts and proportions often remain unresolved or unreliable within current frameworks. In this paper, we propose a novel framework that integrates formal verification into deep learning-based image retrieval through a synergistic combination of graph-based verification methods and neural code generation. Our approach aims to support open-vocabulary natural language queries while producing results that are both trustworthy and verifiable. By grounding retrieval results in a system of formal reasoning, we move beyond the ambiguity and approximation that often characterize vector representations. Instead of accepting uncertainty as a given, our framework explicitly verifies each atomic truth in the user query against the retrieved content. This allows us to not only return matching results, but also to identify and mark which specific constraints are satisfied and which remain unmet, thereby offering a more transparent and accountable retrieval process while boosting the results of the most popular embedding-based approaches.

