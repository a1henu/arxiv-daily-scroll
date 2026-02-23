---
layout: default
title: Click it or Leave it: Detecting and Spoiling Clickbait with Informativeness Measures and Large Language Models
---

# Click it or Leave it: Detecting and Spoiling Clickbait with Informativeness Measures and Large Language Models
**arXiv**：[2602.18171v1](https://arxiv.org/abs/2602.18171) · [PDF](https://arxiv.org/pdf/2602.18171.pdf)  
**作者**：Wojciech Michaluk, Tymoteusz Urban, Mateusz Kubita, Soveatin Kuntur, Anna Wroblewska  

**一句话要点**：提出结合Transformer嵌入与语言学特征的混合方法，以检测和破坏点击诱饵标题。

**关键词**：点击诱饵检测, Transformer嵌入, 语言学特征, XGBoost分类, 自然语言处理, 信息质量评估

## 3 点简述
- 核心问题：点击诱饵标题降低在线信息质量并损害用户信任。
- 方法要点：融合Transformer文本嵌入与15个显式语言学特征，使用XGBoost分类器。
- 实验或效果：最佳模型F1分数达91%，优于传统向量化器和LLM提示分类基线。

## 摘要（原文）

> Clickbait headlines degrade the quality of online information and undermine user trust. We present a hybrid approach to clickbait detection that combines transformer-based text embeddings with linguistically motivated informativeness features. Using natural language processing techniques, we evaluate classical vectorizers, word embedding baselines, and large language model embeddings paired with tree-based classifiers. Our best-performing model, XGBoost over embeddings augmented with 15 explicit features, achieves an F1-score of 91\%, outperforming TF-IDF, Word2Vec, GloVe, LLM prompt based classification, and feature-only baselines. The proposed feature set enhances interpretability by highlighting salient linguistic cues such as second-person pronouns, superlatives, numerals, and attention-oriented punctuation, enabling transparent and well-calibrated clickbait predictions. We release code and trained models to support reproducible research.

