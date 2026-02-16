---
layout: default
title: Evaluating Robustness of Reasoning Models on Parameterized Logical Problems
---

# Evaluating Robustness of Reasoning Models on Parameterized Logical Problems
**arXiv**：[2602.12665v1](https://arxiv.org/abs/2602.12665) · [PDF](https://arxiv.org/pdf/2602.12665.pdf)  
**作者**：Naïm Es-sebbani, Esteban Marquer, Yakoub Salhi, Zied Bouraoui  

**一句话要点**：提出基于参数化2-SAT的诊断基准，以评估LLM推理模型的鲁棒性

**关键词**：逻辑推理评估, 2-SAT基准, 参数化公式, 鲁棒性测试, LLM推理模型, 结构干预

## 3 点简述
- 核心问题：标准SAT基准混淆表面难度与结构现象，难以评估推理模型的实际能力
- 方法要点：构建参数化2-CNF公式家族，通过可解释轴调优，隔离不同能力与失败模式
- 实验或效果：评估模型决策准确性和赋值有效性，揭示结构干预下的性能突变和脆弱性

## 摘要（原文）

> Logic provides a controlled testbed for evaluating LLM-based reasoners, yet standard SAT-style benchmarks often conflate surface difficulty (length, wording, clause order) with the structural phenomena that actually determine satisfiability. We introduce a diagnostic benchmark for 2-SAT built from parameterized families of structured 2--CNF formulas, where satisfiability is characterized by the implication graph and can be tuned along interpretable axes. Our generators isolate distinct competencies and failure modes: (i) contradiction-cycle UNSAT cores with controllable size and imbalance, (ii) SAT instances with a prescribed fraction of free variables to control solution multiplicity, (iii) planted backbones that modulate propagation, (iv) late bridge clauses that couple otherwise monotone regions to probe sensitivity to ordering and revision, and (v) symmetry/duplication variants that test abstraction under renaming and redundant structure. We evaluate LLM-based reasoners on decision accuracy and assignment validity, and quantify robustness under semantics-preserving perturbations such as clause reordering, filler clauses, and variable renaming. Across models, we observe sharp performance transitions under targeted structural interventions even when surface statistics are held fixed, revealing brittleness regimes that are invisible to aggregate SAT accuracy.

