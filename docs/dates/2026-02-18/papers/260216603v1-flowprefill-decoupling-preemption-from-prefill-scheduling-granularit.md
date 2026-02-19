---
layout: default
title: FlowPrefill: Decoupling Preemption from Prefill Scheduling Granularity to Mitigate Head-of-Line Blocking in LLM Serving
---

# FlowPrefill: Decoupling Preemption from Prefill Scheduling Granularity to Mitigate Head-of-Line Blocking in LLM Serving
**arXiv**：[2602.16603v1](https://arxiv.org/abs/2602.16603) · [PDF](https://arxiv.org/pdf/2602.16603.pdf)  
**作者**：Chia-chi Hsieh, Zan Zong, Xinyang Chen, Jianjiang Li, Jidong Zhai, Lijie Wen  

**一句话要点**：提出FlowPrefill以解决LLM服务中预填充阶段因资源垄断导致的头阻塞问题

**关键词**：LLM服务系统, 预填充调度, 头阻塞缓解, 操作符级抢占, 事件驱动调度, TTFT优化

## 3 点简述
- 核心问题：预填充阶段长请求独占资源，导致高优先级请求延迟，违反TTFT SLO
- 方法要点：通过操作符级抢占和事件驱动调度，解耦抢占粒度与调度频率，实现自适应预填充
- 实验或效果：在真实生产轨迹评估中，相比先进系统，最大良好吞吐量提升达5.6倍，满足异构SLO

## 摘要（原文）

> The growing demand for large language models (LLMs) requires serving systems to handle many concurrent requests with diverse service level objectives (SLOs). This exacerbates head-of-line (HoL) blocking during the compute-intensive prefill phase, where long-running requests monopolize resources and delay higher-priority ones, leading to widespread time-to-first-token (TTFT) SLO violations. While chunked prefill enables interruptibility, it introduces an inherent trade-off between responsiveness and throughput: reducing chunk size improves response latency but degrades computational efficiency, whereas increasing chunk size maximizes throughput but exacerbates blocking. This necessitates an adaptive preemption mechanism. However, dynamically balancing execution granularity against scheduling overheads remains a key challenge.
>   In this paper, we propose FlowPrefill, a TTFT-goodput-optimized serving system that resolves this conflict by decoupling preemption granularity from scheduling frequency. To achieve adaptive prefill scheduling, FlowPrefill introduces two key innovations: 1) Operator-Level Preemption, which leverages operator boundaries to enable fine-grained execution interruption without the efficiency loss associated with fixed small chunking; and 2) Event-Driven Scheduling, which triggers scheduling decisions only upon request arrival or completion events, thereby supporting efficient preemption responsiveness while minimizing control-plane overhead. Evaluation on real-world production traces shows that FlowPrefill improves maximum goodput by up to 5.6$\times$ compared to state-of-the-art systems while satisfying heterogeneous SLOs.

