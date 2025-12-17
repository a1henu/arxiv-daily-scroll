---
layout: default
title: Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning
---

# Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning
**arXiv**：[2512.14057v1](https://arxiv.org/abs/2512.14057) · [PDF](https://arxiv.org/pdf/2512.14057.pdf)  
**作者**：Amir M. Soufi Enayati, Homayoun Honari, Homayoun Najjaran  

**一句话要点**：提出CRAFT模型，通过无动作Transformer编码器-解码器实现元强化学习中的任务表示推断。

**关键词**：元强化学习, 任务表示学习, Transformer编码器-解码器, 无动作推断, 机器人控制, 变分推断

## 3 点简述
- 核心问题：标准强化学习泛化能力差，现有元强化学习方法依赖动作信息，导致任务推断与策略耦合。
- 方法要点：CRAFT仅基于状态和奖励序列推断任务表示，使用Transformer编码器-解码器捕获长期依赖，支持模块化训练。
- 实验或效果：在MetaWorld ML-10基准测试中，CRAFT实现更快适应、更好泛化和更有效探索。

## 摘要（原文）

> Reinforcement learning (RL) enables robots to operate in uncertain environments, but standard approaches often struggle with poor generalization to unseen tasks. Context-adaptive meta reinforcement learning addresses these limitations by conditioning on the task representation, yet they mostly rely on complete action information in the experience making task inference tightly coupled to a specific policy. This paper introduces Context Representation via Action Free Transformer encoder decoder (CRAFT), a belief model that infers task representations solely from sequences of states and rewards. By removing the dependence on actions, CRAFT decouples task inference from policy optimization, supports modular training, and leverages amortized variational inference for scalable belief updates. Built on a transformer encoder decoder with rotary positional embeddings, the model captures long range temporal dependencies and robustly encodes both parametric and non-parametric task variations. Experiments on the MetaWorld ML-10 robotic manipulation benchmark show that CRAFT achieves faster adaptation, improved generalization, and more effective exploration compared to context adaptive meta--RL baselines. These findings highlight the potential of action-free inference as a foundation for scalable RL in robotic control.

