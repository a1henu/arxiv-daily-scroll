---
layout: default
title: LogicSkills: A Structured Benchmark for Formal Reasoning in Large Language Models
---

# LogicSkills: A Structured Benchmark for Formal Reasoning in Large Language Models
**arXiv**：[2602.06533v1](https://arxiv.org/abs/2602.06533) · [PDF](https://arxiv.org/pdf/2602.06533.pdf)  
**作者**：Brian Rabern, Philipp Mondorf, Barbara Plank  

**一句话要点**：提出LogicSkills基准以评估大语言模型在形式推理中的核心技能掌握情况

**关键词**：形式推理, 逻辑技能评估, 大语言模型基准, 一阶逻辑, 符号化, 反模型构建

## 3 点简述
- 核心问题：大语言模型在逻辑推理中真正掌握哪些核心技能尚不明确
- 方法要点：设计统一基准，隔离形式符号化、反模型构建和有效性评估三项基本技能
- 实验或效果：模型在有效性评估上表现高，但在符号化和反模型构建上表现低，依赖表面模式

## 摘要（原文）

> Large language models have demonstrated notable performance across various logical reasoning benchmarks. However, it remains unclear which core logical skills they truly master. To address this, we introduce LogicSkills, a unified benchmark designed to isolate three fundamental skills in formal reasoning: (i) $\textit{formal symbolization}\unicode{x2014}$translating premises into first-order logic; (ii) $\textit{countermodel construction}\unicode{x2014}$formulating a finite structure in which all premises are true while the conclusion is false; and (iii) $\textit{validity assessment}\unicode{x2014}$deciding whether a conclusion follows from a given set of premises. Items are drawn from the two-variable fragment of first-order logic (without identity) and are presented in both natural English and a Carroll-style language with nonce words. All examples are verified for correctness and non-triviality using the SMT solver Z3. Across leading models, performance is high on validity but substantially lower on symbolization and countermodel construction, suggesting reliance on surface-level patterns rather than genuine symbolic or rule-based reasoning.

