---
layout: default
title: Programming over Thinking: Efficient and Robust Multi-Constraint Planning
---

# Programming over Thinking: Efficient and Robust Multi-Constraint Planning
**arXiv**：[2601.09097v1](https://arxiv.org/abs/2601.09097) · [PDF](https://arxiv.org/pdf/2601.09097.pdf)  
**作者**：Derrick Goh Xin Deik, Quanyu Long, Zhengyuan Liu, Nancy F. Chen, Wenya Wang  

**一句话要点**：提出SCOPE框架以解决多约束规划中LLM推理不一致与代码生成不灵活的问题

**关键词**：多约束规划, 大型语言模型, 代码执行框架, 推理与执行分离, 求解器函数, 成本效率

## 3 点简述
- 核心问题：现有LLM方法在多约束规划中面临推理不一致、成本高或代码生成不灵活的挑战
- 方法要点：SCOPE分离查询特定推理与通用代码执行，生成一致、确定且可重用的求解器函数
- 实验或效果：在TravelPlanner上达到93.1%成功率，成本降低1.4倍，时间减少约4.67倍

## 摘要（原文）

> Multi-constraint planning involves identifying, evaluating, and refining candidate plans while satisfying multiple, potentially conflicting constraints. Existing large language model (LLM) approaches face fundamental limitations in this domain. Pure reasoning paradigms, which rely on long natural language chains, are prone to inconsistency, error accumulation, and prohibitive cost as constraints compound. Conversely, LLMs combined with coding- or solver-based strategies lack flexibility: they often generate problem-specific code from scratch or depend on fixed solvers, failing to capture generalizable logic across diverse problems. To address these challenges, we introduce the Scalable COde Planning Engine (SCOPE), a framework that disentangles query-specific reasoning from generic code execution. By separating reasoning from execution, SCOPE produces solver functions that are consistent, deterministic, and reusable across queries while requiring only minimal changes to input parameters. SCOPE achieves state-of-the-art performance while lowering cost and latency. For example, with GPT-4o, it reaches 93.1% success on TravelPlanner, a 61.6% gain over the best baseline (CoT) while cutting inference cost by 1.4x and time by ~4.67x. Code is available at https://github.com/DerrickGXD/SCOPE.

