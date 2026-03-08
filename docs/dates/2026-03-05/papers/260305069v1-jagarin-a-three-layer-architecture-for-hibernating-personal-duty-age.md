---
layout: default
title: Jagarin: A Three-Layer Architecture for Hibernating Personal Duty Agents on Mobile
---

# Jagarin: A Three-Layer Architecture for Hibernating Personal Duty Agents on Mobile
**arXiv**：[2603.05069v1](https://arxiv.org/abs/2603.05069) · [PDF](https://arxiv.org/pdf/2603.05069.pdf)  
**作者**：Ravi Kiran Kadaboina  

**一句话要点**：提出Jagarin三层架构，通过结构化休眠和需求驱动唤醒解决移动个人AI代理部署悖论。

**关键词**：移动AI代理, 结构化休眠, 需求驱动唤醒, 三层架构, 紧急度计算, 机器可读通信

## 3 点简述
- 核心问题：移动个人AI代理在持续后台执行与电池消耗、平台沙箱策略间的部署矛盾。
- 方法要点：三层架构包括DAWN（基于信号计算紧急度）、ARIA（邮件代理路由）和ACE（机器可读通信协议）。
- 实验或效果：在Android上演示Flutter原型，结合三层架构，仅用户发起时调用临时云代理。

## 摘要（原文）

> Personal AI agents face a fundamental deployment paradox on mobile: persistent background execution drains battery and violates platform sandboxing policies, yet purely reactive agents miss time-sensitive obligations until the user remembers to ask. We present Jagarin, a three-layer architecture that resolves this paradox through structured hibernation and demand-driven wake. The first layer, DAWN (Duty-Aware Wake Network), is an on-device heuristic engine that computes a composite urgency score from four signals: duty-typed optimal action windows, user behavioral engagement prediction, opportunity cost of inaction, and cross-duty batch resonance. It uses adaptive per-user thresholds to decide when a sleeping agent should nudge or escalate. The second layer, ARIA (Agent Relay Identity Architecture), is a commercial email identity proxy that routes the full commercial inbox -- obligations, promotional offers, loyalty rewards, and platform updates -- to appropriate DAWN handlers by message category, eliminating cold-start and removing manual data entry. The third layer, ACE (Agent-Centric Exchange), is a protocol framework for direct machine-readable communication from institutions to personal agents, replacing human-targeted email as the canonical channel. Together, these three layers form a complete stack from institutional signal to on-device action, without persistent cloud state, continuous background execution, or privacy compromise. A working Flutter prototype is demonstrated on Android, combining all three layers with an ephemeral cloud agent invoked only on user-initiated escalation.

