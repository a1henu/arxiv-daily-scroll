---
layout: default
title: EWSJF: An Adaptive Scheduler with Hybrid Partitioning for Mixed-Workload LLM Inference
---

# EWSJF: An Adaptive Scheduler with Hybrid Partitioning for Mixed-Workload LLM Inference
**arXiv**：[2601.21758v1](https://arxiv.org/abs/2601.21758) · [PDF](https://arxiv.org/pdf/2601.21758.pdf)  
**作者**：Bronislav Sidik, Chaya Levi, Joseph Kampeas  

**一句话要点**：提出EWSJF自适应调度器，通过混合分区优化混合工作负载LLM推理的公平性与吞吐量。

**关键词**：LLM推理调度, 混合工作负载, 自适应调度, 无监督分区, 贝叶斯优化, 吞吐量优化

## 3 点简述
- 核心问题：混合工作负载（短交互查询与长批量请求）下，FCFS调度导致队头阻塞，尾部延迟高且硬件利用率低。
- 方法要点：集成无监督分区、动态队列路由、密度加权评分和贝叶斯元优化，实时学习工作负载结构以自适应调度。
- 实验或效果：在vLLM中实现，相比FCFS，端到端吞吐量提升超30%，短请求平均首令牌时间减少达4倍。

## 摘要（原文）

> Serving Large Language Models (LLMs) under mixed workloads--short, latency-sensitive interactive queries alongside long, throughput-oriented batch requests--poses a fundamental scheduling challenge. Standard First-Come, First-Served (FCFS) policies suffer from severe head-of-line blocking, leading to high tail latency and underutilized hardware. We introduce EWSJF (Effective Workload-based Shortest Job First), an adaptive request-level scheduler that learns workload structure in real time to jointly improve fairness and throughput. EWSJF operates upstream of execution-level schedulers and integrates four components: (1) Refine-and-Prune, an unsupervised partitioning algorithm that discovers performance-homogeneous request groups; (2) Dynamic Queue Routing for assigning requests to these groups; (3) Density-Weighted Scoring, a context-aware prioritization function balancing urgency and fairness; and (4) Bayesian Meta-Optimization, which continuously tunes scoring and partitioning parameters based on live performance feedback. Implemented in vLLM, EWSJF improves end-to-end throughput by over 30% and reduces average Time-To-First-Token for short requests by up to 4x compared to FCFS. These results demonstrate that adaptive, learning-based request scheduling is a critical missing layer for efficient and responsive LLM serving. Implementation available at https://anonymous.4open.science/r/vllm_0110-32D8.

