---
layout: default
title: Unsupervised Learning of Efficient Exploration: Pre-training Adaptive Policies via Self-Imposed Goals
---

# Unsupervised Learning of Efficient Exploration: Pre-training Adaptive Policies via Self-Imposed Goals
**arXiv**：[2601.19810v1](https://arxiv.org/abs/2601.19810) · [PDF](https://arxiv.org/pdf/2601.19810.pdf)  
**作者**：Octavio Pappalardo  

**一句话要点**：提出ULEE方法，通过自设目标和元学习优化探索与适应能力，提升下游任务性能。

**关键词**：无监督预训练, 元学习, 探索策略, 目标生成, 自适应策略, 强化学习

## 3 点简述
- 核心问题：如何无监督预训练以加速下游任务学习，特别是任务分布广泛或未知时。
- 方法要点：结合上下文学习与对抗性目标生成，在元学习框架中优化多回合探索和适应。
- 实验或效果：在XLand-MiniGrid基准上，优于从头学习、DIAYN预训练及其他课程方法。

## 摘要（原文）

> Unsupervised pre-training can equip reinforcement learning agents with prior knowledge and accelerate learning in downstream tasks. A promising direction, grounded in human development, investigates agents that learn by setting and pursuing their own goals. The core challenge lies in how to effectively generate, select, and learn from such goals. Our focus is on broad distributions of downstream tasks where solving every task zero-shot is infeasible. Such settings naturally arise when the target tasks lie outside of the pre-training distribution or when their identities are unknown to the agent. In this work, we (i) optimize for efficient multi-episode exploration and adaptation within a meta-learning framework, and (ii) guide the training curriculum with evolving estimates of the agent's post-adaptation performance. We present ULEE, an unsupervised meta-learning method that combines an in-context learner with an adversarial goal-generation strategy that maintains training at the frontier of the agent's capabilities. On XLand-MiniGrid benchmarks, ULEE pre-training yields improved exploration and adaptation abilities that generalize to novel objectives, environment dynamics, and map structures. The resulting policy attains improved zero-shot and few-shot performance, and provides a strong initialization for longer fine-tuning processes. It outperforms learning from scratch, DIAYN pre-training, and alternative curricula.

