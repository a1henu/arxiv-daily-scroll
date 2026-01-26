---
layout: default
title: BONO-Bench: A Comprehensive Test Suite for Bi-objective Numerical Optimization with Traceable Pareto Sets
---

# BONO-Bench: A Comprehensive Test Suite for Bi-objective Numerical Optimization with Traceable Pareto Sets
**arXiv**：[2601.16970v1](https://arxiv.org/abs/2601.16970) · [PDF](https://arxiv.org/pdf/2601.16970.pdf)  
**作者**：Lennart Schäpermeier, Pascal Kerschke  

**一句话要点**：提出BONO-Bench测试套件以解决双目标数值优化基准测试中问题构造的缺陷

**关键词**：双目标优化, 基准测试, 问题生成, 凸二次函数, 可追踪帕累托集, Python包

## 3 点简述
- 核心问题：现有基准测试问题存在手动构造不现实或复合问题缺乏可控性的缺陷
- 方法要点：基于凸二次函数组合生成可配置属性的双目标优化问题，保持理论可追踪性
- 实验或效果：创建20个问题类别测试套件，并发布Python包bonobench以促进可复现基准测试

## 摘要（原文）

> The evaluation of heuristic optimizers on test problems, better known as \emph{benchmarking}, is a cornerstone of research in multi-objective optimization.
>   However, most test problems used in benchmarking numerical multi-objective black-box optimizers come from one of two flawed approaches: On the one hand, problems are constructed manually, which result in problems with well-understood optimal solutions, but unrealistic properties and biases.
>   On the other hand, more realistic and complex single-objective problems are composited into multi-objective problems, but with a lack of control and understanding of problem properties.
>   This paper proposes an extensive problem generation approach for bi-objective numerical optimization problems consisting of the combination of theoretically well-understood convex-quadratic functions into unimodal and multimodal landscapes with and without global structure.
>   It supports configuration of test problem properties, such as the number of decision variables, local optima, Pareto front shape, plateaus in the objective space, or degree of conditioning, while maintaining theoretical tractability: The optimal front can be approximated to an arbitrary degree of precision regarding Pareto-compliant performance indicators such as the hypervolume or the exact R2 indicator.
>   To demonstrate the generator's capabilities, a test suite of 20 problem categories, called \emph{BONO-Bench}, is created and subsequently used as a basis of an illustrative benchmark study.
>   Finally, the general approach underlying our proposed generator, together with the associated test suite, is publicly released in the Python package \texttt{bonobench} to facilitate reproducible benchmarking.

