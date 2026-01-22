---
layout: default
title: Lineup Regularized Adjusted Plus-Minus (L-RAPM): Basketball Lineup Ratings with Informed Priors
---

# Lineup Regularized Adjusted Plus-Minus (L-RAPM): Basketball Lineup Ratings with Informed Priors
**arXiv**：[2601.15000v1](https://arxiv.org/abs/2601.15000) · [PDF](https://arxiv.org/pdf/2601.15000.pdf)  
**作者**：Christos Petridis, Konstantinos Pelechrinis  

**一句话要点**：提出L-RAPM方法，利用球员信息先验解决篮球阵容数据稀疏性问题。

**关键词**：篮球阵容分析, 数据稀疏性, 回归模型, 先验知识, 预测性能

## 3 点简述
- 核心问题：篮球阵容数据高度稀疏，导致统计噪声大、预测价值低。
- 方法要点：基于回归控制对手影响，并整合球员信息作为先验知识。
- 实验或效果：相比基线方法提升预测能力，尤其在小样本阵容中效果更显著。

## 摘要（原文）

> Identifying combinations of players (that is, lineups) in basketball - and other sports - that perform well when they play together is one of the most important tasks in sports analytics. One of the main challenges associated with this task is the frequent substitutions that occur during a game, which results in highly sparse data. In particular, a National Basketball Association (NBA) team will use more than 600 lineups during a season, which translates to an average lineup having seen the court in approximately 25-30 possessions. Inevitably, any statistics that one collects for these lineups are going to be noisy, with low predictive value. Yet, there is no existing work (in the public at least) that addresses this problem. In this work, we propose a regression-based approach that controls for the opposition faced by each lineup, while it also utilizes information about the players making up the lineups. Our experiments show that L-RAPM provides improved predictive power than the currently used baseline, and this improvement increases as the sample size for the lineups gets smaller.

