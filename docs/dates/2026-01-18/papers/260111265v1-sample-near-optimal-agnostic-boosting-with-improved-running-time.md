---
layout: default
title: Sample-Near-Optimal Agnostic Boosting with Improved Running Time
---

# Sample-Near-Optimal Agnostic Boosting with Improved Running Time
**arXiv**：[2601.11265v1](https://arxiv.org/abs/2601.11265) · [PDF](https://arxiv.org/pdf/2601.11265.pdf)  
**作者**：Arthur da Cunha, Miakel Møller Høgsgaard, Andrea Paudice  

**一句话要点**：提出首个样本复杂度接近最优且运行时间多项式的不可知提升算法

**关键词**：不可知提升, 样本复杂度, 多项式时间算法, 机器学习理论, 提升方法

## 3 点简述
- 核心问题：不可知提升中样本复杂度已近解决，但现有算法运行时间指数级
- 方法要点：设计新算法，在固定其他参数时，运行时间随样本大小多项式增长
- 实验或效果：未知

## 摘要（原文）

> Boosting is a powerful method that turns weak learners, which perform only slightly better than random guessing, into strong learners with high accuracy. While boosting is well understood in the classic setting, it is less so in the agnostic case, where no assumptions are made about the data. Indeed, only recently was the sample complexity of agnostic boosting nearly settled arXiv:2503.09384, but the known algorithm achieving this bound has exponential running time. In this work, we propose the first agnostic boosting algorithm with near-optimal sample complexity, running in time polynomial in the sample size when considering the other parameters of the problem fixed.

