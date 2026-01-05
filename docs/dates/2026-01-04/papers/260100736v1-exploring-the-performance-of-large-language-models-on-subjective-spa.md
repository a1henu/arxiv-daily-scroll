---
layout: default
title: Exploring the Performance of Large Language Models on Subjective Span Identification Tasks
---

# Exploring the Performance of Large Language Models on Subjective Span Identification Tasks
**arXiv**：[2601.00736v1](https://arxiv.org/abs/2601.00736) · [PDF](https://arxiv.org/pdf/2601.00736.pdf)  
**作者**：Alphaeus Dmonte, Roland Oruche, Tharindu Ranasinghe, Marcos Zampieri, Prasad Calyam  

**一句话要点**：评估大型语言模型在主观跨度识别任务中的性能，填补相关研究空白。

**关键词**：主观跨度识别, 大型语言模型, 指令调优, 上下文学习, 思维链, 文本关系

## 3 点简述
- 核心问题：大型语言模型在主观跨度识别任务（如基于方面的情感分析）中性能未知，现有研究多关注显式跨度识别。
- 方法要点：采用指令调优、上下文学习和思维链等策略，评估多种大型语言模型在情感分析、冒犯性语言识别和声明验证任务中的表现。
- 实验或效果：结果表明，文本内部关系有助于大型语言模型识别精确文本跨度，但具体性能指标未知。

## 摘要（原文）

> Identifying relevant text spans is important for several downstream tasks in NLP, as it contributes to model explainability. While most span identification approaches rely on relatively smaller pre-trained language models like BERT, a few recent approaches have leveraged the latest generation of Large Language Models (LLMs) for the task. Current work has focused on explicit span identification like Named Entity Recognition (NER), while more subjective span identification with LLMs in tasks like Aspect-based Sentiment Analysis (ABSA) has been underexplored. In this paper, we fill this important gap by presenting an evaluation of the performance of various LLMs on text span identification in three popular tasks, namely sentiment analysis, offensive language identification, and claim verification. We explore several LLM strategies like instruction tuning, in-context learning, and chain of thought. Our results indicate underlying relationships within text aid LLMs in identifying precise text spans.

