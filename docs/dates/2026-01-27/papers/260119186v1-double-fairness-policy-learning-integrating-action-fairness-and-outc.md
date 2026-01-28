---
layout: default
title: Double Fairness Policy Learning: Integrating Action Fairness and Outcome Fairness in Decision-making
---

# Double Fairness Policy Learning: Integrating Action Fairness and Outcome Fairness in Decision-making
**arXiv**：[2601.19186v1](https://arxiv.org/abs/2601.19186) · [PDF](https://arxiv.org/pdf/2601.19186.pdf)  
**作者**：Zeyu Bian, Lan Wang, Chengchun Shi, Zhengling Qi  

**一句话要点**：提出双公平性学习框架以在决策中平衡行动公平性、结果公平性和价值最大化。

**关键词**：政策学习, 公平性优化, 多目标优化, 决策公平, 机器学习公平

## 3 点简述
- 核心问题：政策学习中行动公平性与结果公平性存在差异，需同时优化。
- 方法要点：采用多目标优化和字典序加权切比雪夫法，理论保证遗憾界。
- 实验或效果：在保险和创业数据集上显著提升公平性，价值损失较小。

## 摘要（原文）

> Fairness is a central pillar of trustworthy machine learning, especially in domains where accuracy- or profit-driven optimization is insufficient. While most fairness research focuses on supervised learning, fairness in policy learning remains less explored. Because policy learning is interventional, it induces two distinct fairness targets: action fairness (equitable action assignments) and outcome fairness (equitable downstream consequences). Crucially, equalizing actions does not generally equalize outcomes when groups face different constraints or respond differently to the same action. We propose a novel double fairness learning (DFL) framework that explicitly manages the trade-off among three objectives: action fairness, outcome fairness, and value maximization. We integrate fairness directly into a multi-objective optimization problem for policy learning and employ a lexicographic weighted Tchebyshev method that recovers Pareto solutions beyond convex settings, with theoretical guarantees on the regret bounds. Our framework is flexible and accommodates various commonly used fairness notions. Extensive simulations demonstrate improved performance relative to competing methods. In applications to a motor third-party liability insurance dataset and an entrepreneurship training dataset, DFL substantially improves both action and outcome fairness while incurring only a modest reduction in overall value.

