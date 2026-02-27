---
layout: default
title: Enhancing CVRP Solver through LLM-driven Automatic Heuristic Design
---

# Enhancing CVRP Solver through LLM-driven Automatic Heuristic Design
**arXiv**：[2602.23092v1](https://arxiv.org/abs/2602.23092) · [PDF](https://arxiv.org/pdf/2602.23092.pdf)  
**作者**：Zhuoliang Xie, Fei Liu, Zhenkun Wang, Qingfu Zhang  

**一句话要点**：提出AILS-AHD方法，利用大语言模型自动设计启发式规则以解决带容量车辆路径问题。

**关键词**：带容量车辆路径问题, 大语言模型, 启发式设计, 组合优化, 自适应迭代局部搜索

## 3 点简述
- 核心问题：带容量车辆路径问题（CVRP）是NP难组合优化问题，大规模实例计算挑战大。
- 方法要点：结合进化搜索与大语言模型，在自适应迭代局部搜索中动态生成和优化破坏启发式规则。
- 实验或效果：在CVRPLib大规模基准测试中，对10个实例中的8个建立了新的最佳已知解，性能优于先进求解器。

## 摘要（原文）

> The Capacitated Vehicle Routing Problem (CVRP), a fundamental combinatorial optimization challenge, focuses on optimizing fleet operations under vehicle capacity constraints. While extensively studied in operational research, the NP-hard nature of CVRP continues to pose significant computational challenges, particularly for large-scale instances. This study presents AILS-AHD (Adaptive Iterated Local Search with Automatic Heuristic Design), a novel approach that leverages Large Language Models (LLMs) to revolutionize CVRP solving. Our methodology integrates an evolutionary search framework with LLMs to dynamically generate and optimize ruin heuristics within the AILS method. Additionally, we introduce an LLM-based acceleration mechanism to enhance computational efficiency. Comprehensive experimental evaluations against state-of-the-art solvers, including AILS-II and HGS, demonstrate the superior performance of AILS-AHD across both moderate and large-scale instances. Notably, our approach establishes new best-known solutions for 8 out of 10 instances in the CVRPLib large-scale benchmark, underscoring the potential of LLM-driven heuristic design in advancing the field of vehicle routing optimization.

