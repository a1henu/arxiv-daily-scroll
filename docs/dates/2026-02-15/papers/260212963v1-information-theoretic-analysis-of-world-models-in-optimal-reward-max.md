---
layout: default
title: Information-theoretic analysis of world models in optimal reward maximizers
---

# Information-theoretic analysis of world models in optimal reward maximizers
**arXiv**：[2602.12963v1](https://arxiv.org/abs/2602.12963) · [PDF](https://arxiv.org/pdf/2602.12963.pdf)  
**作者**：Alfred Harwood, Jose Faustino, Alex Altair  

**一句话要点**：量化最优策略隐含世界模型的信息量，证明互信息为n log m比特

**关键词**：信息论分析, 最优策略, 受控马尔可夫过程, 世界模型, 互信息, 奖励最大化

## 3 点简述
- 核心问题：AI成功行为是否需要内部世界表示，量化最优策略提供环境信息量
- 方法要点：基于受控马尔可夫过程，假设均匀先验，分析最优策略与环境互信息
- 实验或效果：证明互信息为n log m比特，适用于多种奖励最大化目标

## 摘要（原文）

> An important question in the field of AI is the extent to which successful behaviour requires an internal representation of the world. In this work, we quantify the amount of information an optimal policy provides about the underlying environment. We consider a Controlled Markov Process (CMP) with $n$ states and $m$ actions, assuming a uniform prior over the space of possible transition dynamics. We prove that observing a deterministic policy that is optimal for any non-constant reward function then conveys exactly $n \log m$ bits of information about the environment. Specifically, we show that the mutual information between the environment and the optimal policy is $n \log m$ bits. This bound holds across a broad class of objectives, including finite-horizon, infinite-horizon discounted, and time-averaged reward maximization. These findings provide a precise information-theoretic lower bound on the "implicit world model'' necessary for optimality.

