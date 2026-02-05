---
layout: default
title: SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
---

# SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing
**arXiv**：[2602.04418v1](https://arxiv.org/abs/2602.04418) · [PDF](https://arxiv.org/pdf/2602.04418.pdf)  
**作者**：Arnab Mallick, Indraveni Chebolu, Harmesh Rana  

**一句话要点**：提出SPEAR多智能体协调框架，用于智能合约审计的安全分析工作流。

**关键词**：智能合约审计, 多智能体系统, 协调框架, 安全分析, MAS模式

## 3 点简述
- 核心问题：智能合约审计中多智能体协调与恢复机制的设计挑战。
- 方法要点：采用规划、执行和修复智能体，结合MAS模式如合同网协议和AGM信念修订。
- 实验或效果：通过实证研究比较多智能体设计与集中式、流水线式方案在故障场景下的表现。

## 摘要（原文）

> We present SPEAR, a multi-agent coordination framework for smart contract auditing that applies established MAS patterns in a realistic security analysis workflow. SPEAR models auditing as a coordinated mission carried out by specialized agents: a Planning Agent prioritizes contracts using risk-aware heuristics, an Execution Agent allocates tasks via the Contract Net protocol, and a Repair Agent autonomously recovers from brittle generated artifacts using a programmatic-first repair policy. Agents maintain local beliefs updated through AGM-compliant revision, coordinate via negotiation and auction protocols, and revise plans as new information becomes available. An empirical study compares the multi-agent design with centralized and pipeline-based alternatives under controlled failure scenarios, focusing on coordination, recovery behavior, and resource use.

