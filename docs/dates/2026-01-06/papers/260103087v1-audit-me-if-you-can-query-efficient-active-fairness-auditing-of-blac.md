---
layout: default
title: Audit Me If You Can: Query-Efficient Active Fairness Auditing of Black-Box LLMs
---

# Audit Me If You Can: Query-Efficient Active Fairness Auditing of Black-Box LLMs
**arXiv**：[2601.03087v1](https://arxiv.org/abs/2601.03087) · [PDF](https://arxiv.org/pdf/2601.03087.pdf)  
**作者**：David Hartmann, Lena Pohlmann, Lelia Hanslik, Noah Gießing, Bettina Berendt, Pieter Delobelle  

**一句话要点**：提出BAFA方法以高效审计黑盒大语言模型的公平性，通过主动查询减少资源消耗。

**关键词**：公平性审计, 黑盒模型, 主动学习, 不确定性估计, 大语言模型, 查询效率

## 3 点简述
- 核心问题：黑盒大语言模型存在系统性偏见，传统审计方法查询成本高，资源密集。
- 方法要点：将审计建模为目标公平度量的不确定性估计，使用代理模型版本空间和主动查询选择来缩小误差区间。
- 实验或效果：在CivilComments和Bias-in-Bios数据集上，BAFA相比分层采样最多减少40倍查询量，性能更优且方差更低。

## 摘要（原文）

> Large Language Models (LLMs) exhibit systematic biases across demographic groups. Auditing is proposed as an accountability tool for black-box LLM applications, but suffers from resource-intensive query access. We conceptualise auditing as uncertainty estimation over a target fairness metric and introduce BAFA, the Bounded Active Fairness Auditor for query-efficient auditing of black-box LLMs. BAFA maintains a version space of surrogate models consistent with queried scores and computes uncertainty intervals for fairness metrics (e.g., $Δ$ AUC) via constrained empirical risk minimisation. Active query selection narrows these intervals to reduce estimation error. We evaluate BAFA on two standard fairness dataset case studies: \textsc{CivilComments} and \textsc{Bias-in-Bios}, comparing against stratified sampling, power sampling, and ablations. BAFA achieves target error thresholds with up to 40$\times$ fewer queries than stratified sampling (e.g., 144 vs 5,956 queries at $\varepsilon=0.02$ for \textsc{CivilComments}) for tight thresholds, demonstrates substantially better performance over time, and shows lower variance across runs. These results suggest that active sampling can reduce resources needed for independent fairness auditing with LLMs, supporting continuous model evaluations.

