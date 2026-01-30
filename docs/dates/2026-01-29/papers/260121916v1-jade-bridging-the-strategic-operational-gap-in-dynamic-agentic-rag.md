---
layout: default
title: JADE: Bridging the Strategic-Operational Gap in Dynamic Agentic RAG
---

# JADE: Bridging the Strategic-Operational Gap in Dynamic Agentic RAG
**arXiv**：[2601.21916v1](https://arxiv.org/abs/2601.21916) · [PDF](https://arxiv.org/pdf/2601.21916.pdf)  
**作者**：Yiqun Chen, Erhan Zhang, Tianyi Hu, Shijie Wang, Zixuan Yang, Meizhi Zhong, Xiaochi Wei, Yan Gao, Yi Wu, Yao Hu, Jiaxin Mao  

**一句话要点**：提出JADE框架以解决动态代理RAG中规划与执行不匹配的问题

**关键词**：检索增强生成, 动态代理工作流, 联合优化, 多智能体系统, 端到端学习

## 3 点简述
- 核心问题：现有动态RAG系统存在规划与执行模块分离优化，导致策略与操作不匹配，性能提升受限
- 方法要点：通过联合优化规划与执行，建模为共享骨干网络的多智能体协作系统，实现端到端学习
- 实验或效果：实证显示JADE能协同优化模块，显著提升性能，并灵活平衡效率与效果

## 摘要（原文）

> The evolution of Retrieval-Augmented Generation (RAG) has shifted from static retrieval pipelines to dynamic, agentic workflows where a central planner orchestrates multi-turn reasoning. However, existing paradigms face a critical dichotomy: they either optimize modules jointly within rigid, fixed-graph architectures, or empower dynamic planning while treating executors as frozen, black-box tools. We identify that this \textit{decoupled optimization} creates a ``strategic-operational mismatch,'' where sophisticated planning strategies fail to materialize due to unadapted local executors, often leading to negative performance gains despite increased system complexity. In this paper, we propose \textbf{JADE} (\textbf{J}oint \textbf{A}gentic \textbf{D}ynamic \textbf{E}xecution), a unified framework for the joint optimization of planning and execution within dynamic, multi-turn workflows. By modeling the system as a cooperative multi-agent team unified under a single shared backbone, JADE enables end-to-end learning driven by outcome-based rewards. This approach facilitates \textit{co-adaptation}: the planner learns to operate within the capability boundaries of the executors, while the executors evolve to align with high-level strategic intent. Empirical results demonstrate that JADE transforms disjoint modules into a synergistic system, yielding remarkable performance improvements via joint optimization and enabling a flexible balance between efficiency and effectiveness through dynamic workflow orchestration.

