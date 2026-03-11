---
layout: default
title: DataFactory: Collaborative Multi-Agent Framework for Advanced Table Question Answering
---

# DataFactory: Collaborative Multi-Agent Framework for Advanced Table Question Answering
**arXiv**：[2603.09152v1](https://arxiv.org/abs/2603.09152) · [PDF](https://arxiv.org/pdf/2603.09152.pdf)  
**作者**：Tong Wang, Chi Jin, Yongkang Chen, Huan Deng, Xiaohui Kuang, Gang Zhao  

**一句话要点**：提出DataFactory多智能体框架以解决表格问答中的上下文限制、幻觉和复杂推理问题

**关键词**：表格问答, 多智能体系统, 知识图谱转换, 上下文工程, 协作推理, 企业数据分析

## 3 点简述
- 现有LLM方法在表格问答中面临上下文长度限制、幻觉和单智能体架构不足等关键问题
- DataFactory通过Data Leader协调数据库和知识图谱团队，实现查询分解和自动化知识转换
- 在多个基准测试中，该方法显著提升准确率，并优于单团队变体，提供企业数据分析平台

## 摘要（原文）

> Table Question Answering (TableQA) enables natural language interaction with structured tabular data. However, existing large language model (LLM) approaches face critical limitations: context length constraints that restrict data handling capabilities, hallucination issues that compromise answer reliability, and single-agent architectures that struggle with complex reasoning scenarios involving semantic relationships and multi-hop logic. This paper introduces DataFactory, a multi-agent framework that addresses these limitations through specialized team coordination and automated knowledge transformation. The framework comprises a Data Leader employing the ReAct paradigm for reasoning orchestration, together with dedicated Database and Knowledge Graph teams, enabling the systematic decomposition of complex queries into structured and relational reasoning tasks. We formalize automated data-to-knowledge graph transformation via the mapping function T:D x S x R -> G, and implement natural language-based consultation that - unlike fixed workflow multi-agent systems - enables flexible inter-agent deliberation and adaptive planning to improve coordination robustness. We also apply context engineering strategies that integrate historical patterns and domain knowledge to reduce hallucinations and improve query accuracy. Across TabFact, WikiTableQuestions, and FeTaQA, using eight LLMs from five providers, results show consistent gains. Our approach improves accuracy by 20.2% (TabFact) and 23.9% (WikiTQ) over baselines, with significant effects (Cohen's d > 1). Team coordination also outperforms single-team variants (+5.5% TabFact, +14.4% WikiTQ, +17.1% FeTaQA ROUGE-2). The framework offers design guidelines for multi-agent collaboration and a practical platform for enterprise data analysis through integrated structured querying and graph-based knowledge representation.

