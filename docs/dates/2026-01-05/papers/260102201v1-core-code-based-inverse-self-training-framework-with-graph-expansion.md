---
layout: default
title: CORE: Code-based Inverse Self-Training Framework with Graph Expansion for Virtual Agents
---

# CORE: Code-based Inverse Self-Training Framework with Graph Expansion for Virtual Agents
**arXiv**：[2601.02201v1](https://arxiv.org/abs/2601.02201) · [PDF](https://arxiv.org/pdf/2601.02201.pdf)  
**作者**：Keyu Wang, Bingchen Miao, Wendong Bu, Yu Wu, Juncheng Li, Shengyu Zhang, Wenqiao Zhang, Siliang Tang, Jun Xiao, Yueting Zhuang  

**一句话要点**：提出CORE框架以解决多模态虚拟代理训练中行为克隆与强化学习间的冲突

**关键词**：多模态虚拟代理, 行为克隆, 强化学习, 奖励函数推断, 策略图扩展, 轨迹外推

## 3 点简述
- 核心问题：行为克隆缺乏多样性，强化学习依赖手动奖励设计，两者冲突。
- 方法要点：通过语义代码抽象自动推断奖励函数，策略图扩展增强域内多样性，轨迹引导外推丰富域外多样性。
- 实验或效果：在Web和Android平台实验显示，CORE显著提升整体性能和泛化能力。

## 摘要（原文）

> The development of Multimodal Virtual Agents has made significant progress through the integration of Multimodal Large Language Models. However, mainstream training paradigms face key challenges: Behavior Cloning is simple and effective through imitation but suffers from low behavioral diversity, while Reinforcement Learning is capable of discovering novel strategies through exploration but heavily relies on manually designed reward functions. To address the conflict between these two methods, we present CORE, a Code-based Inverse Self-Training Framework with Graph Expansion that bridges imitation and exploration, offering a novel training framework that promotes behavioral diversity while eliminating the reliance on manually reward design. Specifically, we introduce Semantic Code Abstraction to automatically infers reward functions from expert demonstrations without manual design. The inferred reward function, referred to as the Label Function, is executable code that verifies one key step within a task. Building on this, we propose Strategy Graph Expansion to enhance in-domain behavioral diversity, which constructs a multi-path graph called Strategy Graph that captures diverse valid solutions beyond expert demonstrations. Furthermore, we introduce Trajectory-Guided Extrapolation, which enriches out-of-domain behavioral diversity by utilizing both successful and failed trajectories to expand the task space. Experiments on Web and Android platforms demonstrate that CORE significantly improves both overall performance and generalization, highlighting its potential as a robust and generalizable training paradigm for building powerful virtual agents.

