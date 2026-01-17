---
layout: default
title: Queueing-Aware Optimization of Reasoning Tokens for Accuracy-Latency Trade-offs in LLM Servers
---

# Queueing-Aware Optimization of Reasoning Tokens for Accuracy-Latency Trade-offs in LLM Servers
**arXiv**：[2601.10274v1](https://arxiv.org/abs/2601.10274) · [PDF](https://arxiv.org/pdf/2601.10274.pdf)  
**作者**：Emre Ozbas, Melih Bastopcu  

**一句话要点**：提出队列感知的推理令牌优化方法，以平衡LLM服务器中准确性与延迟的权衡。

**关键词**：LLM服务器优化, 令牌分配, 准确性与延迟权衡, 队列理论, M/G/1模型, 约束优化

## 3 点简述
- 核心问题：在异构查询流中，如何分配推理令牌以优化准确性与系统延迟的权衡。
- 方法要点：基于M/G/1队列模型，构建严格凹优化问题，确保最优令牌分配的存在性和唯一性。
- 实验或效果：通过连续解舍入获得整数分配，模拟评估性能损失。

## 摘要（原文）

> We consider a single large language model (LLM) server that serves a heterogeneous stream of queries belonging to $N$ distinct task types. Queries arrive according to a Poisson process, and each type occurs with a known prior probability. For each task type, the server allocates a fixed number of internal thinking tokens, which determines the computational effort devoted to that query. The token allocation induces an accuracy-latency trade-off: the service time follows an approximately affine function of the allocated tokens, while the probability of a correct response exhibits diminishing returns. Under a first-in, first-out (FIFO) service discipline, the system operates as an $M/G/1$ queue, and the mean system time depends on the first and second moments of the resulting service-time distribution. We formulate a constrained optimization problem that maximizes a weighted average accuracy objective penalized by the mean system time, subject to architectural token-budget constraints and queue-stability conditions. The objective function is shown to be strictly concave over the stability region, which ensures existence and uniqueness of the optimal token allocation. The first-order optimality conditions yield a coupled projected fixed-point characterization of the optimum, together with an iterative solution and an explicit sufficient condition for contraction. Moreover, a projected gradient method with a computable global step-size bound is developed to guarantee convergence beyond the contractive regime. Finally, integer-valued token allocations are attained via rounding of the continuous solution, and the resulting performance loss is evaluated in simulation results.

