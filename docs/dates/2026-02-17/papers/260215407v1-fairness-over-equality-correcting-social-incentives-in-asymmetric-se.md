---
layout: default
title: Fairness over Equality: Correcting Social Incentives in Asymmetric Sequential Social Dilemmas
---

# Fairness over Equality: Correcting Social Incentives in Asymmetric Sequential Social Dilemmas
**arXiv**：[2602.15407v1](https://arxiv.org/abs/2602.15407) · [PDF](https://arxiv.org/pdf/2602.15407.pdf)  
**作者**：Alper Demir, Hüseyin Aydın, Kale-ab Abebe Tessera, David Abel, Stefano V. Albrecht  

**一句话要点**：提出基于奖励范围和局部反馈的公平性修正方法，以解决非对称序列社会困境中的合作问题。

**关键词**：序列社会困境, 多智能体强化学习, 公平性修正, 非对称环境, 合作涌现, 局部反馈

## 3 点简述
- 核心问题：现有公平性方法在非对称序列社会困境中因强制平等而错误激励背叛，导致合作困难。
- 方法要点：重新定义公平性以考虑智能体奖励范围，引入基于智能体的加权机制，并局部化社会反馈以无需全局信息。
- 实验或效果：在非对称场景中，该方法比现有方法更快促进合作策略的涌现，且保持可扩展性和实用性。

## 摘要（原文）

> Sequential Social Dilemmas (SSDs) provide a key framework for studying how cooperation emerges when individual incentives conflict with collective welfare. In Multi-Agent Reinforcement Learning, these problems are often addressed by incorporating intrinsic drives that encourage prosocial or fair behavior. However, most existing methods assume that agents face identical incentives in the dilemma and require continuous access to global information about other agents to assess fairness. In this work, we introduce asymmetric variants of well-known SSD environments and examine how natural differences between agents influence cooperation dynamics. Our findings reveal that existing fairness-based methods struggle to adapt under asymmetric conditions by enforcing raw equality that wrongfully incentivize defection. To address this, we propose three modifications: (i) redefining fairness by accounting for agents' reward ranges, (ii) introducing an agent-based weighting mechanism to better handle inherent asymmetries, and (iii) localizing social feedback to make the methods effective under partial observability without requiring global information sharing. Experimental results show that in asymmetric scenarios, our method fosters faster emergence of cooperative policies compared to existing approaches, without sacrificing scalability or practicality.

