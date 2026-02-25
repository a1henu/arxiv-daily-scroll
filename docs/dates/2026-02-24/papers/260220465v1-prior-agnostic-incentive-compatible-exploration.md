---
layout: default
title: Prior-Agnostic Incentive-Compatible Exploration
---

# Prior-Agnostic Incentive-Compatible Exploration
**arXiv**：[2602.20465v1](https://arxiv.org/abs/2602.20465) · [PDF](https://arxiv.org/pdf/2602.20465.pdf)  
**作者**：Ramya Ramalingam, Osbert Bastani, Aaron Roth  

**一句话要点**：提出基于加权交换遗憾的激励兼容探索方法，解决多智能体动态环境中的先验无关问题。

**关键词**：激励兼容探索, 多智能体系统, 加权交换遗憾, 先验无关学习, 在线推荐平台, 贝叶斯纳什均衡

## 3 点简述
- 核心问题：在线推荐平台中，长期主体与短期智能体间的激励错位，需在未知先验下实现探索。
- 方法要点：利用加权交换遗憾界限，确保智能体在近似贝叶斯纳什均衡中忠实跟随预测，无需共享先验。
- 实验或效果：实例化具体算法，保证多臂老虎机设置中的自适应和加权遗憾界限。

## 摘要（原文）

> In bandit settings, optimizing long-term regret metrics requires exploration, which corresponds to sometimes taking myopically sub-optimal actions. When a long-lived principal merely recommends actions to be executed by a sequence of different agents (as in an online recommendation platform) this provides an incentive misalignment: exploration is "worth it" for the principal but not for the agents. Prior work studies regret minimization under the constraint of Bayesian Incentive-Compatibility in a static stochastic setting with a fixed and common prior shared amongst the agents and the algorithm designer.
>   We show that (weighted) swap regret bounds on their own suffice to cause agents to faithfully follow forecasts in an approximate Bayes Nash equilibrium, even in dynamic environments in which agents have conflicting prior beliefs and the mechanism designer has no knowledge of any agents beliefs. To obtain these bounds, it is necessary to assume that the agents have some degree of uncertainty not just about the rewards, but about their arrival time -- i.e. their relative position in the sequence of agents served by the algorithm. We instantiate our abstract bounds with concrete algorithms for guaranteeing adaptive and weighted regret in bandit settings.

