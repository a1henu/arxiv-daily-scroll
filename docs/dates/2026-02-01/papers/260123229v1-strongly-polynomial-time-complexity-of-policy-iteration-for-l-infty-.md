---
layout: default
title: Strongly Polynomial Time Complexity of Policy Iteration for $L_\infty$ Robust MDPs
---

# Strongly Polynomial Time Complexity of Policy Iteration for $L_\infty$ Robust MDPs
**arXiv**：[2601.23229v1](https://arxiv.org/abs/2601.23229) · [PDF](https://arxiv.org/pdf/2601.23229.pdf)  
**作者**：Ali Asadi, Krishnendu Chatterjee, Ehsan Goharshady, Mehrdad Karrabi, Alipasha Montaseri, Carlo Pagano  

**一句话要点**：提出鲁棒策略迭代算法，在固定折扣因子下为$(s,a)$-矩形$L_\infty$鲁棒MDPs实现强多项式时间复杂性

**关键词**：鲁棒马尔可夫决策过程, 强多项式时间, 策略迭代, $L_\infty$不确定性, 折扣因子, 计算复杂性

## 3 点简述
- 核心问题：鲁棒MDPs中是否存在强多项式时间算法是重要开放问题，尤其针对$(s,a)$-矩形$L_\infty$不确定性集模型
- 方法要点：采用鲁棒策略迭代算法，在固定折扣因子下证明其运行时间为强多项式
- 实验或效果：未知，论文未提及实验或具体性能数据，主要贡献为理论复杂性分析

## 摘要（原文）

> Markov decision processes (MDPs) are a fundamental model in sequential decision making. Robust MDPs (RMDPs) extend this framework by allowing uncertainty in transition probabilities and optimizing against the worst-case realization of that uncertainty. In particular, $(s, a)$-rectangular RMDPs with $L_\infty$ uncertainty sets form a fundamental and expressive model: they subsume classical MDPs and turn-based stochastic games. We consider this model with discounted payoffs. The existence of polynomial and strongly-polynomial time algorithms is a fundamental problem for these optimization models. For MDPs, linear programming yields polynomial-time algorithms for any arbitrary discount factor, and the seminal work of Ye established strongly--polynomial time for a fixed discount factor. The generalization of such results to RMDPs has remained an important open problem. In this work, we show that a robust policy iteration algorithm runs in strongly-polynomial time for $(s, a)$-rectangular $L_\infty$ RMDPs with a constant (fixed) discount factor, resolving an important algorithmic question.

