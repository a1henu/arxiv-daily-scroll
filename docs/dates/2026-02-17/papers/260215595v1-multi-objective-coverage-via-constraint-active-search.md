---
layout: default
title: Multi-Objective Coverage via Constraint Active Search
---

# Multi-Objective Coverage via Constraint Active Search
**arXiv**：[2602.15595v1](https://arxiv.org/abs/2602.15595) · [PDF](https://arxiv.org/pdf/2602.15595.pdf)  
**作者**：Zakaria Shams Siam, Xuefeng Liu, Chong Liu  

**一句话要点**：提出MOC-CAS算法以解决多目标覆盖问题，加速药物发现等科学探索。

**关键词**：多目标覆盖, 主动搜索, 高斯过程, 药物发现, 材料设计, 约束优化

## 3 点简述
- 核心问题：多目标覆盖（MOC）旨在从可行多目标空间中选取少量代表性样本，以加速评估过程。
- 方法要点：基于高斯过程后验预测，采用上置信界获取函数和光滑松弛优化，高效搜索乐观样本。
- 实验或效果：在SARS-CoV-2和癌症蛋白质数据集上，MOC-CAS在五个基于SMILES的目标上优于基线方法。

## 摘要（原文）

> In this paper, we formulate the new multi-objective coverage (MOC) problem where our goal is to identify a small set of representative samples whose predicted outcomes broadly cover the feasible multi-objective space. This problem is of great importance in many critical real-world applications, e.g., drug discovery and materials design, as this representative set can be evaluated much faster than the whole feasible set, thus significantly accelerating the scientific discovery process. Existing works cannot be directly applied as they either focus on sample space coverage or multi-objective optimization that targets the Pareto front. However, chemically diverse samples often yield identical objective profiles, and safety constraints are usually defined on the objectives. To solve this MOC problem, we propose a novel search algorithm, MOC-CAS, which employs an upper confidence bound-based acquisition function to select optimistic samples guided by Gaussian process posterior predictions. For enabling efficient optimization, we develop a smoothed relaxation of the hard feasibility test and derive an approximate optimizer. Compared to the competitive baselines, we show that our MOC-CAS empirically achieves superior performances across large-scale protein-target datasets for SARS-CoV-2 and cancer, each assessed on five objectives derived from SMILES-based features.

