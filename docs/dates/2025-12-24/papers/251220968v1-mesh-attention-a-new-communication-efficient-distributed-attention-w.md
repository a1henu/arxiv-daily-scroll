---
layout: default
title: Mesh-Attention: A New Communication-Efficient Distributed Attention with Improved Data Locality
---

# Mesh-Attention: A New Communication-Efficient Distributed Attention with Improved Data Locality
**arXiv**：[2512.20968v1](https://arxiv.org/abs/2512.20968) · [PDF](https://arxiv.org/pdf/2512.20968.pdf)  
**作者**：Sirui Chen, Jingji Chen, Siqi Zhu, Ziheng Jiang, Yanghua Peng, Xuehai Qian  

**一句话要点**：提出Mesh-Attention以解决分布式注意力中通信效率低的问题

**关键词**：分布式注意力, 通信效率, 大语言模型, GPU调度, 可扩展性

## 3 点简述
- 核心问题：现有Ring-Attention因通信流量大导致扩展性受限
- 方法要点：基于矩阵模型分配二维计算块，降低通信计算比
- 实验或效果：在256 GPU上平均加速2.9倍，通信量减少79.0%

## 摘要（原文）

> Distributed attention is a fundamental problem for scaling context window for Large Language Models (LLMs). The state-of-the-art method, Ring-Attention, suffers from scalability limitations due to its excessive communication traffic. This paper proposes a new distributed attention algorithm, Mesh-Attention, by rethinking the design space of distributed attention with a new matrix-based model. Our method assigns a two-dimensional tile -- rather than one-dimensional row or column -- of computation blocks to each GPU to achieve higher efficiency through lower communication-computation (CommCom) ratio. The general approach covers Ring-Attention as a special case, and allows the tuning of CommCom ratio with different tile shapes. Importantly, we propose a greedy algorithm that can efficiently search the scheduling space within the tile with restrictions that ensure efficient communication among GPUs. The theoretical analysis shows that Mesh-Attention leads to a much lower communication complexity and exhibits good scalability comparing to other current algorithms.
>   Our extensive experiment results show that Mesh-Attention can achieve up to 3.4x speedup (2.9x on average) and reduce the communication volume by up to 85.4% (79.0% on average) on 256 GPUs. Our scalability results further demonstrate that Mesh-Attention sustains superior performance as the system scales, substantially reducing overhead in large-scale deployments. The results convincingly confirm the advantage of Mesh-Attention.

