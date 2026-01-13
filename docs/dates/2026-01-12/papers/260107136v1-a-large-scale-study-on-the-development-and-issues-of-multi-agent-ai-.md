---
layout: default
title: A Large-Scale Study on the Development and Issues of Multi-Agent AI Systems
---

# A Large-Scale Study on the Development and Issues of Multi-Agent AI Systems
**arXiv**：[2601.07136v1](https://arxiv.org/abs/2601.07136) · [PDF](https://arxiv.org/pdf/2601.07136.pdf)  
**作者**：Daniel Liu, Krishna Upadhyay, Vinaik Chhetri, A. B. Siddique, Umar Farooq  

**一句话要点**：通过大规模实证研究揭示多智能体AI系统的开发模式与维护问题

**关键词**：多智能体AI系统, 实证研究, 开发模式, 维护问题, 开源软件分析

## 3 点简述
- 核心问题：多智能体AI系统（如LangChain、CrewAI）的实际开发与维护情况未知，缺乏大规模实证分析。
- 方法要点：分析八个领先开源系统的42K+提交和4.7K+已解决议题，识别开发模式与议题分布。
- 实验或效果：发现开发模式分为持续、稳定和爆发驱动型，议题以bug为主，解决时间分布不均，强调生态脆弱性。

## 摘要（原文）

> The rapid emergence of multi-agent AI systems (MAS), including LangChain, CrewAI, and AutoGen, has shaped how large language model (LLM) applications are developed and orchestrated. However, little is known about how these systems evolve and are maintained in practice. This paper presents the first large-scale empirical study of open-source MAS, analyzing over 42K unique commits and over 4.7K resolved issues across eight leading systems. Our analysis identifies three distinct development profiles: sustained, steady, and burst-driven. These profiles reflect substantial variation in ecosystem maturity. Perfective commits constitute 40.8% of all changes, suggesting that feature enhancement is prioritized over corrective maintenance (27.4%) and adaptive updates (24.3%). Data about issues shows that the most frequent concerns involve bugs (22%), infrastructure (14%), and agent coordination challenges (10%). Issue reporting also increased sharply across all frameworks starting in 2023. Median resolution times range from under one day to about two weeks, with distributions skewed toward fast responses but a minority of issues requiring extended attention. These results highlight both the momentum and the fragility of the current ecosystem, emphasizing the need for improved testing infrastructure, documentation quality, and maintenance practices to ensure long-term reliability and sustainability.

