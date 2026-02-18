---
layout: default
title: On inferring cumulative constraints
---

# On inferring cumulative constraints
**arXiv**：[2602.15635v1](https://arxiv.org/abs/2602.15635) · [PDF](https://arxiv.org/pdf/2602.15635.pdf)  
**作者**：Konstantin Sidorov  

**一句话要点**：提出预处理方法以推断累积约束，提升调度问题求解性能。

**关键词**：累积约束, 调度问题, 约束编程, 预处理方法, RCPSP

## 3 点简述
- 核心问题：累积约束传播忽略多资源交互，导致某些基准测试性能下降。
- 方法要点：通过发现任务覆盖集、提升不等式强度并注入约束，捕获交互。
- 实验效果：在RCPSP测试中改善搜索性能，发现新下界和最优解。

## 摘要（原文）

> Cumulative constraints are central in scheduling with constraint programming, yet propagation is typically performed per constraint, missing multi-resource interactions and causing severe slowdowns on some benchmarks. I present a preprocessing method for inferring additional cumulative constraints that capture such interactions without search-time probing. This approach interprets cumulative constraints as linear inequalities over occupancy vectors and generates valid inequalities by (i) discovering covers, the sets of tasks that cannot run in parallel, (ii) strengthening the cover inequalities for the discovered sets with lifting, and (iii) injecting the resulting constraints back into the scheduling problem instance. Experiments on standard RCPSP and RCPSP/max test suites show that these inferred constraints improve search performance and tighten objective bounds on favorable instances, while incurring little degradation on unfavorable ones. Additionally, these experiments discover 25 new lower bounds and five new best solutions; eight of the lower bounds are obtained directly from the inferred constraints.

