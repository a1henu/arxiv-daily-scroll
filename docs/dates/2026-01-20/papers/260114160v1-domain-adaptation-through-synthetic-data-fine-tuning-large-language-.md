---
layout: default
title: Domain-Adaptation through Synthetic Data: Fine-Tuning Large Language Models for German Law
---

# Domain-Adaptation through Synthetic Data: Fine-Tuning Large Language Models for German Law
**arXiv**：[2601.14160v1](https://arxiv.org/abs/2601.14160) · [PDF](https://arxiv.org/pdf/2601.14160.pdf)  
**作者**：Ali Hamza Bashir, Muhammad Rehan Khalid, Kostadin Cvejoski, Jana Birr, Jule Berghaus, Armin Berger, Sandra Halscheidt, Christian Temath, Rafet Sifa, David Berghaus  

**一句话要点**：提出基于合成数据的领域适应方法，以提升大语言模型在德国法律问答中的性能。

**关键词**：领域适应, 合成数据生成, 法律问答, 大语言模型微调, 德国法律

## 3 点简述
- 大语言模型在法律推理等专业领域因知识有限易产生错误输出。
- 从权威德国法规系统生成高质量合成问答对，结合自动过滤和参数高效微调。
- 实验显示，适应后模型在德国法律问答任务上显著优于基线模型。

## 摘要（原文）

> Large language models (LLMs) often struggle in specialized domains such as legal reasoning due to limited expert knowledge, resulting in factually incorrect outputs or hallucinations. This paper presents an effective method for adapting advanced LLMs to German legal question answering through a novel synthetic data generation approach. In contrast to costly human-annotated resources or unreliable synthetic alternatives, our approach systematically produces high-quality, diverse, and legally accurate question-answer pairs directly from authoritative German statutes. Using rigorous automated filtering methods and parameter-efficient fine-tuning techniques, we demonstrate that LLMs adapted with our synthetic dataset significantly outperform their baseline counterparts on German legal question answering tasks. Our results highlight the feasibility of using carefully designed synthetic data as a robust alternative to manual annotation in high-stakes, knowledge-intensive domains.

