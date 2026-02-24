---
layout: default
title: AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization
---

# AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization
**arXiv**：[2602.20133v1](https://arxiv.org/abs/2602.20133) · [PDF](https://arxiv.org/pdf/2602.20133.pdf)  
**作者**：Mert Cemri, Shubham Agrawal, Akshat Gupta, Shu Liu, Audrey Cheng, Qiuyang Mang, Ashwin Naren, Lutfi Eren Erdogan, Koushik Sen, Matei Zaharia, Alex Dimakis, Ion Stoica  

**一句话要点**：提出AdaEvolve框架，通过自适应优化解决LLM驱动进化中静态调度导致的资源浪费问题。

**关键词**：LLM驱动优化, 自适应进化算法, 零阶优化, 资源调度, 程序生成, 开放问题求解

## 3 点简述
- 核心问题：LLM驱动的进化搜索使用静态调度，无法适应搜索过程的非平稳动态，造成计算资源浪费。
- 方法要点：基于累积改进信号，实现局部适应、全局适应和元指导三层自适应优化，动态调整探索强度和资源分配。
- 实验或效果：在185个开放优化问题上，AdaEvolve一致优于开源基线，涵盖组合、系统优化和算法设计问题。

## 摘要（原文）

> The paradigm of automated program generation is shifting from one-shot generation to inference-time search, where Large Language Models (LLMs) function as semantic mutation operators within evolutionary loops. While effective, these systems are currently governed by static schedules that fail to account for the non-stationary dynamics of the search process. This rigidity results in substantial computational waste, as resources are indiscriminately allocated to stagnating populations while promising frontiers remain under-exploited. We introduce AdaEvolve, a framework that reformulates LLM-driven evolution as a hierarchical adaptive optimization problem. AdaEvolve uses an "accumulated improvement signal" to unify decisions across three levels: Local Adaptation, which dynamically modulates the exploration intensity within a population of solution candidates; Global Adaptation, which routes the global resource budget via bandit-based scheduling across different solution candidate populations; and Meta-Guidance which generates novel solution tactics based on the previously generated solutions and their corresponding improvements when the progress stalls. We demonstrate that AdaEvolve consistently outperforms the open-sourced baselines across 185 different open-ended optimization problems including combinatorial, systems optimization and algorithm design problems.

