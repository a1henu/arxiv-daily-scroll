---
layout: default
title: Online Learning with Limited Information in the Sliding Window Model
---

# Online Learning with Limited Information in the Sliding Window Model
**arXiv**：[2601.03533v1](https://arxiv.org/abs/2601.03533) · [PDF](https://arxiv.org/pdf/2601.03533.pdf)  
**作者**：Vladimir Braverman, Sumegha Garg, Chen Wang, David P. Woodruff, Samson Zhou  

**一句话要点**：提出滑动窗口模型下专家问题的在线学习算法，以2次查询和极低内存实现近最优遗憾

**关键词**：滑动窗口模型, 在线学习, 专家问题, 遗憾优化, 流数据处理, 强盗问题

## 3 点简述
- 研究滑动窗口模型中的专家问题，强调近期数据价值更高，适用于流量监控等场景
- 设计算法仅需2次查询和polylog(nT)位内存，实现√(nW)polylog(nT)遗憾，优于先前区间算法
- 扩展至流数据中的强盗问题，首次以polylog内存实现次线性遗憾，并在随机损失下达到最优遗憾

## 摘要（原文）

> Motivated by recent work on the experts problem in the streaming model, we consider the experts problem in the sliding window model. The sliding window model is a well-studied model that captures applications such as traffic monitoring, epidemic tracking, and automated trading, where recent information is more valuable than older data. Formally, we have $n$ experts, $T$ days, the ability to query the predictions of $q$ experts on each day, a limited amount of memory, and should achieve the (near-)optimal regret $\sqrt{nW}\text{polylog}(nT)$ regret over any window of the last $W$ days. While it is impossible to achieve such regret with $1$ query, we show that with $2$ queries we can achieve such regret and with only $\text{polylog}(nT)$ bits of memory. Not only are our algorithms optimal for sliding windows, but we also show for every interval $\mathcal{I}$ of days that we achieve $\sqrt{n\|\mathcal{I}\|}\text{polylog}(nT)$ regret with $2$ queries and only $\text{polylog}(nT)$ bits of memory, providing an exponential improvement on the memory of previous interval regret algorithms. Building upon these techniques, we address the bandit problem in data streams, where $q=1$, achieving $n T^{2/3}\text{polylog}(T)$ regret with $\text{polylog}(nT)$ memory, which is the first sublinear regret in the streaming model in the bandit setting with polylogarithmic memory; this can be further improved to the optimal $\mathcal{O}(\sqrt{nT})$ regret if the best expert's losses are in a random order.

