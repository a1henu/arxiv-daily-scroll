---
layout: default
title: A Content-Based Framework for Cybersecurity Refusal Decisions in Large Language Models
---

# A Content-Based Framework for Cybersecurity Refusal Decisions in Large Language Models
**arXiv**：[2602.15689v1](https://arxiv.org/abs/2602.15689) · [PDF](https://arxiv.org/pdf/2602.15689.pdf)  
**作者**：Meirav Segal, Noa Linder, Omer Antverg, Gil Gekker, Tomer Fichman, Omri Bodenheimer, Edan Maor, Omer Nevo  

**一句话要点**：提出基于内容的网络安全拒绝框架，以解决大语言模型在双用途任务中的不一致决策问题。

**关键词**：大语言模型, 网络安全拒绝, 内容基础框架, 攻防权衡, 风险感知策略

## 3 点简述
- 核心问题：现有拒绝方法依赖主题禁令或攻击分类，导致决策不一致、过度限制合法防御者。
- 方法要点：引入基于内容的框架，通过五个维度（如攻击行动贡献、防御效益）显式建模攻防权衡。
- 实验或效果：该框架能解决前沿模型行为不一致，支持可调、风险感知的拒绝策略构建。

## 摘要（原文）

> Large language models and LLM-based agents are increasingly used for cybersecurity tasks that are inherently dual-use. Existing approaches to refusal, spanning academic policy frameworks and commercially deployed systems, often rely on broad topic-based bans or offensive-focused taxonomies. As a result, they can yield inconsistent decisions, over-restrict legitimate defenders, and behave brittlely under obfuscation or request segmentation. We argue that effective refusal requires explicitly modeling the trade-off between offensive risk and defensive benefit, rather than relying solely on intent or offensive classification. In this paper, we introduce a content-based framework for designing and auditing cyber refusal policies that makes offense-defense tradeoffs explicit. The framework characterizes requests along five dimensions: Offensive Action Contribution, Offensive Risk, Technical Complexity, Defensive Benefit, and Expected Frequency for Legitimate Users, grounded in the technical substance of the request rather than stated intent. We demonstrate that this content-grounded approach resolves inconsistencies in current frontier model behavior and allows organizations to construct tunable, risk-aware refusal policies.

