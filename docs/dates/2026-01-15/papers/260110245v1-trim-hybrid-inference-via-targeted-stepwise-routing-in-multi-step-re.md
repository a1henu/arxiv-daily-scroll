---
layout: default
title: TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks
---

# TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks
**arXiv**：[2601.10245v1](https://arxiv.org/abs/2601.10245) · [PDF](https://arxiv.org/pdf/2601.10245.pdf)  
**作者**：Vansh Kapoor, Aman Gupta, Hao Chen, Anurag Beniwal, Jing Huang, Aviral Kumar  

**一句话要点**：提出TRIM通过目标步级路由提升多步推理任务的效率与准确性

**关键词**：多步推理, 模型路由, 成本效率, 过程奖励模型, 步级不确定性, 数学问题求解

## 3 点简述
- 多步推理任务易因单步错误导致级联失败，现有方法将整个查询路由至单一模型
- TRIM仅将关键步骤路由至大模型，利用过程奖励模型识别错误步骤并基于不确定性和预算决策
- 在MATH-500和AIME基准上实现高达5倍和6倍的成本效率提升，匹配强模型性能时减少80%昂贵令牌

## 摘要（原文）

> Multi-step reasoning tasks like mathematical problem solving are vulnerable to cascading failures, where a single incorrect step leads to complete solution breakdown. Current LLM routing methods assign entire queries to one model, treating all reasoning steps as equal. We propose TRIM (Targeted routing in multi-step reasoning tasks), which routes only critical steps$\unicode{x2013}$those likely to derail the solution$\unicode{x2013}$to larger models while letting smaller models handle routine continuations. Our key insight is that targeted step-level interventions can fundamentally transform inference efficiency by confining expensive calls to precisely those steps where stronger models prevent cascading errors. TRIM operates at the step-level: it uses process reward models to identify erroneous steps and makes routing decisions based on step-level uncertainty and budget constraints. We develop several routing strategies within TRIM, ranging from a simple threshold-based policy to more expressive policies that reason about long-horizon accuracy-cost trade-offs and uncertainty in step-level correctness estimates. On MATH-500, even the simplest thresholding strategy surpasses prior routing methods with 5x higher cost efficiency, while more advanced policies match the strong, expensive model's performance using 80% fewer expensive model tokens. On harder benchmarks such as AIME, TRIM achieves up to 6x higher cost efficiency. All methods generalize effectively across math reasoning tasks, demonstrating that step-level difficulty represents fundamental characteristics of reasoning.

