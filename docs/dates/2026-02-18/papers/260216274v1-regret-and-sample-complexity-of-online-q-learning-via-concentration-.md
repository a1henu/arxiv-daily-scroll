---
layout: default
title: Regret and Sample Complexity of Online Q-Learning via Concentration of Stochastic Approximation with Time-Inhomogeneous Markov Chains
---

# Regret and Sample Complexity of Online Q-Learning via Concentration of Stochastic Approximation with Time-Inhomogeneous Markov Chains
**arXiv**：[2602.16274v1](https://arxiv.org/abs/2602.16274) · [PDF](https://arxiv.org/pdf/2602.16274.pdf)  
**作者**：Rahul Singh, Siddharth Chandak, Eric Moulines, Vivek S. Borkar, Nicholas Bambos  

**一句话要点**：提出高概率遗憾界分析在线Q学习，基于时间非齐次马尔可夫链的随机逼近浓度理论。

**关键词**：在线Q学习, 遗憾界分析, 随机逼近, 马尔可夫链, 强化学习理论, 高概率保证

## 3 点简述
- 核心问题：在线Q学习在无限时域折扣MDP中的高概率遗憾界未知，传统方法依赖乐观项。
- 方法要点：分析Boltzmann Q学习与平滑ε-贪婪探索，证明遗憾界依赖次优性间隙，并开发时间非齐次马尔可夫链的随机逼近浓度界。
- 实验或效果：对于大间隙，遗憾次线性；小间隙时，平滑ε-贪婪探索实现近O(N^{9/10})的间隙鲁棒遗憾界。

## 摘要（原文）

> We present the first high-probability regret bound for classical online Q-learning in infinite-horizon discounted Markov decision processes, without relying on optimism or bonus terms. We first analyze Boltzmann Q-learning with decaying temperature and show that its regret depends critically on the suboptimality gap of the MDP: for sufficiently large gaps, the regret is sublinear, while for small gaps it deteriorates and can approach linear growth. To address this limitation, we study a Smoothed $ε_n$-Greedy exploration scheme that combines $ε_n$-greedy and Boltzmann exploration, for which we prove a gap-robust regret bound of near-$\tilde{O}(N^{9/10})$. To analyze these algorithms, we develop a high-probability concentration bound for contractive Markovian stochastic approximation with iterate- and time-dependent transition dynamics. This bound may be of independent interest as the contraction factor in our bound is governed by the mixing time and is allowed to converge to one asymptotically.

