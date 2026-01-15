---
layout: default
title: Multi-Teacher Ensemble Distillation: A Mathematical Framework for Probability-Domain Knowledge Aggregation
---

# Multi-Teacher Ensemble Distillation: A Mathematical Framework for Probability-Domain Knowledge Aggregation
**arXiv**：[2601.09165v1](https://arxiv.org/abs/2601.09165) · [PDF](https://arxiv.org/pdf/2601.09165.pdf)  
**作者**：Aaron R. Flouro, Shawn P. Chadwick  

**一句话要点**：提出多教师集成蒸馏的数学框架，基于概率域知识聚合，提供理论保证与实现灵活性。

**关键词**：知识蒸馏, 多教师集成, 概率域框架, 操作符理论, 方差减少, 理论保证

## 3 点简述
- 核心问题：多教师知识蒸馏中缺乏统一理论框架，需定义有效知识聚合操作符。
- 方法要点：基于Sparse-KD扩展，定义五个核心公理，证明操作符存在性与非唯一性。
- 实验或效果：提供方差减少、偏差降低、Jensen型边界等理论保证，支持多种实现策略。

## 摘要（原文）

> Building on the probability-domain distillation framework of Sparse-KD, we develop an axiomatic, operator-theoretic framework for multi-teacher ensemble knowledge distillation. Rather than prescribing a specific aggregation formula, we define five core axioms governing valid knowledge aggregation operators, encompassing convexity, positivity, continuity, weight monotonicity, and temperature coherence. We prove the existence and non-uniqueness of operator families satisfying these axioms, establishing that multiple distinct aggregation mechanisms conform to the same foundational principles.
>   Within this framework, we establish operator-agnostic guarantees showing that multi-teacher aggregation reduces both stochastic variance and systematic supervisory bias under heterogeneous teachers, while providing Jensen-type bounds, log-loss guarantees, and safety attenuation properties. For aggregation operators linear in teacher weights, we further establish classical ensemble variance-reduction results under standard independence assumptions, with extensions to correlated-error regimes. The framework provides theoretical grounding for multi-teacher distillation from diverse frontier models while admitting multiple valid implementation strategies.

