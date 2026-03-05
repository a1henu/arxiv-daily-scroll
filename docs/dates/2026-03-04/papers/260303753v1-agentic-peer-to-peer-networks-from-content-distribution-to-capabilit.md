---
layout: default
title: Agentic Peer-to-Peer Networks: From Content Distribution to Capability and Action Sharing
---

# Agentic Peer-to-Peer Networks: From Content Distribution to Capability and Action Sharing
**arXiv**：[2603.03753v1](https://arxiv.org/abs/2603.03753) · [PDF](https://arxiv.org/pdf/2603.03753.pdf)  
**作者**：Taotao Wang, Lizhao You, Jingwen Tong, Chonghe Zhao, Shengli Zhang  

**一句话要点**：提出基于平面架构与分层验证的代理对等网络，以支持边缘AI代理间的安全能力与动作共享。

**关键词**：代理对等网络, 边缘AI代理, 能力共享, 分层验证, 语义发现, 安全协作

## 3 点简述
- 核心问题：代理对等网络中异构、状态依赖的能力与动作共享面临安全与发现挑战。
- 方法要点：采用平面参考架构解耦连接、语义发现与执行，并引入分层验证机制应对对抗环境。
- 实验或效果：通过离散事件模拟，显示分层验证显著提升端到端工作流成功率，同时保持发现延迟与控制开销稳定。

## 摘要（原文）

> The ongoing shift of AI models from centralized cloud APIs to local AI agents on edge devices is enabling \textit{Client-Side Autonomous Agents (CSAAs)} -- persistent personal agents that can plan, access local context, and invoke tools on behalf of users. As these agents begin to collaborate by delegating subtasks directly between clients, they naturally form \emph{Agentic Peer-to-Peer (P2P) Networks}. Unlike classic file-sharing overlays where the exchanged object is static, hash-indexed content (e.g., files in BitTorrent), agentic overlays exchange \emph{capabilities and actions} that are heterogeneous, state-dependent, and potentially unsafe if delegated to untrusted peers. This article outlines the networking foundations needed to make such collaboration practical. We propose a plane-based reference architecture that decouples connectivity/identity, semantic discovery, and execution. Besides, we introduce signed, soft-state capability descriptors to support intent- and constraint-aware discovery. To cope with adversarial settings, we further present a \textit{tiered verification} spectrum: Tier~1 relies on reputation signals, Tier~2 applies lightweight canary challenge-response with fallback selection, and Tier~3 requires evidence packages such as signed tool receipts/traces (and, when applicable, attestation). Using a discrete-event simulator that models registry-based discovery, Sybil-style index poisoning, and capability drift, we show that tiered verification substantially improves end-to-end workflow success while keeping discovery latency near-constant and control-plane overhead modest.

