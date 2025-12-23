---
layout: default
title: From Points to Coalitions: Hierarchical Contrastive Shapley Values for Prioritizing Data Samples
---

# From Points to Coalitions: Hierarchical Contrastive Shapley Values for Prioritizing Data Samples
**arXiv**：[2512.19363v1](https://arxiv.org/abs/2512.19363) · [PDF](https://arxiv.org/pdf/2512.19363.pdf)  
**作者**：Canran Xiao, Jiabao Dou, Zhiming Lin, Zong Ke, Liwei Hou  

**一句话要点**：提出分层对比数据估值框架，以高效量化大规模异构几何结构数据集中样本价值。

**关键词**：数据估值, Shapley值, 对比学习, 分层聚类, 蒙特卡洛方法, 样本优先级

## 3 点简述
- 核心问题：传统Data-Shapley复杂度高且点式视角不适用于大规模异构几何结构数据集的价值量化。
- 方法要点：通过对比学习表示、分层聚类和局部蒙特卡洛博弈分配Shapley式收益，降低复杂度并提升边界样本价值。
- 实验或效果：在多个基准测试中提升准确率、大幅减少估值时间，支持数据增强过滤和流式更新等任务。

## 摘要（原文）

> How should we quantify the value of each training example when datasets are large, heterogeneous, and geometrically structured? Classical Data-Shapley answers in principle, but its O(n!) complexity and point-wise perspective are ill-suited to modern scales. We propose Hierarchical Contrastive Data Valuation (HCDV), a three-stage framework that (i) learns a contrastive, geometry-preserving representation, (ii) organizes the data into a balanced coarse-to-fine hierarchy of clusters, and (iii) assigns Shapley-style payoffs to coalitions via local Monte-Carlo games whose budgets are propagated downward. HCDV collapses the factorial burden to O(T sum_{l} K_{l}) = O(T K_max log n), rewards examples that sharpen decision boundaries, and regularizes outliers through curvature-based smoothness. We prove that HCDV approximately satisfies the four Shapley axioms with surplus loss O(eta log n), enjoys sub-Gaussian coalition deviation tilde O(1/sqrt{T}), and incurs at most k epsilon_infty regret for top-k selection. Experiments on four benchmarks--tabular, vision, streaming, and a 45M-sample CTR task--plus the OpenDataVal suite show that HCDV lifts accuracy by up to +5 pp, slashes valuation time by up to 100x, and directly supports tasks such as augmentation filtering, low-latency streaming updates, and fair marketplace payouts.

