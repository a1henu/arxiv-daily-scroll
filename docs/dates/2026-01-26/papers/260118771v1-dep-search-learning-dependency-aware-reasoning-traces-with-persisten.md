---
layout: default
title: Dep-Search: Learning Dependency-Aware Reasoning Traces with Persistent Memory
---

# Dep-Search: Learning Dependency-Aware Reasoning Traces with Persistent Memory
**arXiv**：[2601.18771v1](https://arxiv.org/abs/2601.18771) · [PDF](https://arxiv.org/pdf/2601.18771.pdf)  
**作者**：Yanming Liu, Xinyue Peng, Zixuan Yan, Yanxin Shen, Wenjie Xu, Yuefeng Huang, Xinyi Wang, Jiannan Cao, Jianwei Yin, Xuhong Zhang  

**一句话要点**：提出Dep-Search框架，通过依赖感知推理和持久内存增强LLMs在复杂问答中的性能。

**关键词**：依赖感知推理, 持久内存, 检索增强生成, 多跳问答, 强化学习优化

## 3 点简述
- 现有搜索框架依赖隐式自然语言推理，难以管理子问题依赖和重用知识。
- Dep-Search集成结构化推理、检索和持久内存，通过GRPO实现显式控制机制。
- 在七个问答数据集上实验显示，Dep-Search显著提升多跳推理能力，优于基线模型。

## 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities in complex reasoning tasks, particularly when augmented with search mechanisms that enable systematic exploration of external knowledge bases. The field has evolved from traditional retrieval-augmented generation (RAG) frameworks to more sophisticated search-based frameworks that orchestrate multi-step reasoning through explicit search strategies. However, existing search frameworks still rely heavily on implicit natural language reasoning to determine search strategies and how to leverage retrieved information across reasoning steps. This reliance on implicit reasoning creates fundamental challenges for managing dependencies between sub-questions, efficiently reusing previously retrieved knowledge, and learning optimal search strategies through reinforcement learning. To address these limitations, we propose Dep-Search, a dependency-aware search framework that advances beyond existing search frameworks by integrating structured reasoning, retrieval, and persistent memory through GRPO. Dep-Search introduces explicit control mechanisms that enable the model to decompose questions with dependency relationships, retrieve information when needed, access previously stored knowledge from memory, and summarize long reasoning contexts into reusable memory entries. Through extensive experiments on seven diverse question answering datasets, we demonstrate that Dep-Search significantly enhances LLMs' ability to tackle complex multi-hop reasoning tasks, achieving substantial improvements over strong baselines across different model scales.

