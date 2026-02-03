---
layout: default
title: Probabilistic Performance Guarantees for Multi-Task Reinforcement Learning
---

# Probabilistic Performance Guarantees for Multi-Task Reinforcement Learning
**arXiv**：[2602.02098v1](https://arxiv.org/abs/2602.02098) · [PDF](https://arxiv.org/pdf/2602.02098.pdf)  
**作者**：Yannik Schnitzer, Mathias Jackermeier, Alessandro Abate, David Parker  

**一句话要点**：提出基于泛化边界的方法，为多任务强化学习策略在新任务上提供高置信度性能保证。

**关键词**：多任务强化学习, 性能保证, 泛化边界, 置信度分析, 安全关键应用

## 3 点简述
- 核心问题：现有多任务强化学习方法缺乏形式化性能保证，难以应用于安全关键场景。
- 方法要点：结合任务内置信下界和任务级泛化，构建新泛化边界以计算新任务性能的高置信度保证。
- 实验或效果：理论证明边界有效，并在实际样本量下展示保证信息丰富，适用于前沿多任务RL方法。

## 摘要（原文）

> Multi-task reinforcement learning trains generalist policies that can execute multiple tasks. While recent years have seen significant progress, existing approaches rarely provide formal performance guarantees, which are indispensable when deploying policies in safety-critical settings. We present an approach for computing high-confidence guarantees on the performance of a multi-task policy on tasks not seen during training. Concretely, we introduce a new generalisation bound that composes (i) per-task lower confidence bounds from finitely many rollouts with (ii) task-level generalisation from finitely many sampled tasks, yielding a high-confidence guarantee for new tasks drawn from the same arbitrary and unknown distribution. Across state-of-the-art multi-task RL methods, we show that the guarantees are theoretically sound and informative at realistic sample sizes.

