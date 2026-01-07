---
layout: default
title: Dynamic Hyperparameter Importance for Efficient Multi-Objective Optimization
---

# Dynamic Hyperparameter Importance for Efficient Multi-Objective Optimization
**arXiv**：[2601.03166v1](https://arxiv.org/abs/2601.03166) · [PDF](https://arxiv.org/pdf/2601.03166.pdf)  
**作者**：Daphne Theodorakopoulos, Marcel Wever, Marius Lindauer  

**一句话要点**：提出动态超参数重要性方法以加速多目标优化搜索过程

**关键词**：多目标优化, 超参数重要性, 动态优化, 帕累托前沿, 机器学习模型选择

## 3 点简述
- 核心问题：现有多目标优化方法忽视超参数重要性随目标权衡变化，导致搜索效率低
- 方法要点：基于HyperSHAP动态计算超参数重要性，结合ParEGO权重调整配置空间，聚焦重要超参数
- 实验或效果：在PyMOO和YAHPO-Gym任务中验证，收敛速度和帕累托前沿质量优于基线

## 摘要（原文）

> Choosing a suitable ML model is a complex task that can depend on several objectives, e.g., accuracy, model size, fairness, inference time, or energy consumption. In practice, this requires trading off multiple, often competing, objectives through multi-objective optimization (MOO). However, existing MOO methods typically treat all hyperparameters as equally important, overlooking that hyperparameter importance (HPI) can vary significantly depending on the trade-off between objectives. We propose a novel dynamic optimization approach that prioritizes the most influential hyperparameters based on varying objective trade-offs during the search process, which accelerates empirical convergence and leads to better solutions. Building on prior work on HPI for MOO post-analysis, we now integrate HPI, calculated with HyperSHAP, into the optimization. For this, we leverage the objective weightings naturally produced by the MOO algorithm ParEGO and adapt the configuration space by fixing the unimportant hyperparameters, allowing the search to focus on the important ones. Eventually, we validate our method with diverse tasks from PyMOO and YAHPO-Gym. Empirical results demonstrate improvements in convergence speed and Pareto front quality compared to baselines.

