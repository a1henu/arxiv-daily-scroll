---
layout: default
title: Hybrid Learning and Optimization-Based Dynamic Scheduling for DL Workloads on Heterogeneous GPU Clusters
---

# Hybrid Learning and Optimization-Based Dynamic Scheduling for DL Workloads on Heterogeneous GPU Clusters
**arXiv**：[2512.10271v1](https://arxiv.org/abs/2512.10271) · [PDF](https://arxiv.org/pdf/2512.10271.pdf)  
**作者**：Shruti Dongare, Redwan Ibne Seraj Khan, Hadeel Albahar, Nannan Zhao, Diego Melendez Maita, Ali R. Butt  

**一句话要点**：提出RLTune框架，通过强化学习与优化结合，动态调度异构GPU集群上的深度学习任务。

**关键词**：异构GPU调度, 强化学习优化, 深度学习工作负载, 动态优先级分配, 混合整数线性规划

## 3 点简述
- 问题：异构GPU集群和任务特性未知导致现有调度器性能受限，依赖离线分析或假设。
- 方法：结合强化学习优先级排序和混合整数线性规划节点映射，实现无任务特定分析的动态调度。
- 效果：在真实生产数据上训练，提升GPU利用率达20%，减少排队延迟81%，缩短任务完成时间70%。

## 摘要（原文）

> Modern cloud platforms increasingly host large-scale deep learning (DL) workloads, demanding high-throughput, low-latency GPU scheduling. However, the growing heterogeneity of GPU clusters and limited visibility into application characteristics pose major challenges for existing schedulers, which often rely on offline profiling or application-specific assumptions. We present RLTune, an application-agnostic reinforcement learning (RL)-based scheduling framework that dynamically prioritizes and allocates DL jobs on heterogeneous GPU clusters. RLTune integrates RL-driven prioritization with MILP-based job-to-node mapping to optimize system-wide objectives such as job completion time (JCT), queueing delay, and resource utilization. Trained on large-scale production traces from Microsoft Philly, Helios, and Alibaba, RLTune improves GPU utilization by up to 20%, reduces queueing delay by up to 81%, and shortens JCT by as much as 70 percent. Unlike prior approaches, RLTune generalizes across diverse workloads without requiring per-job profiling, making it practical for cloud providers to deploy at scale for more efficient, fair, and sustainable DL workload management.

