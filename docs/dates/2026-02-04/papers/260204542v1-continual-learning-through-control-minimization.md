---
layout: default
title: Continual Learning through Control Minimization
---

# Continual Learning through Control Minimization
**arXiv**：[2602.04542v1](https://arxiv.org/abs/2602.04542) · [PDF](https://arxiv.org/pdf/2602.04542.pdf)  
**作者**：Sander de Haan, Yassine Taoudi-Benchekroun, Pau Vilimelis Aceituno, Benjamin F. Grewe  

**一句话要点**：提出基于控制最小化的持续学习框架，以解决神经网络在顺序任务中的灾难性遗忘问题。

**关键词**：持续学习, 灾难性遗忘, 控制理论, 自然梯度, 神经网络, 顺序任务

## 3 点简述
- 核心问题：灾难性遗忘是神经网络在顺序任务训练中的主要挑战，导致先前任务知识丢失。
- 方法要点：将持续学习重构为控制问题，通过最小化控制努力整合新任务，同时保护先前任务表示。
- 实验或效果：在标准基准测试中优于现有方法，无需重放即可恢复先前任务曲率并实现任务区分。

## 摘要（原文）

> Catastrophic forgetting remains a fundamental challenge for neural networks when tasks are trained sequentially. In this work, we reformulate continual learning as a control problem where learning and preservation signals compete within neural activity dynamics. We convert regularization penalties into preservation signals that protect prior-task representations. Learning then proceeds by minimizing the control effort required to integrate new tasks while competing with the preservation of prior tasks. At equilibrium, the neural activities produce weight updates that implicitly encode the full prior-task curvature, a property we term the continual-natural gradient, requiring no explicit curvature storage. Experiments confirm that our learning framework recovers true prior-task curvature and enables task discrimination, outperforming existing methods on standard benchmarks without replay.

