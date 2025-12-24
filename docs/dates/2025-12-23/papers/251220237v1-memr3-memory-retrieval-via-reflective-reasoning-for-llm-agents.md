---
layout: default
title: MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agents
---

# MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agents
**arXiv**：[2512.20237v1](https://arxiv.org/abs/2512.20237) · [PDF](https://arxiv.org/pdf/2512.20237.pdf)  
**作者**：Xingbo Du, Loka Li, Duzhen Zhang, Le Song  

**一句话要点**：提出MemR^3系统，通过闭环控制优化LLM代理的记忆检索，提升答案质量。

**关键词**：记忆检索, 闭环控制, LLM代理, 路由器机制, 证据跟踪

## 3 点简述
- 核心问题：现有记忆系统重压缩存储，轻显式闭环检索控制。
- 方法要点：引入路由器选择检索、反思或回答动作，并跟踪证据收集过程。
- 实验效果：在LoCoMo基准上超越基线，提升RAG和Zep检索器性能。

## 摘要（原文）

> Memory systems have been designed to leverage past experiences in Large Language Model (LLM) agents. However, many deployed memory systems primarily optimize compression and storage, with comparatively less emphasis on explicit, closed-loop control of memory retrieval. From this observation, we build memory retrieval as an autonomous, accurate, and compatible agent system, named MemR$^3$, which has two core mechanisms: 1) a router that selects among retrieve, reflect, and answer actions to optimize answer quality; 2) a global evidence-gap tracker that explicitly renders the answering process transparent and tracks the evidence collection process. This design departs from the standard retrieve-then-answer pipeline by introducing a closed-loop control mechanism that enables autonomous decision-making. Empirical results on the LoCoMo benchmark demonstrate that MemR$^3$ surpasses strong baselines on LLM-as-a-Judge score, and particularly, it improves existing retrievers across four categories with an overall improvement on RAG (+7.29%) and Zep (+1.94%) using GPT-4.1-mini backend, offering a plug-and-play controller for existing memory stores.

