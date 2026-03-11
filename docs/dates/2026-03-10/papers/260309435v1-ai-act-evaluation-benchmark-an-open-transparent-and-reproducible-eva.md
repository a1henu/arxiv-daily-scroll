---
layout: default
title: AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems
---

# AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems
**arXiv**：[2603.09435v1](https://arxiv.org/abs/2603.09435) · [PDF](https://arxiv.org/pdf/2603.09435.pdf)  
**作者**：Athanasios Davvetas, Michael Papademas, Xenia Ziouvelou, Vangelis Karkaletsis  

**一句话要点**：提出开放透明可复现的AI Act评估数据集，用于NLP和RAG系统合规性评估。

**关键词**：AI Act合规评估, RAG系统评估, NLP数据集, 风险分类, 大语言模型生成

## 3 点简述
- 核心问题：AI系统合规评估缺乏资源，手动评估易出错且受限。
- 方法要点：结合领域知识与大语言模型，生成风险分类、文章检索等任务数据集。
- 实验或效果：评估RAG方案在禁止和高风险场景F1分数达0.87和0.85。

## 摘要（原文）

> The rapid rollout of AI in heterogeneous public and societal sectors has subsequently escalated the need for compliance with regulatory standards and frameworks. The EU AI Act has emerged as a landmark in the regulatory landscape. The development of solutions that elicit the level of AI systems' compliance with such standards is often limited by the lack of resources, hindering the semi-automated or automated evaluation of their performance. This generates the need for manual work, which is often error-prone, resource-limited or limited to cases not clearly described by the regulation. This paper presents an open, transparent, and reproducible method of creating a resource that facilitates the evaluation of NLP models with a strong focus on RAG systems. We have developed a dataset that contain the tasks of risk-level classification, article retrieval, obligation generation, and question-answering for the EU AI Act. The dataset files are in a machine-to-machine appropriate format. To generate the files, we utilise domain knowledge as an exegetical basis, combining with the processing and reasoning power of large language models to generate scenarios along with the respective tasks. Our methodology demonstrates a way to harness language models for grounded generation with high document relevancy. Besides, we overcome limitations such as navigating the decision boundaries of risk-levels that are not explicitly defined within the EU AI Act, such as limited and minimal cases. Finally, we demonstrate our dataset's effectiveness by evaluating a RAG-based solution that reaches 0.87 and 0.85 F1-score for prohibited and high-risk scenarios.

