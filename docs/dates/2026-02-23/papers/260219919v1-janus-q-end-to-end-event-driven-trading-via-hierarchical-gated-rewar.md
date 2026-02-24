---
layout: default
title: Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling
---

# Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling
**arXiv**：[2602.19919v1](https://arxiv.org/abs/2602.19919) · [PDF](https://arxiv.org/pdf/2602.19919.pdf)  
**作者**：Xiang Li, Zikai Wei, Yiyan Qi, Wanyun Zhou, Xiang Liu, Penglei Sun, Yongqi Zhang, Xiaowen Chu  

**一句话要点**：提出Janus-Q端到端事件驱动交易框架，通过分层门控奖励建模解决金融新闻事件捕捉与交易决策对齐问题。

**关键词**：事件驱动交易, 金融新闻分析, 分层门控奖励模型, 端到端学习, 强化学习, 异常收益建模

## 3 点简述
- 核心问题：金融事件影响异质且突发，现有方法缺乏事件中心数据集和语言模型与交易行为的对齐。
- 方法要点：构建大规模金融新闻事件数据集，结合监督与强化学习，使用分层门控奖励模型优化多目标权衡。
- 实验或效果：相比市场指数和LLM基线，提升夏普比率达102.0%，方向准确性提高超过17.5%。

## 摘要（原文）

> Financial market movements are often driven by discrete financial events conveyed through news, whose impacts are heterogeneous, abrupt, and difficult to capture under purely numerical prediction objectives. These limitations have motivated growing interest in using textual information as the primary source of trading signals in learning-based systems. Two key challenges hinder existing approaches: (1) the absence of large-scale, event-centric datasets that jointly model news semantics and statistically grounded market reactions, and (2) the misalignment between language model reasoning and financially valid trading behavior under dynamic market conditions. To address these challenges, we propose Janus-Q, an end-to-end event-driven trading framework that elevates financial news events from auxiliary signals to primary decision units. Janus-Q unifies event-centric data construction and model optimization under a two-stage paradigm. Stage I focuses on event-centric data construction, building a large-scale financial news event dataset comprising 62,400 articles annotated with 10 fine-grained event types, associated stocks, sentiment labels, and event-driven cumulative abnormal return (CAR). Stage II performs decision-oriented fine-tuning, combining supervised learning with reinforcement learning guided by a Hierarchical Gated Reward Model (HGRM), which explicitly captures trade-offs among multiple trading objectives. Extensive experiments demonstrate that Janus-Q achieves more consistent, interpretable, and profitable trading decisions than market indices and LLM baselines, improving the Sharpe Ratio by up to 102.0% while increasing direction accuracy by over 17.5% compared to the strongest competing strategies.

