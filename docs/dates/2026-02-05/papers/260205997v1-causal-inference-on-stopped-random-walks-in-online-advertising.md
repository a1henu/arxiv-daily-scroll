---
layout: default
title: Causal Inference on Stopped Random Walks in Online Advertising
---

# Causal Inference on Stopped Random Walks in Online Advertising
**arXiv**：[2602.05997v1](https://arxiv.org/abs/2602.05997) · [PDF](https://arxiv.org/pdf/2602.05997.pdf)  
**作者**：Jia Yuan Yu  

**一句话要点**：提出基于停止随机游走的因果推断方法，以估计在线广告机制的长效处理效应。

**关键词**：因果推断, 在线广告, 停止随机游走, 长效处理效应, 置信区间

## 3 点简述
- 核心问题：在线广告系统中，处理（如拍卖底价）影响瞬时收入、用户交互轨迹和广告商竞价策略，需估计长效效应。
- 方法要点：放弃i.i.d.假设，将实验测量建模为停止随机游走，结合预算分割设计、Anscombe定理和中心极限定理构建置信区间。
- 实验或效果：未知具体实验细节，但方法旨在为长效处理效应（如年广告收入）提供统计推断。

## 摘要（原文）

> We consider a causal inference problem frequently encountered in online advertising systems, where a publisher (e.g., Instagram, TikTok) interacts repeatedly with human users and advertisers by sporadically displaying to each user an advertisement selected through an auction. Each treatment corresponds to a parameter value of the advertising mechanism (e.g., auction reserve-price), and we want to estimate through experiments the corresponding long-term treatment effect (e.g., annual advertising revenue). In our setting, the treatment affects not only the instantaneous revenue from showing an ad, but also changes each user's interaction-trajectory, and each advertiser's bidding policy -- as the latter is constrained by a finite budget. In particular, each a treatment may even affect the size of the population, since users interact longer with a tolerable advertising mechanism. We drop the classical i.i.d. assumption and model the experiment measurements (e.g., advertising revenue) as a stopped random walk, and use a budget-splitting experimental design, the Anscombe Theorem, a Wald-like equation, and a Central Limit Theorem to construct confidence intervals for the long-term treatment effect.

