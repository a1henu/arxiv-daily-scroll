---
layout: default
title: Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference
---

# Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference
**arXiv**：[2512.16134v1](https://arxiv.org/abs/2512.16134) · [PDF](https://arxiv.org/pdf/2512.16134.pdf)  
**作者**：Jian Tian, Shuailong Li, Yang Cao, Wenbo Cui, Minghan Zhu, Wenkang Wu, Jianming Zhang, Yanpeng Wang, Zhiwen Xiao, Zhenyu Hou, Dou Shen  

**一句话要点**：提出交错批量调度以优化大语言模型推理中的首令牌时间和吞吐量

**关键词**：大语言模型推理, 批量调度, 首令牌时间优化, 吞吐量提升, 分布式架构, 负载感知分配

## 3 点简述
- 针对DP+EP架构中高内部同步成本导致的调度挑战，如即时调度引发排队和并行化气泡
- 提出交错批量调度，通过缓冲请求形成最优执行批次，消除内部排队气泡
- 在H800集群上部署，相比基线减少首令牌时间30%-40%，提升吞吐量15%-20%

## 摘要（原文）

> The evolution of Large Language Model (LLM) serving towards complex, distributed architectures--specifically the P/D-separated, large-scale DP+EP paradigm--introduces distinct scheduling challenges. Unlike traditional deployments where schedulers can treat instances as black boxes, DP+EP architectures exhibit high internal synchronization costs. We identify that immediate request dispatching in such systems leads to severe in-engine queuing and parallelization bubbles, degrading Time-to-First-Token (TTFT). To address this, we propose Staggered Batch Scheduling (SBS), a mechanism that deliberately buffers requests to form optimal execution batches. This temporal decoupling eliminates internal queuing bubbles without compromising throughput. Furthermore, leveraging the scheduling window created by buffering, we introduce a Load-Aware Global Allocation strategy that balances computational load across DP units for both Prefill and Decode phases. Deployed on a production H800 cluster serving Deepseek-V3, our system reduces TTFT by 30%-40% and improves throughput by 15%-20% compared to state-of-the-art immediate scheduling baselines.

