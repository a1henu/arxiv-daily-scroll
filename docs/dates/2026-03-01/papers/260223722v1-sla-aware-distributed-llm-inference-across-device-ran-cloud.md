---
layout: default
title: SLA-Aware Distributed LLM Inference Across Device-RAN-Cloud
---

# SLA-Aware Distributed LLM Inference Across Device-RAN-Cloud
**arXiv**：[2602.23722v1](https://arxiv.org/abs/2602.23722) · [PDF](https://arxiv.org/pdf/2602.23722.pdf)  
**作者**：Hariz Yet, Nguyen Thanh Tam, Mao V. Ngo, Lim Yi Shen, Lin Wei, Jihong Park, Binbin Chen, Tony Q. S. Quek  

**一句话要点**：提出SLA感知的分布式LLM推理框架，以解决跨设备-RAN-云异构部署中的实时推理挑战。

**关键词**：分布式LLM推理, SLA感知, 5G AI-RAN, 异构部署, 实时推理, MIG隔离

## 3 点简述
- 核心问题：在5G AI-RAN环境中，跨异构层（设备、RAN边缘、云）实现亚秒级LLM推理，同时避免干扰实时基带处理。
- 方法要点：基于固定基线策略，在5G SA测试床上测量不同层级的推理性能，评估量化模型和MIG隔离对SLA的影响。
- 实验或效果：发现RAN边缘的SLA可行性取决于模型变体选择，云层在0.5秒截止时间下挑战较大，但MIG隔离能保障基带处理安全。

## 摘要（原文）

> Embodied AI requires sub-second inference near the Radio Access Network (RAN), but deployments span heterogeneous tiers (on-device, RAN-edge, cloud) and must not disrupt real-time baseband processing. We report measurements from a 5G Standalone (SA) AI-RAN testbed using a fixed baseline policy for repeatability. The setup includes an on-device tier, a three-node RAN-edge cluster co-hosting a containerized 5G RAN, and a cloud tier. We find that on-device execution remains multi-second and fails to meet sub-second budgets. At the RAN edge, SLA feasibility is primarily determined by model variant choice: quantized models concentrate below 0.5\,s, while unquantized and some larger quantized models incur deadline misses due to stalls and queuing. In the cloud tier, meeting a 0.5\,s deadline is challenging on the measured WAN path (up to 32.9\% of requests complete within 0.5\,s), but all evaluated variants meet a 1.0\,s deadline (100\% within 1.0\,s). Under saturated downlink traffic and up to $N{=}20$ concurrent inference clients, Multi-Instance GPU (MIG) isolation preserves baseband timing-health proxies, supporting safe co-location under fixed partitioning.

