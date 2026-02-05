---
layout: default
title: Improved Dimension Dependence for Bandit Convex Optimization with Gradient Variations
---

# Improved Dimension Dependence for Bandit Convex Optimization with Gradient Variations
**arXiv**：[2602.04761v1](https://arxiv.org/abs/2602.04761) · [PDF](https://arxiv.org/pdf/2602.04761.pdf)  
**作者**：Hang Yu, Yu-Hu Yan, Peng Zhao  

**一句话要点**：改进非连续梯度变差分析以提升带反馈的强盗凸优化维度依赖

**关键词**：强盗凸优化, 梯度变差, 两点反馈, 非连续梯度分析, 维度依赖改进, 遗憾最小化

## 3 点简述
- 研究带反馈的强盗凸优化中梯度变差问题，聚焦两点反馈场景
- 通过精炼非连续梯度变差分析，改进凸和强凸函数的维度依赖
- 验证方法在动态/通用遗憾最小化和强盗游戏中的有效性

## 摘要（原文）

> Gradient-variation online learning has drawn increasing attention due to its deep connections to game theory, optimization, etc. It has been studied extensively in the full-information setting, but is underexplored with bandit feedback. In this work, we focus on gradient variation in Bandit Convex Optimization (BCO) with two-point feedback. By proposing a refined analysis on the non-consecutive gradient variation, a fundamental quantity in gradient variation with bandits, we improve the dimension dependence for both convex and strongly convex functions compared with the best known results (Chiang et al., 2013). Our improved analysis for the non-consecutive gradient variation also implies other favorable problem-dependent guarantees, such as gradient-variance and small-loss regrets. Beyond the two-point setup, we demonstrate the versatility of our technique by achieving the first gradient-variation bound for one-point bandit linear optimization over hyper-rectangular domains. Finally, we validate the effectiveness of our results in more challenging tasks such as dynamic/universal regret minimization and bandit games, establishing the first gradient-variation dynamic and universal regret bounds for two-point BCO and fast convergence rates in bandit games.

