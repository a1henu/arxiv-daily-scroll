---
layout: default
title: Online Prediction of Stochastic Sequences with High Probability Regret Bounds
---

# Online Prediction of Stochastic Sequences with High Probability Regret Bounds
**arXiv**：[2602.16236v1](https://arxiv.org/abs/2602.16236) · [PDF](https://arxiv.org/pdf/2602.16236.pdf)  
**作者**：Matthias Frey, Jonathan H. Manton, Jingge Zhu  

**一句话要点**：提出高概率后悔界以补充随机序列在线预测的期望界

**关键词**：在线预测, 随机序列, 后悔界, 高概率保证, 收敛率分析, 不可能性结果

## 3 点简述
- 研究随机序列在线预测中高概率后悔界的缺失问题
- 推导出与期望界形式相似的高概率后悔界，收敛率为O(T^{-1/2}δ^{-1/2})
- 证明在相同形式下无法改进δ的指数，除非增加假设

## 摘要（原文）

> We revisit the classical problem of universal prediction of stochastic sequences with a finite time horizon $T$ known to the learner. The question we investigate is whether it is possible to derive vanishing regret bounds that hold with high probability, complementing existing bounds from the literature that hold in expectation. We propose such high-probability bounds which have a very similar form as the prior expectation bounds. For the case of universal prediction of a stochastic process over a countable alphabet, our bound states a convergence rate of $\mathcal{O}(T^{-1/2} δ^{-1/2})$ with probability as least $1-δ$ compared to prior known in-expectation bounds of the order $\mathcal{O}(T^{-1/2})$. We also propose an impossibility result which proves that it is not possible to improve the exponent of $δ$ in a bound of the same form without making additional assumptions.

