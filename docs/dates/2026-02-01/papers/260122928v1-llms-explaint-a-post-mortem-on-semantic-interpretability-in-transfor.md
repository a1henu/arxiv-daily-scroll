---
layout: default
title: LLMs Explain't: A Post-Mortem on Semantic Interpretability in Transformer Models
---

# LLMs Explain't: A Post-Mortem on Semantic Interpretability in Transformer Models
**arXiv**：[2601.22928v1](https://arxiv.org/abs/2601.22928) · [PDF](https://arxiv.org/pdf/2601.22928.pdf)  
**作者**：Alhassan Abdelhalim, Janick Edinger, Sören Laue, Michaela Regneri  

**一句话要点**：揭示LLM语义可解释性方法的局限性，挑战现有解释结论的有效性。

**关键词**：大语言模型, 语义可解释性, 注意力机制, 嵌入分析, 方法验证, 分布式计算

## 3 点简述
- 核心问题：探究LLM中语言抽象如何形成，评估现有解释方法的可靠性。
- 方法要点：使用探测和特征映射方法分析注意力头和输入嵌入的语义结构。
- 实验或效果：两种方法均失败，显示解释结果受方法假象和数据集结构影响，而非真实语义理解。

## 摘要（原文）

> Large Language Models (LLMs) are becoming increasingly popular in pervasive computing due to their versatility and strong performance. However, despite their ubiquitous use, the exact mechanisms underlying their outstanding performance remain unclear. Different methods for LLM explainability exist, and many are, as a method, not fully understood themselves. We started with the question of how linguistic abstraction emerges in LLMs, aiming to detect it across different LLM modules (attention heads and input embeddings). For this, we used methods well-established in the literature: (1) probing for token-level relational structures, and (2) feature-mapping using embeddings as carriers of human-interpretable properties.
>   Both attempts failed for different methodological reasons: Attention-based explanations collapsed once we tested the core assumption that later-layer representations still correspond to tokens. Property-inference methods applied to embeddings also failed because their high predictive scores were driven by methodological artifacts and dataset structure rather than meaningful semantic knowledge. These failures matter because both techniques are widely treated as evidence for what LLMs supposedly understand, yet our results show such conclusions are unwarranted. These limitations are particularly relevant in pervasive and distributed computing settings where LLMs are deployed as system components and interpretability methods are relied upon for debugging, compression, and explaining models.

