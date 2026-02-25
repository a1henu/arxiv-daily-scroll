---
layout: default
title: Maximin Share Guarantees via Limited Cost-Sensitive Sharing
---

# Maximin Share Guarantees via Limited Cost-Sensitive Sharing
**arXiv**：[2602.20541v1](https://arxiv.org/abs/2602.20541) · [PDF](https://arxiv.org/pdf/2602.20541.pdf)  
**作者**：Hana Salavcova, Martin Černý, Arpita Biswas  

**一句话要点**：提出有限成本敏感共享以恢复不可分割物品公平分配中的最大最小份额保证

**关键词**：公平分配, 最大最小份额, 有限共享, 成本敏感共享, 算法设计, 理论分析

## 3 点简述
- 研究允许有限共享的不可分割物品公平分配问题，共享最多k个代理并产生成本
- 证明当允许成本敏感共享时，可保证存在精确最大最小份额分配，并设计共享袋填充算法
- 引入共享最大最小份额公平概念，分析其存在性和与约束最大最小份额的联系

## 摘要（原文）

> We study the problem of fairly allocating indivisible goods when limited sharing is allowed, that is, each good may be allocated to up to $k$ agents, while incurring a cost for sharing. While classic maximin share (MMS) allocations may not exist in many instances, we demonstrate that allowing controlled sharing can restore fairness guarantees that are otherwise unattainable in certain scenarios. (1) Our first contribution shows that exact maximin share (MMS) allocations are guaranteed to exist whenever goods are allowed to be cost-sensitively shared among at least half of the agents and the number of agents is even; for odd numbers of agents, we obtain a slightly weaker MMS guarantee. (2) We further design a Shared Bag-Filling Algorithm that guarantees a $(1 - C)(k - 1)$-approximate MMS allocation, where $C$ is the maximum cost of sharing a good. Notably, when $(1 - C)(k - 1) \geq 1$, our algorithm recovers an exact MMS allocation. (3) We additionally introduce the Sharing Maximin Share (SMMS) fairness notion, a natural extension of MMS to the $k$-sharing setting. (4) We show that SMMS allocations always exist under identical utilities and for instances with two agents. (5) We construct a counterexample to show the impossibility of the universal existence of an SMMS allocation. (6) Finally, we establish a connection between SMMS and constrained MMS (CMMS), yielding approximation guarantees for SMMS via existing CMMS results. These contributions provide deep theoretical insights for the problem of fair resource allocation when a limited sharing of resources are allowed in multi-agent environments.

