---
layout: default
title: CompilerKV: Risk-Adaptive KV Compression via Offline Experience Compilation
---

# CompilerKV: Risk-Adaptive KV Compression via Offline Experience Compilation
**arXiv**：[2602.08686v1](https://arxiv.org/abs/2602.08686) · [PDF](https://arxiv.org/pdf/2602.08686.pdf)  
**作者**：Ning Yang, Chengzhi Wang, Yibo Liu, Baoliang Tian, Haijun Zhang  

**一句话要点**：提出CompilerKV框架，通过离线经验编译实现风险自适应和头感知的KV压缩，以解决长上下文LLM中KV缓存内存线性增长问题。

**关键词**：KV缓存压缩, 长上下文LLM, 风险自适应, 注意力头异质性, 离线经验编译, 内存优化

## 3 点简述
- 核心问题：现有KV压缩方法在紧内存预算下忽略提示依赖的压缩风险变化和注意力头功能异质性，导致令牌选择不稳定和尾部失败。
- 方法要点：集成头异质性表和风险自适应阈值门控，利用离线上下文老虎机学习头特定可靠性权重，并基于注意力熵和局部困惑度建模风险。
- 实验或效果：在LongBench上，512令牌预算下优于SOTA方法，恢复FullKV性能的97.7%，比最强竞争对手提升高达5.2分。

## 摘要（原文）

> Large Language Models (LLMs) in long-context scenarios are severely constrained by the linear growth of Key-Value (KV) cache memory. Existing KV compression methods rely either on static thresholds and attention-only heuristics or on coarse memory budget allocation. Under tight memory budgets, these methods overlook two key factors: prompt-dependent variation in compression risk and functional heterogeneity across attention heads, which destabilize token selection and lead to tail failures. To address these challenges, we propose CompilerKV, a risk-adaptive and head-aware compression framework that compiles offline experience into reusable decision tables for prefill-only deployment. CompilerKV integrates two key synergistic components: (i) a Head Heterogeneity Table, learned via offline contextual bandits, which assigns head-specific reliability weights to govern functional differences across attention heads explicitly; and (ii) a Risk-Adaptive Threshold Gating mechanism that jointly models attention entropy and local perplexity, transforming prompt-level risk into deployable retention thresholds. Experiments on LongBench show CompilerKV dominates SOTA methods under a 512-token budget, recovering 97.7\% of FullKV performance while achieving up to +5.2 points gain over the strongest competitor.

