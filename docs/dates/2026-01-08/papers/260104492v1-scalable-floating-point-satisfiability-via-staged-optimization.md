---
layout: default
title: Scalable Floating-Point Satisfiability via Staged Optimization
---

# Scalable Floating-Point Satisfiability via Staged Optimization
**arXiv**：[2601.04492v1](https://arxiv.org/abs/2601.04492) · [PDF](https://arxiv.org/pdf/2601.04492.pdf)  
**作者**：Yuanzhuo Zhang, Zhoulai Fu, Binoy Ravindran  

**一句话要点**：提出StageSAT方法，通过分阶段优化解决浮点数可满足性问题，提升可扩展性与准确性。

**关键词**：浮点数可满足性, 分阶段优化, SMT求解, 数值优化, 正交投影, 可扩展性

## 3 点简述
- 核心问题：浮点数可满足性求解面临可扩展性差和准确性不足的挑战，传统方法依赖位级推理或数值优化，效率受限。
- 方法要点：StageSAT将浮点数公式重构为三个精度递增的优化阶段，包括快速下降、位级优化和晶格细化，利用正交投影避免搜索停滞，并内置正确性保证。
- 实验或效果：在SMT-COMP'25等基准测试中，StageSAT在相同时间预算下解决更多公式，实现99.4%召回率和0%误报，速度比传统方法快5-10倍。

## 摘要（原文）

> This work introduces StageSAT, a new approach to solving floating-point satisfiability that bridges SMT solving with numerical optimization. StageSAT reframes a floating-point formula as a series of optimization problems in three stages of increasing precision. It begins with a fast, projection-aided descent objective to guide the search toward a feasible region, proceeding to bit-level accuracy with ULP$^2$ optimization and a final $n$-ULP lattice refinement.
>   By construction, the final stage uses a representing function that is zero if and only if a candidate satisfies all constraints. Thus, when optimization drives the objective to zero, the resulting assignment is a valid solution, providing a built-in guarantee of soundness.
>   To improve search, StageSAT introduces a partial monotone descent property on linear constraints via orthogonal projection, preventing the optimizer from stalling on flat or misleading landscapes. Critically, this solver requires no heavy bit-level reasoning or specialized abstractions; it treats complex arithmetic as a black-box, using runtime evaluations to navigate the input space.
>   We implement StageSAT and evaluate it on extensive benchmarks, including SMT-COMP'25 suites and difficult cases from prior work. StageSAT proved more scalable and accurate than state-of-the-art optimization-based alternatives. It solved strictly more formulas than any competing solver under the same time budget, finding most satisfiable instances without producing spurious models. This amounts to 99.4% recall on satisfiable cases with 0% false SAT, exceeding the reliability of prior optimization-based solvers. StageSAT also delivered significant speedups (often 5--10$\times$) over traditional bit-precise SMT and numeric solvers. These results demonstrate that staged optimization significantly improves performance and correctness of floating-point satisfiability solving.

