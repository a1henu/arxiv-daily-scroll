---
layout: default
title: Should LLMs, $\textit{like}$, Generate How Users Talk? Building Dialect-Accurate Dialog[ue]s Beyond the American Default with MDial
---

# Should LLMs, $\textit{like}$, Generate How Users Talk? Building Dialect-Accurate Dialog[ue]s Beyond the American Default with MDial
**arXiv**：[2601.22888v1](https://arxiv.org/abs/2601.22888) · [PDF](https://arxiv.org/pdf/2601.22888.pdf)  
**作者**：Jio Oh, Paul Vicinanza, Thomas Butler, Steven Euijong Whang, Dezhi Hong, Amani Namboori  

**一句话要点**：提出MDial框架以生成多方言对话数据，挑战模型应复制用户语法特征的假设。

**关键词**：多方言对话生成, 方言识别, LLM评估基准, 语法特征分析, 数据质量验证

## 3 点简述
- 问题：超80%英语非标准美语使用者与LLM交互时失败率高且易获刻板回应，多方言性能研究不足。
- 方法：MDial基于词汇、拼写和语法特征，通过规则化LLM转换生成九种英语方言的大规模对话数据。
- 效果：MDialBench评估显示前沿模型方言识别准确率低于70%，非标准方言常被误分类为美英变体。

## 摘要（原文）

> More than 80% of the 1.6 billion English speakers do not use Standard American English (SAE) and experience higher failure rates and stereotyped responses when interacting with LLMs as a result. Yet multi-dialectal performance remains underexplored. We introduce $\textbf{MDial}$, the first large-scale framework for generating multi-dialectal conversational data encompassing the three pillars of written dialect -- lexical (vocabulary), orthographic (spelling), and morphosyntactic (grammar) features -- for nine English dialects. Partnering with native linguists, we design an annotated and scalable rule-based LLM transformation to ensure precision. Our approach challenges the assumption that models should mirror users' morphosyntactic features, showing that up to 90% of the grammatical features of a dialect should not be reproduced by models. Independent evaluations confirm data quality, with annotators preferring MDial outputs over prior methods in 98% of pairwise comparisons for dialect naturalness. Using this pipeline, we construct the dialect-parallel $\textbf{MDialBench}$mark with 50k+ dialogs, resulting in 97k+ QA pairs, and evaluate 17 LLMs on dialect identification and response generation tasks. Even frontier models achieve under 70% accuracy, fail to reach 50% for Canadian English, and systematically misclassify non-SAE dialects as American or British. As dialect identification underpins natural language understanding, these errors risk cascading failures into downstream tasks.

