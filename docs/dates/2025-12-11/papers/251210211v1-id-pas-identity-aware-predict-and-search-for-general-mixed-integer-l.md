---
layout: default
title: ID-PaS : Identity-Aware Predict-and-Search for General Mixed-Integer Linear Programs
---

# ID-PaS : Identity-Aware Predict-and-Search for General Mixed-Integer Linear Programs
**arXiv**：[2512.10211v1](https://arxiv.org/abs/2512.10211) · [PDF](https://arxiv.org/pdf/2512.10211.pdf)  
**作者**：Junyang Cai, El Mehdi Er Raqabi, Pascal Van Hentenryck, Bistra Dilkina  

**一句话要点**：提出ID-PaS身份感知学习框架，以扩展预测-搜索方法至参数化混合整数线性规划问题。

**关键词**：混合整数线性规划, 预测-搜索方法, 机器学习集成, 参数化优化, 身份感知学习

## 3 点简述
- 核心问题：现有预测-搜索方法局限于二元问题，且忽略实际中常见的固定变量。
- 方法要点：引入身份感知学习，使机器学习模型能更有效处理异构变量。
- 实验或效果：在多个现实大规模问题上，ID-PaS性能优于Gurobi和PaS。

## 摘要（原文）

> Mixed-Integer Linear Programs (MIPs) are powerful and flexible tools for modeling a wide range of real-world combinatorial optimization problems. Predict-and-Search methods operate by using a predictive model to estimate promising variable assignments and then guiding a search procedure toward high-quality solutions. Recent research has demonstrated that incorporating machine learning (ML) into the Predict-and-Search framework significantly enhances its performance. Still, it is restricted to binary problems and overlooks the presence of fixed variables that commonly arise in practical settings. This work extends the Predict-and-Search (PaS) framework to parametric MIPs and introduces ID-PaS, an identity-aware learning framework that enables the ML model to handle heterogeneous variables more effectively. Experiments on several real-world large-scale problems demonstrate that ID-PaS consistently achieves superior performance compared to the state-of-the-art solver Gurobi and PaS.

