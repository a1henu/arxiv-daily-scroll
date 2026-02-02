---
layout: default
title: HetCCL: Accelerating LLM Training with Heterogeneous GPUs
---

# HetCCL: Accelerating LLM Training with Heterogeneous GPUs
**arXiv**：[2601.22585v1](https://arxiv.org/abs/2601.22585) · [PDF](https://arxiv.org/pdf/2601.22585.pdf)  
**作者**：Heehoon Kim, Jaehwan Lee, Taejeoung Kim, Jongwon Park, Jinpyo Kim, Pyongwon Suh, Ryan H. Choi, Sangwoo Lee, Jaejin Lee  

**一句话要点**：提出HetCCL以解决异构GPU集群中LLM训练通信效率低的问题

**关键词**：异构GPU通信, 集体通信库, LLM训练加速, RDMA通信, 多厂商GPU集群

## 3 点简述
- 核心问题：现有深度学习框架不支持跨厂商GPU的集体通信，导致异构集群训练效率低下
- 方法要点：HetCCL统一厂商后端，通过RDMA实现跨GPU通信，无需修改驱动程序
- 实验或效果：在异构环境中匹配NCCL和RCCL性能，实现高性能训练且无需修改应用

## 摘要（原文）

> The rapid growth of large language models is driving organizations to expand their GPU clusters, often with GPUs from multiple vendors. However, current deep learning frameworks lack support for collective communication across heterogeneous GPUs, leading to inefficiency and higher costs. We present HetCCL, a collective communication library that unifies vendor-specific backends and enables RDMA-based communication across GPUs without requiring driver modifications. HetCCL introduces two novel mechanisms that enable cross-vendor communication while leveraging optimized vendor libraries, NVIDIA NCCL and AMD RCCL. Evaluations on a multi-vendor GPU cluster show that HetCCL matches NCCL and RCCL performance in homogeneous setups while uniquely scaling in heterogeneous environments, enabling practical, high-performance training with both NVIDIA and AMD GPUs without changes to existing deep learning applications.

