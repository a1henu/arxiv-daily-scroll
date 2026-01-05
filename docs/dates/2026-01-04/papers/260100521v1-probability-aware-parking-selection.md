---
layout: default
title: Probability-Aware Parking Selection
---

# Probability-Aware Parking Selection
**arXiv**：[2601.00521v1](https://arxiv.org/abs/2601.00521) · [PDF](https://arxiv.org/pdf/2601.00521.pdf)  
**作者**：Cameron Hickert, Sirui Li, Zhengbing He, Cathy Wu  

**一句话要点**：提出概率感知停车选择框架，以解决停车导航中忽略停车搜索时间的问题。

**关键词**：停车导航, 概率感知选择, 动态编程, 停车可用性估计, 交通优化

## 3 点简述
- 核心问题：现有停车导航系统低估总行程时间，因未考虑停车位搜索时间，影响用户体验和交通排放。
- 方法要点：基于停车场可用性的概率信息，采用动态编程框架进行决策，优化停车位置选择。
- 实验或效果：使用西雅图真实数据验证，概率感知策略相比基线节省时间达66%，但比直达目的地估计仍多耗时。

## 摘要（原文）

> Current parking navigation systems often underestimate total travel time by failing to account for the time spent searching for a parking space, which significantly affects user experience, mode choice, congestion, and emissions. To address this issue, this paper introduces the probability-aware parking selection problem, which aims to direct drivers to the best parking location rather than straight to their destination. An adaptable dynamic programming framework is proposed for decision-making based on probabilistic information about parking availability at the parking lot level. Closed-form analysis determines when it is optimal to target a specific parking lot or explore alternatives, as well as the expected time cost. Sensitivity analysis and three illustrative cases are examined, demonstrating the model's ability to account for the dynamic nature of parking availability. Acknowledging the financial costs of permanent sensing infrastructure, the paper provides analytical and empirical assessments of errors incurred when leveraging stochastic observations to estimate parking availability. Experiments with real-world data from the US city of Seattle indicate this approach's viability, with mean absolute error decreasing from 7% to below 2% as observation frequency grows. In data-based simulations, probability-aware strategies demonstrate time savings up to 66% relative to probability-unaware baselines, yet still take up to 123% longer than direct-to-destination estimates.

