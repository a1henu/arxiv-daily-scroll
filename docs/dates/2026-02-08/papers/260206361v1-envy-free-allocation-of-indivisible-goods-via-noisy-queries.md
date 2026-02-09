---
layout: default
title: Envy-Free Allocation of Indivisible Goods via Noisy Queries
---

# Envy-Free Allocation of Indivisible Goods via Noisy Queries
**arXiv**：[2602.06361v1](https://arxiv.org/abs/2602.06361) · [PDF](https://arxiv.org/pdf/2602.06361.pdf)  
**作者**：Zihan Li, Yan Hao Ling, Jonathan Scarlett, Warut Suksompong  

**一句话要点**：提出基于噪声查询的不可分物品公平分配方法，在双代理高斯噪声场景下分析查询复杂度。

**关键词**：公平分配, 噪声查询, 查询复杂度, 无嫉妒分配, 高斯噪声, 不可分物品

## 3 点简述
- 研究不可分物品公平分配问题，代理估值仅能通过噪声查询间接获取。
- 在双代理高斯噪声和估值有界设定下，推导出寻找无嫉妒分配的查询次数上下界。
- 上界基于非自适应查询和阈值分配算法，下界适用于自适应查询和任意计算时间。

## 摘要（原文）

> We introduce a problem of fairly allocating indivisible goods (items) in which the agents' valuations cannot be observed directly, but instead can only be accessed via noisy queries. In the two-agent setting with Gaussian noise and bounded valuations, we derive upper and lower bounds on the required number of queries for finding an envy-free allocation in terms of the number of items, $m$, and the negative-envy of the optimal allocation, $Δ$. In particular, when $Δ$ is not too small (namely, $Δ\gg m^{1/4}$), we establish that the optimal number of queries scales as $\frac{\sqrt m }{(Δ/ m)^2} = \frac{m^{2.5}}{Δ^2}$ up to logarithmic factors. Our upper bound is based on non-adaptive queries and a simple thresholding-based allocation algorithm that runs in polynomial time, while our lower bound holds even under adaptive queries and arbitrary computation time.

