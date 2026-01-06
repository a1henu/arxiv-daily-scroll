---
layout: default
title: Yukthi Opus: A Multi-Chain Hybrid Metaheuristic for Large-Scale NP-Hard Optimization
---

# Yukthi Opus: A Multi-Chain Hybrid Metaheuristic for Large-Scale NP-Hard Optimization
**arXiv**：[2601.01832v1](https://arxiv.org/abs/2601.01832) · [PDF](https://arxiv.org/pdf/2601.01832.pdf)  
**作者**：SB Danush Vikraman, Hannah Abagail, Prasanna Kesavraj, Gajanan V Honnavar  

**一句话要点**：提出Yukthi Opus多链混合元启发式算法，用于大规模NP难优化问题，在显式评估预算约束下实现高效求解。

**关键词**：NP难优化, 混合元启发式, 多链执行, 评估预算约束, 模拟退火, 马尔可夫链蒙特卡洛

## 3 点简述
- 核心问题：针对大规模NP难优化问题，在有限评估预算下平衡探索与利用，避免陷入局部最优。
- 方法要点：结合MCMC全局探索、贪婪局部搜索和自适应模拟退火，采用两阶段架构与多链执行策略。
- 实验或效果：在Rastrigin、TSP和Rosenbrock基准测试中，相比CMA-ES等方法，展现出竞争性能与稳定性。

## 摘要（原文）

> We present Yukthi Opus (YO), a multi-chain hybrid metaheuristic designed for NP-hard optimization under explicit evaluation budget constraints. YO integrates three complementary mechanisms in a structured two-phase architecture: Markov Chain Monte Carlo (MCMC) for global exploration, greedy local search for exploitation, and simulated annealing with adaptive reheating to enable controlled escape from local minima. A dedicated burn-in phase allocates evaluations to probabilistic exploration, after which a hybrid optimization loop refines promising candidates. YO further incorporates a spatial blacklist mechanism to avoid repeated evaluation of poor regions and a multi-chain execution strategy to improve robustness and reduce sensitivity to initialization.
>   We evaluate YO on three benchmarks: the Rastrigin function (5D) with ablation studies, the Traveling Salesman Problem with 50 to 200 cities, and the Rosenbrock function (5D) with comparisons against established optimizers including CMA-ES, Bayesian optimization, and accelerated particle swarm optimization. Results show that MCMC exploration and greedy refinement are critical for solution quality, while simulated annealing and multi-chain execution primarily improve stability and variance reduction. Overall, YO achieves competitive performance on large and multimodal problems while maintaining predictable evaluation budgets, making it suitable for expensive black-box optimization settings.

