---
layout: default
title: Differentiated Pickup Point Offering for Emission Reduction in Last-Mile Delivery
---

# Differentiated Pickup Point Offering for Emission Reduction in Last-Mile Delivery
**arXiv**：[2601.14196v1](https://arxiv.org/abs/2601.14196) · [PDF](https://arxiv.org/pdf/2601.14196.pdf)  
**作者**：Albina Galiullina, Wouter van Heeswijk, Tom van Woensel  

**一句话要点**：提出差异化取货点推荐策略以动态减少最后一公里配送中的碳排放

**关键词**：最后一公里配送, 碳排放优化, 强化学习, 动态决策, 取货点推荐, 可持续物流

## 3 点简述
- 核心问题：传统取货点虽能减少配送车排放，但客户驾车取货可能抵消环保效益。
- 方法要点：采用强化学习动态推荐单个取货点，考虑空间关系和未来路线整合。
- 实验或效果：在密集城市环境中，该策略总碳排放最多减少9%，平均优于无限制选择或最近点分配。

## 摘要（原文）

> Pickup points are widely recognized as a sustainable alternative to home delivery, as consolidating orders at pickup locations can shorten delivery routes and improve first-attempt success rates. However, these benefits may be negated when customers drive to pick up their orders. This study proposes a Differentiated Pickup Point Offering (DPO) policy that aims to jointly reduce emissions from delivery truck routes and customer travel. Under DPO, each arriving customer is offered a single recommended pickup point, rather than an unrestricted choice among all locations, while retaining the option of home delivery. We study this problem in a dynamic and stochastic setting, where the pickup point offered to each customer depends on previously realized customer locations and delivery choices. To design effective DPO policies, we adopt a reinforcement learning-based approach that accounts for spatial relationships between customers and pickup points and their implications for future route consolidation. Computational experiments show that differentiated pickup point offerings can substantially reduce total carbon emissions. The proposed policies reduce total emissions by up to 9% relative to home-only delivery and by 2% on average compared with alternative policies, including unrestricted pickup point choice and nearest pickup point assignment. Differentiated offerings are particularly effective in dense urban settings with many pickup points and short inter-location distances. Moreover, explicitly accounting for the dynamic nature of customer arrivals and choices is especially important when customers are less inclined to choose pickup point delivery over home delivery.

