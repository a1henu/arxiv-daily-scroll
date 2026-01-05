---
layout: default
title: Cost Optimization in Production Line Using Genetic Algorithm
---

# Cost Optimization in Production Line Using Genetic Algorithm
**arXiv**：[2601.00689v1](https://arxiv.org/abs/2601.00689) · [PDF](https://arxiv.org/pdf/2601.00689.pdf)  
**作者**：Alireza Rezaee  

**一句话要点**：提出基于遗传算法的成本优化方法，用于生产线的任务调度问题。

**关键词**：遗传算法, 成本优化, 任务调度, 生产线, 染色体编码, 组合优化

## 3 点简述
- 核心问题：在生产线中，任务具有时长、成本和约束，需分配到无限工作站以最小化总成本。
- 方法要点：研究两种染色体编码策略，并调整遗传算子以保持可行性和优化成本。
- 实验或效果：任务编码在多种约束结构下表现更优，遗传算法优于梯度法和解析法。

## 摘要（原文）

> This paper presents a genetic algorithm (GA) approach to cost-optimal task scheduling in a production line. The system consists of a set of serial processing tasks, each with a given duration, unit execution cost, and precedence constraints, which must be assigned to an unlimited number of stations subject to a per-station duration bound. The objective is to minimize the total production cost, modeled as a station-wise function of task costs and the duration bound, while strictly satisfying all prerequisite and capacity constraints. Two chromosome encoding strategies are investigated: a station-based representation implemented using the JGAP library with SuperGene validity checks, and a task-based representation in which genes encode station assignments directly. For each encoding, standard GA operators (crossover, mutation, selection, and replacement) are adapted to preserve feasibility and drive the population toward lower-cost schedules. Experimental results on three classes of precedence structures-tightly coupled, loosely coupled, and uncoupled-demonstrate that the task-based encoding yields smoother convergence and more reliable cost minimization than the station-based encoding, particularly when the number of valid schedules is large. The study highlights the advantages of GA over gradient-based and analytical methods for combinatorial scheduling problems, especially in the presence of complex constraints and non-differentiable cost landscapes.

