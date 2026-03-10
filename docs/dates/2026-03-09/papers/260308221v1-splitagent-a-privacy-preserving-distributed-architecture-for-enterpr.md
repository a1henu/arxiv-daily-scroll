---
layout: default
title: SplitAgent: A Privacy-Preserving Distributed Architecture for Enterprise-Cloud Agent Collaboration
---

# SplitAgent: A Privacy-Preserving Distributed Architecture for Enterprise-Cloud Agent Collaboration
**arXiv**：[2603.08221v1](https://arxiv.org/abs/2603.08221) · [PDF](https://arxiv.org/pdf/2603.08221.pdf)  
**作者**：Jianshu She  

**一句话要点**：提出SplitAgent分布式架构以解决企业-云AI代理协作中的隐私保护难题

**关键词**：隐私保护, 分布式架构, 上下文感知脱敏, 差分隐私, 企业AI代理, 云协作

## 3 点简述
- 企业采用云端AI代理面临隐私困境：共享敏感数据或限制本地能力，现有框架不适用。
- 核心方法为上下文感知动态脱敏，基于任务语义自适应隐私保护，扩展协议提供差分隐私保证。
- 实验显示SplitAgent在任务准确率83.8%和隐私保护90.1%上优于静态方法，提升效用并减少泄漏。

## 摘要（原文）

> Enterprise adoption of cloud-based AI agents faces a fundamental privacy dilemma: leveraging powerful cloud models requires sharing sensitive data, while local processing limits capability. Current agent frameworks like MCP and A2A assume complete data sharing, making them unsuitable for enterprise environments with confidential information. We present SplitAgent, a novel distributed architecture that enables privacy-preserving collaboration between enterprise-side privacy agents and cloud-side reasoning agents. Our key innovation is context-aware dynamic sanitization that adapts privacy protection based on task semantics -- contract review requires different sanitization than code review or financial analysis. SplitAgent extends existing agent protocols with differential privacy guarantees, zero-knowledge tool verification, and privacy budget management. Through comprehensive experiments on enterprise scenarios, we demonstrate that SplitAgent achieves 83.8\% task accuracy while maintaining 90.1\% privacy protection, significantly outperforming static approaches (73.2\% accuracy, 79.7\% privacy). Context-aware sanitization improves task utility by 24.1\% over static methods while reducing privacy leakage by 67\%. Our architecture provides a practical path for enterprise AI adoption without compromising sensitive data.

