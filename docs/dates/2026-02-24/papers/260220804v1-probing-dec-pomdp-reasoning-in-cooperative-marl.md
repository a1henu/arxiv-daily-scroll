---
layout: default
title: Probing Dec-POMDP Reasoning in Cooperative MARL
---

# Probing Dec-POMDP Reasoning in Cooperative MARL
**arXiv**：[2602.20804v1](https://arxiv.org/abs/2602.20804) · [PDF](https://arxiv.org/pdf/2602.20804.pdf)  
**作者**：Kale-ab Tessera, Leonard Hinckeldey, Riccardo Zamboni, David Abel, Amos Storkey  

**一句话要点**：提出诊断套件以评估合作多智能体强化学习基准中的Dec-POMDP推理需求

**关键词**：合作多智能体强化学习, Dec-POMDP推理, 基准评估, 信息论探针, 行为复杂性分析, 环境设计

## 3 点简述
- 核心问题：合作MARL基准是否真正需要Dec-POMDP推理，还是允许简单策略成功
- 方法要点：结合统计性能比较和信息论探针，审计基线策略在37个场景中的行为复杂性
- 实验或效果：发现多数场景无需真正Dec-POMDP推理，反应策略可匹配记忆策略性能

## 摘要（原文）

> Cooperative multi-agent reinforcement learning (MARL) is typically framed as a decentralised partially observable Markov decision process (Dec-POMDP), a setting whose hardness stems from two key challenges: partial observability and decentralised coordination. Genuinely solving such tasks requires Dec-POMDP reasoning, where agents use history to infer hidden states and coordinate based on local information. Yet it remains unclear whether popular benchmarks actually demand this reasoning or permit success via simpler strategies. We introduce a diagnostic suite combining statistically grounded performance comparisons and information-theoretic probes to audit the behavioural complexity of baseline policies (IPPO and MAPPO) across 37 scenarios spanning MPE, SMAX, Overcooked, Hanabi, and MaBrax. Our diagnostics reveal that success on these benchmarks rarely requires genuine Dec-POMDP reasoning. Reactive policies match the performance of memory-based agents in over half the scenarios, and emergent coordination frequently relies on brittle, synchronous action coupling rather than robust temporal influence. These findings suggest that some widely used benchmarks may not adequately test core Dec-POMDP assumptions under current training paradigms, potentially leading to over-optimistic assessments of progress. We release our diagnostic tooling to support more rigorous environment design and evaluation in cooperative MARL.

