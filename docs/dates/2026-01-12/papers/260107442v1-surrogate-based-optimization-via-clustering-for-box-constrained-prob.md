---
layout: default
title: Surrogate-based Optimization via Clustering for Box-Constrained Problems
---

# Surrogate-based Optimization via Clustering for Box-Constrained Problems
**arXiv**：[2601.07442v1](https://arxiv.org/abs/2601.07442) · [PDF](https://arxiv.org/pdf/2601.07442.pdf)  
**作者**：Maaz Ahmad, Iftekhar A. Karimi  

**一句话要点**：提出基于聚类的代理优化框架SBOC，用于黑盒模拟和工业系统的全局优化。

**关键词**：代理优化, 全局优化, 聚类算法, 黑盒模拟, 高维优化

## 3 点简述
- 核心问题：大规模复杂系统（如多物理场黑盒模拟）的全局优化计算成本高且困难。
- 方法要点：结合代理模型和k-means聚类，识别未探索区域并在代理最优附近采样以提升效率。
- 实验或效果：在52个测试函数上验证，SBOC能以较低计算成本找到全局最小值，尤其适用于高维问题。

## 摘要（原文）

> Global optimization of large-scale, complex systems such as multi-physics black-box simulations and real-world industrial systems is important but challenging. This work presents a novel Surrogate-Based Optimization framework based on Clustering, SBOC for global optimization of such systems, which can be used with any surrogate modeling technique. At each iteration, it uses a single surrogate model for the entire domain, employs k-means clustering to identify unexplored domain, and exploits a local region around the surrogate optimum to potentially add three new sample points in the domain. SBOC has been tested against sixteen promising benchmarking algorithms using 52 analytical test functions of varying input dimensionalities and shape profiles. It successfully identified a global minimum for most test functions with substantially lower computational effort than other algorithms. It worked especially well on test functions with four or more input variables. It was also among the top six algorithms in approaching a global minimum closely. Overall, SBOC is a robust, reliable, and efficient algorithm for global optimization of box-constrained systems.

