---
layout: default
title: Winner's Curse Drives False Promises in Data-Driven Decisions: A Case Study in Refugee Matching
---

# Winner's Curse Drives False Promises in Data-Driven Decisions: A Case Study in Refugee Matching
**arXiv**：[2602.08892v1](https://arxiv.org/abs/2602.08892) · [PDF](https://arxiv.org/pdf/2602.08892.pdf)  
**作者**：Hamsa Bastani, Osbert Bastani, Bryce McLaughlin  

**一句话要点**：揭示赢家诅咒导致数据驱动决策中虚假承诺，以难民匹配为例

**关键词**：数据驱动决策, 赢家诅咒, 模型评估, 难民匹配, 政策评估, 虚假承诺

## 3 点简述
- 核心问题：模型评估方法因赢家诅咒产生过度乐观效益估计，影响政策评估准确性
- 方法要点：理论分析证明常见辩解无法避免赢家诅咒，即使模型准确、数据随机、模型族正确、使用样本分割
- 实验或效果：基于难民匹配的模拟研究显示，模型方法报告60%增益，而真实效应为零，与文献报告相符

## 摘要（原文）

> A major challenge in data-driven decision-making is accurate policy evaluation-i.e., guaranteeing that a learned decision-making policy achieves the promised benefits. A popular strategy is model-based policy evaluation, which estimates a model from data to infer counterfactual outcomes. This strategy is known to produce unwarrantedly optimistic estimates of the true benefit due to the winner's curse. We searched the recent literature on data-driven decision-making, identifying a sample of 55 papers published in the Management Science in the past decade; all but two relied on this flawed methodology. Several common justifications are provided: (1) the estimated models are accurate, stable, and well-calibrated, (2) the historical data uses random treatment assignment, (3) the model family is well-specified, and (4) the evaluation methodology uses sample splitting. Unfortunately, we show that no combination of these justifications avoids the winner's curse. First, we provide a theoretical analysis demonstrating that the winner's curse can cause large, spurious reported benefits even when all these justifications hold. Second, we perform a simulation study based on the recent and consequential data-driven refugee matching problem. We construct a synthetic refugee matching environment (calibrated to closely match the real setting) but designed so that no assignment policy can improve expected employment compared to random assignment. Model-based methods report large, stable gains of around 60% even when the true effect is zero; these gains are on par with improvements of 22-75% reported in the literature. Our results provide strong evidence against model-based evaluation.

