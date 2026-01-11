---
layout: default
title: LLM-Guided Quantified SMT Solving over Uninterpreted Functions
---

# LLM-Guided Quantified SMT Solving over Uninterpreted Functions
**arXiv**：[2601.04675v1](https://arxiv.org/abs/2601.04675) · [PDF](https://arxiv.org/pdf/2601.04675.pdf)  
**作者**：Kunhang Lv, Yuhang Dong, Rui Han, Fuqi Jia, Feifei Ma, Jian Zhang  

**一句话要点**：提出AquaForte框架，利用大语言模型为含未解释函数的量化SMT求解提供语义指导

**关键词**：SMT求解, 量化公式, 未解释函数, 大语言模型, 语义指导, 自适应实例化

## 3 点简述
- 核心问题：含未解释函数的量化公式在非线性实数算术中导致SMT求解搜索空间大、复杂度高
- 方法要点：通过约束分离预处理，使用结构化提示从LLM生成函数定义候选，结合自适应实例化集成传统算法
- 实验或效果：在SMT-COMP基准测试中，AquaForte解决了Z3和CVC5超时的多个实例，对可满足公式尤其有效

## 摘要（原文）

> Quantified formulas with Uninterpreted Functions (UFs) over non-linear real arithmetic pose fundamental challenges for Satisfiability Modulo Theories (SMT) solving. Traditional quantifier instantiation methods struggle because they lack semantic understanding of UF constraints, forcing them to search through unbounded solution spaces with limited guidance. We present AquaForte, a framework that leverages Large Language Models to provide semantic guidance for UF instantiation by generating instantiated candidates for function definitions that satisfy the constraints, thereby significantly reducing the search space and complexity for solvers. Our approach preprocesses formulas through constraint separation, uses structured prompts to extract mathematical reasoning from LLMs, and integrates the results with traditional SMT algorithms through adaptive instantiation. AquaForte maintains soundness through systematic validation: LLM-guided instantiations yielding SAT solve the original problem, while UNSAT results generate exclusion clauses for iterative refinement. Completeness is preserved by fallback to traditional solvers augmented with learned constraints. Experimental evaluation on SMT-COMP benchmarks demonstrates that AquaForte solves numerous instances where state-of-the-art solvers like Z3 and CVC5 timeout, with particular effectiveness on satisfiable formulas. Our work shows that LLMs can provide valuable mathematical intuition for symbolic reasoning, establishing a new paradigm for SMT constraint solving.

