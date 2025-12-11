---
layout: default
title: CONCUR: A Framework for Continual Constrained and Unconstrained Routing
---

# CONCUR: A Framework for Continual Constrained and Unconstrained Routing
**arXiv**：[2512.09386v1](https://arxiv.org/abs/2512.09386) · [PDF](https://arxiv.org/pdf/2512.09386.pdf)  
**作者**：Peter Baile Chen, Weiyue Li, Dan Roth, Michael Cafarella, Samuel Madden, Jacob Andreas  

**一句话要点**：提出CONCUR框架以解决持续路由中策略扩展和表示不足的问题

**关键词**：持续路由, 模块化预测器, 多重表示, 约束路由, 推理优化, 任务分配

## 3 点简述
- 核心问题：现有路由方法需全模型重训练以适应新策略，且单输入表示限制路由决策优化
- 方法要点：采用模块化设计，为每个策略训练独立预测器，并利用任务和策略的多重表示
- 实验或效果：在分布内外任务上优于最佳单策略和现有路由技术，提高准确性并降低训练和推理成本

## 摘要（原文）

> AI tasks differ in complexity and are best addressed with different computation strategies (e.g., combinations of models and decoding methods). Hence, an effective routing system that maps tasks to the appropriate strategies is crucial. Most prior methods build the routing framework by training a single model across all strategies, which demands full retraining whenever new strategies appear and leads to high overhead. Attempts at such continual routing, however, often face difficulties with generalization. Prior models also typically use a single input representation, limiting their ability to capture the full complexity of the routing problem and leading to sub-optimal routing decisions. To address these gaps, we propose CONCUR, a continual routing framework that supports both constrained and unconstrained routing (i.e., routing with or without a budget). Our modular design trains a separate predictor model for each strategy, enabling seamless incorporation of new strategies with low additional training cost. Our predictors also leverage multiple representations of both tasks and computation strategies to better capture overall problem complexity. Experiments on both in-distribution and out-of-distribution, knowledge- and reasoning-intensive tasks show that our method outperforms the best single strategy and strong existing routing techniques with higher end-to-end accuracy and lower inference cost in both continual and non-continual settings, while also reducing training cost in the continual setting.

