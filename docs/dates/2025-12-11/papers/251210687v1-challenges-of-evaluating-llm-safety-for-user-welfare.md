---
layout: default
title: Challenges of Evaluating LLM Safety for User Welfare
---

# Challenges of Evaluating LLM Safety for User Welfare
**arXiv**：[2512.10687v1](https://arxiv.org/abs/2512.10687) · [PDF](https://arxiv.org/pdf/2512.10687.pdf)  
**作者**：Manon Kempermann, Sai Suresh Macharla Vasu, Mahalakshmi Raveenthiran, Theo Farrell, Ingmar Weber  

**一句话要点**：提出基于用户情境的安全评估方法，以解决LLM在个人高风险建议中的安全评估挑战。

**关键词**：LLM安全评估, 用户情境感知, 高风险建议, 脆弱用户, 评估方法学, 数据集发布

## 3 点简述
- 核心问题：现有LLM安全评估聚焦通用风险，忽略用户情境依赖的个体危害，如金融和健康建议。
- 方法要点：通过评估GPT-5、Claude Sonnet 4和Gemini 2.5 Pro，比较情境盲与情境感知评估者的安全评分差异。
- 实验或效果：发现情境感知评估显著降低高脆弱用户的安全评分，且仅靠用户披露情境的提示不足以改善评估效果。

## 摘要（原文）

> Safety evaluations of large language models (LLMs) typically focus on universal risks like dangerous capabilities or undesirable propensities. However, millions use LLMs for personal advice on high-stakes topics like finance and health, where harms are context-dependent rather than universal. While frameworks like the OECD's AI classification recognize the need to assess individual risks, user-welfare safety evaluations remain underdeveloped. We argue that developing such evaluations is non-trivial due to fundamental questions about accounting for user context in evaluation design. In this exploratory study, we evaluated advice on finance and health from GPT-5, Claude Sonnet 4, and Gemini 2.5 Pro across user profiles of varying vulnerability. First, we demonstrate that evaluators must have access to rich user context: identical LLM responses were rated significantly safer by context-blind evaluators than by those aware of user circumstances, with safety scores for high-vulnerability users dropping from safe (5/7) to somewhat unsafe (3/7). One might assume this gap could be addressed by creating realistic user prompts containing key contextual information. However, our second study challenges this: we rerun the evaluation on prompts containing context users report they would disclose, finding no significant improvement. Our work establishes that effective user-welfare safety evaluation requires evaluators to assess responses against diverse user profiles, as realistic user context disclosure alone proves insufficient, particularly for vulnerable populations. By demonstrating a methodology for context-aware evaluation, this study provides both a starting point for such assessments and foundational evidence that evaluating individual welfare demands approaches distinct from existing universal-risk frameworks. We publish our code and dataset to aid future developments.

