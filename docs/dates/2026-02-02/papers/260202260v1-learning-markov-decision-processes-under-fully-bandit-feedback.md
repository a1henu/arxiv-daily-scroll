---
layout: default
title: Learning Markov Decision Processes under Fully Bandit Feedback
---

# Learning Markov Decision Processes under Fully Bandit Feedback
**arXiv**：[2602.02260v1](https://arxiv.org/abs/2602.02260) · [PDF](https://arxiv.org/pdf/2602.02260.pdf)  
**作者**：Zhengjia Zhuo, Anupam Gupta, Viswanath Nagarajan  

**一句话要点**：提出首个高效算法，在完全强盗反馈下学习马尔可夫决策过程，实现次线性遗憾。

**关键词**：完全强盗反馈, 马尔可夫决策过程, 遗憾分析, 先知不等式, 强化学习

## 3 点简述
- 研究完全强盗反馈模型，代理仅获知聚合奖励，不观察状态-动作对。
- 设计算法实现遗憾上界为O~(√T)，对时间步长有指数依赖，证明其必要性。
- 在k项先知不等式等场景中，算法性能接近详细反馈的先进方法。

## 摘要（原文）

> A standard assumption in Reinforcement Learning is that the agent observes every visited state-action pair in the associated Markov Decision Process (MDP), along with the per-step rewards. Strong theoretical results are known in this setting, achieving nearly-tight $Θ(\sqrt{T})$-regret bounds. However, such detailed feedback can be unrealistic, and recent research has investigated more restricted settings such as trajectory feedback, where the agent observes all the visited state-action pairs, but only a single \emph{aggregate} reward. In this paper, we consider a far more restrictive ``fully bandit'' feedback model for episodic MDPs, where the agent does not even observe the visited state-action pairs -- it only learns the aggregate reward. We provide the first efficient bandit learning algorithm for episodic MDPs with $\widetilde{O}(\sqrt{T})$ regret. Our regret has an exponential dependence on the horizon length $\H$, which we show is necessary. We also obtain improved nearly-tight regret bounds for ``ordered'' MDPs; these can be used to model classical stochastic optimization problems such as $k$-item prophet inequality and sequential posted pricing. Finally, we evaluate the empirical performance of our algorithm for the setting of $k$-item prophet inequalities; despite the highly restricted feedback, our algorithm's performance is comparable to that of a state-of-art learning algorithm (UCB-VI) with detailed state-action feedback.

