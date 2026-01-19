---
layout: default
title: Relational Linearity is a Predictor of Hallucinations
---

# Relational Linearity is a Predictor of Hallucinations
**arXiv**：[2601.11429v1](https://arxiv.org/abs/2601.11429) · [PDF](https://arxiv.org/pdf/2601.11429.pdf)  
**作者**：Yuetian Lu, Yihong Liu, Hinrich Schütze  

**一句话要点**：提出关系线性度作为幻觉预测因子，通过合成实体实验验证其与幻觉率的相关性。

**关键词**：幻觉预测, 关系线性度, 知识存储, 合成实体, 自我评估, 大语言模型

## 3 点简述
- 核心问题：大语言模型在回答未知实体问题时易产生幻觉，难以自我评估知识。
- 方法要点：假设关系线性度影响知识存储方式，线性关系更抽象导致幻觉，使用Δcos测量线性度。
- 实验或效果：构建SyntHal数据集，在四个模型中验证线性度与幻觉率强相关（r∈[.78,.82]）。

## 摘要（原文）

> Hallucination is a central failure mode in large language models (LLMs). We focus on hallucinations of answers to questions like: "Which instrument did Glenn Gould play?", but we ask these questions for synthetic entities that are unknown to the model. Surprisingly, we find that medium-size models like Gemma-7B-IT frequently hallucinate, i.e., they have difficulty recognizing that the hallucinated fact is not part of their knowledge. We hypothesize that an important factor in causing these hallucinations is the linearity of the relation: linear relations tend to be stored more abstractly, making it difficult for the LLM to assess its knowledge; the facts of nonlinear relations tend to be stored more directly, making knowledge assessment easier. To investigate this hypothesis, we create SyntHal, a dataset of 6000 synthetic entities for six relations. In our experiments with four models, we determine, for each relation, the hallucination rate on SyntHal and also measure its linearity, using $Δ\cos$. We find a strong correlation ($r \in [.78,.82]$) between relational linearity and hallucination rate, providing evidence for our hypothesis that the underlying storage of triples of a relation is a factor in how well a model can self-assess its knowledge. This finding has implications for how to manage hallucination behavior and suggests new research directions for improving the representation of factual knowledge in LLMs.

