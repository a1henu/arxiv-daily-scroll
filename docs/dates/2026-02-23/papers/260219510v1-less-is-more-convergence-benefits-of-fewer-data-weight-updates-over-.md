---
layout: default
title: Less is More: Convergence Benefits of Fewer Data Weight Updates over Longer Horizon
---

# Less is More: Convergence Benefits of Fewer Data Weight Updates over Longer Horizon
**arXiv**：[2602.19510v1](https://arxiv.org/abs/2602.19510) · [PDF](https://arxiv.org/pdf/2602.19510.pdf)  
**作者**：Rudrajit Das, Neel Patel, Meisam Razaviyayn, Vahab Mirrokni  

**一句话要点**：分析数据混合中有限内层步数对收敛的影响，证明最优步数随预算对数增长。

**关键词**：数据混合, 双层优化, 收敛分析, 强凸损失, 梯度方法, 机器学习理论

## 3 点简述
- 研究数据混合的双层优化问题，聚焦有限内层步数T的理论收敛行为。
- 证明T=1的贪婪方法可能失败，在强凸假设下推导最优T随总预算N的标度律。
- 通过概念验证实验补充理论结果，支持理论分析。

## 摘要（原文）

> Data mixing--the strategic reweighting of training domains--is a critical component in training robust machine learning models. This problem is naturally formulated as a bilevel optimization task, where the outer loop optimizes domain weights to minimize validation loss, and the inner loop optimizes model parameters to minimize the weighted training loss. Classical bilevel optimization relies on hypergradients, which theoretically require the inner optimization to reach convergence. However, due to computational constraints, state-of-the-art methods use a finite, often small, number of inner update steps before updating the weights. The theoretical implications of this approximation are not well understood. In this work, we rigorously analyze the convergence behavior of data mixing with a finite number of inner steps $T$. We prove that the "greedy" practical approach of using $T=1$ can fail even in a simple quadratic example. Under a fixed parameter update budget $N$ and assuming the per-domain losses are strongly convex, we show that the optimal $T$ scales as $Θ(\log N)$ (resp., $Θ({(N \log N)}^{1/2})$) for the data mixing problem with access to full (resp., stochastic) gradients. We complement our theoretical results with proof-of-concept experiments.

