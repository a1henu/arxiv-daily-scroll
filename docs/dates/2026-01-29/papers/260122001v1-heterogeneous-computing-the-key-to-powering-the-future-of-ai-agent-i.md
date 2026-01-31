---
layout: default
title: Heterogeneous Computing: The Key to Powering the Future of AI Agent Inference
---

# Heterogeneous Computing: The Key to Powering the Future of AI Agent Inference
**arXiv**：[2601.22001v1](https://arxiv.org/abs/2601.22001) · [PDF](https://arxiv.org/pdf/2601.22001.pdf)  
**作者**：Yiren Zhao, Junyi Liu  

**一句话要点**：提出操作强度与容量足迹指标以解决AI代理推理中的内存瓶颈问题

**关键词**：AI代理推理, 内存瓶颈, 异构计算, 操作强度, 容量足迹, 硬件协同设计

## 3 点简述
- AI代理推理面临内存容量、带宽和高速互连瓶颈，超越传统计算限制
- 引入操作强度和容量足迹指标，揭示经典屋顶线分析遗漏的如内存墙等机制
- 基于指标分析，提出异构计算、解耦服务及硬件协同设计等系统级优化方向

## 摘要（原文）

> AI agent inference is driving an inference heavy datacenter future and exposes bottlenecks beyond compute - especially memory capacity, memory bandwidth and high-speed interconnect. We introduce two metrics - Operational Intensity (OI) and Capacity Footprint (CF) - that jointly explain regimes the classic roofline analysis misses, including the memory capacity wall. Across agentic workflows (chat, coding, web use, computer use) and base model choices (GQA/MLA, MoE, quantization), OI/CF can shift dramatically, with long context KV cache making decode highly memory bound. These observations motivate disaggregated serving and system level heterogeneity: specialized prefill and decode accelerators, broader scale up networking, and decoupled compute-memory enabled by optical I/O. We further hypothesize agent-hardware co design, multiple inference accelerators within one system, and high bandwidth, large capacity memory disaggregation as foundations for adaptation to evolving OI/CF. Together, these directions chart a path to sustain efficiency and capability for large scale agentic AI inference.

