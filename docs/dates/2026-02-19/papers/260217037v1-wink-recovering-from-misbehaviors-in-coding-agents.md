---
layout: default
title: Wink: Recovering from Misbehaviors in Coding Agents
---

# Wink: Recovering from Misbehaviors in Coding Agents
**arXiv**：[2602.17037v1](https://arxiv.org/abs/2602.17037) · [PDF](https://arxiv.org/pdf/2602.17037.pdf)  
**作者**：Rahul Nanda, Chandra Maddila, Smriti Jha, Euna Mehnaz Khan, Matteo Paltenghi, Satish Chandra  

**一句话要点**：提出Wink系统以自动恢复编码代理的异常行为，提升软件工程自动化效率。

**关键词**：编码代理, 异常行为恢复, 自干预系统, 软件工程自动化, 工具调用优化, 生产环境部署

## 3 点简述
- 核心问题：编码代理常出现规范漂移、推理问题和工具调用失败等异常行为，影响开发流程。
- 方法要点：开发轻量级异步自干预系统Wink，通过观察代理轨迹并提供针对性指导来纠正行为。
- 实验或效果：在超1万条真实轨迹上评估，单次干预成功解决90%异常，生产环境A/B测试显著减少工具调用失败和工程师干预。

## 摘要（原文）

> Autonomous coding agents, powered by large language models (LLMs), are increasingly being adopted in the software industry to automate complex engineering tasks. However, these agents are prone to a wide range of misbehaviors, such as deviating from the user's instructions, getting stuck in repetitive loops, or failing to use tools correctly. These failures disrupt the development workflow and often require resource-intensive manual intervention. In this paper, we present a system for automatically recovering from agentic misbehaviors at scale. We first introduce a taxonomy of misbehaviors grounded in an analysis of production traffic, identifying three primary categories: Specification Drift, Reasoning Problems, and Tool Call Failures, which we find occur in about 30% of all agent trajectories.
>   To address these issues, we developed a lightweight, asynchronous self-intervention system named Wink. Wink observes agent trajectories and provides targeted course-correction guidance to nudge the agent back to a productive path. We evaluated our system on over 10,000 real world agent trajectories and found that it successfully resolves 90% of the misbehaviors that require a single intervention. Furthermore, a live A/B test in our production environment demonstrated that our system leads to a statistically significant reduction in Tool Call Failures, Tokens per Session and Engineer Interventions per Session. We present our experience designing and deploying this system, offering insights into the challenges of building resilient agentic systems at scale.

