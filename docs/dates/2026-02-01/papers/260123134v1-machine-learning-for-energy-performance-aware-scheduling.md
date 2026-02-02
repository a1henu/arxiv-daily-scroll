---
layout: default
title: Machine Learning for Energy-Performance-aware Scheduling
---

# Machine Learning for Energy-Performance-aware Scheduling
**arXiv**：[2601.23134v1](https://arxiv.org/abs/2601.23134) · [PDF](https://arxiv.org/pdf/2601.23134.pdf)  
**作者**：Zheyuan Hu, Yifei Shi  

**一句话要点**：提出基于贝叶斯优化的高斯过程框架，以自动化搜索异构多核架构上的最优调度配置。

**关键词**：贝叶斯优化, 高斯过程, 异构多核调度, 能量性能权衡, 敏感性分析, 帕累托前沿

## 3 点简述
- 核心问题：后登纳德时代嵌入式系统中，高维非光滑环境下能量效率与延迟的复杂权衡优化。
- 方法要点：使用高斯过程进行贝叶斯优化，近似能量与时间的帕累托前沿，并集成敏感性分析以增强模型可解释性。
- 实验或效果：通过比较不同协方差核（如Matérn与RBF），揭示驱动系统性能的主导硬件参数。

## 摘要（原文）

> In the post-Dennard era, optimizing embedded systems requires navigating complex trade-offs between energy efficiency and latency. Traditional heuristic tuning is often inefficient in such high-dimensional, non-smooth landscapes. In this work, we propose a Bayesian Optimization framework using Gaussian Processes to automate the search for optimal scheduling configurations on heterogeneous multi-core architectures. We explicitly address the multi-objective nature of the problem by approximating the Pareto Frontier between energy and time. Furthermore, by incorporating Sensitivity Analysis (fANOVA) and comparing different covariance kernels (e.g., Matérn vs. RBF), we provide physical interpretability to the black-box model, revealing the dominant hardware parameters driving system performance.

