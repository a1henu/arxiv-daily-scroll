---
layout: default
title: Generative Multi-Objective Bayesian Optimization with Scalable Batch Evaluations for Sample-Efficient De Novo Molecular Design
---

# Generative Multi-Objective Bayesian Optimization with Scalable Batch Evaluations for Sample-Efficient De Novo Molecular Design
**arXiv**：[2512.17659v1](https://arxiv.org/abs/2512.17659) · [PDF](https://arxiv.org/pdf/2512.17659.pdf)  
**作者**：Madhav R. Muthyala, Farshud Sorourifar, Tianhong Tan, You Peng, Joel A. Paulson  

**一句话要点**：提出生成-优化框架与qPMHI采集函数，用于高效多目标分子设计

**关键词**：多目标贝叶斯优化, 分子生成模型, 批量评估, 帕累托前沿, 有机阴极材料, 可持续能源存储

## 3 点简述
- 核心问题：分子设计需满足多冲突目标，化学空间巨大且模拟成本高
- 方法要点：采用模块化生成-优化框架，使用qPMHI实现可扩展批量选择
- 实验或效果：在合成基准和应用案例中优于现有方法，快速发现高性能有机阴极材料

## 摘要（原文）

> Designing molecules that must satisfy multiple, often conflicting objectives is a central challenge in molecular discovery. The enormous size of chemical space and the cost of high-fidelity simulations have driven the development of machine learning-guided strategies for accelerating design with limited data. Among these, Bayesian optimization (BO) offers a principled framework for sample-efficient search, while generative models provide a mechanism to propose novel, diverse candidates beyond fixed libraries. However, existing methods that couple the two often rely on continuous latent spaces, which introduces both architectural entanglement and scalability challenges. This work introduces an alternative, modular "generate-then-optimize" framework for de novo multi-objective molecular design/discovery. At each iteration, a generative model is used to construct a large, diverse pool of candidate molecules, after which a novel acquisition function, qPMHI (multi-point Probability of Maximum Hypervolume Improvement), is used to optimally select a batch of candidates most likely to induce the largest Pareto front expansion. The key insight is that qPMHI decomposes additively, enabling exact, scalable batch selection via only simple ranking of probabilities that can be easily estimated with Monte Carlo sampling. We benchmark the framework against state-of-the-art latent-space and discrete molecular optimization methods, demonstrating significant improvements across synthetic benchmarks and application-driven tasks. Specifically, in a case study related to sustainable energy storage, we show that our approach quickly uncovers novel, diverse, and high-performing organic (quinone-based) cathode materials for aqueous redox flow battery applications.

