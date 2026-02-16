---
layout: default
title: Contextual Online Bilateral Trade
---

# Contextual Online Bilateral Trade
**arXiv**：[2602.12903v1](https://arxiv.org/abs/2602.12903) · [PDF](https://arxiv.org/pdf/2602.12903.pdf)  
**作者**：Romain Cosson, Federico Fusco, Anupam Gupta, Stefano Leonardi, Renato Paes Leme, Matteo Russo  

**一句话要点**：提出上下文在线双边交易算法，在两种反馈模型下实现无遗憾学习并保证预算平衡。

**关键词**：在线学习, 双边交易, 上下文估值, 遗憾最小化, 预算平衡, 反馈模型

## 3 点简述
- 研究上下文估值下的重复双边交易问题，学习者为买卖双方定价以最大化收益或利润。
- 在双比特反馈下，设计算法实现O(d log d)遗憾，并严格保持每步预算平衡。
- 在单比特反馈下，仍可达到类似遗憾界，但可能允许小负利润或需指数依赖维度。

## 摘要（原文）

> We study repeated bilateral trade when the valuations of the sellers and the buyers are contextual. More precisely, the agents' valuations are given by the inner product of a context vector with two unknown $d$-dimensional vectors -- one for the buyers and one for the sellers.
>   At each time step $t$, the learner receives a context and posts two prices, one for the seller and one for the buyer, and the trade happens if both agents accept their price. We study two objectives for this problem, gain from trade and profit, proving no-regret with respect to a surprisingly strong benchmark: the best omniscient dynamic strategy.
>   In the natural scenario where the learner observes \emph{separately} whether the agents accept their price -- the so-called \emph{two-bit} feedback -- we design algorithms that achieve $O(d\log d)$ regret for gain from trade, and $O(d \log\log T + d\log d)$ regret for profit maximization. Both results are tight, up to the $\log(d)$ factor, and implement per-step budget balance, meaning that the learner never incurs negative profit.
>   In the less informative \emph{one-bit} feedback model, the learner only observes whether a trade happens or not. For this scenario, we show that the tight two-bit regret regimes are still attainable, at the cost of allowing the learner to possibly incur a small negative profit of order $O(d\log d)$, which is notably independent of the time horizon. As a final set of results, we investigate the combination of one-bit feedback and per-step budget balance. There, we design an algorithm for gain from trade that suffers regret independent of the time horizon, but \emph{exponential} in the dimension $d$. For profit maximization, we maintain this exponential dependence on the dimension, which gets multiplied by a $\log T$ factor.

