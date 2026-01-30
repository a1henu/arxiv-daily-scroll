---
layout: default
title: SymbXRL: Symbolic Explainable Deep Reinforcement Learning for Mobile Networks
---

# SymbXRL: Symbolic Explainable Deep Reinforcement Learning for Mobile Networks
**arXiv**：[2601.22024v1](https://arxiv.org/abs/2601.22024) · [PDF](https://arxiv.org/pdf/2601.22024.pdf)  
**作者**：Abhishek Duttagupta, MohammadErfan Jabbari, Claudio Fiandrino, Marco Fiore, Joerg Widmer  

**一句话要点**：提出SymbXRL，一种符号可解释深度强化学习方法，用于解决6G移动网络中DRL决策解释性差的问题。

**关键词**：可解释强化学习, 符号AI, 6G移动网络, 深度强化学习, 网络资源分配

## 3 点简述
- 核心问题：DRL在6G网络资源分配中有效，但作为黑盒难以解释，阻碍实际部署。
- 方法要点：结合符号AI，通过符号和规则生成人类可理解的解释，揭示DRL决策过程。
- 实验或效果：在真实网络管理用例中验证，提升解释语义，并实现意图导向控制，中位累积奖励提高12%。

## 摘要（原文）

> The operation of future 6th-generation (6G) mobile networks will increasingly rely on the ability of deep reinforcement learning (DRL) to optimize network decisions in real-time. DRL yields demonstrated efficacy in various resource allocation problems, such as joint decisions on user scheduling and antenna allocation or simultaneous control of computing resources and modulation. However, trained DRL agents are closed-boxes and inherently difficult to explain, which hinders their adoption in production settings. In this paper, we make a step towards removing this critical barrier by presenting SymbXRL, a novel technique for explainable reinforcement learning (XRL) that synthesizes human-interpretable explanations for DRL agents. SymbXRL leverages symbolic AI to produce explanations where key concepts and their relationships are described via intuitive symbols and rules; coupling such a representation with logical reasoning exposes the decision process of DRL agents and offers more comprehensible descriptions of their behaviors compared to existing approaches. We validate SymbXRL in practical network management use cases supported by DRL, proving that it not only improves the semantics of the explanations but also paves the way for explicit agent control: for instance, it enables intent-based programmatic action steering that improves by 12% the median cumulative reward over a pure DRL solution.

