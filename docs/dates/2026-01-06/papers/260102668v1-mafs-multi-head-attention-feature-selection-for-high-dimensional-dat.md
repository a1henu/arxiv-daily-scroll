---
layout: default
title: MAFS: Multi-head Attention Feature Selection for High-Dimensional Data via Deep Fusion of Filter Methods
---

# MAFS: Multi-head Attention Feature Selection for High-Dimensional Data via Deep Fusion of Filter Methods
**arXiv**：[2601.02668v1](https://arxiv.org/abs/2601.02668) · [PDF](https://arxiv.org/pdf/2601.02668.pdf)  
**作者**：Xiaoyan Sun, Qingyu Meng, Yalu Wen  

**一句话要点**：提出MAFS框架，结合统计先验与多头注意力，解决高维生物医学数据特征选择问题。

**关键词**：特征选择, 多头注意力, 高维数据, 生物医学数据分析, 深度学习融合

## 3 点简述
- 核心问题：现有方法难以兼顾高维数据的可扩展性、非线性关系建模与稳定性。
- 方法要点：集成过滤方法先验初始化，多头注意力并行捕获复杂依赖，重排序模块整合输出。
- 实验或效果：在模拟和真实数据集上，MAFS在覆盖率和稳定性方面优于现有方法。

## 摘要（原文）

> Feature selection is essential for high-dimensional biomedical data, enabling stronger predictive performance, reduced computational cost, and improved interpretability in precision medicine applications. Existing approaches face notable challenges. Filter methods are highly scalable but cannot capture complex relationships or eliminate redundancy. Deep learning-based approaches can model nonlinear patterns but often lack stability, interpretability, and efficiency at scale. Single-head attention improves interpretability but is limited in capturing multi-level dependencies and remains sensitive to initialization, reducing reproducibility. Most existing methods rarely combine statistical interpretability with the representational power of deep learning, particularly in ultra-high-dimensional settings. Here, we introduce MAFS (Multi-head Attention-based Feature Selection), a hybrid framework that integrates statistical priors with deep learning capabilities. MAFS begins with filter-based priors for stable initialization and guide learning. It then uses multi-head attention to examine features from multiple perspectives in parallel, capturing complex nonlinear relationships and interactions. Finally, a reordering module consolidates outputs across attention heads, resolving conflicts and minimizing information loss to generate robust and consistent feature rankings. This design combines statistical guidance with deep modeling capacity, yielding interpretable importance scores while maximizing retention of informative signals. Across simulated and real-world datasets, including cancer gene expression and Alzheimer's disease data, MAFS consistently achieves superior coverage and stability compared with existing filter-based and deep learning-based alternatives, offering a scalable, interpretable, and robust solution for feature selection in high-dimensional biomedical data.

