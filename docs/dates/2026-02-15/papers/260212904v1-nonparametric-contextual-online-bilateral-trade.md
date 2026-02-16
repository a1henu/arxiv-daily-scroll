---
layout: default
title: Nonparametric Contextual Online Bilateral Trade
---

# Nonparametric Contextual Online Bilateral Trade
**arXiv**：[2602.12904v1](https://arxiv.org/abs/2602.12904) · [PDF](https://arxiv.org/pdf/2602.12904.pdf)  
**作者**：Emanuele Coccia, Martino Bernasconi, Andrea Celli  

**一句话要点**：提出非参数上下文在线双边交易算法，在单比特反馈和强预算平衡下实现次线性遗憾。

**关键词**：在线双边交易, 非参数学习, 上下文定价, 单比特反馈, 强预算平衡, 遗憾分析

## 3 点简述
- 研究上下文在线双边交易问题，学习者在每轮基于上下文向量为买卖双方定价，仅观察交易是否发生。
- 设计基于分层树构造的算法，处理任意Lipschitz非参数估值函数，保证遗憾为O~(T^{(d-1)/d})。
- 在完全反馈设置下提供匹配下界，证明遗憾界紧致，算法在单比特反馈和强预算平衡约束下有效。

## 摘要（原文）

> We study the problem of contextual online bilateral trade. At each round, the learner faces a seller-buyer pair and must propose a trade price without observing their private valuations for the item being sold. The goal of the learner is to post prices to facilitate trades between the two parties. Before posting a price, the learner observes a $d$-dimensional context vector that influences the agent's valuations. Prior work in the contextual setting has focused on linear models. In this work, we tackle a general nonparametric setting in which the buyer's and seller's valuations behave according to arbitrary Lipschitz functions of the context. We design an algorithm that leverages contextual information through a hierarchical tree construction and guarantees regret $\widetilde{O}(T^{{(d-1)}/d})$. Remarkably, our algorithm operates under two stringent features of the setting: (1) one-bit feedback, where the learner only observes whether a trade occurred or not, and (2) strong budget balance, where the learner cannot subsidize or profit from the market participants. We further provide a matching lower bound in the full-feedback setting, demonstrating the tightness of our regret bound.

