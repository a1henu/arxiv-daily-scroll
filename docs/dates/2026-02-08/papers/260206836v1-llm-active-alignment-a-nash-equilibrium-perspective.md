---
layout: default
title: LLM Active Alignment: A Nash Equilibrium Perspective
---

# LLM Active Alignment: A Nash Equilibrium Perspective
**arXiv**：[2602.06836v1](https://arxiv.org/abs/2602.06836) · [PDF](https://arxiv.org/pdf/2602.06836.pdf)  
**作者**：Tonghan Wang, Yuqi Pan, Xinyi Yang, Yanchen Jiang, Milind Tambe, David C. Parkes  

**一句话要点**：提出基于纳什均衡的LLM主动对齐框架，以调控多智能体LLM行为并避免政治排斥

**关键词**：纳什均衡, LLM对齐, 多智能体系统, 行为预测, 社会媒体调控, 主动对齐

## 3 点简述
- 核心问题：多智能体LLM在开放文本空间中行为预测与对齐的复杂性，可能导致政治排斥等病理现象
- 方法要点：将智能体行为建模为人类子群体的混合，通过纳什均衡分析推导闭式解，提供主动对齐层
- 实验或效果：在社交媒体场景中，该方法能避免LLM群体忽略某些子群体，展示跨领域调控潜力

## 摘要（原文）

> We develop a game-theoretic framework for predicting and steering the behavior of populations of large language models (LLMs) through Nash equilibrium (NE) analysis. To avoid the intractability of equilibrium computation in open-ended text spaces, we model each agent's action as a mixture over human subpopulations. Agents choose actively and strategically which groups to align with, yielding an interpretable and behaviorally substantive policy class. We derive closed-form NE characterizations, adopting standard concave-utility assumptions to enable analytical system-level predictions and give explicit, actionable guidance for shifting alignment targets toward socially desirable outcomes. The method functions as an active alignment layer on top of existing alignment pipelines such as RLHF. In a social-media setting, we show that a population of LLMs, especially reasoning-based models, may exhibit political exclusion, pathologies where some subpopulations are ignored by all LLM agents, which can be avoided by our method, illustrating the promise of applying the method to regulate multi-agent LLM dynamics across domains.

