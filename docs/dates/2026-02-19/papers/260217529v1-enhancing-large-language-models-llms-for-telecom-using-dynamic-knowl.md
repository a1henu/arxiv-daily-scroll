---
layout: default
title: Enhancing Large Language Models (LLMs) for Telecom using Dynamic Knowledge Graphs and Explainable Retrieval-Augmented Generation
---

# Enhancing Large Language Models (LLMs) for Telecom using Dynamic Knowledge Graphs and Explainable Retrieval-Augmented Generation
**arXiv**：[2602.17529v1](https://arxiv.org/abs/2602.17529) · [PDF](https://arxiv.org/pdf/2602.17529.pdf)  
**作者**：Dun Yuan, Hao Zhou, Xue Liu, Hao Chen, Yan Xin, Jianzhong, Zhang  

**一句话要点**：提出KG-RAG框架，结合知识图谱与检索增强生成，以提升大语言模型在电信领域的准确性与可靠性。

**关键词**：知识图谱, 检索增强生成, 大语言模型, 电信领域, 幻觉减少, 可解释性

## 3 点简述
- 核心问题：通用大语言模型在电信领域因领域复杂性、标准演变和术语专业而表现不佳，易产生幻觉。
- 方法要点：集成知识图谱提供结构化领域知识，结合检索增强生成动态检索事实，以增强模型输出。
- 实验或效果：在基准数据集上，KG-RAG相比标准RAG和纯LLM模型，平均准确率分别提升14.3%和21.6%。

## 摘要（原文）

> Large language models (LLMs) have shown strong potential across a variety of tasks, but their application in the telecom field remains challenging due to domain complexity, evolving standards, and specialized terminology. Therefore, general-domain LLMs may struggle to provide accurate and reliable outputs in this context, leading to increased hallucinations and reduced utility in telecom operations.To address these limitations, this work introduces KG-RAG-a novel framework that integrates knowledge graphs (KGs) with retrieval-augmented generation (RAG) to enhance LLMs for telecom-specific tasks. In particular, the KG provides a structured representation of domain knowledge derived from telecom standards and technical documents, while RAG enables dynamic retrieval of relevant facts to ground the model's outputs. Such a combination improves factual accuracy, reduces hallucination, and ensures compliance with telecom specifications.Experimental results across benchmark datasets demonstrate that KG-RAG outperforms both LLM-only and standard RAG baselines, e.g., KG-RAG achieves an average accuracy improvement of 14.3% over RAG and 21.6% over LLM-only models. These results highlight KG-RAG's effectiveness in producing accurate, reliable, and explainable outputs in complex telecom scenarios.

