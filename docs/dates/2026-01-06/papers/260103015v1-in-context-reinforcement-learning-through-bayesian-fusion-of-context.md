---
layout: default
title: In-Context Reinforcement Learning through Bayesian Fusion of Context and Value Prior
---

# In-Context Reinforcement Learning through Bayesian Fusion of Context and Value Prior
**arXiv**：[2601.03015v1](https://arxiv.org/abs/2601.03015) · [PDF](https://arxiv.org/pdf/2601.03015.pdf)  
**作者**：Anaïs Berkes, Vincent Taboga, Donna Vakalis, David Rolnick, Yoshua Bengio  

**一句话要点**：提出SPICE方法，通过贝叶斯融合上下文与价值先验，实现无需参数更新的快速适应强化学习。

**关键词**：上下文强化学习, 贝叶斯更新, 深度集成, 上置信界, 快速适应, 分布偏移鲁棒性

## 3 点简述
- 当前上下文强化学习方法难以超越训练分布或需最优数据，限制了实际应用。
- SPICE利用深度集成学习Q值先验，通过贝叶斯更新结合上下文信息，并采用上置信界规则促进探索与适应。
- 在赌博机和控制基准测试中，SPICE在未见任务上实现近最优决策，显著降低遗憾并快速适应分布偏移。

## 摘要（原文）

> In-context reinforcement learning (ICRL) promises fast adaptation to unseen environments without parameter updates, but current methods either cannot improve beyond the training distribution or require near-optimal data, limiting practical adoption. We introduce SPICE, a Bayesian ICRL method that learns a prior over Q-values via deep ensemble and updates this prior at test-time using in-context information through Bayesian updates. To recover from poor priors resulting from training on sub-optimal data, our online inference follows an Upper-Confidence Bound rule that favours exploration and adaptation. We prove that SPICE achieves regret-optimal behaviour in both stochastic bandits and finite-horizon MDPs, even when pretrained only on suboptimal trajectories. We validate these findings empirically across bandit and control benchmarks. SPICE achieves near-optimal decisions on unseen tasks, substantially reduces regret compared to prior ICRL and meta-RL approaches while rapidly adapting to unseen tasks and remaining robust under distribution shift.

