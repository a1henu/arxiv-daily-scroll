---
layout: default
title: RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees
---

# RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees
**arXiv**：[2512.14069v1](https://arxiv.org/abs/2512.14069) · [PDF](https://arxiv.org/pdf/2512.14069.pdf)  
**作者**：Junjie Ma, Jinlong Li  

**一句话要点**：提出RADAR方法，基于强化学习动态生成草稿树以加速大语言模型推理

**关键词**：大语言模型推理加速, 推测采样, 强化学习, 动态草稿树, 离线训练

## 3 点简述
- 核心问题：推测采样中草稿模型调用次数固定，缺乏灵活性，影响推理效率
- 方法要点：将草稿树生成建模为马尔可夫决策过程，利用离线强化学习训练预测模型实时决策调用
- 实验或效果：在三个大语言模型和四个任务上评估，相比自回归解码基线实现3.17-4.82倍加速

## 摘要（原文）

> Inference with modern Large Language Models (LLMs) is expensive and slow, and speculative sampling has emerged as an effective solution to this problem, however, the number of the calls to the draft model for generating candidate tokens in speculative sampling is a preset hyperparameter, lacking flexibility. To generate and utilize the candidate tokens more effectively, we propose RADAR, a novel speculative sampling method with RL-based dynamic draft trees. RADAR formulates the draft tree generation process as a Markov Decision Process (MDP) and employs offline reinforcement learning to train a prediction model, which enables real-time decision on the calls to the draft model, reducing redundant computations and further accelerating inference. Evaluations across three LLMs and four tasks show that RADAR achieves a speedup of 3.17x-4.82x over the auto-regressive decoding baseline. The code is available at https://github.com/minaduki-sora/RADAR.

