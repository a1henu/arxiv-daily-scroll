---
layout: default
title: InferF: Declarative Factorization of AI/ML Inferences over Joins
---

# InferF: Declarative Factorization of AI/ML Inferences over Joins
**arXiv**：[2511.20489v1](https://arxiv.org/abs/2511.20489) · [PDF](https://arxiv.org/pdf/2511.20489.pdf)  
**作者**：Kanchan Chowdhury, Lixi Zhou, Lulu Xie, Xinwei Fu, Jia Zou  

**一句话要点**：提出InferF系统以优化多路连接上的AI/ML推理计算

**关键词**：因子化机器学习, 多路连接推理, 声明式系统, 计算优化, 数据库引擎集成

## 3 点简述
- 核心问题：多路连接中重复数据导致AI/ML推理计算冗余，现有因子化方法讨论不足。
- 方法要点：基于声明式表达式，将因子化计算下推到连接树节点，最小化计算和连接开销。
- 实验或效果：在真实数据集上实现高达11.3倍加速，并总结因子化ML的适用条件。

## 摘要（原文）

> Real-world AI/ML workflows often apply inference computations to feature vectors joined from multiple datasets. To avoid the redundant AI/ML computations caused by repeated data records in the join's output, factorized ML has been proposed to decompose ML computations into sub-computations to be executed on each normalized dataset. However, there is insufficient discussion on how factorized ML could impact AI/ML inference over multi-way joins. To address the limitations, we propose a novel declarative InferF system, focusing on the factorization of arbitrary inference workflows represented as analyzable expressions over the multi-way joins. We formalize our problem to flexibly push down partial factorized computations to qualified nodes in the join tree to minimize the overall inference computation and join costs and propose two algorithms to resolve the problem: (1) a greedy algorithm based on a per-node cost function that estimates the influence on overall latency if a subset of factorized computations is pushed to a node, and (2) a genetic algorithm for iteratively enumerating and evaluating promising factorization plans. We implement InferF on Velox, an open-sourced database engine from Meta, evaluate it on real-world datasets, observed up to 11.3x speedups, and systematically summarized the factors that determine when factorized ML can benefit AI/ML inference workflows.

