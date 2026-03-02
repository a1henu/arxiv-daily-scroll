---
layout: default
title: Portfolio Reinforcement Learning with Scenario-Context Rollout
---

# Portfolio Reinforcement Learning with Scenario-Context Rollout
**arXiv**：[2602.24037v1](https://arxiv.org/abs/2602.24037) · [PDF](https://arxiv.org/pdf/2602.24037.pdf)  
**作者**：Vanya Priscillia Bendatu, Yao Lu  

**一句话要点**：提出基于场景上下文展开的宏观条件化方法，以稳定强化学习在投资组合再平衡中的应用。

**关键词**：投资组合再平衡, 强化学习, 场景生成, 分布偏移, 奖励不匹配, 夏普比率

## 3 点简述
- 市场机制变化导致分布偏移，影响投资组合再平衡策略性能。
- 通过生成压力事件下的多变量回报场景，并解决奖励-转移不匹配问题。
- 在31个美国股票和ETF组合中，夏普比率提升最高76%，最大回撤降低最高53%。

## 摘要（原文）

> Market regime shifts induce distribution shifts that can degrade the performance of portfolio rebalancing policies. We propose macro-conditioned scenario-context rollout (SCR) that generates plausible next-day multivariate return scenarios under stress events. However, doing so faces new challenges, as history will never tell what would have happened differently. As a result, incorporating scenario-based rewards from rollouts introduces a reward--transition mismatch in temporal-difference learning, destabilizing RL critic training.
>   We analyze this inconsistency and show it leads to a mixed evaluation target. Guided by this analysis, we construct a counterfactual next state using the rollout-implied continuations and augment the critic agent's bootstrap target. Doing so stabilizes the learning and provides a viable bias-variance tradeoff.
>   In out-of-sample evaluations across 31 distinct universes of U.S. equity and ETF portfolios, our method improves Sharpe ratio by up to 76% and reduces maximum drawdown by up to 53% compared with classic and RL-based portfolio rebalancing baselines.

