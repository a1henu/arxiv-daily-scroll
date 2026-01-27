---
layout: default
title: AI Agent for Reverse-Engineering Legacy Finite-Difference Code and Translating to Devito
---

# AI Agent for Reverse-Engineering Legacy Finite-Difference Code and Translating to Devito
**arXiv**：[2601.18381v1](https://arxiv.org/abs/2601.18381) · [PDF](https://arxiv.org/pdf/2601.18381.pdf)  
**作者**：Yinghan Hou, Zongyou Yang  

**一句话要点**：提出集成AI代理框架，将遗留有限差分代码逆向工程并翻译至Devito环境。

**关键词**：逆向工程, 代码翻译, 检索增强生成, 知识图谱, 有限差分法, Devito框架

## 3 点简述
- 核心问题：遗留有限差分代码难以迁移至现代Devito环境，需自动化翻译与验证。
- 方法要点：结合RAG与LLM，通过多阶段检索、知识图谱构建和约束代码合成实现翻译。
- 实验或效果：采用综合验证框架评估代码正确性、结构完整性和API合规性，支持迭代优化。

## 摘要（原文）

> To facilitate the transformation of legacy finite difference implementations into the Devito environment, this study develops an integrated AI agent framework. Retrieval-Augmented Generation (RAG) and open-source Large Language Models are combined through multi-stage iterative workflows in the system's hybrid LangGraph architecture. The agent constructs an extensive Devito knowledge graph through document parsing, structure-aware segmentation, extraction of entity relationships, and Leiden-based community detection. GraphRAG optimisation enhances query performance across semantic communities that include seismic wave simulation, computational fluid dynamics, and performance tuning libraries. A reverse engineering component derives three-level query strategies for RAG retrieval through static analysis of Fortran source code. To deliver precise contextual information for language model guidance, the multi-stage retrieval pipeline performs parallel searching, concept expansion, community-scale retrieval, and semantic similarity analysis. Code synthesis is governed by Pydantic-based constraints to guarantee structured outputs and reliability. A comprehensive validation framework integrates conventional static analysis with the G-Eval approach, covering execution correctness, structural soundness, mathematical consistency, and API compliance. The overall agent workflow is implemented on the LangGraph framework and adopts concurrent processing to support quality-based iterative refinement and state-aware dynamic routing. The principal contribution lies in the incorporation of feedback mechanisms motivated by reinforcement learning, enabling a transition from static code translation toward dynamic and adaptive analytical behavior.

