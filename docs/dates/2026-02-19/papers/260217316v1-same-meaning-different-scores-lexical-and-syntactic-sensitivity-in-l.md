---
layout: default
title: Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation
---

# Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation
**arXiv**：[2602.17316v1](https://arxiv.org/abs/2602.17316) · [PDF](https://arxiv.org/pdf/2602.17316.pdf)  
**作者**：Bogdan Kostić, Conor Fallon, Julian Risch, Alexander Löser  

**一句话要点**：研究词汇和句法扰动对LLM评估的影响，揭示模型对表面模式的依赖。

**关键词**：大语言模型评估, 词汇扰动, 句法扰动, 鲁棒性测试, 基准可靠性

## 3 点简述
- 核心问题：LLM评估基准对输入提示的浅层变化敏感，可靠性受质疑。
- 方法要点：使用同义词替换和句法转换生成意义保留的扰动，测试23个模型。
- 实验或效果：词汇扰动导致性能显著下降，句法扰动效果异质，模型鲁棒性不随规模一致提升。

## 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) has established standardized evaluation benchmarks as the primary instrument for model comparison. Yet, their reliability is increasingly questioned due to sensitivity to shallow variations in input prompts. This paper examines how controlled, truth-conditionally equivalent lexical and syntactic perturbations affect the absolute performance and relative ranking of 23 contemporary LLMs across three benchmarks: MMLU, SQuAD, and AMEGA. We employ two linguistically principled pipelines to generate meaning-preserving variations: one performing synonym substitution for lexical changes, and another using dependency parsing to determine applicable syntactic transformations. Results show that lexical perturbations consistently induce substantial, statistically significant performance degradation across nearly all models and tasks, while syntactic perturbations have more heterogeneous effects, occasionally improving results. Both perturbation types destabilize model leaderboards on complex tasks. Furthermore, model robustness did not consistently scale with model size, revealing strong task dependence. Overall, the findings suggest that LLMs rely more on surface-level lexical patterns than on abstract linguistic competence, underscoring the need for robustness testing as a standard component of LLM evaluation.

