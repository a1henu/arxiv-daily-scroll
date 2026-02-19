---
layout: default
title: The Diversity Paradox revisited: Systemic Effects of Feedback Loops in Recommender Systems
---

# The Diversity Paradox revisited: Systemic Effects of Feedback Loops in Recommender Systems
**arXiv**：[2602.16315v1](https://arxiv.org/abs/2602.16315) · [PDF](https://arxiv.org/pdf/2602.16315.pdf)  
**作者**：Gabriele Barlacchi, Margherita Lalli, Emanuele Ferragina, Fosca Giannotti, Dino Pedreschi, Luca Pappalardo  

**一句话要点**：提出反馈循环模型以分析推荐系统对个体与集体消费的系统性影响

**关键词**：推荐系统, 反馈循环, 系统性效应, 个体多样性, 集体需求, 动态评估

## 3 点简述
- 核心问题：推荐系统反馈循环的系统效应，现有模拟研究假设不现实
- 方法要点：模型包含隐式反馈、定期重训练、概率采纳和异构推荐器
- 实验或效果：基于零售和音乐数据，发现个体多样性可能增加但集体需求集中

## 摘要（原文）

> Recommender systems shape individual choices through feedback loops in which user behavior and algorithmic recommendations coevolve over time. The systemic effects of these loops remain poorly understood, in part due to unrealistic assumptions in existing simulation studies. We propose a feedback-loop model that captures implicit feedback, periodic retraining, probabilistic adoption of recommendations, and heterogeneous recommender systems. We apply the framework on online retail and music streaming data and analyze systemic effects of the feedback loop. We find that increasing recommender adoption may lead to a progressive diversification of individual consumption, while collective demand is redistributed in model- and domain-dependent ways, often amplifying popularity concentration. Temporal analyses further reveal that apparent increases in individual diversity observed in static evaluations are illusory: when adoption is fixed and time unfolds, individual diversity consistently decreases across all models. Our results highlight the need to move beyond static evaluations and explicitly account for feedback-loop dynamics when designing recommender systems.

