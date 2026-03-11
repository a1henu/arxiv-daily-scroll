---
layout: default
title: FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation
---

# FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation
**arXiv**：[2603.09046v1](https://arxiv.org/abs/2603.09046) · [PDF](https://arxiv.org/pdf/2603.09046.pdf)  
**作者**：Yinpeng Wu, Yitong Chen, Lixiang Wang, Jinyu Gu, Zhichao Hua, Yubin Xia  

**一句话要点**：提出FlexServe系统，通过灵活资源隔离在移动设备上实现快速安全的LLM推理

**关键词**：移动设备LLM推理, ARM TrustZone安全, 灵活资源隔离, 安全NPU, 多模型调度, 时间到首令牌加速

## 3 点简述
- 核心问题：ARM TrustZone保护LLM推理时因内存和NPU隔离不灵活导致高开销
- 方法要点：设计灵活资源隔离机制，包括Flex-Mem和Flex-NPU，支持高效模式切换
- 实验或效果：相比基线设计，平均TTFT加速10.05倍，多模型工作流端到端加速最高24.30倍

## 摘要（原文）

> Device-side Large Language Models (LLMs) have witnessed explosive growth, offering higher privacy and availability compared to cloud-side LLMs. During LLM inference, both model weights and user data are valuable, and attackers may even compromise the OS kernel to steal them. ARM TrustZone is the de facto hardware-based isolation technology on mobile devices, used to protect sensitive applications from a compromised OS. However, protecting LLM inference with TrustZone incurs significant overhead due to its inflexible isolation of memory and the NPU. To address these challenges, this paper introduces FlexServe, a fast and secure LLM serving system for mobile devices. It first introduces a Flexible Resource Isolation mechanism to construct Flexible Secure Memory (Flex-Mem) and Flexible Secure NPU (Flex-NPU). Both memory pages and the NPU can be efficiently switched between unprotected and protected modes. Based on these mechanisms, FlexServe designs a fast and secure LLM inference framework within TrustZone's secure world. The LLM-Aware Memory Management and Secure Inference Pipeline are introduced to accelerate inference. A Multi-Model Scheduler is proposed to optimize multi-model workflows. We implement a prototype of FlexServe and compare it with two TrustZone-based strawman designs. The results show that FlexServe achieves an average $10.05\times$ speedup in Time to First Token (TTFT) compared to the strawman, and an average $2.44\times$ TTFT speedup compared to an optimized strawman with pipeline and secure NPU enabled. For multi-model agent workflows, the end-to-end speedup is up to $24.30\times$ and $4.05\times$ compared to the strawman and optimized strawman, respectively.

