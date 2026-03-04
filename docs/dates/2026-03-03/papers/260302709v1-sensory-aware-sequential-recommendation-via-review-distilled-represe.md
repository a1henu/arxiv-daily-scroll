---
layout: default
title: Sensory-Aware Sequential Recommendation via Review-Distilled Representations
---

# Sensory-Aware Sequential Recommendation via Review-Distilled Representations
**arXiv**：[2603.02709v1](https://arxiv.org/abs/2603.02709) · [PDF](https://arxiv.org/pdf/2603.02709.pdf)  
**作者**：Yeo Chan Yoon  

**一句话要点**：提出ASEGR框架，通过评论蒸馏感官属性增强序列推荐

**关键词**：感官感知序列推荐, 属性蒸馏, 评论分析, 嵌入学习, 大语言模型应用

## 3 点简述
- 核心问题：序列推荐中物品表示缺乏感官属性信息，难以捕捉用户体验语义。
- 方法要点：使用大语言模型提取评论中的感官属性-值对，并蒸馏到学生Transformer生成可重用嵌入。
- 实验或效果：在四个亚马逊领域集成感官嵌入，提升SASRec等模型的推荐性能，验证互补性。

## 摘要（原文）

> We propose a novel framework for sensory-aware sequential recommendation that enriches item representations with linguistically extracted sensory attributes from product reviews. Our approach, \textsc{ASEGR} (Attribute-based Sensory Enhanced Generative Recommendation), introduces a two-stage pipeline in which a large language model is first fine-tuned as a teacher to extract structured sensory attribute--value pairs, such as \textit{color: matte black} and \textit{scent: vanilla}, from unstructured review text. The extracted structures are then distilled into a compact student transformer that produces fixed-dimensional sensory embeddings for each item. These embeddings encode experiential semantics in a reusable form and are incorporated into standard sequential recommender architectures as additional item-level representations. We evaluate our method on four Amazon domains and integrate the learned sensory embeddings into representative sequential recommendation models, including SASRec, BERT4Rec, and BSARec. Across domains, sensory-enhanced models consistently outperform their identifier-based counterparts, indicating that linguistically grounded sensory representations provide complementary signals to behavioral interaction patterns. Qualitative analysis further shows that the extracted attributes align closely with human perceptions of products, enabling interpretable connections between natural language descriptions and recommendation behavior. Overall, this work demonstrates that sensory attribute distillation offers a principled and scalable way to bridge information extraction and sequential recommendation through structured semantic representation learning.

