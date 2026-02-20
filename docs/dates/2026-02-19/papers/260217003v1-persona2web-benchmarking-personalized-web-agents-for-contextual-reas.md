---
layout: default
title: Persona2Web: Benchmarking Personalized Web Agents for Contextual Reasoning with User History
---

# Persona2Web: Benchmarking Personalized Web Agents for Contextual Reasoning with User History
**arXiv**：[2602.17003v1](https://arxiv.org/abs/2602.17003) · [PDF](https://arxiv.org/pdf/2602.17003.pdf)  
**作者**：Serin Kim, Sangam Lee, Dongha Lee  

**一句话要点**：提出Persona2Web基准以评估基于用户历史的个性化网页代理在模糊查询中的推理能力

**关键词**：个性化网页代理, 用户历史推理, 模糊查询处理, 基准评估, 上下文推理

## 3 点简述
- 核心问题：当前网页代理缺乏个性化能力，无法从模糊查询中推断用户偏好和上下文。
- 方法要点：基于澄清到个性化原则，构建包含用户历史、模糊查询和推理感知评估框架的基准。
- 实验或效果：通过多种代理架构、骨干模型和历史访问方案实验，揭示个性化网页代理的关键挑战。

## 摘要（原文）

> Large language models have advanced web agents, yet current agents lack personalization capabilities. Since users rarely specify every detail of their intent, practical web agents must be able to interpret ambiguous queries by inferring user preferences and contexts. To address this challenge, we present Persona2Web, the first benchmark for evaluating personalized web agents on the real open web, built upon the clarify-to-personalize principle, which requires agents to resolve ambiguity based on user history rather than relying on explicit instructions. Persona2Web consists of: (1) user histories that reveal preferences implicitly over long time spans, (2) ambiguous queries that require agents to infer implicit user preferences, and (3) a reasoning-aware evaluation framework that enables fine-grained assessment of personalization. We conduct extensive experiments across various agent architectures, backbone models, history access schemes, and queries with varying ambiguity levels, revealing key challenges in personalized web agent behavior. For reproducibility, our codes and datasets are publicly available at https://anonymous.4open.science/r/Persona2Web-73E8.

