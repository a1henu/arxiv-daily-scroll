---
layout: default
title: History Is Not Enough: An Adaptive Dataflow System for Financial Time-Series Synthesis
---

# History Is Not Enough: An Adaptive Dataflow System for Financial Time-Series Synthesis
**arXiv**：[2601.10143v1](https://arxiv.org/abs/2601.10143) · [PDF](https://arxiv.org/pdf/2601.10143.pdf)  
**作者**：Haochong Xia, Yao Long Teng, Regan Tan, Molei Qin, Xinrun Wang, Bo An  

**一句话要点**：提出自适应数据流系统以解决金融时间序列合成中的概念漂移问题

**关键词**：金融时间序列合成, 自适应数据流, 概念漂移, 梯度双层优化, 数据增强, 工作流自动化

## 3 点简述
- 核心问题：金融数据的概念漂移和分布非平稳性导致模型过拟合和泛化差
- 方法要点：集成机器学习自适应控制，结合参数化数据操作和梯度双层优化
- 实验或效果：在预测和强化学习交易任务中提升模型鲁棒性和风险调整收益

## 摘要（原文）

> In quantitative finance, the gap between training and real-world performance-driven by concept drift and distributional non-stationarity-remains a critical obstacle for building reliable data-driven systems. Models trained on static historical data often overfit, resulting in poor generalization in dynamic markets. The mantra "History Is Not Enough" underscores the need for adaptive data generation that learns to evolve with the market rather than relying solely on past observations. We present a drift-aware dataflow system that integrates machine learning-based adaptive control into the data curation process. The system couples a parameterized data manipulation module comprising single-stock transformations, multi-stock mix-ups, and curation operations, with an adaptive planner-scheduler that employs gradient-based bi-level optimization to control the system. This design unifies data augmentation, curriculum learning, and data workflow management under a single differentiable framework, enabling provenance-aware replay and continuous data quality monitoring. Extensive experiments on forecasting and reinforcement learning trading tasks demonstrate that our framework enhances model robustness and improves risk-adjusted returns. The system provides a generalizable approach to adaptive data management and learning-guided workflow automation for financial data.

