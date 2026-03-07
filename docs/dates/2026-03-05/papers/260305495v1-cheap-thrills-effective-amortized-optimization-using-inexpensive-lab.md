---
layout: default
title: Cheap Thrills: Effective Amortized Optimization Using Inexpensive Labels
---

# Cheap Thrills: Effective Amortized Optimization Using Inexpensive Labels
**arXiv**：[2603.05495v1](https://arxiv.org/abs/2603.05495) · [PDF](https://arxiv.org/pdf/2603.05495.pdf)  
**作者**：Khai Nguyen, Petros Ellinas, Anvita Bhagavathula, Priya Donti  

**一句话要点**：提出三阶段框架以解决优化问题中机器学习代理模型对昂贵标签的依赖

**关键词**：优化问题求解, 机器学习代理模型, 监督预训练, 自监督学习, 廉价标签, 离线成本降低

## 3 点简述
- 核心问题：现有方法依赖高质量标签或面临优化困难，难以扩展优化问题求解
- 方法要点：先收集廉价不完美标签进行监督预训练，再通过自监督学习精炼模型
- 实验或效果：在非凸约束优化、电网操作等场景验证，提升收敛速度、准确性和可行性，离线成本降低高达59倍

## 摘要（原文）

> To scale the solution of optimization and simulation problems, prior work has explored machine-learning surrogates that inexpensively map problem parameters to corresponding solutions. Commonly used approaches, including supervised and self-supervised learning with either soft or hard feasibility enforcement, face inherent challenges such as reliance on expensive, high-quality labels or difficult optimization landscapes. To address their trade-offs, we propose a novel framework that first collects "cheap" imperfect labels, then performs supervised pretraining, and finally refines the model through self-supervised learning to improve overall performance. Our theoretical analysis and merit-based criterion show that labeled data need only place the model within a basin of attraction, confirming that only modest numbers of inexact labels and training epochs are required. We empirically validate our simple three-stage strategy across challenging domains, including nonconvex constrained optimization, power-grid operation, and stiff dynamical systems, and show that it yields faster convergence; improved accuracy, feasibility, and optimality; and up to 59x reductions in total offline cost.

