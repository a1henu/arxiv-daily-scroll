---
layout: default
title: Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory
---

# Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory
**arXiv**：[2601.07470v1](https://arxiv.org/abs/2601.07470) · [PDF](https://arxiv.org/pdf/2601.07470.pdf)  
**作者**：Sirui Liang, Pengfei Cao, Jian Zhao, Wenhao Teng, Xiangwen Liao, Jun Zhao, Kang Liu  

**一句话要点**：提出元认知记忆抽象方法以解决LLM代理在长时决策任务中记忆泛化与负迁移问题

**关键词**：元认知学习, 记忆抽象, 长时决策, LLM代理, 直接偏好优化, 跨任务迁移

## 3 点简述
- 核心问题：现有方法以固定表示存储记忆，在分布偏移时泛化受限且易导致负迁移
- 方法要点：将记忆抽象作为可学习技能，通过冻结任务模型与学习记忆副驾驶实现任务执行与记忆管理解耦
- 实验或效果：在ALFWorld等基准上显著提升性能、分布外泛化与跨任务迁移能力

## 摘要（原文）

> Large language model (LLM) agents increasingly rely on accumulated memory to solve long-horizon decision-making tasks. However, most existing approaches store memory in fixed representations and reuse it at a single or implicit level of abstraction, which limits generalization and often leads to negative transfer when distribution shift. This paper proposes the Meta-Cognitive Memory Abstraction method (MCMA), which treats memory abstraction as a learnable cognitive skill rather than a fixed design choice. MCMA decouples task execution from memory management by combining a frozen task model with a learned memory copilot. The memory copilot is trained using direct preference optimization, it determines how memories should be structured, abstracted, and reused. Memories are further organized into a hierarchy of abstraction levels, enabling selective reuse based on task similarity. When no memory is transferable, MCMA transfers the ability to abstract and manage memory by transferring the memory copilot. Experiments on ALFWorld, ScienceWorld, and BabyAI demonstrate substantial improvements in performance, out-of-distribution generalization, and cross-task transfer over several baselines.

