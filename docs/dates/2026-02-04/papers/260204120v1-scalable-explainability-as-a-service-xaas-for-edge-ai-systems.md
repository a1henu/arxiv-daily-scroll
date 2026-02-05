---
layout: default
title: Scalable Explainability-as-a-Service (XaaS) for Edge AI Systems
---

# Scalable Explainability-as-a-Service (XaaS) for Edge AI Systems
**arXiv**：[2602.04120v1](https://arxiv.org/abs/2602.04120) · [PDF](https://arxiv.org/pdf/2602.04120.pdf)  
**作者**：Samaresh Kumar Singh, Joyjit Roy  

**一句话要点**：提出可扩展的解释即服务架构，以解决边缘AI系统中解释性低效和可扩展性差的问题。

**关键词**：边缘AI, 可解释人工智能, 分布式架构, 解释缓存, 轻量级验证, 自适应解释

## 3 点简述
- 核心问题：现有XAI方法在边缘系统中耦合推理与解释生成，导致冗余计算、高延迟和可扩展性差。
- 方法要点：通过解耦推理与解释生成，引入分布式解释缓存、轻量级验证协议和自适应解释引擎。
- 实验或效果：在三个真实边缘AI用例中评估，XaaS降低延迟38%，同时保持高解释质量。

## 摘要（原文）

> Though Explainable AI (XAI) has made significant advancements, its inclusion in edge and IoT systems is typically ad-hoc and inefficient. Most current methods are "coupled" in such a way that they generate explanations simultaneously with model inferences. As a result, these approaches incur redundant computation, high latency and poor scalability when deployed across heterogeneous sets of edge devices. In this work we propose Explainability-as-a-Service (XaaS), a distributed architecture for treating explainability as a first-class system service (as opposed to a model-specific feature). The key innovation in our proposed XaaS architecture is that it decouples inference from explanation generation allowing edge devices to request, cache and verify explanations subject to resource and latency constraints. To achieve this, we introduce three main innovations: (1) A distributed explanation cache with a semantic similarity based explanation retrieval method which significantly reduces redundant computation; (2) A lightweight verification protocol that ensures the fidelity of both cached and newly generated explanations; and (3) An adaptive explanation engine that chooses explanation methods based upon device capability and user requirement. We evaluated the performance of XaaS on three real-world edge-AI use cases: (i) manufacturing quality control; (ii) autonomous vehicle perception; and (iii) healthcare diagnostics. Experimental results show that XaaS reduces latency by 38\% while maintaining high explanation quality across three real-world deployments. Overall, this work enables the deployment of transparent and accountable AI across large scale, heterogeneous IoT systems, and bridges the gap between XAI research and edge-practicality.

