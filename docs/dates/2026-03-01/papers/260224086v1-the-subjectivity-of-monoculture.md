---
layout: default
title: The Subjectivity of Monoculture
---

# The Subjectivity of Monoculture
**arXiv**：[2602.24086v1](https://arxiv.org/abs/2602.24086) · [PDF](https://arxiv.org/pdf/2602.24086.pdf)  
**作者**：Nathanael Jo, Nikhil Garg, Manish Raghavan  

**一句话要点**：提出主观性框架以评估机器学习模型的单文化现象

**关键词**：单文化评估, 主观性分析, 基线零模型, 模型一致性, 上下文依赖推断

## 3 点简述
- 核心问题：模型单文化评估的主观性，依赖基线零模型和上下文选择
- 方法要点：理论分析不同零模型和模型/项目群体对一致性推断的影响
- 实验或效果：在大规模基准上验证，显示不同零模型导致推断显著差异

## 摘要（原文）

> Machine learning models -- including large language models (LLMs) -- are often said to exhibit monoculture, where outputs agree strikingly often. But what does it actually mean for models to agree too much? We argue that this question is inherently subjective, relying on two key decisions.
>   First, the analyst must specify a baseline null model for what "independence" should look like. This choice is inherently subjective, and as we show, different null models result in dramatically different inferences about excess agreement. Second, we show that inferences depend on the population of models and items under consideration. Models that seem highly correlated in one context may appear independent when evaluated on a different set of questions, or against a different set of peers. Experiments on two large-scale benchmarks validate our theoretical findings. For example, we find drastically different inferences when using a null model with item difficulty compared to previous works that do not. Together, our results reframe monoculture evaluation not as an absolute property of model behavior, but as a context-dependent inference problem.

