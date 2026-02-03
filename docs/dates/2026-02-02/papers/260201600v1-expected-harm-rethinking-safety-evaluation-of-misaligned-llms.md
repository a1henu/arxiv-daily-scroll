---
layout: default
title: Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs
---

# Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs
**arXiv**：[2602.01600v1](https://arxiv.org/abs/2602.01600) · [PDF](https://arxiv.org/pdf/2602.01600.pdf)  
**作者**：Yen-Shan Chen, Zhi Rui Tam, Cheng-Kuang Wu, Yun-Nung Chen  

**一句话要点**：提出预期危害指标以重新评估大语言模型安全，揭示模型风险校准不足问题。

**关键词**：大语言模型安全, 预期危害, 风险校准, 执行概率, 线性探测, 攻击成功率

## 3 点简述
- 核心问题：现有安全评估依赖严重性分类，忽略威胁执行概率，导致风险假设不准确。
- 方法要点：引入预期危害指标，结合严重性和执行成本建模的执行概率，量化危害。
- 实验或效果：实证分析显示模型存在逆风险校准，攻击成功率可提升至2倍，线性探测揭示模型对执行成本无内部表征。

## 摘要（原文）

> Current evaluations of LLM safety predominantly rely on severity-based taxonomies to assess the harmfulness of malicious queries. We argue that this formulation requires re-examination as it assumes uniform risk across all malicious queries, neglecting Execution Likelihood--the conditional probability of a threat being realized given the model's response. In this work, we introduce Expected Harm, a metric that weights the severity of a jailbreak by its execution likelihood, modeled as a function of execution cost. Through empirical analysis of state-of-the-art models, we reveal a systematic Inverse Risk Calibration: models disproportionately exhibit stronger refusal behaviors for low-likelihood (high-cost) threats while remaining vulnerable to high-likelihood (low-cost) queries. We demonstrate that this miscalibration creates a structural vulnerability: by exploiting this property, we increase the attack success rate of existing jailbreaks by up to $2\times$. Finally, we trace the root cause of this failure using linear probing, which reveals that while models encode severity in their latent space to drive refusal decisions, they possess no distinguishable internal representation of execution cost, making them "blind" to this critical dimension of risk.

