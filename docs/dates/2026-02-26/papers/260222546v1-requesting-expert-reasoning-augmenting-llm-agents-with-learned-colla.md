---
layout: default
title: Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention
---

# Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention
**arXiv**：[2602.22546v1](https://arxiv.org/abs/2602.22546) · [PDF](https://arxiv.org/pdf/2602.22546.pdf)  
**作者**：Zhiming Wang, Jinwei He, Feng Lu  

**一句话要点**：提出AHCE框架以解决LLM代理在专业领域因长尾知识缺失而失败的问题

**关键词**：LLM代理增强, 人机协作, 长尾知识, 交互式推理, Minecraft实验

## 3 点简述
- 核心问题：LLM代理在专业领域因训练数据缺乏长尾知识而表现不佳，人类专家指导非结构化且不可靠
- 方法要点：AHCE框架通过Human Feedback Module学习策略，将人类专家视为交互式推理工具进行按需协作
- 实验或效果：在Minecraft实验中，任务成功率在普通难度提升32%，高难度提升近70%，人类干预最小化

## 摘要（原文）

> Large Language Model (LLM) based agents excel at general reasoning but often fail in specialized domains where success hinges on long-tail knowledge absent from their training data. While human experts can provide this missing knowledge, their guidance is often unstructured and unreliable, making its direct integration into an agent's plan problematic. To address this, we introduce AHCE (Active Human-Augmented Challenge Engagement), a framework for on-demand Human-AI collaboration. At its core, the Human Feedback Module (HFM) employs a learned policy to treat the human expert as an interactive reasoning tool. Extensive experiments in Minecraft demonstrate the framework's effectiveness, increasing task success rates by 32% on normal difficulty tasks and nearly 70% on highly difficult tasks, all with minimal human intervention. Our work demonstrates that successfully augmenting agents requires learning how to request expert reasoning, moving beyond simple requests for help.

