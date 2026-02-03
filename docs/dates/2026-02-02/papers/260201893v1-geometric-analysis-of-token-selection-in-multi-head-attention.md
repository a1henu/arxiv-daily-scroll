---
layout: default
title: Geometric Analysis of Token Selection in Multi-Head Attention
---

# Geometric Analysis of Token Selection in Multi-Head Attention
**arXiv**：[2602.01893v1](https://arxiv.org/abs/2602.01893) · [PDF](https://arxiv.org/pdf/2602.01893.pdf)  
**作者**：Timur Mudarisov, Mikhal Burtsev, Tatiana Petrova, Radu State  

**一句话要点**：提出几何框架分析多头注意力中的令牌选择，用于大语言模型的可解释性与设计优化。

**关键词**：多头注意力, 几何分析, 令牌选择, 大语言模型, 可解释性, 稀疏化

## 3 点简述
- 核心问题：分析多头注意力机制中令牌选择的几何特性，量化选择与非选择令牌的可分性。
- 方法要点：基于几何度量（精确率、召回率、F分数）和非渐近边界，在值状态空间中研究标准注意力的行为。
- 实验或效果：在LLaMA-2-7B等模型上验证理论预测，发现注意力头分为检索器、混合器和重置器三种几何模式。

## 摘要（原文）

> We present a geometric framework for analysing multi-head attention in large language models (LLMs). Without altering the mechanism, we view standard attention through a top-N selection lens and study its behaviour directly in value-state space. We define geometric metrics - Precision, Recall, and F-score - to quantify separability between selected and non-selected tokens, and derive non-asymptotic bounds with explicit dependence on dimension and margin under empirically motivated assumptions (stable value norms with a compressed sink token, exponential similarity decay, and piecewise attention weight profiles). The theory predicts a small-N operating regime of strongest non-trivial separability and clarifies how sequence length and sink similarity shape the metrics. Empirically, across LLaMA-2-7B, Gemma-7B, and Mistral-7B, measurements closely track the theoretical envelopes: top-N selection sharpens separability, sink similarity correlates with Recall. We also found that in LLaMA-2-7B heads specialize into three regimes - Retriever, Mixer, Reset - with distinct geometric signatures. Overall, attention behaves as a structured geometric classifier with measurable criteria for token selection, offering head level interpretability and informing geometry-aware sparsification and design of attention in LLMs.

