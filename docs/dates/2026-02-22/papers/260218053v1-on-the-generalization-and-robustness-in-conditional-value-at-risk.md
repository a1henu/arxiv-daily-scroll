---
layout: default
title: On the Generalization and Robustness in Conditional Value-at-Risk
---

# On the Generalization and Robustness in Conditional Value-at-Risk
**arXiv**：[2602.18053v1](https://arxiv.org/abs/2602.18053) · [PDF](https://arxiv.org/pdf/2602.18053.pdf)  
**作者**：Dinesh Karthik Mulumudi, Piyushi Manupriya, Gholamali Aminian, Anant Raj  

**一句话要点**：分析条件风险价值在重尾和污染数据下的泛化与鲁棒性，提出截断中位数均值估计器。

**关键词**：条件风险价值, 重尾数据, 泛化分析, 鲁棒性保证, 风险敏感学习, 对抗污染

## 3 点简述
- 研究条件风险价值在重尾数据下的统计行为，揭示其与期望风险的根本差异。
- 建立高概率泛化和超额风险界，扩展到依赖数据，并证明极小极大最优性。
- 提出截断中位数均值估计器，在对抗污染下实现最优鲁棒性，并分析决策不稳定性。

## 摘要（原文）

> Conditional Value-at-Risk (CVaR) is a widely used risk-sensitive objective for learning under rare but high-impact losses, yet its statistical behavior under heavy-tailed data remains poorly understood. Unlike expectation-based risk, CVaR depends on an endogenous, data-dependent quantile, which couples tail averaging with threshold estimation and fundamentally alters both generalization and robustness properties. In this work, we develop a learning-theoretic analysis of CVaR-based empirical risk minimization under heavy-tailed and contaminated data. We establish sharp, high-probability generalization and excess risk bounds under minimal moment assumptions, covering fixed hypotheses, finite and infinite classes, and extending to $β$-mixing dependent data; we further show that these rates are minimax optimal. To capture the intrinsic quantile sensitivity of CVaR, we derive a uniform Bahadur-Kiefer type expansion that isolates a threshold-driven error term absent in mean-risk ERM and essential in heavy-tailed regimes. We complement these results with robustness guarantees by proposing a truncated median-of-means CVaR estimator that achieves optimal rates under adversarial contamination. Finally, we show that CVaR decisions themselves can be intrinsically unstable under heavy tails, establishing a fundamental limitation on decision robustness even when the population optimum is well separated. Together, our results provide a principled characterization of when CVaR learning generalizes and is robust, and when instability is unavoidable due to tail scarcity.

