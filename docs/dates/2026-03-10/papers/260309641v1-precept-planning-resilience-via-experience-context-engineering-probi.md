---
layout: default
title: PRECEPT: Planning Resilience via Experience, Context Engineering & Probing Trajectories A Unified Framework for Test-Time Adaptation with Compositional Rule Learning and Pareto-Guided Prompt Evolution
---

# PRECEPT: Planning Resilience via Experience, Context Engineering & Probing Trajectories A Unified Framework for Test-Time Adaptation with Compositional Rule Learning and Pareto-Guided Prompt Evolution
**arXiv**：[2603.09641v1](https://arxiv.org/abs/2603.09641) · [PDF](https://arxiv.org/pdf/2603.09641.pdf)  
**作者**：Arash Shahmansoori  

**一句话要点**：提出PRECEPT框架，通过结构化规则检索和冲突感知内存解决LLM代理在测试时适应中的知识检索与组合问题。

**关键词**：测试时适应, 规则检索, 冲突感知内存, 提示进化, LLM代理, 组合学习

## 3 点简述
- 核心问题：LLM代理在条件增多时知识检索性能下降，规则组合不可靠，缺乏检测陈旧或对抗性知识的机制。
- 方法要点：采用确定性精确匹配规则检索、冲突感知内存和Pareto引导的提示进化循环。
- 实验或效果：在首次尝试、组合泛化、连续学习和漂移恢复等方面显著优于基线，统计显著。

## 摘要（原文）

> LLM agents that store knowledge as natural language suffer steep retrieval degradation as condition count grows, often struggle to compose learned rules reliably, and typically lack explicit mechanisms to detect stale or adversarial knowledge. We introduce PRECEPT, a unified framework for test-time adaptation with three tightly coupled components: (1) deterministic exact-match rule retrieval over structured condition keys, (2) conflict-aware memory with Bayesian source reliability and threshold-based rule invalidation, and (3) COMPASS, a Pareto-guided prompt-evolution outer loop. Exact retrieval eliminates partial-match interpretation errors on the deterministic path (0% by construction, vs 94.4% under Theorem~B.6's independence model at N=10) and supports compositional stacking through a semantic tier hierarchy; conflict-aware memory resolves static--dynamic disagreements and supports drift adaptation; COMPASS evaluates prompts through the same end-to-end execution pipeline.
>   Results (9--10 seeds): PRECEPT achieves a +41.1pp first-try advantage over Full Reflexion (d>1.9), +33.3pp compositional generalization (d=1.55), 100% $P_1$ on 2-way logistics compositions (d=2.64), +40--55pp continuous learning gains, strong eventual robustness under adversarial static knowledge (100% logistics with adversarial SK active; partial recovery on integration), +55.0pp drift recovery (d=0.95, p=0.031), and 61% fewer steps. Core comparisons are statistically significant, often at p<0.001.

