---
layout: default
title: Debate is efficient with your time
---

# Debate is efficient with your time
**arXiv**：[2602.08630v1](https://arxiv.org/abs/2602.08630) · [PDF](https://arxiv.org/pdf/2602.08630.pdf)  
**作者**：Jonah Brown-Cohen, Geoffrey Irving, Simon C. Marshall, Ilan Newman, Georgios Piliouras, Mario Szegedy  

**一句话要点**：提出辩论查询复杂度以分析AI安全辩论中人类监督的查询效率

**关键词**：AI安全辩论, 查询复杂度, PSPACE/poly, 电路复杂度, 人类监督, 对数查询

## 3 点简述
- 核心问题：分析AI安全辩论中人类法官验证复杂任务所需的查询成本
- 方法要点：引入辩论查询复杂度，刻画PSPACE/poly类问题仅需对数查询
- 实验或效果：证明对数查询足够高效，并连接电路复杂度以提供新下界

## 摘要（原文）

> AI safety via debate uses two competing models to help a human judge verify complex computational tasks. Previous work has established what problems debate can solve in principle, but has not analysed the practical cost of human oversight: how many queries must the judge make to the debate transcript? We introduce Debate Query Complexity}(DQC), the minimum number of bits a verifier must inspect to correctly decide a debate.
>   Surprisingly, we find that PSPACE/poly (the class of problems which debate can efficiently decide) is precisely the class of functions decidable with O(log n) queries. This characterisation shows that debate is remarkably query-efficient: even for highly complex problems, logarithmic oversight suffices. We also establish that functions depending on all their input bits require Omega(log n) queries, and that any function computable by a circuit of size s satisfies DQC(f) <= log(s) + 3. Interestingly, this last result implies that proving DQC lower bounds of log(n) + 6 for languages in P would yield new circuit lower bounds, connecting debate query complexity to central questions in circuit complexity.

