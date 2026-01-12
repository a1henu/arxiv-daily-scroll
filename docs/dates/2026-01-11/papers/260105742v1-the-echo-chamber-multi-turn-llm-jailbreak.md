---
layout: default
title: The Echo Chamber Multi-Turn LLM Jailbreak
---

# The Echo Chamber Multi-Turn LLM Jailbreak
**arXiv**：[2601.05742v1](https://arxiv.org/abs/2601.05742) · [PDF](https://arxiv.org/pdf/2601.05742.pdf)  
**作者**：Ahmad Alobaid, Martí Jordà Roca, Carlos Castillo, Joan Vendrell  

**一句话要点**：提出Echo Chamber多轮攻击以解决LLM安全防护绕过问题

**关键词**：大语言模型安全, 多轮越狱攻击, 逐步升级策略, 聊天机器人防护, 模型评估

## 3 点简述
- 核心问题：多轮攻击作为新型越狱方法，通过精心设计的交互链绕过聊天机器人安全护栏。
- 方法要点：采用逐步升级策略，构建Echo Chamber攻击，详细描述并与其他多轮攻击比较。
- 实验或效果：通过广泛评估，展示该攻击在多个先进模型上的性能表现。

## 摘要（原文）

> The availability of Large Language Models (LLMs) has led to a new generation of powerful chatbots that can be developed at relatively low cost. As companies deploy these tools, security challenges need to be addressed to prevent financial loss and reputational damage. A key security challenge is jailbreaking, the malicious manipulation of prompts and inputs to bypass a chatbot's safety guardrails. Multi-turn attacks are a relatively new form of jailbreaking involving a carefully crafted chain of interactions with a chatbot. We introduce Echo Chamber, a new multi-turn attack using a gradual escalation method. We describe this attack in detail, compare it to other multi-turn attacks, and demonstrate its performance against multiple state-of-the-art models through extensive evaluation.

