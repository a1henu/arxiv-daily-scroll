---
layout: default
title: Challenges of Evaluating LLM Safety for User Welfare
---

# Challenges of Evaluating LLM Safety for User Welfare
**arXiv**：[2512.10687v1](https://arxiv.org/abs/2512.10687) · [PDF](https://arxiv.org/pdf/2512.10687.pdf)  
**作者**：Manon Kempermann, Sai Suresh Macharla Vasu, Mahalakshmi Raveenthiran, Theo Farrell, Ingmar Weber  

**一句话要点**：提出基于用户情境的安全评估方法，以解决大语言模型在个人高风险建议中的安全评估挑战。

**关键词**：大语言模型安全评估, 用户福利风险, 情境感知评估, 高风险建议, 脆弱用户群体, 评估方法学

## 3 点简述
- 核心问题：现有LLM安全评估聚焦通用风险，忽视用户情境依赖的个人福利风险。
- 方法要点：设计情境感知评估，比较不同脆弱性用户档案下模型建议的安全性。
- 实验或效果：发现情境盲评估高估安全性，用户情境披露不足以改善评估，需多样化用户档案。

## 摘要（原文）

> Safety evaluations of large language models (LLMs) typically focus on universal risks like dangerous capabilities or undesirable propensities. However, millions use LLMs for personal advice on high-stakes topics like finance and health, where harms are context-dependent rather than universal. While frameworks like the OECD's AI classification recognize the need to assess individual risks, user-welfare safety evaluations remain underdeveloped. We argue that developing such evaluations is non-trivial due to fundamental questions about accounting for user context in evaluation design. In this exploratory study, we evaluated advice on finance and health from GPT-5, Claude Sonnet 4, and Gemini 2.5 Pro across user profiles of varying vulnerability. First, we demonstrate that evaluators must have access to rich user context: identical LLM responses were rated significantly safer by context-blind evaluators than by those aware of user circumstances, with safety scores for high-vulnerability users dropping from safe (5/7) to somewhat unsafe (3/7). One might assume this gap could be addressed by creating realistic user prompts containing key contextual information. However, our second study challenges this: we rerun the evaluation on prompts containing context users report they would disclose, finding no significant improvement. Our work establishes that effective user-welfare safety evaluation requires evaluators to assess responses against diverse user profiles, as realistic user context disclosure alone proves insufficient, particularly for vulnerable populations. By demonstrating a methodology for context-aware evaluation, this study provides both a starting point for such assessments and foundational evidence that evaluating individual welfare demands approaches distinct from existing universal-risk frameworks. We publish our code and dataset to aid future developments.

