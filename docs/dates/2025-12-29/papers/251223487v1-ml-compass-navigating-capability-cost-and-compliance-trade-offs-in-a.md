---
layout: default
title: ML Compass: Navigating Capability, Cost, and Compliance Trade-offs in AI Model Deployment
---

# ML Compass: Navigating Capability, Cost, and Compliance Trade-offs in AI Model Deployment
**arXiv**：[2512.23487v1](https://arxiv.org/abs/2512.23487) · [PDF](https://arxiv.org/pdf/2512.23487.pdf)  
**作者**：Vassilis Digalakis, Ramayya Krishnan, Gonzalo Martin Fernandez, Agni Orfanoudaki  

**一句话要点**：提出ML Compass框架，通过约束优化解决AI模型部署中的能力、成本与合规权衡问题。

**关键词**：模型选择, 部署优化, 能力-成本前沿, 合规约束, 系统级框架, 约束优化

## 3 点简述
- 核心问题：能力排行榜无法直接指导部署决策，存在能力-部署差距，需综合考虑用户效用、成本和合规要求。
- 方法要点：采用系统级视角，将模型选择视为能力-成本前沿上的约束优化问题，理论分析最优配置的三区结构。
- 实验或效果：在对话和医疗案例中验证，推荐结果与纯能力排名差异显著，阐明权衡如何影响最优模型选择。

## 摘要（原文）

> We study how organizations should select among competing AI models when user utility, deployment costs, and compliance requirements jointly matter. Widely used capability leaderboards do not translate directly into deployment decisions, creating a capability--deployment gap; to bridge it, we take a systems-level view in which model choice is tied to application outcomes, operating constraints, and a capability--cost frontier. We develop ML Compass, a framework that treats model selection as constrained optimization over this frontier. On the theory side, we characterize optimal model configurations under a parametric frontier and show a three-regime structure in optimal internal measures: some dimensions are pinned at compliance minima, some saturate at maximum levels, and the remainder take interior values governed by frontier curvature. We derive comparative statics that quantify how budget changes, regulatory tightening, and technological progress propagate across capability dimensions and costs. On the implementation side, we propose a pipeline that (i) extracts low-dimensional internal measures from heterogeneous model descriptors, (ii) estimates an empirical frontier from capability and cost data, (iii) learns a user- or task-specific utility function from interaction outcome data, and (iv) uses these components to target capability--cost profiles and recommend models. We validate ML Compass with two case studies: a general-purpose conversational setting using the PRISM Alignment dataset and a healthcare setting using a custom dataset we build using HealthBench. In both environments, our framework produces recommendations -- and deployment-aware leaderboards based on predicted deployment value under constraints -- that can differ materially from capability-only rankings, and clarifies how trade-offs between capability, cost, and safety shape optimal model choice.

