---
layout: default
title: AgentShield: Make MAS more secure and efficient
---

# AgentShield: Make MAS more secure and efficient
**arXiv**：[2511.22924v1](https://arxiv.org/abs/2511.22924) · [PDF](https://arxiv.org/pdf/2511.22924.pdf)  
**作者**：Kaixiang Wang, Zhaojiacheng Zhou, Bunyod Suvonov, Jiong Lou, Jie LI  

**一句话要点**：提出AgentShield分布式框架以增强多智能体系统安全与效率

**关键词**：多智能体系统, 对抗攻击防御, 分布式审计, 轻量模型, 共识机制, 安全效率权衡

## 3 点简述
- 核心问题：基于LLM的多智能体系统易受对抗攻击，现有防御存在单点故障或效率低下问题。
- 方法要点：采用三层防御机制，包括关键节点审计、轻量令牌审计和两轮共识审计，实现去中心化高效审计。
- 实验或效果：实验显示恢复率达92.5%，审计开销降低超70%，保持高协作准确性。

## 摘要（原文）

> Large Language Model (LLM)-based Multi-Agent Systems (MAS) offer powerful cooperative reasoning but remain vulnerable to adversarial attacks, where compromised agents can undermine the system's overall performance. Existing defenses either depend on single trusted auditors, creating single points of failure, or sacrifice efficiency for robustness. To resolve this tension, we propose \textbf{AgentShield}, a distributed framework for efficient, decentralized auditing. AgentShield introduces a novel three-layer defense: \textbf{(i) Critical Node Auditing} prioritizes high-influence agents via topological analysis; \textbf{(ii) Light Token Auditing} implements a cascade protocol using lightweight sentry models for rapid discriminative verification; and \textbf{(iii) Two-Round Consensus Auditing} triggers heavyweight arbiters only upon uncertainty to ensure global agreement. This principled design optimizes the robustness-efficiency trade-off. Experiments demonstrate that AgentShield achieves a 92.5\% recovery rate and reduces auditing overhead by over 70\% compared to existing methods, maintaining high collaborative accuracy across diverse MAS topologies and adversarial scenarios.

