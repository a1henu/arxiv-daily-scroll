---
layout: default
title: Routing, Cascades, and User Choice for LLMs
---

# Routing, Cascades, and User Choice for LLMs
**arXiv**：[2602.09902v1](https://arxiv.org/abs/2602.09902) · [PDF](https://arxiv.org/pdf/2602.09902.pdf)  
**作者**：Rafid Mahmood  

**一句话要点**：提出基于Stackelberg博弈的LLM路由策略分析，以优化性能与成本权衡

**关键词**：LLM路由策略, Stackelberg博弈, 用户行为分析, 成本效用权衡, 延迟抑制

## 3 点简述
- 研究LLM提供商基于任务难度和延迟的路由策略对用户行为的影响
- 构建提供商与用户间的博弈模型，分析最优路由策略和用户最佳响应
- 揭示提供商与用户目标错配可能导致延迟抑制和效用下降的条件

## 摘要（原文）

> To mitigate the trade-offs between performance and costs, LLM providers route user tasks to different models based on task difficulty and latency. We study the effect of LLM routing with respect to user behavior. We propose a game between an LLM provider with two models (standard and reasoning) and a user who can re-prompt or abandon tasks if the routed model cannot solve them. The user's goal is to maximize their utility minus the delay from using the model, while the provider minimizes the cost of servicing the user. We solve this Stackelberg game by fully characterizing the user best response and simplifying the provider problem. We observe that in nearly all cases, the optimal routing policy involves a static policy with no cascading that depends on the expected utility of the models to the user. Furthermore, we reveal a misalignment gap between the provider-optimal and user-preferred routes when the user's and provider's rankings of the models with respect to utility and cost differ. Finally, we demonstrate conditions for extreme misalignment where providers are incentivized to throttle the latency of the models to minimize their costs, consequently depressing user utility. The results yield simple threshold rules for single-provider, single-user interactions and clarify when routing, cascading, and throttling help or harm.

