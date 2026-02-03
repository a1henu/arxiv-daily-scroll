---
layout: default
title: Learning to Route and Schedule LLMs from User Retrials via Contextual Queueing Bandits
---

# Learning to Route and Schedule LLMs from User Retrials via Contextual Queueing Bandits
**arXiv**：[2602.02061v1](https://arxiv.org/abs/2602.02061) · [PDF](https://arxiv.org/pdf/2602.02061.pdf)  
**作者**：Seoungbin Bae, Junyoung Son, Dabeen Lee  

**一句话要点**：提出基于上下文排队老虎机的联合路由调度算法，利用用户重试行为优化LLM服务效率。

**关键词**：LLM路由调度, 上下文排队老虎机, 用户重试行为, Thompson采样, 队列稳定性, 隐式反馈学习

## 3 点简述
- 核心问题：LLM服务中用户查询积压和重试行为导致服务器负载增加，现有算法忽略用户反馈体验。
- 方法要点：引入CQB-MNL框架，结合Thompson采样和衰减强制探索，实现路由和调度的联合优化。
- 实验或效果：在多个数据集上验证算法优于基线，路由累积遗憾为√t量级，队列长度遗憾为t^{-1/4}量级。

## 摘要（原文）

> Explosive demands for LLMs often cause user queries to accumulate in server queues, requiring efficient routing (query-LLM matching) and scheduling (query prioritization) mechanisms. Several online algorithms are being deployed, but they overlook the following two key challenges inherent to conversational LLM services: (1) unsatisfied users may retry queries, increasing the server backlog, and (2) requests for ``explicit" feedback, such as ratings, degrade user experiences. In this paper, we develop a joint routing and scheduling algorithm that leverages ``implicit" feedback inferred from user retrial behaviors. The key idea is to propose and study the framework of contextual queueing bandits with multinomial logit feedback (CQB-MNL). CQB-MNL models query retrials, as well as context-based learning for user preferences over LLMs. Our algorithm, anytime CQB (ACQB), achieves efficient learning while maintaining queue stability by combining Thompson sampling with forced exploration at a decaying rate. We show that ACQB simultaneously achieves a cumulative regret of $\widetilde{\mathcal{O}}(\sqrt{t})$ for routing and a queue length regret of $\widetilde{\mathcal{O}}(t^{-1/4})$ for any large $t$. For experiments, we refine query embeddings via contrastive learning while adopting a disjoint parameter model to learn LLM-specific parameters. Experiments on SPROUT, EmbedLLM, and RouterBench datasets confirm that both algorithms consistently outperform baselines.

