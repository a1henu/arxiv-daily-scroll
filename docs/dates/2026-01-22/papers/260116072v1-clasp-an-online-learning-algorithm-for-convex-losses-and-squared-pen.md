---
layout: default
title: CLASP: An online learning algorithm for Convex Losses And Squared Penalties
---

# CLASP: An online learning algorithm for Convex Losses And Squared Penalties
**arXiv**：[2601.16072v1](https://arxiv.org/abs/2601.16072) · [PDF](https://arxiv.org/pdf/2601.16072.pdf)  
**作者**：Ricardo N. Ferreira, Cláudia Soares, João Xavier  

**一句话要点**：提出CLASP算法以解决带约束的在线凸优化问题，最小化累积损失与平方约束违反。

**关键词**：在线凸优化, 约束优化, 凸投影算子, 遗憾分析, 平方惩罚, 强凸性

## 3 点简述
- 研究带约束的在线凸优化，学习者在迭代中选择动作，面临凸损失和凸约束。
- CLASP算法利用凸投影算子的严格非扩张性，分析中首次应用此证明策略。
- 在强凸问题中，首次实现对数级别的遗憾和累积平方惩罚上界保证。

## 摘要（原文）

> We study Constrained Online Convex Optimization (COCO), where a learner chooses actions iteratively, observes both unanticipated convex loss and convex constraint, and accumulates loss while incurring penalties for constraint violations. We introduce CLASP (Convex Losses And Squared Penalties), an algorithm that minimizes cumulative loss together with squared constraint violations. Our analysis departs from prior work by fully leveraging the firm non-expansiveness of convex projectors, a proof strategy not previously applied in this setting. For convex losses, CLASP achieves regret $O\left(T^{\max\{β,1-β\}}\right)$ and cumulative squared penalty $O\left(T^{1-β}\right)$ for any $β\in (0,1)$. Most importantly, for strongly convex problems, CLASP provides the first logarithmic guarantees on both regret and cumulative squared penalty. In the strongly convex case, the regret is upper bounded by $O( \log T )$ and the cumulative squared penalty is also upper bounded by $O( \log T )$.

