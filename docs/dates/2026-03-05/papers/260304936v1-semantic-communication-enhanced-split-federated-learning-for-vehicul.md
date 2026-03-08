---
layout: default
title: Semantic Communication-Enhanced Split Federated Learning for Vehicular Networks: Architecture, Challenges, and Case Study
---

# Semantic Communication-Enhanced Split Federated Learning for Vehicular Networks: Architecture, Challenges, and Case Study
**arXiv**：[2603.04936v1](https://arxiv.org/abs/2603.04936) · [PDF](https://arxiv.org/pdf/2603.04936.pdf)  
**作者**：Lu Yu, Zheng Chang, Ying-Chang Liang  

**一句话要点**：提出语义通信增强的U型分割联邦学习框架，以解决车联网中通信开销和隐私问题。

**关键词**：语义通信, 分割联邦学习, 车联网, 隐私保护, 通信优化, 自适应压缩

## 3 点简述
- 核心问题：车联网中传统集中式学习通信开销大、隐私风险高，分割联邦学习存在通信瓶颈和标签隐私担忧。
- 方法要点：设计语义通信模块压缩传输任务相关语义信息，结合网络状态监控自适应调整压缩率，本地化敏感计算增强隐私。
- 实验或效果：框架在资源受限车联网环境中平衡通信负载、保护隐私并保持学习性能，通过案例研究验证有效性。

## 摘要（原文）

> Vehicular edge intelligence (VEI) is vital for future intelligent transportation systems. However, traditional centralized learning in dynamic vehicular networks faces significant communication overhead and privacy risks. Split federated learning (SFL) offers a distributed solution but is often hindered by substantial communication bottlenecks from transmitting high-dimensional intermediate features and can present label privacy concerns. Semantic communication offers a transformative approach to alleviate these communication challenges in SFL by focusing on transmitting only task-relevant information. This paper leverages the advantages of semantic communication in the design of SFL, and presents a case study the semantic communication-enhanced U-Shaped split federated learning (SC-USFL) framework that inherently enhances label privacy by localizing sensitive computations with reduced overhead. It features a dedicated semantic communication module (SCM), with pre-trained and parameter-frozen encoding/decoding units, to efficiently compress and transmit only the task-relevant semantic information over the critical uplink path from vehicular users to the edge server (ES). Furthermore, a network status monitor (NSM) module enables adaptive adjustment of the semantic compression rate in real-time response to fluctuating wireless channel conditions. The SC-USFL framework demonstrates a promising approach for efficiently balancing communication load, preserving privacy, and maintaining learning performance in resource-constrained vehicular environments. Finally, this paper highlights key open research directions to further advance the synergy between semantic communication and SFL in the vehicular network.

