---
layout: default
title: The Promptware Kill Chain: How Prompt Injections Gradually Evolved Into a Multi-Step Malware
---

# The Promptware Kill Chain: How Prompt Injections Gradually Evolved Into a Multi-Step Malware
**arXiv**：[2601.09625v1](https://arxiv.org/abs/2601.09625) · [PDF](https://arxiv.org/pdf/2601.09625.pdf)  
**作者**：Ben Nassi, Bruce Schneier, Oleg Brodt  

**一句话要点**：提出提示软件杀伤链模型以分析LLM系统多步攻击威胁

**关键词**：提示软件, 杀伤链模型, LLM安全, 多步攻击, 威胁建模, AI安全

## 3 点简述
- 核心问题：LLM系统攻击常被简化为提示注入，但实际涉及多步序列，类似传统恶意软件活动。
- 方法要点：引入五步杀伤链模型，包括初始访问、权限提升、持久化、横向移动和目标行动。
- 实验或效果：通过映射近期攻击案例，验证模型能系统化分析威胁，为安全实践提供结构化方法。

## 摘要（原文）

> The rapid adoption of large language model (LLM)-based systems -- from chatbots to autonomous agents capable of executing code and financial transactions -- has created a new attack surface that existing security frameworks inadequately address. The dominant framing of these threats as "prompt injection" -- a catch-all phrase for security failures in LLM-based systems -- obscures a more complex reality: Attacks on LLM-based systems increasingly involve multi-step sequences that mirror traditional malware campaigns. In this paper, we propose that attacks targeting LLM-based applications constitute a distinct class of malware, which we term \textit{promptware}, and introduce a five-step kill chain model for analyzing these threats. The framework comprises Initial Access (prompt injection), Privilege Escalation (jailbreaking), Persistence (memory and retrieval poisoning), Lateral Movement (cross-system and cross-user propagation), and Actions on Objective (ranging from data exfiltration to unauthorized transactions). By mapping recent attacks to this structure, we demonstrate that LLM-related attacks follow systematic sequences analogous to traditional malware campaigns. The promptware kill chain offers security practitioners a structured methodology for threat modeling and provides a common vocabulary for researchers across AI safety and cybersecurity to address a rapidly evolving threat landscape.

