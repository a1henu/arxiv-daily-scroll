---
layout: default
title: Agentic AI-RAN: Enabling Intent-Driven, Explainable and Self-Evolving Open RAN Intelligence
---

# Agentic AI-RAN: Enabling Intent-Driven, Explainable and Self-Evolving Open RAN Intelligence
**arXiv**：[2602.24115v1](https://arxiv.org/abs/2602.24115) · [PDF](https://arxiv.org/pdf/2602.24115.pdf)  
**作者**：Zhizhou He, Yang Luo, Xinkai Liu, Mahdi Boloursaz Mashhadi, Mohammad Shojafar, Merouane Debbah, Rahim Tafazolli  

**一句话要点**：提出基于智能体AI的O-RAN控制器，以提升网络切片和资源管理的性能与可解释性。

**关键词**：智能体AI, 开放无线接入网, 网络切片, 资源管理, 可解释性, 自演化

## 3 点简述
- 核心问题：O-RAN架构在多租户、多目标场景下操作复杂，缺乏安全可审计的控制机制。
- 方法要点：引入智能体AI原语（如规划-行动-观察-反思、技能工具使用、记忆与证据、自管理门控），构建长生命周期控制循环。
- 实验或效果：在模拟中，相比传统基线，平均减少8.83%的资源使用，并改善切片生命周期和RRM性能。

## 摘要（原文）

> Open RAN (O-RAN) exposes rich control and telemetry interfaces across the Non-RT RIC, Near-RT RIC, and distributed units, but also makes it harder to operate multi-tenant, multi-objective RANs in a safe and auditable manner. In parallel, agentic AI systems with explicit planning, tool use, memory, and self-management offer a natural way to structure long-lived control loops. This article surveys how such agentic controllers can be brought into O-RAN: we review the O-RAN architecture, contrast agentic controllers with conventional ML/RL xApps, and organise the task landscape around three clusters: network slice life-cycle, radio resource management (RRM) closed loops, and cross-cutting security, privacy, and compliance. We then introduce a small set of agentic primitives (Plan-Act-Observe-Reflect, skills as tool use, memory and evidence, and self-management gates) and show, in a multi-cell O-RAN simulation, how they improve slice life-cycle and RRM performance compared to conventional baselines and ablations that remove individual primitives. Security, privacy, and compliance are discussed as architectural constraints and open challenges for standards-aligned deployments. This framework achieves an average 8.83\% reduction in resource usage across three classic network slices.

