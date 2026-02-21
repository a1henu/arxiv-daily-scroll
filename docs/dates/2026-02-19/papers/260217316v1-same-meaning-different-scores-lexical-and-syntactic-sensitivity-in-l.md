---
layout: default
title: Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation
---

# Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation
**arXiv**：[2602.17316v1](https://arxiv.org/abs/2602.17316) · [PDF](https://arxiv.org/pdf/2602.17316.pdf)  
**作者**：Bogdan Kostić, Conor Fallon, Julian Risch, Alexander Löser  

**一句话要点**：揭示大语言模型评估对词汇和句法扰动的敏感性，质疑基准测试可靠性

**关键词**：大语言模型评估, 基准测试鲁棒性, 词汇扰动, 句法扰动, 模型比较

## 3 点简述
- 核心问题：大语言模型评估基准对输入提示的浅层变化敏感，可靠性受质疑
- 方法要点：使用词汇同义词替换和句法依赖解析生成语义等价扰动
- 实验效果：词汇扰动普遍导致性能显著下降，句法扰动效果更异质，模型鲁棒性与规模无关

## 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) has established standardized evaluation benchmarks as the primary instrument for model comparison. Yet, their reliability is increasingly questioned due to sensitivity to shallow variations in input prompts. This paper examines how controlled, truth-conditionally equivalent lexical and syntactic perturbations affect the absolute performance and relative ranking of 23 contemporary LLMs across three benchmarks: MMLU, SQuAD, and AMEGA. We employ two linguistically principled pipelines to generate meaning-preserving variations: one performing synonym substitution for lexical changes, and another using dependency parsing to determine applicable syntactic transformations. Results show that lexical perturbations consistently induce substantial, statistically significant performance degradation across nearly all models and tasks, while syntactic perturbations have more heterogeneous effects, occasionally improving results. Both perturbation types destabilize model leaderboards on complex tasks. Furthermore, model robustness did not consistently scale with model size, revealing strong task dependence. Overall, the findings suggest that LLMs rely more on surface-level lexical patterns than on abstract linguistic competence, underscoring the need for robustness testing as a standard component of LLM evaluation.

