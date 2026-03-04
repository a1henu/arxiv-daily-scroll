---
layout: default
title: Learning Demographic-Conditioned Mobility Trajectories with Aggregate Supervision
---

# Learning Demographic-Conditioned Mobility Trajectories with Aggregate Supervision
**arXiv**：[2603.03275v1](https://arxiv.org/abs/2603.03275) · [PDF](https://arxiv.org/pdf/2603.03275.pdf)  
**作者**：Jessie Z. Li, Zhiqing Hong, Toru Shirakawa, Serina Chang  

**一句话要点**：提出ATLAS方法，利用聚合监督生成人口统计条件化的移动轨迹，以解决轨迹数据缺乏人口标签的异质性建模问题。

**关键词**：移动轨迹生成, 弱监督学习, 人口统计建模, 聚合监督, 异质性分析, 轨迹模拟

## 3 点简述
- 核心问题：现有轨迹生成模型难以捕捉不同人口群体的移动异质性，因为多数轨迹数据集缺乏人口统计标签。
- 方法要点：ATLAS采用弱监督方法，仅使用无标签个体轨迹、区域级聚合移动特征和人口构成数据，训练条件化轨迹生成器。
- 实验或效果：在真实带标签数据上，ATLAS显著提升人口真实性，JSD降低12%–69%，接近强监督训练效果。

## 摘要（原文）

> Human mobility trajectories are widely studied in public health and social science, where different demographic groups exhibit significantly different mobility patterns. However, existing trajectory generation models rarely capture this heterogeneity because most trajectory datasets lack demographic labels. To address this gap in data, we propose ATLAS, a weakly supervised approach for demographic-conditioned trajectory generation using only (i) individual trajectories without demographic labels, (ii) region-level aggregated mobility features, and (iii) region-level demographic compositions from census data. ATLAS trains a trajectory generator and fine-tunes it so that simulated mobility matches observed regional aggregates while conditioning on demographics. Experiments on real trajectory data with demographic labels show that ATLAS substantially improves demographic realism over baselines (JSD $\downarrow$ 12%--69%) and closes much of the gap to strongly supervised training. We further develop theoretical analyses for when and why ATLAS works, identifying key factors including demographic diversity across regions and the informativeness of the aggregate feature, paired with experiments demonstrating the practical implications of our theory. We release our code at https://github.com/schang-lab/ATLAS.

