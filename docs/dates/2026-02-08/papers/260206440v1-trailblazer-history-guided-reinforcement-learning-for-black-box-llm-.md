---
layout: default
title: TrailBlazer: History-Guided Reinforcement Learning for Black-Box LLM Jailbreaking
---

# TrailBlazer: History-Guided Reinforcement Learning for Black-Box LLM Jailbreaking
**arXiv**：[2602.06440v1](https://arxiv.org/abs/2602.06440) · [PDF](https://arxiv.org/pdf/2602.06440.pdf)  
**作者**：Sung-Hoon Yoon, Ruizhi Qian, Minda Zhao, Weiyue Li, Mengyu Wang  

**一句话要点**：提出历史感知强化学习框架TrailBlazer，以提升黑盒大语言模型越狱攻击的效率和成功率。

**关键词**：大语言模型越狱, 强化学习, 历史感知, 注意力机制, 黑盒攻击, 查询效率

## 3 点简述
- 核心问题：现有越狱方法未能有效利用交互历史中的漏洞信号，导致攻击效率低且不稳定。
- 方法要点：引入基于注意力的历史重加权机制，分析并突出关键漏洞，指导强化学习决策。
- 实验或效果：在AdvBench和HarmBench上实现最先进的越狱性能，显著提高查询效率。

## 摘要（原文）

> Large Language Models (LLMs) have become integral to many domains, making their safety a critical priority. Prior jailbreaking research has explored diverse approaches, including prompt optimization, automated red teaming, obfuscation, and reinforcement learning (RL) based methods. However, most existing techniques fail to effectively leverage vulnerabilities revealed in earlier interaction turns, resulting in inefficient and unstable attacks. Since jailbreaking involves sequential interactions in which each response influences future actions, reinforcement learning provides a natural framework for this problem. Motivated by this, we propose a history-aware RL-based jailbreak framework that analyzes and reweights vulnerability signals from prior steps to guide future decisions. We show that incorporating historical information alone improves jailbreak success rates. Building on this insight, we introduce an attention-based reweighting mechanism that highlights critical vulnerabilities within the interaction history, enabling more efficient exploration with fewer queries. Extensive experiments on AdvBench and HarmBench demonstrate that our method achieves state-of-the-art jailbreak performance while significantly improving query efficiency. These results underscore the importance of historical vulnerability signals in reinforcement learning-driven jailbreak strategies and offer a principled pathway for advancing adversarial research on LLM safeguards.

