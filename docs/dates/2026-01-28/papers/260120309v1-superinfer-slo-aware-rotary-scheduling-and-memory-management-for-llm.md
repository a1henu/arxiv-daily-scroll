---
layout: default
title: SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips
---

# SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips
**arXiv**：[2601.20309v1](https://arxiv.org/abs/2601.20309) · [PDF](https://arxiv.org/pdf/2601.20309.pdf)  
**作者**：Jiahuan Yu, Mingtao Hu, Zichao Lin, Minjia Zhang  

**一句话要点**：提出SuperInfer系统，通过SLO感知旋转调度和内存管理优化Superchip上的LLM推理性能。

**关键词**：LLM推理系统, SLO感知调度, Superchip优化, KV缓存管理, NVLink-C2C传输

## 3 点简述
- 核心问题：LLM推理中高请求率导致KV缓存不足，引发头阻塞，难以满足TTFT和TBT SLO。
- 方法要点：设计RotaSched旋转调度器和DuplexKV引擎，利用NVLink-C2C实现全双工传输，提升Superchip响应性。
- 实验或效果：在GH200上评估，TTFT SLO达成率提升高达74.7%，同时保持可比TBT和吞吐量。

## 摘要（原文）

> Large Language Model (LLM) serving faces a fundamental tension between stringent latency Service Level Objectives (SLOs) and limited GPU memory capacity. When high request rates exhaust the KV cache budget, existing LLM inference systems often suffer severe head-of-line (HOL) blocking. While prior work explored PCIe-based offloading, these approaches cannot sustain responsiveness under high request rates, often failing to meet tight Time-To-First-Token (TTFT) and Time-Between-Tokens (TBT) SLOs. We present SuperInfer, a high-performance LLM inference system designed for emerging Superchips (e.g., NVIDIA GH200) with tightly coupled GPU-CPU architecture via NVLink-C2C. SuperInfer introduces RotaSched, the first proactive, SLO-aware rotary scheduler that rotates requests to maintain responsiveness on Superchips, and DuplexKV, an optimized rotation engine that enables full-duplex transfer over NVLink-C2C. Evaluations on GH200 using various models and datasets show that SuperInfer improves TTFT SLO attainment rates by up to 74.7% while maintaining comparable TBT and throughput compared to state-of-the-art systems, demonstrating that SLO-aware scheduling and memory co-design unlocks the full potential of Superchips for responsive LLM serving.

