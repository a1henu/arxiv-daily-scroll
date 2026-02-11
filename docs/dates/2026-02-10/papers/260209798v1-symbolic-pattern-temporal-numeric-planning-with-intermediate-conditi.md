---
layout: default
title: Symbolic Pattern Temporal Numeric Planning with Intermediate Conditions and Effects
---

# Symbolic Pattern Temporal Numeric Planning with Intermediate Conditions and Effects
**arXiv**：[2602.09798v1](https://arxiv.org/abs/2602.09798) · [PDF](https://arxiv.org/pdf/2602.09798.pdf)  
**作者**：Matteo Cardellini, Enrico Giunchiglia  

**一句话要点**：扩展符号模式规划至含中间条件与效果的时序规划，提升求解性能

**关键词**：符号模式规划, 时序规划, 中间条件与效果, SMT编码, 动作重叠, 规划器性能

## 3 点简述
- 核心问题：时序规划中动作可重叠且条件/效果可在执行期间任意时间点检查/应用，传统方法效率受限
- 方法要点：基于符号模式规划，通过模式扩展编码SMT公式，支持中间条件与效果片段
- 实验效果：在多数无ICE时序域中优于现有规划器，在有ICE域中与SoTA搜索规划器相当或更优

## 摘要（原文）

> Recently, a Symbolic Pattern Planning (SPP) approach was proposed for numeric planning where a pattern (i.e., a finite sequence of actions) suggests a causal order between actions. The pattern is then encoded in a SMT formula whose models correspond to valid plans. If the suggestion by the pattern is inaccurate and no valid plan can be found, the pattern is extended until it contains the causal order of actions in a valid plan, making the approach complete. In this paper, we extend the SPP approach to the temporal planning with Intermediate Conditions and Effects (ICEs) fragment, where $(i)$ actions are durative (and thus can overlap over time) and have conditions/effects which can be checked/applied at any time during an action's execution, and $(ii)$ one can specify plan's conditions/effects that must be checked/applied at specific times during the plan execution. Experimental results show that our SPP planner Patty $(i)$ outperforms all other planners in the literature in the majority of temporal domains without ICEs, $(ii)$ obtains comparable results with the SoTA search planner for ICS in literature domains with ICEs, and $(iii)$ outperforms the same planner in a novel domain based on a real-world application.

