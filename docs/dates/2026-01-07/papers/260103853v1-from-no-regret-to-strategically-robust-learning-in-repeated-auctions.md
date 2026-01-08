---
layout: default
title: From No-Regret to Strategically Robust Learning in Repeated Auctions
---

# From No-Regret to Strategically Robust Learning in Repeated Auctions
**arXiv**：[2601.03853v1](https://arxiv.org/abs/2601.03853) · [PDF](https://arxiv.org/pdf/2601.03853.pdf)  
**作者**：Junyao Zhao  

**一句话要点**：证明无遗憾学习算法在重复拍卖中具有策略鲁棒性，适用于满足单调分配和自愿参与的任何拍卖格式。

**关键词**：重复拍卖, 策略鲁棒性, 无遗憾学习, 分位数表示, 单调分配, Myerson拍卖理论

## 3 点简述
- 核心问题：在重复拍卖中，如何确保竞拍者使用学习算法时，拍卖者无法通过调整保留价格来过度提高收益。
- 方法要点：将单调竞价策略表示为分位数空间的分区，利用无遗憾学习算法（如MWU）更新策略，基于梯度反馈实现策略鲁棒性。
- 实验或效果：理论证明无遗憾算法能保证拍卖者平均收益不超过Myerson最优拍卖，无需显式最小化交换遗憾。

## 摘要（原文）

> In Bayesian single-item auctions, a monotone bidding strategy--one that prescribes a higher bid for a higher value type--can be equivalently represented as a partition of the quantile space into consecutive intervals corresponding to increasing bids. Kumar et al. (2024) prove that agile online gradient descent (OGD), when used to update a monotone bidding strategy through its quantile representation, is strategically robust in repeated first-price auctions: when all bidders employ agile OGD in this way, the auctioneer's average revenue per round is at most the revenue of Myerson's optimal auction, regardless of how she adjusts the reserve price over time.
>   In this work, we show that this strategic robustness guarantee is not unique to agile OGD or to the first-price auction: any no-regret learning algorithm, when fed gradient feedback with respect to the quantile representation, is strategically robust, even if the auction format changes every round, provided the format satisfies allocation monotonicity and voluntary participation. In particular, the multiplicative weights update (MWU) algorithm simultaneously achieves the optimal regret guarantee and the best-known strategic robustness guarantee. At a technical level, our results are established via a simple relation that bridges Myerson's auction theory and standard no-regret learning theory. This showcases the potential of translating standard regret guarantees into strategic robustness guarantees for specific games, without explicitly minimizing any form of swap regret.

