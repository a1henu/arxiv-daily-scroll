---
layout: default
title: Queue Length Regret Bounds for Contextual Queueing Bandits
---

# Queue Length Regret Bounds for Contextual Queueing Bandits
**arXiv**：[2601.19300v1](https://arxiv.org/abs/2601.19300) · [PDF](https://arxiv.org/pdf/2601.19300.pdf)  
**作者**：Seoungbin Bae, Garyeong Kang, Dabeen Lee  

**一句话要点**：提出上下文排队赌博机框架，通过策略切换队列和耦合论证实现队列长度遗憾界分析。

**关键词**：上下文排队赌博机, 队列长度遗憾, 调度学习, 耦合论证, 服务率估计

## 3 点简述
- 核心问题：在未知服务率下，基于上下文特征调度作业以最大化离开率，并评估队列长度遗憾。
- 方法要点：引入策略切换队列和耦合论证，分解遗憾以分析短期和长期效应，设计CQB-ε和CQB-Opt算法。
- 实验或效果：理论证明CQB-ε遗憾上界为O~(T^{-1/4})，CQB-Opt在对抗性上下文中为O(log^2 T)，实验验证结果。

## 摘要（原文）

> We introduce contextual queueing bandits, a new context-aware framework for scheduling while simultaneously learning unknown service rates. Individual jobs carry heterogeneous contextual features, based on which the agent chooses a job and matches it with a server to maximize the departure rate. The service/departure rate is governed by a logistic model of the contextual feature with an unknown server-specific parameter. To evaluate the performance of a policy, we consider queue length regret, defined as the difference in queue length between the policy and the optimal policy. The main challenge in the analysis is that the lists of remaining job features in the queue may differ under our policy versus the optimal policy for a given time step, since they may process jobs in different orders. To address this, we propose the idea of policy-switching queues equipped with a sophisticated coupling argument. This leads to a novel queue length regret decomposition framework, allowing us to understand the short-term effect of choosing a suboptimal job-server pair and its long-term effect on queue state differences. We show that our algorithm, CQB-$\varepsilon$, achieves a regret upper bound of $\widetilde{\mathcal{O}}(T^{-1/4})$. We also consider the setting of adversarially chosen contexts, for which our second algorithm, CQB-Opt, achieves a regret upper bound of $\mathcal{O}(\log^2 T)$. Lastly, we provide experimental results that validate our theoretical findings.

