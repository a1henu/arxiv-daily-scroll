---
layout: default
title: Stabilizing Test-Time Adaptation of High-Dimensional Simulation Surrogates via D-Optimal Statistics
---

# Stabilizing Test-Time Adaptation of High-Dimensional Simulation Surrogates via D-Optimal Statistics
**arXiv**：[2602.15820v1](https://arxiv.org/abs/2602.15820) · [PDF](https://arxiv.org/pdf/2602.15820.pdf)  
**作者**：Anna Zimmel, Paul Setinek, Gianluca Galletti, Johannes Brandstetter, Werner Zellinger  

**一句话要点**：提出基于D-最优统计的测试时适应框架，以稳定高维仿真代理模型的分布偏移问题。

**关键词**：测试时适应, 仿真代理模型, 高维回归, 分布偏移, D-最优统计, 生成设计优化

## 3 点简述
- 核心问题：仿真代理模型在训练与部署间的分布偏移导致性能下降，现有测试时适应方法对高维回归问题不稳定。
- 方法要点：利用D-最优统计存储最大化信息，实现稳定适应和参数选择，适用于高维非结构化回归。
- 实验或效果：在SIMSHIFT和EngiBench基准上验证，分布外性能提升达7%，计算成本可忽略。

## 摘要（原文）

> Machine learning surrogates are increasingly used in engineering to accelerate costly simulations, yet distribution shifts between training and deployment often cause severe performance degradation (e.g., unseen geometries or configurations). Test-Time Adaptation (TTA) can mitigate such shifts, but existing methods are largely developed for lower-dimensional classification with structured outputs and visually aligned input-output relationships, making them unstable for the high-dimensional, unstructured and regression problems common in simulation. We address this challenge by proposing a TTA framework based on storing maximally informative (D-optimal) statistics, which jointly enables stable adaptation and principled parameter selection at test time. When applied to pretrained simulation surrogates, our method yields up to 7% out-of-distribution improvements at negligible computational cost. To the best of our knowledge, this is the first systematic demonstration of effective TTA for high-dimensional simulation regression and generative design optimization, validated on the SIMSHIFT and EngiBench benchmarks.

