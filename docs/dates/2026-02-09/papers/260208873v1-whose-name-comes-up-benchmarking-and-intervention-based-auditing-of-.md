---
layout: default
title: Whose Name Comes Up? Benchmarking and Intervention-Based Auditing of LLM-Based Scholar Recommendation
---

# Whose Name Comes Up? Benchmarking and Intervention-Based Auditing of LLM-Based Scholar Recommendation
**arXiv**：[2602.08873v1](https://arxiv.org/abs/2602.08873) · [PDF](https://arxiv.org/pdf/2602.08873.pdf)  
**作者**：Lisette Espin-Noboa, Gonzalo Gabriel Mendez  

**一句话要点**：提出LLMScholarBench基准，联合评估LLM学术专家推荐中的模型基础设施与用户干预。

**关键词**：学术专家推荐, 大语言模型审计, 用户干预评估, 基准测试, 检索增强生成, 社会表示

## 3 点简述
- 核心问题：现有审计孤立评估模型输出，忽略用户干预对推荐失败（如拒绝、幻觉）的影响。
- 方法要点：通过多任务基准，结合温度变化、表示约束提示和RAG等干预，测量技术质量与社会表示。
- 实验或效果：干预不统一改进，而是重新分配错误；温度升高降低有效性，RAG提高技术质量但减少多样性。

## 摘要（原文）

> Large language models (LLMs) are increasingly used for academic expert recommendation. Existing audits typically evaluate model outputs in isolation, largely ignoring end-user inference-time interventions. As a result, it remains unclear whether failures such as refusals, hallucinations, and uneven coverage stem from model choice or deployment decisions. We introduce LLMScholarBench, a benchmark for auditing LLM-based scholar recommendation that jointly evaluates model infrastructure and end-user interventions across multiple tasks. LLMScholarBench measures both technical quality and social representation using nine metrics. We instantiate the benchmark in physics expert recommendation and audit 22 LLMs under temperature variation, representation-constrained prompting, and retrieval-augmented generation (RAG) via web search. Our results show that end-user interventions do not yield uniform improvements but instead redistribute error across dimensions. Higher temperature degrades validity, consistency, and factuality. Representation-constrained prompting improves diversity at the expense of factuality, while RAG primarily improves technical quality while reducing diversity and parity. Overall, end-user interventions reshape trade-offs rather than providing a general fix. We release code and data that can be adapted to other disciplines by replacing domain-specific ground truth and metrics.

