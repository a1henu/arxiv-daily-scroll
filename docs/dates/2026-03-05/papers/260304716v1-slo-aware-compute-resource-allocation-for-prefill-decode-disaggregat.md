---
layout: default
title: SLO-Aware Compute Resource Allocation for Prefill-Decode Disaggregated LLM Inference
---

# SLO-Aware Compute Resource Allocation for Prefill-Decode Disaggregated LLM Inference
**arXiv**：[2603.04716v1](https://arxiv.org/abs/2603.04716) · [PDF](https://arxiv.org/pdf/2603.04716.pdf)  
**作者**：Luchang Li, Dongfang Li, Bozhao Gong, Yu Zhang  

**一句话要点**：提出混合方法以优化预填充-解码解耦LLM推理中的计算资源分配

**关键词**：LLM推理优化, 预填充-解码解耦, 服务级别目标, 排队论建模, 资源分配

## 3 点简述
- 核心问题：缺乏在吞吐量、SLO和请求特征约束下确定预填充-解码硬件资源数量的方法
- 方法要点：结合理论建模与实证基准，基于排队论和批量大小优化预测资源需求
- 实验或效果：实验证明该方法能准确预测现实场景中的最优资源分配

## 摘要（原文）

> Prefill-Decode (P/D) disaggregation has emerged as a widely adopted optimization strategy for Large Language Model (LLM) inference. However, there currently exists no well-established methodology for determining the optimal number of P/D hardware resources, subject to constraints on total throughput, service level objectives (SLOs), and request characteristics - specifically input and output lengths. To address this gap, we propose a hybrid approach that combines theoretical modeling with empirical benchmarking. First, we present a theoretical model for calculating P/D resource counts, which is based on total throughput requirements, request input and output lengths, as well as prefill and decode throughput. Then, to obtain the actual prefill and decode throughput under SLO constraints, we model the prefill process using M/M/1 queuing theory, deriving the achieved prefill throughput from the benchmarked maximum prefill throughput and Time-To-First-Token (TTFT). For the decode phase, we determine the decode batch sizes that meet Time-Per-Output-Token (TPOT) requirements and obtain the corresponding decode throughput through empirical measurements. Our experimental results demonstrate that the proposed method can accurately predict optimal P/D resource allocation in real-world LLM inference scenarios.

