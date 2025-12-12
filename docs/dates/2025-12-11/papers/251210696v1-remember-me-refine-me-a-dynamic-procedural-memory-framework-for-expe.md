---
layout: default
title: Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
---

# Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
**arXiv**：[2512.10696v1](https://arxiv.org/abs/2512.10696) · [PDF](https://arxiv.org/pdf/2512.10696.pdf)  
**作者**：Zouying Cao, Jiaji Deng, Li Yu, Weikang Zhou, Zhaoyang Liu, Bolin Ding, Hai Zhao  

**一句话要点**：提出ReMe框架以解决LLM智能体记忆系统静态积累问题，实现动态经验驱动进化。

**关键词**：LLM智能体, 程序记忆, 经验蒸馏, 动态推理, 终身学习, 记忆系统

## 3 点简述
- 核心问题：现有LLM智能体记忆框架多为被动积累，缺乏动态推理与更新机制。
- 方法要点：通过多面蒸馏、上下文自适应重用和基于效用的精炼，实现记忆全生命周期管理。
- 实验或效果：在BFCL-V3和AppWorld上达到SOTA，Qwen3-8B+ReMe超越无记忆Qwen3-14B，展现内存缩放效应。

## 摘要（原文）

> Procedural memory enables large language model (LLM) agents to internalize "how-to" knowledge, theoretically reducing redundant trial-and-error. However, existing frameworks predominantly suffer from a "passive accumulation" paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose $\textbf{ReMe}$ ($\textit{Remember Me, Refine Me}$), a comprehensive framework for experience-driven agent evolution. ReMe innovates across the memory lifecycle via three mechanisms: 1) $\textit{multi-faceted distillation}$, which extracts fine-grained experiences by recognizing success patterns, analyzing failure triggers and generating comparative insights; 2) $\textit{context-adaptive reuse}$, which tailors historical insights to new contexts via scenario-aware indexing; and 3) $\textit{utility-based refinement}$, which autonomously adds valid memories and prunes outdated ones to maintain a compact, high-quality experience pool. Extensive experiments on BFCL-V3 and AppWorld demonstrate that ReMe establishes a new state-of-the-art in agent memory system. Crucially, we observe a significant memory-scaling effect: Qwen3-8B equipped with ReMe outperforms larger, memoryless Qwen3-14B, suggesting that self-evolving memory provides a computation-efficient pathway for lifelong learning. We release our code and the $\texttt{reme.library}$ dataset to facilitate further research.

