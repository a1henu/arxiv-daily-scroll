---
layout: default
title: Pareto-Optimal Anytime Algorithms via Bayesian Racing
---

# Pareto-Optimal Anytime Algorithms via Bayesian Racing
**arXiv**：[2603.08493v1](https://arxiv.org/abs/2603.08493) · [PDF](https://arxiv.org/pdf/2603.08493.pdf)  
**作者**：Jonathan Wurth, Helena Stegherr, Neele Kemper, Michael Heider, Jörg Hähner  

**一句话要点**：提出PolarBear框架，通过贝叶斯竞赛识别帕累托最优随时算法，解决算法比较中预算未知和归一化需求问题。

**关键词**：随时算法比较, 帕累托优化, 贝叶斯推理, 排名模型, 自适应采样, 算法选择

## 3 点简述
- 核心问题：算法比较时部署计算预算未知，现有方法需归一化或产生不稳定结论。
- 方法要点：基于时间点排名的帕累托优化，无需边界或归一化，使用贝叶斯推理自适应采样。
- 实验或效果：识别非支配算法集，支持下游算法选择，适应任意时间偏好和风险配置。

## 摘要（原文）

> Selecting an optimization algorithm requires comparing candidates across problem instances, but the computational budget for deployment is often unknown at benchmarking time. Current methods either collapse anytime performance into a scalar, require manual interpretation of plots, or produce conclusions that change when algorithms are added or removed. Moreover, methods based on raw objective values require normalization, which needs bounds or optima that are often unavailable and breaks coherent aggregation across instances. We propose a framework that formulates anytime algorithm comparison as Pareto optimization over time: an algorithm is non-dominated if no competitor beats it at every timepoint. By using rankings rather than objective values, our approach requires no bounds, no normalization, and aggregates coherently across arbitrary instance distributions without requiring known optima. We introduce PolarBear (Pareto-optimal anytime algorithms via Bayesian racing), a procedure that identifies the anytime Pareto set through adaptive sampling with calibrated uncertainty. Bayesian inference over a temporal Plackett-Luce ranking model provides posterior beliefs about pairwise dominance, enabling early elimination of confidently dominated algorithms. The output Pareto set together with the posterior supports downstream algorithm selection under arbitrary time preferences and risk profiles without additional experiments.

