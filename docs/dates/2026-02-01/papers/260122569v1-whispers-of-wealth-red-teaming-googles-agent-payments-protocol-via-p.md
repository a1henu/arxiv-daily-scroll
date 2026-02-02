---
layout: default
title: Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection
---

# Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection
**arXiv**：[2601.22569v1](https://arxiv.org/abs/2601.22569) · [PDF](https://arxiv.org/pdf/2601.22569.pdf)  
**作者**：Tanusree Debi, Wentian Zhu  

**一句话要点**：提出品牌耳语攻击和保险库耳语攻击，揭示基于LLM的代理支付协议在提示注入下的脆弱性。

**关键词**：代理支付协议, 提示注入攻击, LLM安全, 红队评估, 金融交易自动化

## 3 点简述
- 核心问题：LLM代理在金融交易中依赖上下文推理，易受提示注入攻击，威胁支付安全。
- 方法要点：通过间接和直接提示注入，设计攻击技术操纵产品排名和提取用户敏感数据。
- 实验或效果：基于Gemini-2.5-Flash和Google ADK框架构建AP2购物代理，验证攻击可可靠颠覆代理行为。

## 摘要（原文）

> Large language model (LLM) based agents are increasingly used to automate financial transactions, yet their reliance on contextual reasoning exposes payment systems to prompt-driven manipulation. The Agent Payments Protocol (AP2) aims to secure agent-led purchases through cryptographically verifiable mandates, but its practical robustness remains underexplored. In this work, we perform an AI red-teaming evaluation of AP2 and identify vulnerabilities arising from indirect and direct prompt injection. We introduce two attack techniques, the Branded Whisper Attack and the Vault Whisper Attack which manipulate product ranking and extract sensitive user data. Using a functional AP2 based shopping agent built with Gemini-2.5-Flash and the Google ADK framework, we experimentally validate that simple adversarial prompts can reliably subvert agent behavior. Our findings reveal critical weaknesses in current agentic payment architectures and highlight the need for stronger isolation and defensive safeguards in LLM-mediated financial systems.

