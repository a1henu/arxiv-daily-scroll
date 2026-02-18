---
layout: default
title: AI-Paging: Lease-Based Execution Anchoring for Network-Exposed AI-as-a-Service
---

# AI-Paging: Lease-Based Execution Anchoring for Network-Exposed AI-as-a-Service
**arXiv**：[2602.15286v1](https://arxiv.org/abs/2602.15286) · [PDF](https://arxiv.org/pdf/2602.15286.pdf)  
**作者**：Merve Saimler, Mohaned Chraiti  

**一句话要点**：提出AI-Paging机制，基于租约锚定执行以解决6G网络中AIaaS模型选择与放置问题。

**关键词**：AI-as-a-Service, 6G网络, 控制平面, 租约机制, QoS约束, 执行锚定

## 3 点简述
- 核心问题：AIaaS部署多提供商与模型层级，用户运行时选择模型超出其知识与控制范围。
- 方法要点：网络通过AI-paging控制平面交易，将意图解析为服务身份、会话令牌和租约，在策略与QoS约束下锚定执行端点。
- 实验或效果：原型基于现有机制实现，评估交易延迟、中断、租约到期正确性及移动与故障下的开销。

## 摘要（原文）

> With AI-as-a-Service (AIaaS) now deployed across multiple providers and model tiers, selecting the appropriate model instance at run time is increasingly outside the end user's knowledge and operational control. Accordingly, the 6G service providers are envisioned to play a crucial role in exposing AIaaS in a setting where users submit only an intent while the network helps in the intent-to-model matching (resolution) and execution placement under policy, trust, and Quality of Service (QoS) constraints. The network role becomes to discover candidate execution endpoints and selects a suitable model/anchor under policy and QoS constraints in a process referred here to as AI-paging (by analogy to cellular call paging). In the proposed architecture, AI-paging is a control-plane transaction that resolves an intent into an AI service identity (AISI), a scoped session token (AIST), and an expiring admission lease (COMMIT) that authorizes user-plane steering to a selected AI execution anchor (AEXF) under a QoS binding. AI-Paging enforces two invariants: (i) lease-gated steering (without COMMIT, no steering state is installed) and (ii) make-before-break anchoring to support continuity and reliability of AIaaS services under dynamic network conditions. We prototype AI-Paging using existing control- and user-plane mechanisms (service-based control, QoS flows, and policy-based steering) with no new packet headers, ensuring compatibility with existing 3GPP-based exposure and management architectures, and evaluate transaction latency, relocation interruption, enforcement correctness under lease expiry, and audit-evidence overhead under mobility and failures.

