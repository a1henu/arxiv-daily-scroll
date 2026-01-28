---
layout: default
title: PROTEUS: SLA-Aware Routing via Lagrangian RL for Multi-LLM Serving Systems
---

# PROTEUS: SLA-Aware Routing via Lagrangian RL for Multi-LLM Serving Systems
**arXiv**：[2601.19402v1](https://arxiv.org/abs/2601.19402) · [PDF](https://arxiv.org/pdf/2601.19402.pdf)  
**作者**：Amit Singh Bhatti, Vishal Vaddina, Dagnachew Birru  

**一句话要点**：提出PROTEUS路由系统，通过拉格朗日强化学习实现多LLM服务中SLA感知的准确率目标路由。

**关键词**：多LLM服务系统, SLA感知路由, 拉格朗日强化学习, 准确率目标优化, 模型路由

## 3 点简述
- 核心问题：LLM路由系统缺乏直接接受准确率目标的能力，导致操作员需离线调参且难以预测结果。
- 方法要点：采用拉格朗日对偶控制，学习对偶变量跟踪约束违反，将指定准确率目标转化为满足条件的路由决策。
- 实验或效果：在RouterBench和SPROUT数据集上，PROTEUS实现高目标响应相关性，准确率接近oracle，成本节省达89.8%。

## 摘要（原文）

> Production LLM deployments serve diverse workloads where cost and quality requirements vary by customer tier, time of day, and query criticality. Model serving systems accept latency SLOs directly. LLM routers do not. They force operators to tune parameters offline and guess what accuracy might result. The relationship between parameters and outcomes is indirect, non-monotonic, and dataset-dependent. Operators need to specify accuracy targets, not infer them from opaque settings. We present PROTEUS (Polymorphic Router for Operational Target Enforcement with Unified SLA), a router that accepts accuracy targets tau as runtime input. PROTEUS uses Lagrangian dual control. A learned dual variable lambda tracks constraint violations during training and conditions the policy network. This lets the router translate specified tau values into routing decisions that satisfy them. A single trained model serves the full accuracy spectrum without retraining.We evaluate on RouterBench (11 models, 405K queries) and SPROUT (14 models, 45K queries). PROTEUS achieves consistent floor compliance where accuracy meets or exceeds tau. The target-response correlation reaches 0.97 to 0.98. The closest baseline, OmniRouter, meets floors only 22% of the time despite also using Lagrangian optimization. PROTEUS operates across tau in [0.85, 0.95] from a single model. On RouterBench it achieves 90.1% accuracy, within 1.3% of oracle. On SPROUT it achieves 94.0% accuracy, within 4.6% of oracle. Cost savings reach 89.8% versus the best fixed model.

