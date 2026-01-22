---
layout: default
title: Query-Efficient Agentic Graph Extraction Attacks on GraphRAG Systems
---

# Query-Efficient Agentic Graph Extraction Attacks on GraphRAG Systems
**arXiv**：[2601.14662v1](https://arxiv.org/abs/2601.14662) · [PDF](https://arxiv.org/pdf/2601.14662.pdf)  
**作者**：Shuhua Yang, Jiahao Zhang, Yilong Wang, Dongwon Lee, Suhang Wang  

**一句话要点**：提出AGEA框架以在查询预算限制下高效窃取GraphRAG系统的隐藏图结构

**关键词**：图检索增强生成, 图结构窃取攻击, 查询效率优化, 黑盒攻击, 多跳推理系统

## 3 点简述
- 研究GraphRAG系统在查询预算约束下隐藏图结构被窃取的可行性问题
- 提出AGEA框架，结合探索-利用策略、外部图记忆模块和两阶段提取流程
- 在多个数据集和系统上评估，AGEA显著优于基线，恢复高达90%的实体和关系

## 摘要（原文）

> Graph-based retrieval-augmented generation (GraphRAG) systems construct knowledge graphs over document collections to support multi-hop reasoning. While prior work shows that GraphRAG responses may leak retrieved subgraphs, the feasibility of query-efficient reconstruction of the hidden graph structure remains unexplored under realistic query budgets. We study a budget-constrained black-box setting where an adversary adaptively queries the system to steal its latent entity-relation graph. We propose AGEA (Agentic Graph Extraction Attack), a framework that leverages a novelty-guided exploration-exploitation strategy, external graph memory modules, and a two-stage graph extraction pipeline combining lightweight discovery with LLM-based filtering. We evaluate AGEA on medical, agriculture, and literary datasets across Microsoft-GraphRAG and LightRAG systems. Under identical query budgets, AGEA significantly outperforms prior attack baselines, recovering up to 90% of entities and relationships while maintaining high precision. These results demonstrate that modern GraphRAG systems are highly vulnerable to structured, agentic extraction attacks, even under strict query limits.

