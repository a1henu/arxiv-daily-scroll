---
layout: default
title: The Supportiveness-Safety Tradeoff in LLM Well-Being Agents
---

# The Supportiveness-Safety Tradeoff in LLM Well-Being Agents
**arXiv**：[2602.04487v1](https://arxiv.org/abs/2602.04487) · [PDF](https://arxiv.org/pdf/2602.04487.pdf)  
**作者**：Himanshi Lalwani, Hanan Salam  

**一句话要点**：评估LLM在福祉代理中支持性与安全性的权衡，发现适度支持提示可平衡两者。

**关键词**：大型语言模型, 社会辅助机器人, 提示设计, 安全性评估, 福祉支持, 共情质量

## 3 点简述
- 核心问题：LLM在福祉代理中，增加支持性提示如何影响安全性行为。
- 方法要点：使用6个LLM、3种支持性提示，在4个福祉领域合成查询评估。
- 实验或效果：适度支持提示提升共情与支持，保持安全；强验证提示显著降低安全。

## 摘要（原文）

> Large language models (LLMs) are being integrated into socially assistive robots (SARs) and other conversational agents providing mental health and well-being support. These agents are often designed to sound empathic and supportive in order to maximize user's engagement, yet it remains unclear how increasing the level of supportive framing in system prompts influences safety relevant behavior. We evaluated 6 LLMs across 3 system prompts with varying levels of supportiveness on 80 synthetic queries spanning 4 well-being domains (1440 responses). An LLM judge framework, validated against human ratings, assessed safety and care quality. Moderately supportive prompts improved empathy and constructive support while maintaining safety. In contrast, strongly validating prompts significantly degraded safety and, in some cases, care across all domains, with substantial variation across models. We discuss implications for prompt design, model selection, and domain specific safeguards in SARs deployment.

