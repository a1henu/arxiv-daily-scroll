---
layout: default
title: TIDE: Tuning-Integrated Dynamic Evolution for LLM-Based Automated Heuristic Design
---

# TIDE: Tuning-Integrated Dynamic Evolution for LLM-Based Automated Heuristic Design
**arXiv**：[2601.21239v1](https://arxiv.org/abs/2601.21239) · [PDF](https://arxiv.org/pdf/2601.21239.pdf)  
**作者**：Chentong Chen, Mengyuan Zhong, Ye Fan, Jialong Shi, Jianyong Sun  

**一句话要点**：提出TIDE框架以解决基于LLM的自动启发式设计中结构与参数耦合问题

**关键词**：自动启发式设计, 大语言模型, 算法演化, 参数调优, 组合优化, 树相似编辑距离

## 3 点简述
- 核心问题：现有方法将算法演化视为单一文本生成任务，忽略离散结构与连续参数的耦合，导致算法丢弃和早熟收敛
- 方法要点：采用嵌套架构，外层并行岛屿模型用树相似编辑距离驱动结构多样性，内层结合LLM逻辑生成与差分变异算子进行参数调优
- 实验或效果：在九个组合优化问题中，TIDE发现的启发式在解质量上显著优于基线，同时提升搜索效率并降低计算成本

## 摘要（原文）

> Although Large Language Models have advanced Automated Heuristic Design, treating algorithm evolution as a monolithic text generation task overlooks the coupling between discrete algorithmic structures and continuous numerical parameters. Consequently, existing methods often discard promising algorithms due to uncalibrated constants and suffer from premature convergence resulting from simple similarity metrics. To address these limitations, we propose TIDE, a Tuning-Integrated Dynamic Evolution framework designed to decouple structural reasoning from parameter optimization. TIDE features a nested architecture where an outer parallel island model utilizes Tree Similarity Edit Distance to drive structural diversity, while an inner loop integrates LLM-based logic generation with a differential mutation operator for parameter tuning. Additionally, a UCB-based scheduler dynamically prioritizes high-yield prompt strategies to optimize resource allocation. Extensive experiments across nine combinatorial optimization problems demonstrate that TIDE discovers heuristics that significantly outperform state-of-the-art baselines in solution quality while achieving improved search efficiency and reduced computational costs.

