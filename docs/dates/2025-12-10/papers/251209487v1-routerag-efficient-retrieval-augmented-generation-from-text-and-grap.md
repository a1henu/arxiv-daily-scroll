---
layout: default
title: RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning
---

# RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning
**arXiv**：[2512.09487v1](https://arxiv.org/abs/2512.09487) · [PDF](https://arxiv.org/pdf/2512.09487.pdf)  
**作者**：Yucan Guo, Miao Su, Saiping Guan, Zihao Sun, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng  

**一句话要点**：提出RouteRAG框架，通过强化学习实现文本与图混合检索增强生成，以支持自适应高效的多轮推理

**关键词**：检索增强生成, 强化学习, 图文本混合检索, 多轮推理, 自适应检索, 问答系统

## 3 点简述
- 核心问题：现有混合检索系统依赖固定流程，无法自适应整合文本与图证据，且图检索成本高
- 方法要点：基于强化学习联合优化生成过程，学习何时推理、从何处检索及何时输出答案
- 实验效果：在五个问答基准上显著超越现有RAG基线，验证了端到端强化学习的优势

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) integrates non-parametric knowledge into Large Language Models (LLMs), typically from unstructured texts and structured graphs. While recent progress has advanced text-based RAG to multi-turn reasoning through Reinforcement Learning (RL), extending these advances to hybrid retrieval introduces additional challenges. Existing graph-based or hybrid systems typically depend on fixed or handcrafted retrieval pipelines, lacking the ability to integrate supplementary evidence as reasoning unfolds. Besides, while graph evidence provides relational structures crucial for multi-hop reasoning, it is substantially more expensive to retrieve. To address these limitations, we introduce \model{}, an RL-based framework that enables LLMs to perform multi-turn and adaptive graph-text hybrid RAG. \model{} jointly optimizes the entire generation process via RL, allowing the model to learn when to reason, what to retrieve from either texts or graphs, and when to produce final answers, all within a unified generation policy. To guide this learning process, we design a two-stage training framework that accounts for both task outcome and retrieval efficiency, enabling the model to exploit hybrid evidence while avoiding unnecessary retrieval overhead. Experimental results across five question answering benchmarks demonstrate that \model{} significantly outperforms existing RAG baselines, highlighting the benefits of end-to-end RL in supporting adaptive and efficient retrieval for complex reasoning.

