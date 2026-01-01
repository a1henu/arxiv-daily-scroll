---
layout: default
title: R-Debater: Retrieval-Augmented Debate Generation through Argumentative Memory
---

# R-Debater: Retrieval-Augmented Debate Generation through Argumentative Memory
**arXiv**：[2512.24684v1](https://arxiv.org/abs/2512.24684) · [PDF](https://arxiv.org/pdf/2512.24684.pdf)  
**作者**：Maoyuan Li, Zhongsheng Wang, Haoyuan Li, Jiamou Liu  

**一句话要点**：提出R-Debater框架，通过论证记忆增强检索以生成多轮辩论

**关键词**：辩论生成, 检索增强, 论证记忆, 多轮对话, 角色代理, 知识库检索

## 3 点简述
- 核心问题：如何生成一致、证据支持的多轮辩论，保持立场连贯性并回应对手
- 方法要点：集成辩论知识库检索案例证据和先验辩论动作，结合基于角色的代理生成连贯话语
- 实验或效果：在ORCHID数据集上评估，R-Debater在单轮和多轮任务中优于LLM基线，人类评估确认其一致性和证据使用

## 摘要（原文）

> We present R-Debater, an agentic framework for generating multi-turn debates built on argumentative memory. Grounded in rhetoric and memory studies, the system views debate as a process of recalling and adapting prior arguments to maintain stance consistency, respond to opponents, and support claims with evidence. Specifically, R-Debater integrates a debate knowledge base for retrieving case-like evidence and prior debate moves with a role-based agent that composes coherent utterances across turns. We evaluate on standardized ORCHID debates, constructing a 1,000-item retrieval corpus and a held-out set of 32 debates across seven domains. Two tasks are evaluated: next-utterance generation, assessed by InspireScore (subjective, logical, and factual), and adversarial multi-turn simulations, judged by Debatrix (argument, source, language, and overall). Compared with strong LLM baselines, R-Debater achieves higher single-turn and multi-turn scores. Human evaluation with 20 experienced debaters further confirms its consistency and evidence use, showing that combining retrieval grounding with structured planning yields more faithful, stance-aligned, and coherent debates across turns.

