---
layout: default
title: Constraint-Aware Generative Auto-bidding via Pareto-Prioritized Regret Optimization
---

# Constraint-Aware Generative Auto-bidding via Pareto-Prioritized Regret Optimization
**arXiv**：[2602.08261v1](https://arxiv.org/abs/2602.08261) · [PDF](https://arxiv.org/pdf/2602.08261.pdf)  
**作者**：Binglin Wu, Yingyi Zhang, Xianneng Li, Ruyue Deng, Chuan Yue, Weiru Zhang, Xiaoyi Zeng  

**一句话要点**：提出PRO-Bid框架以解决自动出价中的约束感知与性能优化问题

**关键词**：自动出价系统, 约束优化, 决策变换器, 帕累托表示, 反事实学习, 在线广告

## 3 点简述
- 核心问题：标准决策变换器在自动出价中忽视成本维度导致状态混淆，且回归方法限制性能优化至约束边界。
- 方法要点：引入约束解耦帕累托表示分解约束为递归上下文，并采用反事实遗憾优化主动提升策略。
- 实验或效果：在公开基准和在线A/B测试中，PRO-Bid在约束满足和价值获取方面优于现有基线。

## 摘要（原文）

> Auto-bidding systems aim to maximize marketing value while satisfying strict efficiency constraints such as Target Cost-Per-Action (CPA). Although Decision Transformers provide powerful sequence modeling capabilities, applying them to this constrained setting encounters two challenges: 1) standard Return-to-Go conditioning causes state aliasing by neglecting the cost dimension, preventing precise resource pacing; and 2) standard regression forces the policy to mimic average historical behaviors, thereby limiting the capacity to optimize performance toward the constraint boundary. To address these challenges, we propose PRO-Bid, a constraint-aware generative auto-bidding framework based on two synergistic mechanisms: 1) Constraint-Decoupled Pareto Representation (CDPR) decomposes global constraints into recursive cost and value contexts to restore resource perception, while reweighting trajectories based on the Pareto frontier to focus on high-efficiency data; and 2) Counterfactual Regret Optimization (CRO) facilitates active improvement by utilizing a global outcome predictor to identify superior counterfactual actions. By treating these high-utility outcomes as weighted regression targets, the model transcends historical averages to approach the optimal constraint boundary. Extensive experiments on two public benchmarks and online A/B tests demonstrate that PRO-Bid achieves superior constraint satisfaction and value acquisition compared to state-of-the-art baselines.

