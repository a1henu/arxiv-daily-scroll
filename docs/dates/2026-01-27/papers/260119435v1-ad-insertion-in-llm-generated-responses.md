---
layout: default
title: Ad Insertion in LLM-Generated Responses
---

# Ad Insertion in LLM-Generated Responses
**arXiv**：[2601.19435v1](https://arxiv.org/abs/2601.19435) · [PDF](https://arxiv.org/pdf/2601.19435.pdf)  
**作者**：Shengwei Xu, Zhaohua Chen, Xiaotie Deng, Zhiyi Huang, Grant Schoenebeck  

**一句话要点**：提出基于流派解耦的广告插入框架，以解决大语言模型可持续变现中的上下文一致性与效率挑战。

**关键词**：大语言模型广告, 上下文一致性, 流派解耦, VCG拍卖, 计算效率, 伦理标准

## 3 点简述
- 核心问题：传统搜索广告无法捕捉对话流中的瞬时用户意图，需兼顾上下文一致性、计算效率和伦理标准。
- 方法要点：通过广告与响应生成解耦确保安全披露，使用流派作为代理解耦竞价，应用VCG机制实现近似激励兼容。
- 实验或效果：引入LLM-as-a-Judge指标评估上下文一致性，与人类评分强相关（Spearman ρ≈0.66），优于80%个体评估者。

## 摘要（原文）

> Sustainable monetization of Large Language Models (LLMs) remains a critical open challenge. Traditional search advertising, which relies on static keywords, fails to capture the fleeting, context-dependent user intents--the specific information, goods, or services a user seeks--embedded in conversational flows. Beyond the standard goal of social welfare maximization, effective LLM advertising imposes additional requirements on contextual coherence (ensuring ads align semantically with transient user intents) and computational efficiency (avoiding user interaction latency), as well as adherence to ethical and regulatory standards, including preserving privacy and ensuring explicit ad disclosure. Although various recent solutions have explored bidding on token-level and query-level, both categories of approaches generally fail to holistically satisfy this multifaceted set of constraints.
>   We propose a practical framework that resolves these tensions through two decoupling strategies. First, we decouple ad insertion from response generation to ensure safety and explicit disclosure. Second, we decouple bidding from specific user queries by using ``genres'' (high-level semantic clusters) as a proxy. This allows advertisers to bid on stable categories rather than sensitive real-time response, reducing computational burden and privacy risks. We demonstrate that applying the VCG auction mechanism to this genre-based framework yields approximately dominant strategy incentive compatibility (DSIC) and individual rationality (IR), as well as approximately optimal social welfare, while maintaining high computational efficiency. Finally, we introduce an "LLM-as-a-Judge" metric to estimate contextual coherence. Our experiments show that this metric correlates strongly with human ratings (Spearman's $ρ\approx 0.66$), outperforming 80% of individual human evaluators.

