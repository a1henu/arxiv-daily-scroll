---
layout: default
title: Crisis-Bench: Benchmarking Strategic Ambiguity and Reputation Management in Large Language Models
---

# Crisis-Bench: Benchmarking Strategic Ambiguity and Reputation Management in Large Language Models
**arXiv**：[2601.05570v1](https://arxiv.org/abs/2601.05570) · [PDF](https://arxiv.org/pdf/2601.05570.pdf)  
**作者**：Cooper Lin, Maohao Ran, Yanting Zhang, Zhenglin Wan, Hongwei Fan, Yibo Xu, Yike Guo, Wei Xue, Jun Song  

**一句话要点**：提出Crisis-Bench基准以评估大语言模型在危机管理中的战略模糊性与声誉管理能力

**关键词**：大语言模型评估, 战略模糊性, 声誉管理, 多智能体模拟, 部分可观察马尔可夫决策过程, 危机管理

## 3 点简述
- 核心问题：通用安全对齐导致大语言模型在需战略模糊的专业领域（如公关）存在效用差距
- 方法要点：基于多智能体POMDP构建动态危机模拟，引入裁决者-市场循环作为评估指标
- 实验或效果：在80个跨行业情景中测试，揭示模型在道德与战略保留间的二分行为

## 摘要（原文）

> Standard safety alignment optimizes Large Language Models (LLMs) for universal helpfulness and honesty, effectively instilling a rigid "Boy Scout" morality. While robust for general-purpose assistants, this one-size-fits-all ethical framework imposes a "transparency tax" on professional domains requiring strategic ambiguity and information withholding, such as public relations, negotiation, and crisis management. To measure this gap between general safety and professional utility, we introduce Crisis-Bench, a multi-agent Partially Observable Markov Decision Process (POMDP) that evaluates LLMs in high-stakes corporate crises. Spanning 80 diverse storylines across 8 industries, Crisis-Bench tasks an LLM-based Public Relations (PR) Agent with navigating a dynamic 7-day corporate crisis simulation while managing strictly separated Private and Public narrative states to enforce rigorous information asymmetry. Unlike traditional benchmarks that rely on static ground truths, we introduce the Adjudicator-Market Loop: a novel evaluation metric where public sentiment is adjudicated and translated into a simulated stock price, creating a realistic economic incentive structure. Our results expose a critical dichotomy: while some models capitulate to ethical concerns, others demonstrate the capacity for Machiavellian, legitimate strategic withholding in order to stabilize the simulated stock price. Crisis-Bench provides the first quantitative framework for assessing "Reputation Management" capabilities, arguing for a shift from rigid moral absolutism to context-aware professional alignment.

