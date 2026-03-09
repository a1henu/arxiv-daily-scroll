---
layout: default
title: MoEless: Efficient MoE LLM Serving via Serverless Computing
---

# MoEless: Efficient MoE LLM Serving via Serverless Computing
**arXiv**：[2603.06350v1](https://arxiv.org/abs/2603.06350) · [PDF](https://arxiv.org/pdf/2603.06350.pdf)  
**作者**：Hanfei Yu, Bei Ouyang, Shwai He, Ang Li, Hao Wang  

**一句话要点**：提出MoEless框架，通过无服务器计算解决MoE大语言模型推理中的专家负载失衡问题

**关键词**：MoE模型推理, 无服务器计算, 负载均衡, 专家并行, GPU优化, 推理加速

## 3 点简述
- 核心问题：MoE模型稀疏激活导致专家负载失衡，引发推理延迟和成本增加
- 方法要点：使用轻量级预测器估计负载分布，设计优化专家扩展和放置策略
- 实验或效果：在八GPU测试床上，相比现有方案降低43%延迟和84%成本

## 摘要（原文）

> Large Language Models (LLMs) have become a cornerstone of AI, driving progress across diverse domains such as content creation, search and recommendation systems, and AI-assisted workflows. To alleviate extreme training costs and advancing model scales, Mixture-of-Experts (MoE) has become a popular backbone for modern LLMs, which are commonly served in distributed deployment using expert parallelism (EP). However, MoE's sparse activation mechanism leads to severe expert load imbalance, where a few experts become overloaded while others remain idle, resulting in expert stragglers that inflate inference latency and serving cost. Existing expert load balancing solutions assume static resource configurations on serverful infrastructures, limiting expert scalability and elasticity, and resulting in either costly real-time expert swapping or degraded generation quality. We present MoEless, the first serverless MoE serving framework that mitigates expert load imbalance and accelerates inference via serverless experts. MoEless employs lightweight, layer-aware predictors to accurately estimate incoming expert load distributions and proactively identify stragglers. We design optimized expert scaling and placement strategies to maximize function locality, improve GPU utilization, and balance loads across experts and GPUs. MoEless is prototyped on top of Megatron-LM and deployed on an eight-GPU testbed. Experiments with open-source MoE models and real-world workloads show that MoEless reduces inference latency by 43% and inference cost by 84% compared to state-of-the-art solutions.

