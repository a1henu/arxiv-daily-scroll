---
layout: default
title: Trusted AI Agents in the Cloud
---

# Trusted AI Agents in the Cloud
**arXiv**：[2512.05951v1](https://arxiv.org/abs/2512.05951) · [PDF](https://arxiv.org/pdf/2512.05951.pdf)  
**作者**：Teofil Bodea, Masanori Misono, Julian Pritzi, Patrick Sabanic, Thore Sommer, Harshavardhan Unnibhavi, David Schall, Nuno Santos, Dimitrios Stavrakakis, Pramod Bhatotia  

**一句话要点**：提出Omega系统以解决云中AI代理在多方生态中的安全与信任问题

**关键词**：可信AI代理, 云安全, 机密计算, 多代理系统, 差分认证, 政策执行

## 3 点简述
- 核心问题：AI代理在云中运行时面临数据泄露、篡改等风险，现有CVMs缺乏跨主体信任和加速器隔离保障
- 方法要点：基于CVMs和Confidential GPUs构建可信代理平台，通过嵌套隔离、差分认证和政策框架实现端到端安全
- 实验或效果：在AMD SEV-SNP和NVIDIA H100上实现，确保CVM-GPU间状态安全，支持高性能、高密度、合规的多代理部署

## 摘要（原文）

> AI agents powered by large language models are increasingly deployed as cloud services that autonomously access sensitive data, invoke external tools, and interact with other agents. However, these agents run within a complex multi-party ecosystem, where untrusted components can lead to data leakage, tampering, or unintended behavior. Existing Confidential Virtual Machines (CVMs) provide only per binary protection and offer no guarantees for cross-principal trust, accelerator-level isolation, or supervised agent behavior. We present Omega, a system that enables trusted AI agents by enforcing end-to-end isolation, establishing verifiable trust across all contributing principals, and supervising every external interaction with accountable provenance. Omega builds on Confidential VMs and Confidential GPUs to create a Trusted Agent Platform that hosts many agents within a single CVM using nested isolation. It also provides efficient multi-agent orchestration with cross-principal trust establishment via differential attestation, and a policy specification and enforcement framework that governs data access, tool usage, and inter-agent communication for data protection and regulatory compliance. Implemented on AMD SEV-SNP and NVIDIA H100, Omega fully secures agent state across CVM-GPU, and achieves high performance while enabling high-density, policy-compliant multi-agent deployments at cloud scale.

