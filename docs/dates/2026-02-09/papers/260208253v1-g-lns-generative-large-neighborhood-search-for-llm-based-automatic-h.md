---
layout: default
title: G-LNS: Generative Large Neighborhood Search for LLM-Based Automatic Heuristic Design
---

# G-LNS: Generative Large Neighborhood Search for LLM-Based Automatic Heuristic Design
**arXiv**：[2602.08253v1](https://arxiv.org/abs/2602.08253) · [PDF](https://arxiv.org/pdf/2602.08253.pdf)  
**作者**：Baoyun Zhao, He Wang, Liang Zeng  

**一句话要点**：提出G-LNS框架，基于大语言模型自动设计大邻域搜索算子以解决组合优化问题

**关键词**：大语言模型, 自动启发式设计, 大邻域搜索, 组合优化, 协同演化

## 3 点简述
- 现有基于大语言模型的自动启发式设计方法局限于固定启发式形式，搜索空间受限，难以逃离局部最优
- G-LNS利用大语言模型协同演化破坏与修复算子对，通过合作评估机制捕捉交互，实现结构破坏与重建
- 在旅行商问题和带容量车辆路径问题等基准测试中，G-LNS显著优于现有方法，发现启发式具有鲁棒泛化能力

## 摘要（原文）

> While Large Language Models (LLMs) have recently shown promise in Automated Heuristic Design (AHD), existing approaches typically formulate AHD around constructive priority rules or parameterized local search guidance, thereby restricting the search space to fixed heuristic forms. Such designs offer limited capacity for structural exploration, making it difficult to escape deep local optima in complex Combinatorial Optimization Problems (COPs). In this work, we propose G-LNS, a generative evolutionary framework that extends LLM-based AHD to the automated design of Large Neighborhood Search (LNS) operators. Unlike prior methods that evolve heuristics in isolation, G-LNS leverages LLMs to co-evolve tightly coupled pairs of destroy and repair operators. A cooperative evaluation mechanism explicitly captures their interaction, enabling the discovery of complementary operator logic that jointly performs effective structural disruption and reconstruction. Extensive experiments on challenging COP benchmarks, such as Traveling Salesman Problems (TSP) and Capacitated Vehicle Routing Problems (CVRP), demonstrate that G-LNS significantly outperforms LLM-based AHD methods as well as strong classical solvers. The discovered heuristics not only achieve near-optimal solutions with reduced computational budgets but also exhibit robust generalization across diverse and unseen instance distributions.

