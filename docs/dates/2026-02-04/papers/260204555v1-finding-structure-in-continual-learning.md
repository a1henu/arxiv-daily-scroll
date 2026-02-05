---
layout: default
title: Finding Structure in Continual Learning
---

# Finding Structure in Continual Learning
**arXiv**：[2602.04555v1](https://arxiv.org/abs/2602.04555) · [PDF](https://arxiv.org/pdf/2602.04555.pdf)  
**作者**：Pourya Shamsolmoali, Masoumeh Zareapoor  

**一句话要点**：提出基于Douglas-Rachford Splitting的持续学习目标重构，以平衡稳定性和可塑性。

**关键词**：持续学习, Douglas-Rachford Splitting, 灾难性遗忘, 梯度冲突, 近端算子, 稳定性-可塑性平衡

## 3 点简述
- 核心问题：持续学习中新任务学习导致旧知识灾难性遗忘，现有方法常引发梯度冲突。
- 方法要点：将学习目标重构为可塑性和稳定性的解耦协商，通过近端算子迭代达成共识。
- 实验或效果：无需外部记忆或复杂模块，实现高效平衡，提供更简单强大的学习范式。

## 摘要（原文）

> Learning from a stream of tasks usually pits plasticity against stability: acquiring new knowledge often causes catastrophic forgetting of past information. Most methods address this by summing competing loss terms, creating gradient conflicts that are managed with complex and often inefficient strategies such as external memory replay or parameter regularization. We propose a reformulation of the continual learning objective using Douglas-Rachford Splitting (DRS). This reframes the learning process not as a direct trade-off, but as a negotiation between two decoupled objectives: one promoting plasticity for new tasks and the other enforcing stability of old knowledge. By iteratively finding a consensus through their proximal operators, DRS provides a more principled and stable learning dynamic. Our approach achieves an efficient balance between stability and plasticity without the need for auxiliary modules or complex add-ons, providing a simpler yet more powerful paradigm for continual learning systems.

