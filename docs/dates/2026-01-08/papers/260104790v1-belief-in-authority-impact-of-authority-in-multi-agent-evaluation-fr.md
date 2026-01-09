---
layout: default
title: Belief in Authority: Impact of Authority in Multi-Agent Evaluation Framework
---

# Belief in Authority: Impact of Authority in Multi-Agent Evaluation Framework
**arXiv**：[2601.04790v1](https://arxiv.org/abs/2601.04790) · [PDF](https://arxiv.org/pdf/2601.04790.pdf)  
**作者**：Junhyuk Choi, Jeongyoun Kwon, Heeju Kim, Haeun Cho, Hayeong Jung, Sehee Min, Bugeun Kim  

**一句话要点**：分析权威角色在多智能体评估框架中的影响，揭示专家和参照权力作用更强

**关键词**：多智能体系统, 权威偏见, 角色分类, ChatEval评估, 权力理论, 非对称交互

## 3 点简述
- 核心问题：权威偏见在多智能体交互中的影响未充分探索，需系统分析角色型权威偏差
- 方法要点：基于French和Raven权力理论，将权威角色分类为合法、参照和专家类型，使用ChatEval进行自由形式多智能体评估
- 实验或效果：GPT-4o和DeepSeek R1实验显示，专家和参照权力角色影响力大于合法权力角色，权威偏见源于权威角色坚持立场而非普通智能体主动顺从

## 摘要（原文）

> Multi-agent systems utilizing large language models often assign authoritative roles to improve performance, yet the impact of authority bias on agent interactions remains underexplored. We present the first systematic analysis of role-based authority bias in free-form multi-agent evaluation using ChatEval. Applying French and Raven's power-based theory, we classify authoritative roles into legitimate, referent, and expert types and analyze their influence across 12-turn conversations. Experiments with GPT-4o and DeepSeek R1 reveal that Expert and Referent power roles exert stronger influence than Legitimate power roles. Crucially, authority bias emerges not through active conformity by general agents, but through authoritative roles consistently maintaining their positions while general agents demonstrate flexibility. Furthermore, authority influence requires clear position statements, as neutral responses fail to generate bias. These findings provide key insights for designing multi-agent frameworks with asymmetric interaction patterns.

