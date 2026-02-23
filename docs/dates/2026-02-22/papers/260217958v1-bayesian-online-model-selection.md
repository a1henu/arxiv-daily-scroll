---
layout: default
title: Bayesian Online Model Selection
---

# Bayesian Online Model Selection
**arXiv**：[2602.17958v1](https://arxiv.org/abs/2602.17958) · [PDF](https://arxiv.org/pdf/2602.17958.pdf)  
**作者**：Aida Afshar, Yuke Zhang, Aldo Pacchiano  

**一句话要点**：提出贝叶斯在线模型选择算法以解决随机多臂老虎机中的探索挑战。

**关键词**：贝叶斯在线模型选择, 随机多臂老虎机, 贝叶斯遗憾, 探索-利用权衡, 数据共享

## 3 点简述
- 核心问题：在贝叶斯老虎机中，如何自适应探索多个基础学习器并与最优者竞争。
- 方法要点：设计新贝叶斯算法，证明贝叶斯遗憾界为O(d*M√T + √(MT))。
- 实验或效果：在多种随机老虎机设置中验证，性能与最优基础学习器竞争，并研究数据共享效果。

## 摘要（原文）

> Online model selection in Bayesian bandits raises a fundamental exploration challenge: When an environment instance is sampled from a prior distribution, how can we design an adaptive strategy that explores multiple bandit learners and competes with the best one in hindsight? We address this problem by introducing a new Bayesian algorithm for online model selection in stochastic bandits. We prove an oracle-style guarantee of $O\left( d^* M \sqrt{T} + \sqrt{(MT)} \right)$ on the Bayesian regret, where $M$ is the number of base learners, $d^*$ is the regret coefficient of the optimal base learner, and $T$ is the time horizon. We also validate our method empirically across a range of stochastic bandit settings, demonstrating performance that is competitive with the best base learner. Additionally, we study the effect of sharing data among base learners and its role in mitigating prior mis-specification.

