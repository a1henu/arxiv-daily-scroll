---
layout: default
title: Active Transfer Bagging: A New Approach for Accelerated Active Learning Acquisition of Data by Combined Transfer Learning and Bagging Based Models
---

# Active Transfer Bagging: A New Approach for Accelerated Active Learning Acquisition of Data by Combined Transfer Learning and Bagging Based Models
**arXiv**：[2602.02415v1](https://arxiv.org/abs/2602.02415) · [PDF](https://arxiv.org/pdf/2602.02415.pdf)  
**作者**：Vivienne Pelletier, Daniel J. Rivera, Obinna Nwokonkwo, Steven A. Wilson, Christopher L. Muhich  

**一句话要点**：提出ATBagging方法，结合迁移学习和装袋模型，以加速主动学习的数据获取。

**关键词**：主动学习, 迁移学习, 装袋模型, 种子集选择, 信息增益, 特征多样性

## 3 点简述
- 核心问题：主动学习早期性能受随机种子集限制，标注成本高。
- 方法要点：基于贝叶斯装袋模型估计信息量，使用DPP确保特征空间多样性。
- 实验效果：在四个真实数据集上，ATBagging提升早期主动学习性能，尤其在低数据场景。

## 摘要（原文）

> Modern machine learning has achieved remarkable success on many problems, but this success often depends on the existence of large, labeled datasets. While active learning can dramatically reduce labeling cost when annotations are expensive, early performance is frequently dominated by the initial seed set, typically chosen at random. In many applications, however, related or approximate datasets are readily available and can be leveraged to construct a better seed set. We introduce a new method for selecting the seed data set for active learning, Active-Transfer Bagging (ATBagging). ATBagging estimates the informativeness of candidate data point from a Bayesian interpretation of bagged ensemble models by comparing in-bag and out-of-bag predictive distributions from the labeled dataset, yielding an information-gain proxy. To avoid redundant selections, we impose feature-space diversity by sampling a determinantal point process (DPP) whose kernel uses Random Fourier Features and a quality-diversity factorization that incorporates the informativeness scores. This same blended method is used for selection of new data points to collect during the active learning phase. We evaluate ATBagging on four real-world datasets covering both target-transfer and feature-shift scenarios (QM9, ERA5, Forbes 2000, and Beijing PM2.5). Across seed sizes nseed = 10-100, ATBagging improves or ties early active learning and increases area under the learning-curve relative to alternative seed subset selection methodologies in almost all cases, with strongest benefits in low-data regimes. Thus, ATBagging provides a low-cost, high reward means to initiating active learning-based data collection.

