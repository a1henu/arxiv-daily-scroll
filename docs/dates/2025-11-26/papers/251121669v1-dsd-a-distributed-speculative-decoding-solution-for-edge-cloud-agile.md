---
layout: default
title: DSD: A Distributed Speculative Decoding Solution for Edge-Cloud Agile Large Model Serving
---

# DSD: A Distributed Speculative Decoding Solution for Edge-Cloud Agile Large Model Serving
**arXiv**：[2511.21669v1](https://arxiv.org/abs/2511.21669) · [PDF](https://arxiv.org/pdf/2511.21669.pdf)  
**作者**：Fengze Yu, Leshu Li, Brad McDanel, Saiqian Zhang  

**一句话要点**：提出分布式推测解码框架DSD以解决边缘云异构环境中大模型推理延迟高和可扩展性差的问题

**关键词**：分布式推测解码, 边缘云推理, 大语言模型服务, 自适应窗口控制, 离散事件模拟

## 3 点简述
- 核心问题：大语言模型推理在异构边缘云环境中解码延迟高、可扩展性受限
- 方法要点：通过协调草稿-目标执行将推测解码扩展到多设备部署，并设计自适应窗口控制策略
- 实验或效果：实验显示DSD相比现有基线最高加速1.1倍，吞吐量提升9.7%

## 摘要（原文）

> Large language model (LLM) inference often suffers from high decoding latency and limited scalability across heterogeneous edge-cloud environments. Existing speculative decoding (SD) techniques accelerate token generation but remain confined to single-node execution. We propose DSD, a distributed speculative decoding framework that extends SD to multi-device deployments through coordinated draft-target execution. Given the lack of prior work on simulating this paradigm, we first introduce DSD-Sim, a discrete-event simulator that captures network, batching, and scheduling dynamics. Building on insights from DSD-Sim, we further design an Adaptive Window Control (AWC) policy that dynamically adjusts speculation window size to optimize throughput. Experiments across diverse workloads show that DSD achieves up to 1.1x speedup and 9.7% higher throughput over existing SD baselines, enabling agile and scalable LLM serving across edge and cloud.

