---
layout: default
title: Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge
---

# Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge
**arXiv**：[2602.09341v1](https://arxiv.org/abs/2602.09341) · [PDF](https://arxiv.org/pdf/2602.09341.pdf)  
**作者**：Wei Yang, Shixuan Li, Heng Ping, Peiyu Zhang, Paul Bogdan, Jesse Thomason  

**一句话要点**：提出AgentAuditor以解决多智能体系统中多数投票丢弃推理结构的问题，通过推理树路径搜索提升准确性。

**关键词**：多智能体系统, 推理树, 路径搜索, 多数投票改进, ACPO训练, LLM推理

## 3 点简述
- 核心问题：多数投票在多智能体系统中忽略推理轨迹证据，易受相关偏见导致的错误共识影响。
- 方法要点：引入AgentAuditor，基于推理树表示智能体间一致与分歧，通过局部验证解决冲突；提出ACPO训练裁决器奖励基于证据的少数选择。
- 实验或效果：在5种流行设置中，相比多数投票和LLM-as-Judge，绝对准确率提升最高达5%和3%。

## 摘要（原文）

> Multi-agent systems (MAS) can substantially extend the reasoning capacity of large language models (LLMs), yet most frameworks still aggregate agent outputs with majority voting. This heuristic discards the evidential structure of reasoning traces and is brittle under the confabulation consensus, where agents share correlated biases and converge on the same incorrect rationale. We introduce AgentAuditor, which replaces voting with a path search over a Reasoning Tree that explicitly represents agreements and divergences among agent traces. AgentAuditor resolves conflicts by comparing reasoning branches at critical divergence points, turning global adjudication into efficient, localized verification. We further propose Anti-Consensus Preference Optimization (ACPO), which trains the adjudicator on majority-failure cases and rewards evidence-based minority selections over popular errors. AgentAuditor is agnostic to MAS setting, and we find across 5 popular settings that it yields up to 5% absolute accuracy improvement over a majority vote, and up to 3% over using LLM-as-Judge.

