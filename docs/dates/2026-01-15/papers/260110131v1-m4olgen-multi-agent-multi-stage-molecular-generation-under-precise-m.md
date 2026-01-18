---
layout: default
title: M^4olGen: Multi-Agent, Multi-Stage Molecular Generation under Precise Multi-Property Constraints
---

# M^4olGen: Multi-Agent, Multi-Stage Molecular Generation under Precise Multi-Property Constraints
**arXiv**：[2601.10131v1](https://arxiv.org/abs/2601.10131) · [PDF](https://arxiv.org/pdf/2601.10131.pdf)  
**作者**：Yizhan Li, Florence Cloutier, Sifan Wu, Ali Parviz, Boris Knyazev, Yan Zhang, Glen Berseth, Bang Liu  

**一句话要点**：提出M^4olGen框架，通过多智能体多阶段方法解决分子生成中精确多属性约束的挑战。

**关键词**：分子生成, 多属性约束, 多智能体推理, 强化学习优化, 片段级编辑, 检索增强

## 3 点简述
- 核心问题：分子生成需满足精确数值多属性约束，现有大语言模型难以实现精确控制和数值推理。
- 方法要点：采用两阶段框架，包括原型生成和基于强化学习的细粒度优化，利用片段级编辑和检索增强。
- 实验或效果：在两组属性约束下，有效性及多属性目标精确满足度优于强基线模型和基于图的算法。

## 摘要（原文）

> Generating molecules that satisfy precise numeric constraints over multiple physicochemical properties is critical and challenging. Although large language models (LLMs) are expressive, they struggle with precise multi-objective control and numeric reasoning without external structure and feedback. We introduce \textbf{M olGen}, a fragment-level, retrieval-augmented, two-stage framework for molecule generation under multi-property constraints. Stage I : Prototype generation: a multi-agent reasoner performs retrieval-anchored, fragment-level edits to produce a candidate near the feasible region. Stage II : RL-based fine-grained optimization: a fragment-level optimizer trained with Group Relative Policy Optimization (GRPO) applies one- or multi-hop refinements to explicitly minimize the property errors toward our target while regulating edit complexity and deviation from the prototype. A large, automatically curated dataset with reasoning chains of fragment edits and measured property deltas underpins both stages, enabling deterministic, reproducible supervision and controllable multi-hop reasoning. Unlike prior work, our framework better reasons about molecules by leveraging fragments and supports controllable refinement toward numeric targets. Experiments on generation under two sets of property constraints (QED, LogP, Molecular Weight and HOMO, LUMO) show consistent gains in validity and precise satisfaction of multi-property targets, outperforming strong LLMs and graph-based algorithms.

