---
layout: default
title: Semiparametric Preference Optimization: Your Language Model is Secretly a Single-Index Model
---

# Semiparametric Preference Optimization: Your Language Model is Secretly a Single-Index Model
**arXiv**：[2512.21917v1](https://arxiv.org/abs/2512.21917) · [PDF](https://arxiv.org/pdf/2512.21917.pdf)  
**作者**：Nathan Kallus  

**一句话要点**：提出半参数偏好优化方法，在未知链接函数下对齐语言模型策略

**关键词**：偏好对齐, 半参数模型, 策略学习, 单指标模型, f-散度优化, 语言模型对齐

## 3 点简述
- 核心问题：偏好对齐中链接函数未知可能导致奖励偏差和策略错位
- 方法要点：基于f-散度约束奖励最大化，推导半参数单指标模型，开发多种策略学习器
- 实验或效果：提供有限样本策略误差界，实现鲁棒性优化，适用于神经网络和批量数据

## 摘要（原文）

> Aligning large language models to preference data is commonly implemented by assuming a known link function between the distribution of observed preferences and the unobserved rewards (e.g., a logistic link as in Bradley-Terry). If the link is wrong, however, inferred rewards can be biased and policies be misaligned. We study policy alignment to preferences under an unknown and unrestricted link. We consider an $f$-divergence-constrained reward maximization problem and show that realizability of the solution in a policy class implies a semiparametric single-index binary choice model, where a scalar-valued index determined by a policy captures the dependence on demonstrations and the rest of the preference distribution is an unrestricted function thereof. Rather than focus on estimation of identifiable finite-dimensional structural parameters in the index as in econometrics, we focus on policy learning, focusing on error to the optimal policy and allowing unidentifiable and nonparametric indices. We develop a variety of policy learners based on profiling the link function, orthogonalizing the link function, and using link-agnostic bipartite ranking objectives. We analyze these and provide finite-sample policy error bounds that depend on generic functional complexity measures of the index class. We further consider practical implementations using first-order optimization suited to neural networks and batched data. The resulting methods are robust to unknown preference noise distribution and scale, while preserving the direct optimization of policies without explicitly fitting rewards.

