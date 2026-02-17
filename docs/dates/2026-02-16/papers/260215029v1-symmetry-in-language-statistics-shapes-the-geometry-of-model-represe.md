---
layout: default
title: Symmetry in language statistics shapes the geometry of model representations
---

# Symmetry in language statistics shapes the geometry of model representations
**arXiv**：[2602.15029v1](https://arxiv.org/abs/2602.15029) · [PDF](https://arxiv.org/pdf/2602.15029.pdf)  
**作者**：Dhruva Karkada, Daniel J. Korchinski, Andres Nava, Matthieu Wyart, Yasaman Bahri  

**一句话要点**：揭示语言统计对称性塑造模型表示几何结构，并证明其鲁棒性源于潜在变量控制。

**关键词**：语言统计对称性, 模型表示几何, 词嵌入模型, 潜在变量控制, 鲁棒性分析

## 3 点简述
- 核心问题：大语言模型表示中简单几何结构的成因未知，如月份形成圆形、年份形成一维流形。
- 方法要点：证明语言统计具有平移对称性，并理论推导其控制高维词嵌入模型的几何结构。
- 实验或效果：在词嵌入、文本嵌入和大语言模型中实证验证，即使统计受扰动，结构仍保持鲁棒。

## 摘要（原文）

> Although learned representations underlie neural networks' success, their fundamental properties remain poorly understood. A striking example is the emergence of simple geometric structures in LLM representations: for example, calendar months organize into a circle, years form a smooth one-dimensional manifold, and cities' latitudes and longitudes can be decoded by a linear probe. We show that the statistics of language exhibit a translation symmetry -- e.g., the co-occurrence probability of two months depends only on the time interval between them -- and we prove that the latter governs the aforementioned geometric structures in high-dimensional word embedding models. Moreover, we find that these structures persist even when the co-occurrence statistics are strongly perturbed (for example, by removing all sentences in which two months appear together) and at moderate embedding dimension. We show that this robustness naturally emerges if the co-occurrence statistics are collectively controlled by an underlying continuous latent variable. We empirically validate this theoretical framework in word embedding models, text embedding models, and large language models.

