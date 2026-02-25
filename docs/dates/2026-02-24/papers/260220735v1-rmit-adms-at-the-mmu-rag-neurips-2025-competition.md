---
layout: default
title: RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition
---

# RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition
**arXiv**：[2602.20735v1](https://arxiv.org/abs/2602.20735) · [PDF](https://arxiv.org/pdf/2602.20735.pdf)  
**作者**：Kun Ran, Marwah Alaofi, Danula Hettiachchi, Chenglong Ma, Khoi Nguyen Dinh Anh, Khoi Vo Nguyen, Sachin Pathiyan Cherumanal, Lida Rashidi, Falk Scholer, Damiano Spina, Shuoqi Sun, Oleg Zendel  

**一句话要点**：提出Routing-to-RAG架构，基于查询复杂性和证据充分性动态调整检索策略，用于NeurIPS 2025 MMU-RAG竞赛的文本到文本任务。

**关键词**：检索增强生成, 动态检索策略, 轻量级架构, 文本到文本任务, 资源效率优化

## 3 点简述
- 核心问题：在资源受限环境下，如何高效支持复杂研究任务的检索增强生成，需动态适应查询和证据。
- 方法要点：采用轻量级组件构建R2RAG架构，基于G-RAG系统扩展，通过模块化设计优化检索策略。
- 实验或效果：在NeurIPS 2025竞赛中获最佳动态评估奖，单消费级GPU运行，展示高有效性和资源效率。

## 摘要（原文）

> This paper presents the award-winning RMIT-ADM+S system for the Text-to-Text
>   track of the NeurIPS~2025 MMU-RAG Competition. We introduce Routing-to-RAG
>   (R2RAG), a research-focused retrieval-augmented generation (RAG)
>   architecture composed of lightweight components that dynamically adapt the
>   retrieval strategy based on inferred query complexity and evidence
>   sufficiency. The system uses smaller LLMs, enabling operation on a single
>   consumer-grade GPU while supporting complex research tasks. It builds on the
>   G-RAG system, winner of the ACM~SIGIR~2025 LiveRAG Challenge, and extends it
>   with modules informed by qualitative review of outputs. R2RAG won the Best
>   Dynamic Evaluation award in the Open Source category, demonstrating high
>   effectiveness with careful design and efficient use of resources.

