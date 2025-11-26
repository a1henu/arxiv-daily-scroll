---
layout: default
title: BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents
---

# BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents
**arXiv**：[2511.20597v1](https://arxiv.org/abs/2511.20597) · [PDF](https://arxiv.org/pdf/2511.20597.pdf)  
**作者**：Kaiyuan Zhang, Mark Tenenholtz, Kyle Polley, Jerry Ma, Denis Yarats, Ninghui Li  

**一句话要点**：提出多层级防御策略以保护AI浏览器代理免受提示注入攻击

**关键词**：提示注入攻击, AI浏览器代理, 安全基准, 多层级防御, 实证评估

## 3 点简述
- 核心问题：AI浏览器代理面临提示注入攻击，影响现实世界行动而非仅文本输出
- 方法要点：构建包含复杂HTML负载的基准，评估现有防御并设计多层级防御策略
- 实验或效果：通过基准对前沿AI模型进行实证评估，验证防御有效性

## 摘要（原文）

> The integration of artificial intelligence (AI) agents into web browsers introduces security challenges that go beyond traditional web application threat models. Prior work has identified prompt injection as a new attack vector for web agents, yet the resulting impact within real-world environments remains insufficiently understood.
>   In this work, we examine the landscape of prompt injection attacks and synthesize a benchmark of attacks embedded in realistic HTML payloads. Our benchmark goes beyond prior work by emphasizing injections that can influence real-world actions rather than mere text outputs, and by presenting attack payloads with complexity and distractor frequency similar to what real-world agents encounter. We leverage this benchmark to conduct a comprehensive empirical evaluation of existing defenses, assessing their effectiveness across a suite of frontier AI models. We propose a multi-layered defense strategy comprising both architectural and model-based defenses to protect against evolving prompt injection attacks. Our work offers a blueprint for designing practical, secure web agents through a defense-in-depth approach.

