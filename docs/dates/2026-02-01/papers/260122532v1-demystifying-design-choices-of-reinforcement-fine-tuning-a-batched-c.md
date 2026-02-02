---
layout: default
title: Demystifying Design Choices of Reinforcement Fine-tuning: A Batched Contextual Bandit Learning Perspective
---

# Demystifying Design Choices of Reinforcement Fine-tuning: A Batched Contextual Bandit Learning Perspective
**arXiv**：[2601.22532v1](https://arxiv.org/abs/2601.22532) · [PDF](https://arxiv.org/pdf/2601.22532.pdf)  
**作者**：Hong Xie, Xiao Hu, Tao Tan, Haoran Gu, Xin Li, Jianyu Han, Defu Lian, Enhong Chen  

**一句话要点**：从批量上下文赌博机视角解析强化微调设计选择，揭示关键因素与作用机制

**关键词**：强化微调, 设计选择分析, 批量上下文赌博机, 实验消融研究, 学习动态

## 3 点简述
- 核心问题：强化微调中设计选择作用不明，导致性能提升难以归因和结论不一致
- 方法要点：构建简约基线连接批量上下文赌博机，通过实验分析设计选择的边际增益
- 实验或效果：在三个基础模型和两个数据集上实验，识别关键设计选择并理解其对学习和泛化的影响

## 摘要（原文）

> The reinforcement fine-tuning area is undergoing an explosion papers largely on optimizing design choices. Though performance gains are often claimed, inconsistent conclusions also arise from time to time, making the progress illusive. Reflecting on this illusion, we still lack principled answers to two fundamental questions: 1) what is the role of each design choice? 2) which ones are critical? This paper aims to shed light on them. The underlying challenge is that design choices are entangled together, making their contribution to learning and generalization difficult to attribute. To address this challenge, we first construct a minimalist baseline for disentangling factors: one rollout per query in each round, the outcome reward serving as the training signal without any advantage trick, and a batch size of thirty-two. This baseline connects to batched contextual bandit learning, which facilitates experimental analysis. Centering around this baseline, we design an experiment pipeline, examining the marginal gains of factors like advantage, number of rollouts, etc. Experiments on three base models and two datasets, not only reveal new understanding on the role of various design choices on learning and generalization dynamics, but also identify critical ones that deserve more effort.

