---
layout: default
title: A Dynamic Framework for Grid Adaptation in Kolmogorov-Arnold Networks
---

# A Dynamic Framework for Grid Adaptation in Kolmogorov-Arnold Networks
**arXiv**：[2601.18672v1](https://arxiv.org/abs/2601.18672) · [PDF](https://arxiv.org/pdf/2601.18672.pdf)  
**作者**：Spyros Rigas, Thanasis Papaioannou, Panagiotis Trakadas, Georgios Alexandridis  

**一句话要点**：提出基于曲率的动态网格适应框架，以提升Kolmogorov-Arnold Networks在科学机器学习中的性能。

**关键词**：Kolmogorov-Arnold Networks, 网格适应, 曲率驱动, 科学机器学习, 密度估计, 偏微分方程求解

## 3 点简述
- 现有KAN网格适应策略仅依赖输入数据密度，忽略目标函数几何复杂性或训练动态。
- 提出通用框架，将节点分配视为重要性密度函数控制的密度估计任务，引入曲率驱动适应策略。
- 在合成函数拟合、Feynman数据集回归和Helmholtz PDE基准上验证，平均相对误差显著降低，统计显著。

## 摘要（原文）

> Kolmogorov-Arnold Networks (KANs) have recently demonstrated promising potential in scientific machine learning, partly due to their capacity for grid adaptation during training. However, existing adaptation strategies rely solely on input data density, failing to account for the geometric complexity of the target function or metrics calculated during network training. In this work, we propose a generalized framework that treats knot allocation as a density estimation task governed by Importance Density Functions (IDFs), allowing training dynamics to determine grid resolution. We introduce a curvature-based adaptation strategy and evaluate it across synthetic function fitting, regression on a subset of the Feynman dataset and different instances of the Helmholtz PDE, demonstrating that it significantly outperforms the standard input-based baseline. Specifically, our method yields average relative error reductions of 25.3% on synthetic functions, 9.4% on the Feynman dataset, and 23.3% on the PDE benchmark. Statistical significance is confirmed via Wilcoxon signed-rank tests, establishing curvature-based adaptation as a robust and computationally efficient alternative for KAN training.

