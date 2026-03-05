---
layout: default
title: RAGNav: A Retrieval-Augmented Topological Reasoning Framework for Multi-Goal Visual-Language Navigation
---

# RAGNav: A Retrieval-Augmented Topological Reasoning Framework for Multi-Goal Visual-Language Navigation
**arXiv**：[2603.03745v1](https://arxiv.org/abs/2603.03745) · [PDF](https://arxiv.org/pdf/2603.03745.pdf)  
**作者**：Ling Luo, Qiangian Bai  

**一句话要点**：提出RAGNav框架以解决多目标视觉语言导航中的空间幻觉和规划漂移问题

**关键词**：多目标视觉语言导航, 检索增强生成, 拓扑推理, 空间建模, 语义校准

## 3 点简述
- 核心问题：多目标VLN中，通用RAG范式因缺乏显式空间建模，易产生空间幻觉和规划漂移
- 方法要点：引入双基记忆系统，结合低层拓扑图和高层语义森林，实现锚点引导检索和拓扑邻居分数传播
- 实验或效果：在复杂多目标导航任务中达到SOTA性能，提升目标间可达性推理和顺序规划效率

## 摘要（原文）

> Vision-Language Navigation (VLN) is evolving from single-point pathfinding toward the more challenging Multi-Goal VLN. This task requires agents to accurately identify multiple entities while collaboratively reasoning over their spatial-physical constraints and sequential execution order. However, generic Retrieval-Augmented Generation (RAG) paradigms often suffer from spatial hallucinations and planning drift when handling multi-object associations due to the lack of explicit spatial modeling.To address these challenges, we propose RAGNav, a framework that bridges the gap between semantic reasoning and physical structure. The core of RAGNav is a Dual-Basis Memory system, which integrates a low-level topological map for maintaining physical connectivity with a high-level semantic forest for hierarchical environment abstraction. Building on this representation, the framework introduces an anchor-guided conditional retrieval and a topological neighbor score propagation mechanism. This approach facilitates the rapid screening of candidate targets and the elimination of semantic noise, while performing semantic calibration by leveraging the physical associations inherent in the topological neighborhood.This mechanism significantly enhances the capability of inter-target reachability reasoning and the efficiency of sequential planning. Experimental results demonstrate that RAGNav achieves state-of-the-art (SOTA) performance in complex multi-goal navigation tasks.

