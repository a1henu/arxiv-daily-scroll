---
layout: default
title: Learning in Context, Guided by Choice: A Reward-Free Paradigm for Reinforcement Learning with Transformers
---

# Learning in Context, Guided by Choice: A Reward-Free Paradigm for Reinforcement Learning with Transformers
**arXiv**：[2602.08244v1](https://arxiv.org/abs/2602.08244) · [PDF](https://arxiv.org/pdf/2602.08244.pdf)  
**作者**：Juncheng Dong, Bowen He, Moyang Guo, Ethan X. Fang, Zhuoran Yang, Vahid Tarokh  

**一句话要点**：提出基于偏好的上下文强化学习范式，以解决无奖励监督下的任务泛化问题。

**关键词**：上下文强化学习, 偏好学习, Transformer模型, 无奖励监督, 任务泛化

## 3 点简述
- 现有上下文强化学习依赖显式奖励信号，限制了在奖励模糊或获取成本高场景的应用。
- 提出ICPRL，仅使用偏好反馈进行预训练和部署，包括即时偏好和轨迹偏好两种变体。
- 实验表明ICPRL在未见任务上实现强泛化，性能接近有奖励监督的方法。

## 摘要（原文）

> In-context reinforcement learning (ICRL) leverages the in-context learning capabilities of transformer models (TMs) to efficiently generalize to unseen sequential decision-making tasks without parameter updates. However, existing ICRL methods rely on explicit reward signals during pretraining, which limits their applicability when rewards are ambiguous, hard to specify, or costly to obtain. To overcome this limitation, we propose a new learning paradigm, In-Context Preference-based Reinforcement Learning (ICPRL), in which both pretraining and deployment rely solely on preference feedback, eliminating the need for reward supervision. We study two variants that differ in the granularity of feedback: Immediate Preference-based RL (I-PRL) with per-step preferences, and Trajectory Preference-based RL (T-PRL) with trajectory-level comparisons. We first show that supervised pretraining, a standard approach in ICRL, remains effective under preference-only context datasets, demonstrating the feasibility of in-context reinforcement learning using only preference signals. To further improve data efficiency, we introduce alternative preference-native frameworks for I-PRL and T-PRL that directly optimize TM policies from preference data without requiring reward signals nor optimal action labels.Experiments on dueling bandits, navigation, and continuous control tasks demonstrate that ICPRL enables strong in-context generalization to unseen tasks, achieving performance comparable to ICRL methods trained with full reward supervision.

