---
layout: default
title: CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty
---

# CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty
**arXiv**：[2601.22027v1](https://arxiv.org/abs/2601.22027) · [PDF](https://arxiv.org/pdf/2601.22027.pdf)  
**作者**：Johannes Kirmayr, Lukas Stappen, Elisabeth André  

**一句话要点**：提出CAR-bench以评估车载语音助手场景下LLM代理在现实不确定性中的一致性和能力感知

**关键词**：LLM代理评估, 车载语音助手, 不确定性处理, 工具使用, 一致性测试, 能力感知

## 3 点简述
- 现有基准忽视LLM代理在现实应用中的可靠性，如处理不完整或模糊请求时的内在不确定性
- CAR-bench引入多轮对话、工具使用和策略遵守，测试一致性、不确定性处理和能力感知
- 基线结果显示前沿LLM在消歧任务中一致通过率低于50%，在幻觉任务中常违反策略或捏造信息

## 摘要（原文）

> Existing benchmarks for Large Language Model (LLM) agents focus on task completion under idealistic settings but overlook reliability in real-world, user-facing applications. In domains, such as in-car voice assistants, users often issue incomplete or ambiguous requests, creating intrinsic uncertainty that agents must manage through dialogue, tool use, and policy adherence. We introduce CAR-bench, a benchmark for evaluating consistency, uncertainty handling, and capability awareness in multi-turn, tool-using LLM agents in an in-car assistant domain. The environment features an LLM-simulated user, domain policies, and 58 interconnected tools spanning navigation, productivity, charging, and vehicle control. Beyond standard task completion, CAR-bench introduces Hallucination tasks that test agents' limit-awareness under missing tools or information, and Disambiguation tasks that require resolving uncertainty through clarification or internal information gathering. Baseline results reveal large gaps between occasional and consistent success on all task types. Even frontier reasoning LLMs achieve less than 50% consistent pass rate on Disambiguation tasks due to premature actions, and frequently violate policies or fabricate information to satisfy user requests in Hallucination tasks, underscoring the need for more reliable and self-aware LLM agents in real-world settings.

