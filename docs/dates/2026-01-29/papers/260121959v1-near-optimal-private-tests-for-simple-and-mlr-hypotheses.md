---
layout: default
title: Near-Optimal Private Tests for Simple and MLR Hypotheses
---

# Near-Optimal Private Tests for Simple and MLR Hypotheses
**arXiv**：[2601.21959v1](https://arxiv.org/abs/2601.21959) · [PDF](https://arxiv.org/pdf/2601.21959.pdf)  
**作者**：Yu-Wei Chen, Raghu Pasupathy, Jordan Awan  

**一句话要点**：提出基于高斯差分隐私的近最优测试方法，用于简单和单调似然比假设检验。

**关键词**：差分隐私, 假设检验, 单调似然比, 私有均值估计, 统计功效, 高斯机制

## 3 点简述
- 核心问题：在差分隐私下设计高效假设检验，平衡隐私保护与统计功效。
- 方法要点：使用数据驱动截断的私有均值估计器，匹配私有极小极大风险率。
- 实验或效果：数值实验显示优于其他DP方法，接近非私有最优测试功效。

## 摘要（原文）

> We develop a near-optimal testing procedure under the framework of Gaussian differential privacy for simple as well as one- and two-sided tests under monotone likelihood ratio conditions. Our mechanism is based on a private mean estimator with data-driven clamping bounds, whose population risk matches the private minimax rate up to logarithmic factors. Using this estimator, we construct private test statistics that achieve the same asymptotic relative efficiency as the non-private, most powerful tests while maintaining conservative type I error control. In addition to our theoretical results, our numerical experiments show that our private tests outperform competing DP methods and offer comparable power to the non-private most powerful tests, even at moderately small sample sizes and privacy loss budgets.

