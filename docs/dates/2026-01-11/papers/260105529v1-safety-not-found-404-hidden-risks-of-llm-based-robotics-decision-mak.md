---
layout: default
title: Safety Not Found (404): Hidden Risks of LLM-Based Robotics Decision Making
---

# Safety Not Found (404): Hidden Risks of LLM-Based Robotics Decision Making
**arXiv**：[2601.05529v1](https://arxiv.org/abs/2601.05529) · [PDF](https://arxiv.org/pdf/2601.05529.pdf)  
**作者**：Jua Han, Jaeyoon Seo, Jungbin Min, Jean Oh, Jihie Kim  

**一句话要点**：评估LLM在机器人安全决策中的风险，揭示其在火灾疏散等场景的严重漏洞

**关键词**：LLM安全评估, 机器人决策, 空间推理, 灾难性风险, 火灾疏散场景

## 3 点简述
- 核心问题：LLM在安全关键场景的微小错误可导致灾难性后果，需系统评估其风险。
- 方法要点：通过定性火灾疏散案例，设计三类定量任务（完整信息、不完整信息、安全导向空间推理）。
- 实验或效果：基准测试显示模型在ASCII导航中成功率低，模拟火灾中引导机器人走向危险区域。

## 摘要（原文）

> One mistake by an AI system in a safety-critical setting can cost lives. As Large Language Models (LLMs) become integral to robotics decision-making, the physical dimension of risk grows; a single wrong instruction can directly endanger human safety. This paper addresses the urgent need to systematically evaluate LLM performance in scenarios where even minor errors are catastrophic. Through a qualitative evaluation of a fire evacuation scenario, we identified critical failure cases in LLM-based decision-making. Based on these, we designed seven tasks for quantitative assessment, categorized into: Complete Information, Incomplete Information, and Safety-Oriented Spatial Reasoning (SOSR). Complete information tasks utilize ASCII maps to minimize interpretation ambiguity and isolate spatial reasoning from visual processing. Incomplete information tasks require models to infer missing context, testing for spatial continuity versus hallucinations. SOSR tasks use natural language to evaluate safe decision-making in life-threatening contexts. We benchmark various LLMs and Vision-Language Models (VLMs) across these tasks. Beyond aggregate performance, we analyze the implications of a 1% failure rate, highlighting how "rare" errors escalate into catastrophic outcomes. Results reveal serious vulnerabilities: several models achieved a 0% success rate in ASCII navigation, while in a simulated fire drill, models instructed robots to move toward hazardous areas instead of emergency exits. Our findings lead to a sobering conclusion: current LLMs are not ready for direct deployment in safety-critical systems. A 99% accuracy rate is dangerously misleading in robotics, as it implies one out of every hundred executions could result in catastrophic harm. We demonstrate that even state-of-the-art models cannot guarantee safety, and absolute reliance on them creates unacceptable risks.

