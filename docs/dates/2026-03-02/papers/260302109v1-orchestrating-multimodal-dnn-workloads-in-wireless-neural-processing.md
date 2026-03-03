---
layout: default
title: Orchestrating Multimodal DNN Workloads in Wireless Neural Processing
---

# Orchestrating Multimodal DNN Workloads in Wireless Neural Processing
**arXiv**：[2603.02109v1](https://arxiv.org/abs/2603.02109) · [PDF](https://arxiv.org/pdf/2603.02109.pdf)  
**作者**：Sai Xu, Kai-Kit Wong, Yanan Du, Hyundong Shin  

**一句话要点**：提出O-WiN框架以优化无线神经处理中的多模态DNN工作负载编排

**关键词**：无线神经处理, 多模态DNN, 通信-计算协同, 工作负载编排, 端到端优化

## 3 点简述
- 核心问题：无线传输与加速器级DNN执行缺乏协调，导致端到端推理延迟较高。
- 方法要点：开发统一通信-计算模型，提出O-WiN框架，包含RTFS和PACS算法实现调度。
- 实验或效果：PACS通过通信-计算重叠在高模态异构下显著优于RTFS，降低延迟。

## 摘要（原文）

> In edge inference, wireless resource allocation and accelerator-level deep neural network (DNN) scheduling have yet to be co-optimized in an end-to-end manner. The lack of coordination between wireless transmission and accelerator-level DNN execution prevents efficient overlap, leading to higher end-to-end inference latency. To address this issue, this paper investigates multimodal DNN workload orchestration in wireless neural processing (WNP), a paradigm that integrates wireless transmission and multi-core accelerator execution into a unified end-to-end pipeline. First, we develop a unified communication-computation model for multimodal DNN execution and formulate the corresponding optimization problem. Second, we propose O-WiN, a framework that orchestrates DNN workloads in WNP through two tightly coupled stages: simulation-based optimization and runtime execution. Third, we develop two algorithms, RTFS and PACS. RTFS schedules communication and computation sequentially, whereas PACS interleaves them to enable pipeline parallelism by overlapping wireless data transfer with accelerator-level DNN execution. Simulation results demonstrate that PACS significantly outperforms RTFS under high modality heterogeneity by better masking wireless latency through communication-computation overlap, thereby highlighting the effectiveness of communication-computation pipelining in accelerating multimodal DNN execution in WNP.

