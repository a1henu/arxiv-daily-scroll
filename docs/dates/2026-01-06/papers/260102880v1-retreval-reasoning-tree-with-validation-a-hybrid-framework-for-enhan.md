---
layout: default
title: ReTreVal: Reasoning Tree with Validation - A Hybrid Framework for Enhanced LLM Multi-Step Reasoning
---

# ReTreVal: Reasoning Tree with Validation - A Hybrid Framework for Enhanced LLM Multi-Step Reasoning
**arXiv**：[2601.02880v1](https://arxiv.org/abs/2601.02880) · [PDF](https://arxiv.org/pdf/2601.02880.pdf)  
**作者**：Abhishek HS, Pavan C Shekar, Arpit Jain, Ashwanth Krishnan  

**一句话要点**：提出ReTreVal框架，通过结构化探索与验证增强LLM多步推理能力

**关键词**：多步推理, 思维树, 自精炼, 反思记忆, LLM验证, 知识迁移

## 3 点简述
- 针对LLM在数学与创意写作等复杂领域多步推理的挑战
- 结合思维树探索、自精炼、LLM评分与反思记忆的混合框架
- 在500个任务上超越ReAct等方法，实现探索性推理与知识迁移

## 摘要（原文）

> Multi-step reasoning remains a key challenge for Large Language Models (LLMs), particularly in complex domains such as mathematics and creative writing. While recent approaches including ReAct, Reflexion, and Self-Refine improve reasoning through iterative refinement and reflection, they often lack structured exploration of alternative solution paths and persistent learning across problems. We propose ReTreVal (Reasoning Tree with Validation), a hybrid framework that integrates Tree-of-Thoughts exploration, self-refinement, LLM-based critique scoring, and reflexion memory to enable bounded and validated multi-step reasoning. ReTreVal constructs a structured reasoning tree with adaptive depth based on problem complexity, where each node undergoes iterative self-critique and refinement guided by explicit LLM-generated feedback. A dual validation mechanism evaluates reasoning quality, coherence, and correctness at each node while persistently storing insights from successful reasoning paths and failure patterns in a reflexion memory buffer, enabling cross-problem learning. Critique-based pruning retains only the top-k highest-scoring nodes at each level, controlling computational cost while preserving high-quality solution paths. We evaluate ReTreVal against ReAct, Reflexion, and Self-Refine across 500 mathematical problems and creative writing tasks using Qwen 2.5 7B as the underlying LLM, and demonstrate that ReTreVal consistently outperforms existing methods through its combination of structured exploration, critique-driven refinement, and cross-problem memory, making it particularly effective for tasks requiring exploratory reasoning, rigorous verification, and knowledge transfer.

