---
layout: default
title: Vectorized Online POMDP Planning
---

# Vectorized Online POMDP Planning
**arXiv**：[2510.27191v1](https://arxiv.org/abs/2510.27191) · [PDF](https://arxiv.org/pdf/2510.27191.pdf)  
**作者**：Marcus Hoerger, Muhammad Sudrajat, Hanna Kurniawati  

**一句话要点**：提出向量化在线POMDP规划器以解决部分可观测环境下的并行规划瓶颈

**关键词**：部分可观测马尔可夫决策过程, 在线规划, 向量化计算, 并行求解, 机器人自主规划

## 3 点简述
- 核心问题：部分可观测马尔可夫决策过程求解中，并行化存在依赖和同步瓶颈，抵消硬件并行优势。
- 方法要点：利用分析优化部分组件，将规划数据结构表示为张量，实现全向量化无依赖计算。
- 实验或效果：相比现有并行在线求解器，计算效率提升至少20倍，获得近似最优解。

## 摘要（原文）

> Planning under partial observability is an essential capability of autonomous
> robots. The Partially Observable Markov Decision Process (POMDP) provides a
> powerful framework for planning under partial observability problems, capturing
> the stochastic effects of actions and the limited information available through
> noisy observations. POMDP solving could benefit tremendously from massive
> parallelization of today's hardware, but parallelizing POMDP solvers has been
> challenging. They rely on interleaving numerical optimization over actions with
> the estimation of their values, which creates dependencies and synchronization
> bottlenecks between parallel processes that can quickly offset the benefits of
> parallelization. In this paper, we propose Vectorized Online POMDP Planner
> (VOPP), a novel parallel online solver that leverages a recent POMDP
> formulation that analytically solves part of the optimization component,
> leaving only the estimation of expectations for numerical computation. VOPP
> represents all data structures related to planning as a collection of tensors
> and implements all planning steps as fully vectorized computations over this
> representation. The result is a massively parallel solver with no dependencies
> and synchronization bottlenecks between parallel computations. Experimental
> results indicate that VOPP is at least 20X more efficient in computing
> near-optimal solutions compared to an existing state-of-the-art parallel online
> solver.

