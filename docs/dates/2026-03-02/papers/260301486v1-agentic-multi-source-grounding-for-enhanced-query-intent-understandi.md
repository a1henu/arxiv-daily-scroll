---
layout: default
title: Agentic Multi-Source Grounding for Enhanced Query Intent Understanding: A DoorDash Case Study
---

# Agentic Multi-Source Grounding for Enhanced Query Intent Understanding: A DoorDash Case Study
**arXiv**：[2603.01486v1](https://arxiv.org/abs/2603.01486) · [PDF](https://arxiv.org/pdf/2603.01486.pdf)  
**作者**：Emmanuel Aboah Boateng, Kyle MacDonald, Akshad Viswanathan, Sudeep Das  

**一句话要点**：提出基于代理多源接地的系统，通过实体检索和网络搜索解决多类别市场查询意图模糊问题

**关键词**：查询意图理解, 多源接地, 代理系统, 意图消歧, 多类别市场

## 3 点简述
- 核心问题：多类别市场中上下文稀疏查询存在意图模糊，传统分类器强制单一标签，通用LLM产生幻觉
- 方法要点：结合分阶段目录实体检索和代理网络搜索工具，输出有序多意图集，通过可配置消歧层解析
- 实验效果：在DoorDash平台评估，相比未接地LLM基线提升10.9个百分点，长尾查询准确率达90.7%

## 摘要（原文）

> Accurately mapping user queries to business categories is a fundamental Information Retrieval challenge for multi-category marketplaces, where context-sparse queries such as "Wildflower" exhibit intent ambiguity, simultaneously denoting a restaurant chain, a retail product, and a floral item. Traditional classifiers force a winner-takes-all assignment, while general-purpose LLMs hallucinate unavailable inventory. We introduce an Agentic Multi-Source Grounded system that addresses both failure modes by grounding LLM inference in (i) a staged catalog entity retrieval pipeline and (ii) an agentic web-search tool invoked autonomously for cold-start queries. Rather than predicting a single label, the model emits an ordered multi-intent set, resolved by a configurable disambiguation layer that applies deterministic business policies and is designed for extensibility to personalization signals. This decoupled design generalizes across domains, allowing any marketplace to supply its own grounding sources and resolution rules without modifying the core architecture. Evaluated on DoorDash's multi-vertical search platform, the system achieves +10.9pp over the ungrounded LLM baseline and +4.6pp over the legacy production system. On long-tail queries, incremental ablations attribute +8.3pp to catalog grounding, +3.2pp to agentic web search grounding, and +1.5pp to dual intent disambiguation, yielding 90.7% accuracy (+13.0pp over baseline). The system is deployed in production, serving over 95% of daily search impressions, and establishes a generalizable paradigm for applications requiring foundation models grounded in proprietary context and real-time web knowledge to resolve ambiguous, context-sparse decision problems at scale.

