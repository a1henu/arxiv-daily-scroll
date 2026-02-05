---
layout: default
title: Optimal Rates for Feasible Payoff Set Estimation in Games
---

# Optimal Rates for Feasible Payoff Set Estimation in Games
**arXiv**：[2602.04397v1](https://arxiv.org/abs/2602.04397) · [PDF](https://arxiv.org/pdf/2602.04397.pdf)  
**作者**：Annalisa Barbara, Riccardo Poiani, Martino Bernasconi, Andrea Celli  

**一句话要点**：提出逆博弈论中可行收益集估计的极小极大最优率，适用于零和与一般和博弈。

**关键词**：逆博弈论, 可行收益集估计, 极小极大最优率, 纳什均衡, 多智能体学习, 集合推断

## 3 点简述
- 研究在仅观察玩家行动下，如何推断与纳什均衡一致的收益函数集。
- 首次为精确和近似均衡提供Hausdorff度量下的极小极大最优估计率。
- 为多智能体环境中的集合值收益推断奠定学习理论基础。

## 摘要（原文）

> We study a setting in which two players play a (possibly approximate) Nash equilibrium of a bimatrix game, while a learner observes only their actions and has no knowledge of the equilibrium or the underlying game. A natural question is whether the learner can rationalize the observed behavior by inferring the players' payoff functions. Rather than producing a single payoff estimate, inverse game theory aims to identify the entire set of payoffs consistent with observed behavior, enabling downstream use in, e.g., counterfactual analysis and mechanism design across applications like auctions, pricing, and security games. We focus on the problem of estimating the set of feasible payoffs with high probability and up to precision $ε$ on the Hausdorff metric. We provide the first minimax-optimal rates for both exact and approximate equilibrium play, in zero-sum as well as general-sum games. Our results provide learning-theoretic foundations for set-valued payoff inference in multi-agent environments.

