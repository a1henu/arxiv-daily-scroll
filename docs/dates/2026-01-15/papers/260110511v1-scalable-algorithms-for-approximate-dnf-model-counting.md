---
layout: default
title: Scalable Algorithms for Approximate DNF Model Counting
---

# Scalable Algorithms for Approximate DNF Model Counting
**arXiv**：[2601.10511v1](https://arxiv.org/abs/2601.10511) · [PDF](https://arxiv.org/pdf/2601.10511.pdf)  
**作者**：Paul Burkhardt, David G. Harris, Kevin T Schmitt  

**一句话要点**：提出自适应蒙特卡洛算法以高效近似DNF模型计数，适用于概率推理等场景。

**关键词**：DNF模型计数, 近似算法, 蒙特卡洛方法, 概率推理, 自适应停止规则

## 3 点简述
- 核心问题：DNF公式模型计数在概率推理中关键但计算困难，需高效近似算法。
- 方法要点：新蒙特卡洛方法结合自适应停止规则和短路评估，证明PAC界且渐近更高效。
- 实验或效果：实验显示性能优于先前算法数个数量级，可扩展至百万变量问题。

## 摘要（原文）

> Model counting of Disjunctive Normal Form (DNF) formulas is a critical problem in applications such as probabilistic inference and network reliability. For example, it is often used for query evaluation in probabilistic databases. Due to the computational intractability of exact DNF counting, there has been a line of research into a variety of approximation algorithms. These include Monte Carlo approaches such as the classical algorithms of Karp, Luby, and Madras (1989), as well as methods based on hashing (Soos et al. 2023), and heuristic approximations based on Neural Nets (Abboud, Ceylan, and Lukasiewicz 2020).
>   We develop a new Monte Carlo approach with an adaptive stopping rule and short-circuit formula evaluation. We prove it achieves Probably Approximately Correct (PAC) learning bounds and is asymptotically more efficient than the previous methods. We also show experimentally that it out-performs prior algorithms by orders of magnitude, and can scale to much larger problems with millions of variables.

