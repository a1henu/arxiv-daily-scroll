---
layout: default
title: Additive Control Variates Dominate Self-Normalisation in Off-Policy Evaluation
---

# Additive Control Variates Dominate Self-Normalisation in Off-Policy Evaluation
**arXiv**：[2602.14914v1](https://arxiv.org/abs/2602.14914) · [PDF](https://arxiv.org/pdf/2602.14914.pdf)  
**作者**：Olivier Jeunen, Shashank Gupta  

**一句话要点**：证明最优加性控制变量在离策略评估中优于自归一化方法

**关键词**：离策略评估, 控制变量, 方差减少, 推荐系统, 排名系统, 渐近分析

## 3 点简述
- 核心问题：离策略评估中自归一化方法可能非最优，缺乏加性控制变量的理论保证。
- 方法要点：提出β*-IPS估计器，证明其均方误差渐近优于SNIPS，并分解方差差距。
- 实验或效果：理论分析表明加性基线校正更优，适用于排名和推荐系统评估。

## 摘要（原文）

> Off-policy evaluation (OPE) is essential for assessing ranking and recommendation systems without costly online interventions. Self-Normalised Inverse Propensity Scoring (SNIPS) is a standard tool for variance reduction in OPE, leveraging a multiplicative control variate. Recent advances in off-policy learning suggest that additive control variates (baseline corrections) may offer superior performance, yet theoretical guarantees for evaluation are lacking. This paper provides a definitive answer: we prove that $β^\star$-IPS, an estimator with an optimal additive baseline, asymptotically dominates SNIPS in Mean Squared Error. By analytically decomposing the variance gap, we show that SNIPS is asymptotically equivalent to using a specific -- but generally sub-optimal -- additive baseline. Our results theoretically justify shifting from self-normalisation to optimal baseline corrections for both ranking and recommendation.

