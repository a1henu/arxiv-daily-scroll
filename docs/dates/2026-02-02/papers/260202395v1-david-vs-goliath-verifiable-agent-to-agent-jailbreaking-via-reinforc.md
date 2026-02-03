---
layout: default
title: David vs. Goliath: Verifiable Agent-to-Agent Jailbreaking via Reinforcement Learning
---

# David vs. Goliath: Verifiable Agent-to-Agent Jailbreaking via Reinforcement Learning
**arXiv**：[2602.02395v1](https://arxiv.org/abs/2602.02395) · [PDF](https://arxiv.org/pdf/2602.02395.pdf)  
**作者**：Samuel Nellessen, Tal Kachman  

**一句话要点**：提出Tag-Along攻击威胁模型与Slingshot强化学习框架，以验证工具增强环境中代理间越狱风险。

**关键词**：代理越狱, 强化学习攻击, 工具增强环境, 威胁模型验证, 零样本迁移

## 3 点简述
- 核心问题：大型语言模型作为自主代理时，攻击者可能通过对话滥用工具权限，形成Tag-Along攻击威胁。
- 方法要点：开发Slingshot强化学习框架，从零开始自动发现攻击向量，生成简短指令式模式而非多轮说服。
- 实验或效果：在极端难度任务上，Slingshot对Qwen2.5-32B-Instruct-AWQ攻击成功率达67.0%，并零样本迁移至其他模型家族。

## 摘要（原文）

> The evolution of large language models into autonomous agents introduces adversarial failures that exploit legitimate tool privileges, transforming safety evaluation in tool-augmented environments from a subjective NLP task into an objective control problem. We formalize this threat model as Tag-Along Attacks: a scenario where a tool-less adversary "tags along" on the trusted privileges of a safety-aligned Operator to induce prohibited tool use through conversation alone. To validate this threat, we present Slingshot, a 'cold-start' reinforcement learning framework that autonomously discovers emergent attack vectors, revealing a critical insight: in our setting, learned attacks tend to converge to short, instruction-like syntactic patterns rather than multi-turn persuasion. On held-out extreme-difficulty tasks, Slingshot achieves a 67.0% success rate against a Qwen2.5-32B-Instruct-AWQ Operator (vs. 1.7% baseline), reducing the expected attempts to first success (on solved tasks) from 52.3 to 1.3. Crucially, Slingshot transfers zero-shot to several model families, including closed-source models like Gemini 2.5 Flash (56.0% attack success rate) and defensive-fine-tuned open-source models like Meta-SecAlign-8B (39.2% attack success rate). Our work establishes Tag-Along Attacks as a first-class, verifiable threat model and shows that effective agentic attacks can be elicited from off-the-shelf open-weight models through environment interaction alone.

