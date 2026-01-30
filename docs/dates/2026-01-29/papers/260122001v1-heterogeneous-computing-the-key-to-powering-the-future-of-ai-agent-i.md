---
layout: default
title: Heterogeneous Computing: The Key to Powering the Future of AI Agent Inference
---

# Heterogeneous Computing: The Key to Powering the Future of AI Agent Inference
**arXiv**：[2601.22001v1](https://arxiv.org/abs/2601.22001) · [PDF](https://arxiv.org/pdf/2601.22001.pdf)  
**作者**：Yiren Zhao, Junyi Liu  

**一句话要点**：提出OI/CF指标与异构计算方案以解决AI代理推理中的内存瓶颈问题

**关键词**：AI代理推理, 内存瓶颈, 异构计算, 操作强度, 容量占用, 系统优化

## 3 点简述
- 核心问题：AI代理推理面临内存容量、带宽和互连瓶颈，传统屋顶线分析无法覆盖
- 方法要点：引入操作强度与容量占用指标，分析不同工作流和模型下的内存约束变化
- 实验或效果：基于指标提出解耦服务、异构加速器和光I/O等系统级优化方向

## 摘要（原文）

> AI agent inference is driving an inference heavy datacenter future and exposes bottlenecks beyond compute - especially memory capacity, memory bandwidth and high-speed interconnect. We introduce two metrics - Operational Intensity (OI) and Capacity Footprint (CF) - that jointly explain regimes the classic roofline analysis misses, including the memory capacity wall. Across agentic workflows (chat, coding, web use, computer use) and base model choices (GQA/MLA, MoE, quantization), OI/CF can shift dramatically, with long context KV cache making decode highly memory bound. These observations motivate disaggregated serving and system level heterogeneity: specialized prefill and decode accelerators, broader scale up networking, and decoupled compute-memory enabled by optical I/O. We further hypothesize agent-hardware co design, multiple inference accelerators within one system, and high bandwidth, large capacity memory disaggregation as foundations for adaptation to evolving OI/CF. Together, these directions chart a path to sustain efficiency and capability for large scale agentic AI inference.

