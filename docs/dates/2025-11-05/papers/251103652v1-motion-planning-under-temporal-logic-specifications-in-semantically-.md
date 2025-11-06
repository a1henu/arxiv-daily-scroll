---
layout: default
title: Motion Planning Under Temporal Logic Specifications In Semantically Unknown Environments
---

# Motion Planning Under Temporal Logic Specifications In Semantically Unknown Environments
**arXiv**：[2511.03652v1](https://arxiv.org/abs/2511.03652) · [PDF](https://arxiv.org/pdf/2511.03652.pdf)  
**作者**：Azizollah Taheri, Derya Aksaray  

**一句话要点**：提出基于自动机与值迭代的在线重规划方法，解决语义不确定环境下的时空逻辑运动规划问题。

**关键词**：运动规划, 时空逻辑, 不确定性建模, 自动机理论, 值迭代, 在线重规划

## 3 点简述
- 核心问题：在语义标签不确定的环境中，实现满足时空逻辑规范的运动规划。
- 方法要点：构建特殊乘积自动机捕获语义不确定性，并设计边缘奖励函数。
- 实验或效果：通过仿真验证方法有效性，并展示理论结果。

## 摘要（原文）

> This paper addresses a motion planning problem to achieve
> spatio-temporal-logical tasks, expressed by syntactically co-safe linear
> temporal logic specifications (scLTL\next), in uncertain environments. Here,
> the uncertainty is modeled as some probabilistic knowledge on the semantic
> labels of the environment. For example, the task is "first go to region 1, then
> go to region 2"; however, the exact locations of regions 1 and 2 are not known
> a priori, instead a probabilistic belief is available. We propose a novel
> automata-theoretic approach, where a special product automaton is constructed
> to capture the uncertainty related to semantic labels, and a reward function is
> designed for each edge of this product automaton. The proposed algorithm
> utilizes value iteration for online replanning. We show some theoretical
> results and present some simulations/experiments to demonstrate the efficacy of
> the proposed approach.

