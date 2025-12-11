---
layout: default
title: Semantic-Aware Cooperative Communication and Computation Framework in Vehicular Networks
---

# Semantic-Aware Cooperative Communication and Computation Framework in Vehicular Networks
**arXiv**：[2512.09621v1](https://arxiv.org/abs/2512.09621) · [PDF](https://arxiv.org/pdf/2512.09621.pdf)  
**作者**：Jingbo Zhang, Maoxin Ji, Qiong Wu, Pingyi Fan, Kezhi Wang, Wen Chen  

**一句话要点**：提出三方协同语义通信框架，以优化车联网中语义任务卸载的延迟与符号数。

**关键词**：语义通信, 车联网, 任务卸载, 多智能体强化学习, 边缘计算, 优化算法

## 3 点简述
- 核心问题：车联网中语义通信与边缘计算结合时，任务延迟和语义符号数的优化问题。
- 方法要点：采用混合整数非线性规划，分解为符号数优化（基于MAPPO-PDN）和卸载比例优化（基于线性规划）。
- 实验或效果：仿真显示该方案在性能上优于其他算法，具体提升未知。

## 摘要（原文）

> Semantic Communication (SC) combined with Vehicular edge computing (VEC) provides an efficient edge task processing paradigm for Internet of Vehicles (IoV). Focusing on highway scenarios, this paper proposes a Tripartite Cooperative Semantic Communication (TCSC) framework, which enables Vehicle Users (VUs) to perform semantic task offloading via Vehicle-to-Infrastructure (V2I) and Vehicle-to-Vehicle (V2V) communications. Considering task latency and the number of semantic symbols, the framework constructs a Mixed-Integer Nonlinear Programming (MINLP) problem, which is transformed into two subproblems. First, we innovatively propose a multi-agent proximal policy optimization task offloading optimization method based on parametric distribution noise (MAPPO-PDN) to solve the optimization problem of the number of semantic symbols; second, linear programming (LP) is used to solve offloading ratio. Simulations show that performance of this scheme is superior to that of other algorithms.

