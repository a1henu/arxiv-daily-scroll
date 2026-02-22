---
layout: default
title: ReIn: Conversational Error Recovery with Reasoning Inception
---

# ReIn: Conversational Error Recovery with Reasoning Inception
**arXiv**：[2602.17022v1](https://arxiv.org/abs/2602.17022) · [PDF](https://arxiv.org/pdf/2602.17022.pdf)  
**作者**：Takyoung Kim, Jinseok Nam, Chandrayee Basu, Xing Fan, Chengyuan Ma, Heng Ji, Gokhan Tur, Dilek Hakkani-Tür  

**一句话要点**：提出ReIn方法，通过植入初始推理实现对话错误恢复，无需修改模型参数或提示。

**关键词**：对话错误恢复, 推理植入, 测试时干预, 工具集成, 任务导向对话

## 3 点简述
- 核心问题：对话代理在用户诱导错误下易失败，需准确诊断并恢复。
- 方法要点：外部模块识别错误并生成恢复计划，集成到代理推理中引导纠正。
- 实验效果：ReIn显著提升任务成功率，优于显式提示修改方法，泛化至未见错误。

## 摘要（原文）

> Conversational agents powered by large language models (LLMs) with tool integration achieve strong performance on fixed task-oriented dialogue datasets but remain vulnerable to unanticipated, user-induced errors. Rather than focusing on error prevention, this work focuses on error recovery, which necessitates the accurate diagnosis of erroneous dialogue contexts and execution of proper recovery plans. Under realistic constraints precluding model fine-tuning or prompt modification due to significant cost and time requirements, we explore whether agents can recover from contextually flawed interactions and how their behavior can be adapted without altering model parameters and prompts. To this end, we propose Reasoning Inception (ReIn), a test-time intervention method that plants an initial reasoning into the agent's decision-making process. Specifically, an external inception module identifies predefined errors within the dialogue context and generates recovery plans, which are subsequently integrated into the agent's internal reasoning process to guide corrective actions, without modifying its parameters or system prompts. We evaluate ReIn by systematically simulating conversational failure scenarios that directly hinder successful completion of user goals: user's ambiguous and unsupported requests. Across diverse combinations of agent models and inception modules, ReIn substantially improves task success and generalizes to unseen error types. Moreover, it consistently outperforms explicit prompt-modification approaches, underscoring its utility as an efficient, on-the-fly method. In-depth analysis of its operational mechanism, particularly in relation to instruction hierarchy, indicates that jointly defining recovery tools with ReIn can serve as a safe and effective strategy for improving the resilience of conversational agents without modifying the backbone models or system prompts.

