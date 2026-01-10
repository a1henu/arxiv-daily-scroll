---
layout: default
title: When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail
---

# When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail
**arXiv**：[2601.04748v1](https://arxiv.org/abs/2601.04748) · [PDF](https://arxiv.org/pdf/2601.04748.pdf)  
**作者**：Xiaoxiao Li  

**一句话要点**：提出单技能代理替代多代理系统，分析其效率与规模限制

**关键词**：技能选择, 多代理系统, 认知科学, 语义混淆, 分层路由, 可扩展性

## 3 点简述
- 探讨单代理通过技能库选择替代多代理协作，以减少通信开销
- 发现技能选择存在容量限制，类似人类认知的相变现象
- 实验显示语义混淆影响选择准确性，分层组织可能提升可扩展性

## 摘要（原文）

> Multi-agent AI systems have proven effective for complex reasoning. These systems are compounded by specialized agents, which collaborate through explicit communication, but incur substantial computational overhead. A natural question arises: can we achieve similar modularity benefits with a single agent that selects from a library of skills? We explore this question by viewing skills as internalized agent behaviors. From this perspective, a multi-agent system can be compiled into an equivalent single-agent system, trading inter-agent communication for skill selection. Our preliminary experiments suggest this approach can substantially reduce token usage and latency while maintaining competitive accuracy on reasoning benchmarks. However, this efficiency raises a deeper question that has received little attention: how does skill selection scale as libraries grow?
>   Drawing on principles from cognitive science, we propose that LLM skill selection exhibits bounded capacity analogous to human decision-making. We investigate the scaling behavior of skill selection and observe a striking pattern. Rather than degrading gradually, selection accuracy remains stable up to a critical library size, then drops sharply, indicating a phase transition reminiscent of capacity limits in human cognition. Furthermore, we find evidence that semantic confusability among similar skills, rather than library size alone, plays a central role in this degradation. This perspective suggests that hierarchical organization, which has long helped humans manage complex choices, may similarly benefit AI systems. Our initial results with hierarchical routing support this hypothesis. This work opens new questions about the fundamental limits of semantic-based skill selection in LLMs and offers a cognitive-grounded framework and practical guidelines for designing scalable skill-based agents.

