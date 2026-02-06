---
layout: default
title: Efficient Algorithms for Robust Markov Decision Processes with $s$-Rectangular Ambiguity Sets
---

# Efficient Algorithms for Robust Markov Decision Processes with $s$-Rectangular Ambiguity Sets
**arXiv**：[2602.05591v1](https://arxiv.org/abs/2602.05591) · [PDF](https://arxiv.org/pdf/2602.05591.pdf)  
**作者**：Chin Pang Ho, Marek Petrik, Wolfram Wiesemann  

**一句话要点**：提出高效算法以解决s-矩形模糊集鲁棒马尔可夫决策过程问题

**关键词**：鲁棒马尔可夫决策过程, s-矩形模糊集, 高效算法, 转移核优化, 样本外性能

## 3 点简述
- 核心问题：鲁棒MDPs在模糊集下优化最差转移核，提升样本外性能
- 方法要点：开发统一框架处理s-矩形模糊集，独立考虑各状态最差概率
- 实验或效果：算法比商业求解器快数个数量级，接近经典MDPs速度

## 摘要（原文）

> Robust Markov decision processes (MDPs) have attracted significant interest due to their ability to protect MDPs from poor out-of-sample performance in the presence of ambiguity. In contrast to classical MDPs, which account for stochasticity by modeling the dynamics through a stochastic process with a known transition kernel, a robust MDP additionally accounts for ambiguity by optimizing against the most adverse transition kernel from an ambiguity set constructed via historical data. In this paper, we develop a unified solution framework for a broad class of robust MDPs with $s$-rectangular ambiguity sets, where the most adverse transition probabilities are considered independently for each state. Using our algorithms, we show that $s$-rectangular robust MDPs with $1$- and $2$-norm as well as $φ$-divergence ambiguity sets can be solved several orders of magnitude faster than with state-of-the-art commercial solvers, and often only a logarithmic factor slower than classical MDPs. We demonstrate the favorable scaling properties of our algorithms on a range of synthetically generated as well as standard benchmark instances.

