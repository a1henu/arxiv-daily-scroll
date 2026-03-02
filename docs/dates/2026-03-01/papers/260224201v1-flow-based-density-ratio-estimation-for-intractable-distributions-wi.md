---
layout: default
title: Flow-Based Density Ratio Estimation for Intractable Distributions with Applications in Genomics
---

# Flow-Based Density Ratio Estimation for Intractable Distributions with Applications in Genomics
**arXiv**：[2602.24201v1](https://arxiv.org/abs/2602.24201) · [PDF](https://arxiv.org/pdf/2602.24201.pdf)  
**作者**：Egor Antipov, Alessandro Palma, Lorenzo Consoli, Stephan Günnemann, Andrea Dittadi, Fabian J. Theis  

**一句话要点**：提出基于流匹配的密度比估计方法，用于处理难处理分布，应用于单细胞基因组学分析。

**关键词**：密度比估计, 流匹配, 单细胞基因组学, 难处理分布, 条件感知建模

## 3 点简述
- 核心问题：估计难处理数据分布间的密度比，以比较不同条件下的样本似然。
- 方法要点：利用条件感知流匹配，通过单一动力学公式追踪生成轨迹中的密度比。
- 实验或效果：在模拟基准上表现竞争性，支持单细胞基因组学中的处理效应估计和批次校正评估。

## 摘要（原文）

> Estimating density ratios between pairs of intractable data distributions is a core problem in probabilistic modeling, enabling principled comparisons of sample likelihoods under different data-generating processes across conditions and covariates. While exact-likelihood models such as normalizing flows offer a promising approach to density ratio estimation, naive flow-based evaluations are computationally expensive, as they require simulating costly likelihood integrals for each distribution separately. In this work, we leverage condition-aware flow matching to derive a single dynamical formulation for tracking density ratios along generative trajectories. We demonstrate competitive performance on simulated benchmarks for closed-form ratio estimation, and show that our method supports versatile tasks in single-cell genomics data analysis, where likelihood-based comparisons of cellular states across experimental conditions enable treatment effect estimation and batch correction evaluation.

