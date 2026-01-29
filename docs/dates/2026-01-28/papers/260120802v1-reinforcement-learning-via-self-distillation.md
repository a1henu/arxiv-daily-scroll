---
layout: default
title: Reinforcement Learning via Self-Distillation
---

# Reinforcement Learning via Self-Distillation
**arXiv**：[2601.20802v1](https://arxiv.org/abs/2601.20802) · [PDF](https://arxiv.org/pdf/2601.20802.pdf)  
**作者**：Jonas Hübotter, Frederike Lübeck, Lejs Behric, Anton Baumann, Marco Bagatella, Daniel Marta, Ido Hakimi, Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, Andreas Krause  

**一句话要点**：提出自蒸馏策略优化以解决可验证奖励强化学习中的信用分配瓶颈问题

**关键词**：强化学习, 自蒸馏, 可验证奖励, 文本反馈, 策略优化, 信用分配

## 3 点简述
- 核心问题：可验证奖励强化学习仅依赖标量奖励，导致信用分配困难，忽略丰富的文本反馈。
- 方法要点：SDPO利用模型自身作为教师，将反馈信息蒸馏回策略，无需外部奖励模型。
- 实验或效果：在科学推理、工具使用和编程任务中，SDPO提升样本效率和准确性，优于基线方法。

## 摘要（原文）

> Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain why an attempt failed. We formalize this setting as reinforcement learning with rich feedback and introduce Self-Distillation Policy Optimization (SDPO), which converts tokenized feedback into a dense learning signal without any external teacher or explicit reward model. SDPO treats the current model conditioned on feedback as a self-teacher and distills its feedback-informed next-token predictions back into the policy. In this way, SDPO leverages the model's ability to retrospectively identify its own mistakes in-context. Across scientific reasoning, tool use, and competitive programming on LiveCodeBench v6, SDPO improves sample efficiency and final accuracy over strong RLVR baselines. Notably, SDPO also outperforms baselines in standard RLVR environments that only return scalar feedback by using successful rollouts as implicit feedback for failed attempts. Finally, applying SDPO to individual questions at test time accelerates discovery on difficult binary-reward tasks, achieving the same discovery probability as best-of-k sampling or multi-turn conversations with 3x fewer attempts.

