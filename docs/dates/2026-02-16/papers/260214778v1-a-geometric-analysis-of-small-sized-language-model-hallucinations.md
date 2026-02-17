---
layout: default
title: A Geometric Analysis of Small-sized Language Model Hallucinations
---

# A Geometric Analysis of Small-sized Language Model Hallucinations
**arXiv**：[2602.14778v1](https://arxiv.org/abs/2602.14778) · [PDF](https://arxiv.org/pdf/2602.14778.pdf)  
**作者**：Emanuele Ricco, Elia Onofri, Lorenzo Cima, Stefano Cresci, Roberto Di Pietro  

**一句话要点**：提出基于几何视角的小型语言模型幻觉分析方法，通过嵌入空间聚类实现高效分类

**关键词**：语言模型幻觉, 几何分析, 嵌入空间聚类, 标签高效分类, 小型语言模型

## 3 点简述
- 研究小型语言模型中的幻觉问题，即流畅但不正确的响应，影响模型可靠性
- 从几何角度分析，证明真实响应在嵌入空间中聚类更紧密，并实现可分离性
- 开发标签高效传播方法，仅需30-50个标注即可分类大量响应，F1分数超90%

## 摘要（原文）

> Hallucinations -- fluent but factually incorrect responses -- pose a major challenge to the reliability of language models, especially in multi-step or agentic settings.
>   This work investigates hallucinations in small-sized LLMs through a geometric perspective, starting from the hypothesis that when models generate multiple responses to the same prompt, genuine ones exhibit tighter clustering in the embedding space, we prove this hypothesis and, leveraging this geometrical insight, we also show that it is possible to achieve a consistent level of separability. This latter result is used to introduce a label-efficient propagation method that classifies large collections of responses from just 30-50 annotations, achieving F1 scores above 90%.
>   Our findings, framing hallucinations from a geometric perspective in the embedding space, complement traditional knowledge-centric and single-response evaluation paradigms, paving the way for further research.

