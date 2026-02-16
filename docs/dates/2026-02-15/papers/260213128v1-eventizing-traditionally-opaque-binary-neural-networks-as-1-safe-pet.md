---
layout: default
title: Eventizing Traditionally Opaque Binary Neural Networks as 1-safe Petri net Models
---

# Eventizing Traditionally Opaque Binary Neural Networks as 1-safe Petri net Models
**arXiv**：[2602.13128v1](https://arxiv.org/abs/2602.13128) · [PDF](https://arxiv.org/pdf/2602.13128.pdf)  
**作者**：Mohamed Tarraf, Alex Chan, Alex Yakovlev, Rishad Shafik  

**一句话要点**：提出基于Petri网的事件化框架，以增强二进制神经网络的因果透明性与形式验证能力

**关键词**：二进制神经网络, Petri网建模, 形式验证, 因果透明度, 安全关键系统, 事件驱动分析

## 3 点简述
- 二进制神经网络因离散非线性行为难以解释和验证，限制其在安全关键领域的应用
- 通过事件化操作构建Petri网模型，捕获内部并发、顺序和状态演化以支持因果分析
- 验证模型满足1-安全性、无死锁等性质，并评估其可扩展性和复杂度

## 摘要（原文）

> Binary Neural Networks (BNNs) offer a low-complexity and energy-efficient alternative to traditional full-precision neural networks by constraining their weights and activations to binary values. However, their discrete, highly non-linear behavior makes them difficult to explain, validate and formally verify. As a result, BNNs remain largely opaque, limiting their suitability in safety-critical domains, where causal transparency and behavioral guarantees are essential. In this work, we introduce a Petri net (PN)-based framework that captures the BNN's internal operations as event-driven processes. By "eventizing" their operations, we expose their causal relationships and dependencies for a fine-grained analysis of concurrency, ordering, and state evolution. Here, we construct modular PN blueprints for core BNN components including activation, gradient computation and weight updates, and compose them into a complete system-level model. We then validate the composed PN against a reference software-based BNN, verify it against reachability and structural checks to establish 1-safeness, deadlock-freeness, mutual exclusion and correct-by-construction causal sequencing, before we assess its scalability and complexity at segment, component, and system levels using the automated measurement tools in Workcraft. Overall, this framework enables causal introspection of transparent and event-driven BNNs that are amenable to formal reasoning and verification.

