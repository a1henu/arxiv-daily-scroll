---
layout: default
title: Distributional Regression with Tabular Foundation Models: Evaluating Probabilistic Predictions via Proper Scoring Rules
---

# Distributional Regression with Tabular Foundation Models: Evaluating Probabilistic Predictions via Proper Scoring Rules
**arXiv**：[2603.08206v1](https://arxiv.org/abs/2603.08206) · [PDF](https://arxiv.org/pdf/2603.08206.pdf)  
**作者**：Jonas Landsgesell, Pascal Knoll  

**一句话要点**：提出使用连续排序概率评分评估表格基础模型的概率预测，以解决回归基准中仅关注点估计的问题。

**关键词**：概率回归, 适当评分规则, 连续排序概率评分, 表格基础模型, 分布回归, 基准评估

## 3 点简述
- 当前表格回归基准过度依赖均方误差等点估计指标，忽略概率预测的评估。
- 论文倡导在基准中引入连续排序概率评分等适当评分规则来评估概率回归。
- 研究表明评分规则选择影响模型归纳偏差，建议微调或提示表格基础模型。

## 摘要（原文）

> Prior-Data Fitted Networks (PFNs), such as TabPFN and TabICL, have revolutionized tabular deep learning by leveraging in-context learning for tabular data.
>   These models are meant as foundation models for classification and regression settings and promise to greatly simplify deployment in practical settings because their performance is unprecedented (in terms of mean squared error or $R^2$, when measured on common benchmarks like TabArena or TALENT).
>   However, we see an important weakness of current benchmarks for the regression setting: the current benchmarks focus on evaluating win rates and performance using metrics like (root) mean squared error or $R^2$.
>   Therefore, these leaderboards (implicitly and explicitly) push researchers to optimize for machine learning pipelines which elicit a good mean value estimate.
>   The main problem is that this approach only evaluates a point estimate (namely the mean estimator which is the Bayes estimator associated with the mean squared error loss).
>   In this article we discuss the application of proper scoring rules for evaluating the goodness of probabilistic forecasts in distributional regression.
>   We also propose to enhance common machine learning benchmarks with metrics for probabilistic regression.
>   To improve the status quo and make the machine learning community aware of scoring rules for probabilistic regression, we advocate to use the continuous ranked probability score (CRPS) in benchmarks for probabilistic regression.
>   However, we also illustrate that the choice of the scoring rule changes the inductive bias of the trained model. We, therefore, advocate for finetuning or promptable tabular foundation models.

