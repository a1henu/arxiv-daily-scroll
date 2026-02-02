---
layout: default
title: Optimal Fair Aggregation of Crowdsourced Noisy Labels using Demographic Parity Constraints
---

# Optimal Fair Aggregation of Crowdsourced Noisy Labels using Demographic Parity Constraints
**arXiv**：[2601.23221v1](https://arxiv.org/abs/2601.23221) · [PDF](https://arxiv.org/pdf/2601.23221.pdf)  
**作者**：Gabriel Singer, Samuel Gruffaz, Olivier Vo Van, Nicolas Vayatis, Argyris Kalogeratos  

**一句话要点**：提出基于人口统计奇偶约束的最优公平聚合方法，以解决众包噪声标签中的偏见放大问题。

**关键词**：众包聚合, 公平性约束, 人口统计奇偶, 噪声标签, 贝叶斯聚合, 后处理算法

## 3 点简述
- 分析多数投票和最优贝叶斯聚合在ε-公平框架下的公平性，推导小规模众包中公平差距上界。
- 证明聚合共识公平差距在可解释条件下指数快速收敛到真实标签公平差距，并推广多类公平后处理算法。
- 在合成和真实数据集上验证方法有效性，支持理论见解。

## 摘要（原文）

> As acquiring reliable ground-truth labels is usually costly, or infeasible, crowdsourcing and aggregation of noisy human annotations is the typical resort. Aggregating subjective labels, though, may amplify individual biases, particularly regarding sensitive features, raising fairness concerns. Nonetheless, fairness in crowdsourced aggregation remains largely unexplored, with no existing convergence guarantees and only limited post-processing approaches for enforcing $\varepsilon$-fairness under demographic parity. We address this gap by analyzing the fairness s of crowdsourced aggregation methods within the $\varepsilon$-fairness framework, for Majority Vote and Optimal Bayesian aggregation. In the small-crowd regime, we derive an upper bound on the fairness gap of Majority Vote in terms of the fairness gaps of the individual annotators. We further show that the fairness gap of the aggregated consensus converges exponentially fast to that of the ground-truth under interpretable conditions. Since ground-truth itself may still be unfair, we generalize a state-of-the-art multiclass fairness post-processing algorithm from the continuous to the discrete setting, which enforces strict demographic parity constraints to any aggregation rule. Experiments on synthetic and real datasets demonstrate the effectiveness of our approach and corroborate the theoretical insights.

