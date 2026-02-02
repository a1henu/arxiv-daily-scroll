---
layout: default
title: OneFlowSBI: One Model, Many Queries for Simulation-Based Inference
---

# OneFlowSBI: One Model, Many Queries for Simulation-Based Inference
**arXiv**：[2601.22951v1](https://arxiv.org/abs/2601.22951) · [PDF](https://arxiv.org/pdf/2601.22951.pdf)  
**作者**：Mayank Nautiyal, Li Ju, Melker Ernfors, Klara Hagland, Ville Holma, Maximilian Werkö Söderholm, Andreas Hellander, Prashant Singh  

**一句话要点**：提出OneFlowSBI框架，通过单一流匹配模型支持多种仿真推断任务

**关键词**：仿真推断, 流匹配模型, 多任务学习, 后验采样, 条件分布估计, 逆问题求解

## 3 点简述
- 核心问题：仿真推断中需为不同任务训练专门模型，效率低且不灵活
- 方法要点：训练时使用查询感知掩码分布，学习参数与观测的联合分布，实现多任务推断
- 实验或效果：在十项基准和两项高维实际逆问题上，性能媲美先进方法，采样高效且鲁棒

## 摘要（原文）

> We introduce \textit{OneFlowSBI}, a unified framework for simulation-based inference that learns a single flow-matching generative model over the joint distribution of parameters and observations. Leveraging a query-aware masking distribution during training, the same model supports multiple inference tasks, including posterior sampling, likelihood estimation, and arbitrary conditional distributions, without task-specific retraining. We evaluate \textit{OneFlowSBI} on ten benchmark inference problems and two high-dimensional real-world inverse problems across multiple simulation budgets. \textit{OneFlowSBI} is shown to deliver competitive performance against state-of-the-art generalized inference solvers and specialized posterior estimators, while enabling efficient sampling with few ODE integration steps and remaining robust under noisy and partially observed data.

