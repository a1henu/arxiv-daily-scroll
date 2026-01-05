---
layout: default
title: LLM Agents for Combinatorial Efficient Frontiers: Investment Portfolio Optimization
---

# LLM Agents for Combinatorial Efficient Frontiers: Investment Portfolio Optimization
**arXiv**：[2601.00770v1](https://arxiv.org/abs/2601.00770) · [PDF](https://arxiv.org/pdf/2601.00770.pdf)  
**作者**：Simon Paquette-Greenbaum, Jiangbo Yu  

**一句话要点**：提出基于LLM智能体的组合优化框架，用于投资组合优化中的CCPO问题。

**关键词**：投资组合优化, 组合优化, 智能体框架, 混合整数二次规划, 启发式算法

## 3 点简述
- 核心问题：CCPO作为混合整数二次规划问题，精确求解困难，需依赖启发式算法。
- 方法要点：设计新型智能体框架，自动化复杂工作流和算法开发，探索多种架构。
- 实验或效果：在基准测试中匹配最先进算法，减轻工作负担，误差在可接受范围内。

## 摘要（原文）

> Investment portfolio optimization is a task conducted in all major financial institutions. The Cardinality Constrained Mean-Variance Portfolio Optimization (CCPO) problem formulation is ubiquitous for portfolio optimization. The challenge of this type of portfolio optimization, a mixed-integer quadratic programming (MIQP) problem, arises from the intractability of solutions from exact solvers, where heuristic algorithms are used to find approximate portfolio solutions. CCPO entails many laborious and complex workflows and also requires extensive effort pertaining to heuristic algorithm development, where the combination of pooled heuristic solutions results in improved efficient frontiers. Hence, common approaches are to develop many heuristic algorithms. Agentic frameworks emerge as a promising candidate for many problems within combinatorial optimization, as they have been shown to be equally efficient with regard to automating large workflows and have been shown to be excellent in terms of algorithm development, sometimes surpassing human-level performance. This study implements a novel agentic framework for the CCPO and explores several concrete architectures. In benchmark problems, the implemented agentic framework matches state-of-the-art algorithms. Furthermore, complex workflows and algorithm development efforts are alleviated, while in the worst case, lower but acceptable error is reported.

