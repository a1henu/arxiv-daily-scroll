---
layout: default
title: SEAL: Self-Evolving Agentic Learning for Conversational Question Answering over Knowledge Graphs
---

# SEAL: Self-Evolving Agentic Learning for Conversational Question Answering over Knowledge Graphs
**arXiv**：[2512.04868v1](https://arxiv.org/abs/2512.04868) · [PDF](https://arxiv.org/pdf/2512.04868.pdf)  
**作者**：Hao Wang, Jialun Zhong, Changcheng Wang, Zhujun Nie, Zheng Li, Shunyu Yao, Yanzeng Li, Xinchi Li  

**一句话要点**：提出SEAL框架以解决知识图谱对话问答中的结构准确性和计算效率问题

**关键词**：知识图谱对话问答, 语义解析, 自进化学习, 代理校准, S表达式生成, 多跳推理

## 3 点简述
- 核心问题：知识图谱对话问答面临指代消解、上下文依赖建模和复杂逻辑推理的挑战，现有方法存在结构不准确和高计算成本问题。
- 方法要点：采用两阶段语义解析框架，包括LLM提取核心S表达式和代理校准模块修正，结合模板完成和自进化机制实现持续适应。
- 实验或效果：在SPICE基准测试中达到最先进性能，尤其在多跳推理、比较和聚合任务中，验证了结构准确性和计算效率的显著提升。

## 摘要（原文）

> Knowledge-based conversational question answering (KBCQA) confronts persistent challenges in resolving coreference, modeling contextual dependencies, and executing complex logical reasoning. Existing approaches, whether end-to-end semantic parsing or stepwise agent-based reasoning, often suffer from structural inaccuracies and prohibitive computational costs, particularly when processing intricate queries over large knowledge graphs. To address these limitations, we introduce SEAL, a novel two-stage semantic parsing framework grounded in self-evolving agentic learning. In the first stage, a large language model (LLM) extracts a minimal S-expression core that captures the essential semantics of the input query. This core is then refined by an agentic calibration module, which corrects syntactic inconsistencies and aligns entities and relations precisely with the underlying knowledge graph. The second stage employs template-based completion, guided by question-type prediction and placeholder instantiation, to construct a fully executable S-expression. This decomposition not only simplifies logical form generation but also significantly enhances structural fidelity and linking efficiency. Crucially, SEAL incorporates a self-evolving mechanism that integrates local and global memory with a reflection module, enabling continuous adaptation from dialog history and execution feedback without explicit retraining. Extensive experiments on the SPICE benchmark demonstrate that SEAL achieves state-of-the-art performance, especially in multi-hop reasoning, comparison, and aggregation tasks. The results validate notable gains in both structural accuracy and computational efficiency, underscoring the framework's capacity for robust and scalable conversational reasoning.

