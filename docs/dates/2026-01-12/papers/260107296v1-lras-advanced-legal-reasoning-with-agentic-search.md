---
layout: default
title: LRAS: Advanced Legal Reasoning with Agentic Search
---

# LRAS: Advanced Legal Reasoning with Agentic Search
**arXiv**：[2601.07296v1](https://arxiv.org/abs/2601.07296) · [PDF](https://arxiv.org/pdf/2601.07296.pdf)  
**作者**：Yujin Zhou, Chuxue Cao, Jinluan Yang, Lijun Wu, Conghui He, Sirui Han, Yike Guo  

**一句话要点**：提出LRAS框架以解决法律大模型在推理中因知识边界不清导致的错误结论问题

**关键词**：法律推理, 大语言模型, 主动查询, 内省模仿学习, 强化学习, 知识边界

## 3 点简述
- 核心问题：法律大模型依赖内部参数知识进行闭环推理，缺乏知识边界意识，易产生自信但错误的结论
- 方法要点：通过内省模仿学习和难度感知强化学习，实现从静态闭环思维到动态主动查询的转变
- 实验或效果：LRAS在实验中超越基线模型8.2-32%，在需要可靠知识的深度推理任务中提升最显著

## 摘要（原文）

> While Large Reasoning Models (LRMs) have demonstrated exceptional logical capabilities in mathematical domains, their application to the legal field remains hindered by the strict requirements for procedural rigor and adherence to legal logic. Existing legal LLMs, which rely on "closed-loop reasoning" derived solely from internal parametric knowledge, frequently suffer from lack of self-awareness regarding their knowledge boundaries, leading to confident yet incorrect conclusions. To address this challenge, we present Legal Reasoning with Agentic Search (LRAS), the first framework designed to transition legal LLMs from static and parametric "closed-loop thinking" to dynamic and interactive "Active Inquiry". By integrating Introspective Imitation Learning and Difficulty-aware Reinforcement Learning, LRAS enables LRMs to identify knowledge boundaries and handle legal reasoning complexity. Empirical results demonstrate that LRAS outperforms state-of-the-art baselines by 8.2-32\%, with the most substantial gains observed in tasks requiring deep reasoning with reliable knowledge. We will release our data and models for further exploration soon.

