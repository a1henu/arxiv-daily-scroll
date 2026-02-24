---
layout: default
title: LLM-enabled Applications Require System-Level Threat Monitoring
---

# LLM-enabled Applications Require System-Level Threat Monitoring
**arXiv**：[2602.19844v1](https://arxiv.org/abs/2602.19844) · [PDF](https://arxiv.org/pdf/2602.19844.pdf)  
**作者**：Yedi Zhang, Haoyu Wang, Xianglin Yang, Jin Song Dong, Jun Sun  

**一句话要点**：主张系统级威胁监控作为LLM应用可靠部署的先决条件

**关键词**：LLM应用安全, 系统级监控, 威胁检测, 可靠性挑战, 事件响应框架

## 3 点简述
- 核心问题：LLM应用的非确定性和学习驱动特性引入新可靠性挑战，扩大安全攻击面
- 方法要点：将风险视为预期操作条件，需建立系统级威胁监控机制检测部署后异常
- 实验或效果：未知，本文为立场论文，强调监控机制作为事件响应框架的基础

## 摘要（原文）

> LLM-enabled applications are rapidly reshaping the software ecosystem by using large language models as core reasoning components for complex task execution. This paradigm shift, however, introduces fundamentally new reliability challenges and significantly expands the security attack surface, due to the non-deterministic, learning-driven, and difficult-to-verify nature of LLM behavior. In light of these emerging and unavoidable safety challenges, we argue that such risks should be treated as expected operational conditions rather than exceptional events, necessitating a dedicated incident-response perspective. Consequently, the primary barrier to trustworthy deployment is not further improving model capability but establishing system-level threat monitoring mechanisms that can detect and contextualize security-relevant anomalies after deployment -- an aspect largely underexplored beyond testing or guardrail-based defenses. Accordingly, this position paper advocates systematic and comprehensive monitoring of security threats in LLM-enabled applications as a prerequisite for reliable operation and a foundation for dedicated incident-response frameworks.

