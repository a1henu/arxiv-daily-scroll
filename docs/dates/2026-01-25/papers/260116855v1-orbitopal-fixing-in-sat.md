---
layout: default
title: Orbitopal Fixing in SAT
---

# Orbitopal Fixing in SAT
**arXiv**：[2601.16855v1](https://arxiv.org/abs/2601.16855) · [PDF](https://arxiv.org/pdf/2601.16855.pdf)  
**作者**：Markus Anders, Cayden Codel, Marijn J. H. Heule  

**一句话要点**：提出基于轨道面固定的静态对称性处理方法，以提升SAT求解器在对称性丰富基准上的性能。

**关键词**：布尔可满足性求解, 对称性处理, 轨道面固定, 证明生成, 静态对称性打破, SAT求解器优化

## 3 点简述
- SAT求解器易受对称性影响，导致重复探索对称搜索区域，影响效率。
- 采用轨道面固定技术，仅添加单位子句，减少对求解器启发式策略的干扰。
- 在satsuma工具中实现，对称性丰富基准上性能提升显著，其他基准无显著退化。

## 摘要（原文）

> Despite their sophisticated heuristics, boolean satisfiability (SAT) solvers are still vulnerable to symmetry, causing them to visit search regions that are symmetric to ones already explored. While symmetry handling is routine in other solving paradigms, integrating it into state-of-the-art proof-producing SAT solvers is difficult: added reasoning must be fast, non-interfering with solver heuristics, and compatible with formal proof logging. To address these issues, we present a practical static symmetry breaking approach based on orbitopal fixing, a technique adapted from mixed-integer programming. Our approach adds only unit clauses, which minimizes downstream slowdowns, and it emits succinct proof certificates in the substitution redundancy proof system. Implemented in the satsuma tool, our methods deliver consistent speedups on symmetry-rich benchmarks with negligible regressions elsewhere.

