---
layout: default
title: DMind-3: A Sovereign Edge--Local--Cloud AI System with Controlled Deliberation and Correction-Based Tuning for Safe, Low-Latency Transaction Execution
---

# DMind-3: A Sovereign Edge--Local--Cloud AI System with Controlled Deliberation and Correction-Based Tuning for Safe, Low-Latency Transaction Execution
**arXiv**：[2602.11651v1](https://arxiv.org/abs/2602.11651) · [PDF](https://arxiv.org/pdf/2602.11651.pdf)  
**作者**：Enhao Huang, Frank Li, Tony Lin, Lowes Yang  

**一句话要点**：提出DMind-3主权边缘-本地-云AI系统，以解决Web3环境中安全低延迟交易执行问题。

**关键词**：主权AI系统, 边缘计算, Web3安全, 分层预测合成, 对比校正微调, 低延迟交易

## 3 点简述
- 核心问题：现有云中心助手牺牲隐私且网络拥塞时失效，纯本地方案缺乏全局生态上下文。
- 方法要点：采用三层协作架构，包括边缘确定性签名意图防火墙、本地私有高保真推理引擎和云策略治理全局上下文合成器。
- 实验或效果：在协议约束任务中实现93.7%多轮成功率，优于通用基线，提供可扩展安全框架。

## 摘要（原文）

> This paper introduces DMind-3, a sovereign Edge-Local-Cloud intelligence stack designed to secure irreversible financial execution in Web3 environments against adversarial risks and strict latency constraints. While existing cloud-centric assistants compromise privacy and fail under network congestion, and purely local solutions lack global ecosystem context, DMind-3 resolves these tensions by decomposing capability into three cooperating layers: a deterministic signing-time intent firewall at the edge, a private high-fidelity reasoning engine on user hardware, and a policy-governed global context synthesizer in the cloud. We propose policy-driven selective offloading to route computation based on privacy sensitivity and uncertainty, supported by two novel training objectives: Hierarchical Predictive Synthesis (HPS) for fusing time-varying macro signals, and Contrastive Chain-of-Correction Supervised Fine-Tuning (C$^3$-SFT) to enhance local verification reliability. Extensive evaluations demonstrate that DMind-3 achieves a 93.7% multi-turn success rate in protocol-constrained tasks and superior domain reasoning compared to general-purpose baselines, providing a scalable framework where safety is bound to the edge execution primitive while maintaining sovereignty over sensitive user intent.

