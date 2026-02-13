---
layout: default
title: Is Online Linear Optimization Sufficient for Strategic Robustness?
---

# Is Online Linear Optimization Sufficient for Strategic Robustness?
**arXiv**：[2602.12253v1](https://arxiv.org/abs/2602.12253) · [PDF](https://arxiv.org/pdf/2602.12253.pdf)  
**作者**：Yang Cai, Haipeng Luo, Chen-Yu Wei, Weiqiang Zheng  

**一句话要点**：提出基于在线线性优化的黑盒转换方法，实现重复贝叶斯一价拍卖中的策略鲁棒无遗憾竞价。

**关键词**：在线线性优化, 贝叶斯一价拍卖, 策略鲁棒性, 无遗憾学习, 黑盒转换, 竞价算法

## 3 点简述
- 研究重复贝叶斯一价拍卖中竞价算法的策略鲁棒性问题，探索在线线性优化是否足够。
- 通过黑盒转换将在线线性优化算法转化为策略鲁棒无遗憾竞价算法，适用于已知和未知价值分布场景。
- 在已知分布下实现O(√(T log K))遗憾，未知分布下实现高概率O(√(T (log K+log(T/δ)))遗憾，改进现有结果。

## 摘要（原文）

> We consider bidding in repeated Bayesian first-price auctions. Bidding algorithms that achieve optimal regret have been extensively studied, but their strategic robustness to the seller's manipulation remains relatively underexplored. Bidding algorithms based on no-swap-regret algorithms achieve both desirable properties, but are suboptimal in terms of statistical and computational efficiency. In contrast, online gradient ascent is the only algorithm that achieves $O(\sqrt{TK})$ regret and strategic robustness [KSS24], where $T$ denotes the number of auctions and $K$ the number of bids.
>   In this paper, we explore whether simple online linear optimization (OLO) algorithms suffice for bidding algorithms with both desirable properties. Our main result shows that sublinear linearized regret is sufficient for strategic robustness. Specifically, we construct simple black-box reductions that convert any OLO algorithm into a strategically robust no-regret bidding algorithm, in both known and unknown value distribution settings. For the known value distribution case, our reduction yields a bidding algorithm that achieves $O(\sqrt{T \log K})$ regret and strategic robustness (with exponential improvement on the $K$-dependence compared to [KSS24]). For the unknown value distribution case, our reduction gives a bidding algorithm with high-probability $O(\sqrt{T (\log K+\log(T/δ)})$ regret and strategic robustness, while removing the bounded density assumption made in [KSS24].

