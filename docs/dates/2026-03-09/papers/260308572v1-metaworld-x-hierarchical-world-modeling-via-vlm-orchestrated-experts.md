---
layout: default
title: MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation
---

# MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation
**arXiv**：[2603.08572v1](https://arxiv.org/abs/2603.08572) · [PDF](https://arxiv.org/pdf/2603.08572.pdf)  
**作者**：Yutong Shen, Hangxu Liu, Penghui Liu, Jiashuo Luo, Yongkang Zhang, Rex Morvley, Chen Jiang, Jianwei Zhang, Lei Zhang  

**一句话要点**：提出MetaWorld-X分层世界模型框架，通过VLM编排专家策略解决人形机器人全身控制问题。

**关键词**：人形机器人控制, 分层世界模型, 专家策略, 视觉语言模型, 全身控制, 模仿约束强化学习

## 3 点简述
- 核心问题：单策略方法在人形机器人全身控制中易导致梯度干扰和运动冲突，限制自然性与泛化性。
- 方法要点：基于分治原则，分解为专家策略，结合模仿约束强化学习确保生物力学一致性，并由VLM指导动态组合。
- 实验或效果：未知，但框架旨在提升运动自然性、稳定性和复杂任务组合的泛化能力。

## 摘要（原文）

> Learning natural, stable, and compositionally generalizable whole-body control policies for humanoid robots performing simultaneous locomotion and manipulation (loco-manipulation) remains a fundamental challenge in robotics. Existing reinforcement learning approaches typically rely on a single monolithic policy to acquire multiple skills, which often leads to cross-skill gradient interference and motion pattern conflicts in high-degree-of-freedom systems. As a result, generated behaviors frequently exhibit unnatural movements, limited stability, and poor generalization to complex task compositions. To address these limitations, we propose MetaWorld-X, a hierarchical world model framework for humanoid control. Guided by a divide-and-conquer principle, our method decomposes complex control problems into a set of specialized expert policies (Specialized Expert Policies, SEP). Each expert is trained under human motion priors through imitation-constrained reinforcement learning, introducing biomechanically consistent inductive biases that ensure natural and physically plausible motion generation. Building upon this foundation, we further develop an Intelligent Routing Mechanism (IRM) supervised by a Vision-Language Model (VLM), enabling semantic-driven expert composition. The VLM-guided router dynamically integrates expert policies according to high-level task semantics, facilitating compositional generalization and adaptive execution in multi-stage loco-manipulation tasks.

