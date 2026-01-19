---
layout: default
title: Deep GraphRAG: A Balanced Approach to Hierarchical Retrieval and Adaptive Integration
---

# Deep GraphRAG: A Balanced Approach to Hierarchical Retrieval and Adaptive Integration
**arXiv**：[2601.11144v1](https://arxiv.org/abs/2601.11144) · [PDF](https://arxiv.org/pdf/2601.11144.pdf)  
**作者**：Yuejie Li, Ke Yang, Tao Wang, Bolin Chen, Bowen Li, Chengjun Mao  

**一句话要点**：提出Deep GraphRAG框架，通过分层检索和自适应集成平衡图检索增强生成的全面性与效率。

**关键词**：图检索增强生成, 分层检索, 自适应集成, 动态重排序, 强化学习训练, 知识集成

## 3 点简述
- 核心问题：现有GraphRAG方法在全局搜索全面性和局部搜索效率间存在权衡，缺乏稳健的多阶段重排序。
- 方法要点：采用分层全局到局部检索策略，结合三阶段过程和动态重排序模块，并引入基于DW-GRPO的知识集成模块。
- 实验或效果：在Natural Questions和HotpotQA上评估，准确性和效率显著优于基线图检索方法。

## 摘要（原文）

> Graph-based Retrieval-Augmented Generation (GraphRAG) frameworks face a trade-off between the comprehensiveness of global search and the efficiency of local search. Existing methods are often challenged by navigating large-scale hierarchical graphs, optimizing retrieval paths, and balancing exploration-exploitation dynamics, frequently lacking robust multi-stage re-ranking. To overcome these deficits, we propose Deep GraphRAG, a framework designed for a balanced approach to hierarchical retrieval and adaptive integration. It introduces a hierarchical global-to-local retrieval strategy that integrates macroscopic inter-community and microscopic intra-community contextual relations. This strategy employs a three-stage process: (1) inter-community filtering, which prunes the search space using local context; (2) community-level refinement, which prioritizes relevant subgraphs via entity-interaction analysis; and (3) entity-level fine-grained search within target communities. A beam search-optimized dynamic re-ranking module guides this process, continuously filtering candidates to balance efficiency and global comprehensiveness. Deep GraphRAG also features a Knowledge Integration Module leveraging a compact LLM, trained with Dynamic Weighting Reward GRPO (DW-GRPO). This novel reinforcement learning approach dynamically adjusts reward weights to balance three key objectives: relevance, faithfulness, and conciseness. This training enables compact models (1.5B) to approach the performance of large models (70B) in the integration task. Evaluations on Natural Questions and HotpotQA demonstrate that Deep GraphRAG significantly outperforms baseline graph retrieval methods in both accuracy and efficiency.

