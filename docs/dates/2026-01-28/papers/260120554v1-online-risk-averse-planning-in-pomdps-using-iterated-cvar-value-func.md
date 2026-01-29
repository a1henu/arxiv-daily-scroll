---
layout: default
title: Online Risk-Averse Planning in POMDPs Using Iterated CVaR Value Function
---

# Online Risk-Averse Planning in POMDPs Using Iterated CVaR Value Function
**arXiv**：[2601.20554v1](https://arxiv.org/abs/2601.20554) · [PDF](https://arxiv.org/pdf/2601.20554.pdf)  
**作者**：Yaacov Pariente, Vadim Indelman  

**一句话要点**：提出基于迭代CVaR的在线风险规避规划方法，用于部分可观测马尔可夫决策过程。

**关键词**：部分可观测马尔可夫决策过程, 风险敏感规划, 迭代条件风险价值, 在线规划算法, 尾部风险降低

## 3 点简述
- 研究部分可观测环境下的风险敏感规划，采用迭代条件风险价值作为动态风险度量。
- 扩展三种在线规划算法以优化ICVaR值函数，并引入风险参数α控制风险规避程度。
- 实验表明ICVaR规划器在基准POMDP领域相比风险中性方法能降低尾部风险。

## 摘要（原文）

> We study risk-sensitive planning under partial observability using the dynamic risk measure Iterated Conditional Value-at-Risk (ICVaR). A policy evaluation algorithm for ICVaR is developed with finite-time performance guarantees that do not depend on the cardinality of the action space. Building on this foundation, three widely used online planning algorithms--Sparse Sampling, Particle Filter Trees with Double Progressive Widening (PFT-DPW), and Partially Observable Monte Carlo Planning with Observation Widening (POMCPOW)--are extended to optimize the ICVaR value function rather than the expectation of the return. Our formulations introduce a risk parameter $α$, where $α= 1$ recovers standard expectation-based planning and $α< 1$ induces increasing risk aversion. For ICVaR Sparse Sampling, we establish finite-time performance guarantees under the risk-sensitive objective, which further enable a novel exploration strategy tailored to ICVaR. Experiments on benchmark POMDP domains demonstrate that the proposed ICVaR planners achieve lower tail risk compared to their risk-neutral counterparts.

