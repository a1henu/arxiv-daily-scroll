---
layout: default
title: QuantGraph: A Receding-Horizon Quantum Graph Solver
---

# QuantGraph: A Receding-Horizon Quantum Graph Solver
**arXiv**：[2512.15476v1](https://arxiv.org/abs/2512.15476) · [PDF](https://arxiv.org/pdf/2512.15476.pdf)  
**作者**：Pranav Vaidhyanathan, Aristotelis Papatheodorou, David R. M. Arvidsson-Shukur, Mark T. Mitchison, Natalia Ares, Ioannis Havoutis  

**一句话要点**：提出QuantGraph量子增强框架，通过两阶段搜索解决图优化问题，提升精度与效率。

**关键词**：量子图优化, Grover搜索算法, 模型预测控制, 动态规划, 两阶段框架

## 3 点简述
- 核心问题：动态规划在图优化中随问题规模扩展性差，计算复杂度高。
- 方法要点：采用局部与全局两阶段量子搜索，结合Grover算法和模型预测控制，减少搜索空间。
- 实验或效果：在固定查询预算下，控制离散化精度提升2倍，搜索空间减少达60%。

## 摘要（原文）

> Dynamic programming is a cornerstone of graph-based optimization. While effective, it scales unfavorably with problem size. In this work, we present QuantGraph, a two-stage quantum-enhanced framework that casts local and global graph-optimization problems as quantum searches over discrete trajectory spaces. The solver is designed to operate efficiently by first finding a sequence of locally optimal transitions in the graph (local stage), without considering full trajectories. The accumulated cost of these transitions acts as a threshold that prunes the search space (up to 60% reduction for certain examples). The subsequent global stage, based on this threshold, refines the solution. Both stages utilize variants of the Grover-adaptive-search algorithm. To achieve scalability and robustness, we draw on principles from control theory and embed QuantGraph's global stage within a receding-horizon model-predictive-control scheme. This classical layer stabilizes and guides the quantum search, improving precision and reducing computational burden. In practice, the resulting closed-loop system exhibits robust behavior and lower overall complexity. Notably, for a fixed query budget, QuantGraph attains a 2x increase in control-discretization precision while still benefiting from Grover-search's inherent quadratic speedup compared to classical methods.

