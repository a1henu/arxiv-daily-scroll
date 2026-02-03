---
layout: default
title: Efficiently Solving Mixed-Hierarchy Games with Quasi-Policy Approximations
---

# Efficiently Solving Mixed-Hierarchy Games with Quasi-Policy Approximations
**arXiv**：[2602.01568v1](https://arxiv.org/abs/2602.01568) · [PDF](https://arxiv.org/pdf/2602.01568.pdf)  
**作者**：Hamzah Khan, Dong Ho Lee, Jingqi Li, Tianyu Qiu, Christian Ellis, Jesse Milzman, Wesley Suttle, David Fridovich-Keil  

**一句话要点**：提出准策略近似与不精确牛顿法以高效求解森林结构混合层次博弈

**关键词**：混合层次博弈, 准策略近似, 不精确牛顿法, 多机器人协调, KKT条件, Julia库

## 3 点简述
- 研究多机器人协调中的混合层次博弈，结合同时与层级决策，现有求解器难以处理
- 引入准策略近似消除高阶策略导数，开发不精确牛顿法求解近似KKT系统
- 证明算法在非二次目标和非线性约束下的局部指数收敛，实验展示实时收敛性能

## 摘要（原文）

> Multi-robot coordination often exhibits hierarchical structure, with some robots' decisions depending on the planned behaviors of others. While game theory provides a principled framework for such interactions, existing solvers struggle to handle mixed information structures that combine simultaneous (Nash) and hierarchical (Stackelberg) decision-making. We study N-robot forest-structured mixed-hierarchy games, in which each robot acts as a Stackelberg leader over its subtree while robots in different branches interact via Nash equilibria. We derive the Karush-Kuhn-Tucker (KKT) first-order optimality conditions for this class of games and show that they involve increasingly high-order derivatives of robots' best-response policies as the hierarchy depth grows, rendering a direct solution intractable. To overcome this challenge, we introduce a quasi-policy approximation that removes higher-order policy derivatives and develop an inexact Newton method for efficiently solving the resulting approximated KKT systems. We prove local exponential convergence of the proposed algorithm for games with non-quadratic objectives and nonlinear constraints. The approach is implemented in a highly optimized Julia library (MixedHierarchyGames.jl) and evaluated in simulated experiments, demonstrating real-time convergence for complex mixed-hierarchy information structures.

