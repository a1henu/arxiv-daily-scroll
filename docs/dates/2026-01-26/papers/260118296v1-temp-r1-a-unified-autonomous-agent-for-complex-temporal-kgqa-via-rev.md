---
layout: default
title: Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning
---

# Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning
**arXiv**：[2601.18296v1](https://arxiv.org/abs/2601.18296) · [PDF](https://arxiv.org/pdf/2601.18296.pdf)  
**作者**：Zhaoyan Gong, Zhiqiang Liu, Songze Li, Xiaoke Guo, Yuanxiang Liu, Xinle Deng, Zhizhen Liu, Lei Liang, Huajun Chen, Wen Zhang  

**一句话要点**：提出Temp-R1，首个基于强化学习的自主端到端代理，用于解决复杂时序知识图谱问答。

**关键词**：时序知识图谱问答, 强化学习, 自主代理, 反向课程学习, 端到端训练

## 3 点简述
- 核心问题：时序知识图谱问答需处理动态事实的多跳依赖和复杂时序约束，现有方法灵活性差。
- 方法要点：通过强化学习训练，扩展动作空间并引入反向课程学习，从难到易优化推理能力。
- 实验或效果：在MultiTQ和TimelineKGQA上实现SOTA，复杂问题性能提升19.8%。

## 摘要（原文）

> Temporal Knowledge Graph Question Answering (TKGQA) is inherently challenging, as it requires sophisticated reasoning over dynamic facts with multi-hop dependencies and complex temporal constraints. Existing methods rely on fixed workflows and expensive closed-source APIs, limiting flexibility and scalability. We propose Temp-R1, the first autonomous end-to-end agent for TKGQA trained through reinforcement learning. To address cognitive overload in single-action reasoning, we expand the action space with specialized internal actions alongside external action. To prevent shortcut learning on simple questions, we introduce reverse curriculum learning that trains on difficult questions first, forcing the development of sophisticated reasoning before transferring to easier cases. Our 8B-parameter Temp-R1 achieves state-of-the-art performance on MultiTQ and TimelineKGQA, improving 19.8% over strong baselines on complex questions. Our work establishes a new paradigm for autonomous temporal reasoning agents. Our code will be publicly available soon at https://github.com/zjukg/Temp-R1.

