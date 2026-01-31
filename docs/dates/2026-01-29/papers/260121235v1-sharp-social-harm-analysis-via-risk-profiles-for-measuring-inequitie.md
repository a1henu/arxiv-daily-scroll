---
layout: default
title: SHARP: Social Harm Analysis via Risk Profiles for Measuring Inequities in Large Language Models
---

# SHARP: Social Harm Analysis via Risk Profiles for Measuring Inequities in Large Language Models
**arXiv**：[2601.21235v1](https://arxiv.org/abs/2601.21235) · [PDF](https://arxiv.org/pdf/2601.21235.pdf)  
**作者**：Alok Abhishek, Tushar Bandopadhyay, Lisa Erickson  

**一句话要点**：提出SHARP框架以评估大型语言模型的社会危害风险，关注多维度和尾部行为。

**关键词**：社会危害评估, 风险分析框架, 尾部风险度量, 多维评估, 大型语言模型, 条件风险价值

## 3 点简述
- 核心问题：现有评估基准简化社会风险为标量分数，忽略分布结构和最坏情况行为。
- 方法要点：SHARP将危害建模为多元随机变量，集成偏差、公平性、伦理和认知可靠性分解，使用CVaR95等风险敏感统计量。
- 实验或效果：应用于11个前沿LLM，发现相似平均风险模型在尾部暴露和波动性上差异显著，揭示异质失败结构。

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed in high-stakes domains, where rare but severe failures can result in irreversible harm. However, prevailing evaluation benchmarks often reduce complex social risk to mean-centered scalar scores, thereby obscuring distributional structure, cross-dimensional interactions, and worst-case behavior. This paper introduces Social Harm Analysis via Risk Profiles (SHARP), a framework for multidimensional, distribution-aware evaluation of social harm. SHARP models harm as a multivariate random variable and integrates explicit decomposition into bias, fairness, ethics, and epistemic reliability with a union-of-failures aggregation reparameterized as additive cumulative log-risk. The framework further employs risk-sensitive distributional statistics, with Conditional Value at Risk (CVaR95) as a primary metric, to characterize worst-case model behavior. Application of SHARP to eleven frontier LLMs, evaluated on a fixed corpus of n=901 socially sensitive prompts, reveals that models with similar average risk can exhibit more than twofold differences in tail exposure and volatility. Across models, dimension-wise marginal tail behavior varies systematically across harm dimensions, with bias exhibiting the strongest tail severities, epistemic and fairness risks occupying intermediate regimes, and ethical misalignment consistently lower; together, these patterns reveal heterogeneous, model-dependent failure structures that scalar benchmarks conflate. These findings indicate that responsible evaluation and governance of LLMs require moving beyond scalar averages toward multidimensional, tail-sensitive risk profiling.

