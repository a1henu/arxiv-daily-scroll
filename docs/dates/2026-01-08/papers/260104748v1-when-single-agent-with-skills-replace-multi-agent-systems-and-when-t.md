---
layout: default
title: When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail
---

# When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail
**arXiv**：[2601.04748v1](https://arxiv.org/abs/2601.04748) · [PDF](https://arxiv.org/pdf/2601.04748.pdf)  
**作者**：Xiaoxiao Li  

**一句话要点**：提出单技能代理替代多代理系统的方法，并揭示其规模限制与语义混淆问题。

**关键词**：技能选择, 多代理系统, 语义混淆, 规模限制, 认知科学, 分层路由

## 3 点简述
- 核心问题：多代理系统计算开销大，能否用单代理技能库实现类似模块化效益？
- 方法要点：将多代理系统编译为单代理系统，通过技能选择替代代理间通信。
- 实验或效果：初步实验显示减少令牌使用和延迟，但技能选择在库规模增大时出现相变式性能下降。

## 摘要（原文）

> Multi-agent AI systems have proven effective for complex reasoning. These systems are compounded by specialized agents, which collaborate through explicit communication, but incur substantial computational overhead. A natural question arises: can we achieve similar modularity benefits with a single agent that selects from a library of skills? We explore this question by viewing skills as internalized agent behaviors. From this perspective, a multi-agent system can be compiled into an equivalent single-agent system, trading inter-agent communication for skill selection. Our preliminary experiments suggest this approach can substantially reduce token usage and latency while maintaining competitive accuracy on reasoning benchmarks. However, this efficiency raises a deeper question that has received little attention: how does skill selection scale as libraries grow?
>   Drawing on principles from cognitive science, we propose that LLM skill selection exhibits bounded capacity analogous to human decision-making. We investigate the scaling behavior of skill selection and observe a striking pattern. Rather than degrading gradually, selection accuracy remains stable up to a critical library size, then drops sharply, indicating a phase transition reminiscent of capacity limits in human cognition. Furthermore, we find evidence that semantic confusability among similar skills, rather than library size alone, plays a central role in this degradation. This perspective suggests that hierarchical organization, which has long helped humans manage complex choices, may similarly benefit AI systems. Our initial results with hierarchical routing support this hypothesis. This work opens new questions about the fundamental limits of semantic-based skill selection in LLMs and offers a cognitive-grounded framework and practical guidelines for designing scalable skill-based agents.

