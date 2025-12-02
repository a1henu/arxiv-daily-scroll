---
layout: default
title: Provably Safe Model Updates
---

# Provably Safe Model Updates
**arXiv**：[2512.01899v1](https://arxiv.org/abs/2512.01899) · [PDF](https://arxiv.org/pdf/2512.01899.pdf)  
**作者**：Leo Elmecker-Plakolm, Pierre Fasterling, Philip Sosnin, Calvin Tsay, Matthew Wicker  

**一句话要点**：提出可证明安全模型更新框架，以解决动态环境中模型更新可能违反性能规范的问题。

**关键词**：模型更新安全, 局部不变域, 形式化认证, 持续学习, 基础模型微调, 参数化抽象域

## 3 点简述
- 核心问题：模型更新可能导致灾难性遗忘或对齐漂移，现有启发式方法无法提供形式化安全保证。
- 方法要点：将问题形式化为计算最大局部不变域，通过参数化抽象域实现高效认证，支持投影更新到安全域。
- 实验或效果：在持续学习和基础模型微调基准上，匹配或超越启发式基线，同时提供形式化安全保证。

## 摘要（原文）

> Safety-critical environments are inherently dynamic. Distribution shifts, emerging vulnerabilities, and evolving requirements demand continuous updates to machine learning models. Yet even benign parameter updates can have unintended consequences, such as catastrophic forgetting in classical models or alignment drift in foundation models. Existing heuristic approaches (e.g., regularization, parameter isolation) can mitigate these effects but cannot certify that updated models continue to satisfy required performance specifications. We address this problem by introducing a framework for provably safe model updates. Our approach first formalizes the problem as computing the largest locally invariant domain (LID): a connected region in parameter space where all points are certified to satisfy a given specification. While exact maximal LID computation is intractable, we show that relaxing the problem to parameterized abstract domains (orthotopes, zonotopes) yields a tractable primal-dual formulation. This enables efficient certification of updates - independent of the data or algorithm used - by projecting them onto the safe domain. Our formulation further allows computation of multiple approximately optimal LIDs, incorporation of regularization-inspired biases, and use of lookahead data buffers. Across continual learning and foundation model fine-tuning benchmarks, our method matches or exceeds heuristic baselines for avoiding forgetting while providing formal safety guarantees.

