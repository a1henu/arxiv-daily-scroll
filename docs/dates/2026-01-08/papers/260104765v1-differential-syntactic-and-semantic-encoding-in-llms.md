---
layout: default
title: Differential syntactic and semantic encoding in LLMs
---

# Differential syntactic and semantic encoding in LLMs
**arXiv**：[2601.04765v1](https://arxiv.org/abs/2601.04765) · [PDF](https://arxiv.org/pdf/2601.04765.pdf)  
**作者**：Santiago Acevedo, Alessandro Laio, Marco Baroni  

**一句话要点**：研究大型语言模型内部表示中句法与语义的差异编码，基于DeepSeek-V3分析线性编码特性

**关键词**：大型语言模型, 句法编码, 语义编码, 内部表示分析, 线性编码, DeepSeek-V3

## 3 点简述
- 核心问题：探索大型语言模型内部层表示如何编码句法和语义信息
- 方法要点：通过平均共享句法结构或语义的句子隐藏表示向量，提取句法和语义中心向量
- 实验或效果：发现句法和语义编码在跨层分布不同，且可部分解耦，表明差异编码

## 摘要（原文）

> We study how syntactic and semantic information is encoded in inner layer representations of Large Language Models (LLMs), focusing on the very large DeepSeek-V3. We find that, by averaging hidden-representation vectors of sentences sharing syntactic structure or meaning, we obtain vectors that capture a significant proportion of the syntactic and semantic information contained in the representations. In particular, subtracting these syntactic and semantic ``centroids'' from sentence vectors strongly affects their similarity with syntactically and semantically matched sentences, respectively, suggesting that syntax and semantics are, at least partially, linearly encoded. We also find that the cross-layer encoding profiles of syntax and semantics are different, and that the two signals can to some extent be decoupled, suggesting differential encoding of these two types of linguistic information in LLM representations.

