---
layout: default
title: Beyond Cosine Similarity
---

# Beyond Cosine Similarity
**arXiv**：[2602.05266v1](https://arxiv.org/abs/2602.05266) · [PDF](https://arxiv.org/pdf/2602.05266.pdf)  
**作者**：Xinbo Ai  

**一句话要点**：提出recos相似度度量以解决余弦相似度在复杂语义空间中非线性关系建模不足的问题。

**关键词**：相似度度量, 语义分析, 向量空间, 非线性关系, 嵌入模型, 语义文本相似性

## 3 点简述
- 核心问题：余弦相似度基于柯西-施瓦茨不等式，仅能捕捉线性关系，难以建模真实语义空间的复杂非线性结构。
- 方法要点：通过推导比柯西-施瓦茨更紧的上界，提出recos度量，基于排序向量分量归一化点积，放宽完美相似性条件为序数一致性。
- 实验或效果：在11种嵌入模型上实验，recos在语义文本相似性基准上比余弦相似度更符合人类判断，表现更优。

## 摘要（原文）

> Cosine similarity, the standard metric for measuring semantic similarity in vector spaces, is mathematically grounded in the Cauchy-Schwarz inequality, which inherently limits it to capturing linear relationships--a constraint that fails to model the complex, nonlinear structures of real-world semantic spaces. We advance this theoretical underpinning by deriving a tighter upper bound for the dot product than the classical Cauchy-Schwarz bound. This new bound leads directly to recos, a similarity metric that normalizes the dot product by the sorted vector components. recos relaxes the condition for perfect similarity from strict linear dependence to ordinal concordance, thereby capturing a broader class of relationships. Extensive experiments across 11 embedding models--spanning static, contextualized, and universal types--demonstrate that recos consistently outperforms traditional cosine similarity, achieving higher correlation with human judgments on standard Semantic Textual Similarity (STS) benchmarks. Our work establishes recos as a mathematically principled and empirically superior alternative, offering enhanced accuracy for semantic analysis in complex embedding spaces.

