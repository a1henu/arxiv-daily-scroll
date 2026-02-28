---
layout: default
title: Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention
---

# Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention
**arXiv**：[2602.22546v1](https://arxiv.org/abs/2602.22546) · [PDF](https://arxiv.org/pdf/2602.22546.pdf)  
**作者**：Zhiming Wang, Jinwei He, Feng Lu  

**一句话要点**：提出AHCE框架，通过主动请求专家推理增强LLM代理在专业领域的性能。

**关键词**：LLM代理增强, 人机协作, 专家推理请求, 主动学习策略, 专业领域任务

## 3 点简述
- 核心问题：LLM代理在专业领域因缺乏长尾知识而失败，人类专家指导非结构化且不可靠。
- 方法要点：AHCE框架包含人类反馈模块，学习策略将专家视为交互式推理工具进行按需协作。
- 实验或效果：在Minecraft实验中，任务成功率提升32%（普通难度）和近70%（高难度），人类干预最小化。

## 摘要（原文）

> Large Language Model (LLM) based agents excel at general reasoning but often fail in specialized domains where success hinges on long-tail knowledge absent from their training data. While human experts can provide this missing knowledge, their guidance is often unstructured and unreliable, making its direct integration into an agent's plan problematic. To address this, we introduce AHCE (Active Human-Augmented Challenge Engagement), a framework for on-demand Human-AI collaboration. At its core, the Human Feedback Module (HFM) employs a learned policy to treat the human expert as an interactive reasoning tool. Extensive experiments in Minecraft demonstrate the framework's effectiveness, increasing task success rates by 32% on normal difficulty tasks and nearly 70% on highly difficult tasks, all with minimal human intervention. Our work demonstrates that successfully augmenting agents requires learning how to request expert reasoning, moving beyond simple requests for help.

