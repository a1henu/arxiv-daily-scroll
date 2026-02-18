---
layout: default
title: Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections
---

# Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections
**arXiv**：[2602.15654v1](https://arxiv.org/abs/2602.15654) · [PDF](https://arxiv.org/pdf/2602.15654.pdf)  
**作者**：Xianglin Yang, Yufei He, Shuo Ji, Bryan Hooi, Jin Song Dong  

**一句话要点**：提出僵尸代理攻击框架，揭示自进化LLM代理在长期记忆更新中的持久安全风险。

**关键词**：自进化LLM代理, 长期记忆安全, 僵尸代理攻击, 黑盒攻击框架, 持久控制风险, 记忆演化漏洞

## 3 点简述
- 核心问题：自进化LLM代理通过长期记忆更新提升任务性能，但外部恶意内容可被存储并后续执行，导致持久攻击风险。
- 方法要点：设计黑盒攻击框架，分感染和触发两阶段，利用正常记忆更新机制植入载荷，抵抗截断和相关性过滤。
- 实验或效果：在代表性代理设置中评估攻击，显示记忆演化能将一次性间接注入转化为持久妥协，提示仅会话级过滤防御不足。

## 摘要（原文）

> Self-evolving LLM agents update their internal state across sessions, often by writing and reusing long-term memory. This design improves performance on long-horizon tasks but creates a security risk: untrusted external content observed during a benign session can be stored as memory and later treated as instruction. We study this risk and formalize a persistent attack we call a Zombie Agent, where an attacker covertly implants a payload that survives across sessions, effectively turning the agent into a puppet of the attacker.
>   We present a black-box attack framework that uses only indirect exposure through attacker-controlled web content. The attack has two phases. During infection, the agent reads a poisoned source while completing a benign task and writes the payload into long-term memory through its normal update process. During trigger, the payload is retrieved or carried forward and causes unauthorized tool behavior. We design mechanism-specific persistence strategies for common memory implementations, including sliding-window and retrieval-augmented memory, to resist truncation and relevance filtering. We evaluate the attack on representative agent setups and tasks, measuring both persistence over time and the ability to induce unauthorized actions while preserving benign task quality. Our results show that memory evolution can convert one-time indirect injection into persistent compromise, which suggests that defenses focused only on per-session prompt filtering are not sufficient for self-evolving agents.

