---
layout: default
title: The Law of Task-Achieving Body Motion: Axiomatizing Success of Robot Manipulation Actions
---

# The Law of Task-Achieving Body Motion: Axiomatizing Success of Robot Manipulation Actions
**arXiv**：[2602.06572v1](https://arxiv.org/abs/2602.06572) · [PDF](https://arxiv.org/pdf/2602.06572.pdf)  
**作者**：Malte Huerkamp, Jonas Dech, Michael Beetz  

**一句话要点**：提出任务实现体运动定律，为机器人操作动作提供公理化正确性规范

**关键词**：机器人操作, 体运动验证, 语义数字孪生, 任务分解, 可行性分析

## 3 点简述
- 核心问题：机器人需确保体运动在语义、因果和可行性上正确以实现任务
- 方法要点：引入任务-环境-体现类，分解任务实现为语义满足、因果充分和可行性验证
- 实验或效果：在厨房环境中实例化，用于三个移动操作平台的容器操作演示

## 摘要（原文）

> Autonomous agents that perform everyday manipulation actions need to ensure that their body motions are semantically correct with respect to a task request, causally effective within their environment, and feasible for their embodiment. In order to enable robots to verify these properties, we introduce the Law of Task-Achieving Body Motion as an axiomatic correctness specification for body motions. To that end we introduce scoped Task-Environment-Embodiment (TEE) classes that represent world states as Semantic Digital Twins (SDTs) and define applicable physics models to decompose task achievement into three predicates: SatisfiesRequest for semantic request satisfaction over SDT state evolution; Causes for causal sufficiency under the scoped physics model; and CanPerform for safety and feasibility verification at the embodiment level. This decomposition yields a reusable, implementation-independent interface that supports motion synthesis and the verification of given body motions. It also supports typed failure diagnosis (semantic, causal, embodiment and out-of-scope), feasibility across robots and environments, and counterfactual reasoning about robot body motions. We demonstrate the usability of the law in practice by instantiating it for articulated container manipulation in kitchen environments on three contrasting mobile manipulation platforms

