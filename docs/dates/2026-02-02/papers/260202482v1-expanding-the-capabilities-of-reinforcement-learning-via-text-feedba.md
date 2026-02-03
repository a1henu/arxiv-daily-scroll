---
layout: default
title: Expanding the Capabilities of Reinforcement Learning via Text Feedback
---

# Expanding the Capabilities of Reinforcement Learning via Text Feedback
**arXiv**：[2602.02482v1](https://arxiv.org/abs/2602.02482) · [PDF](https://arxiv.org/pdf/2602.02482.pdf)  
**作者**：Yuda Song, Lili Chen, Fahim Tajwar, Remi Munos, Deepak Pathak, J. Andrew Bagnell, Aarti Singh, Andrea Zanette  

**一句话要点**：提出RLTF方法，利用文本反馈增强强化学习，提升大语言模型单轮推理性能

**关键词**：强化学习, 文本反馈, 大语言模型, 自蒸馏, 反馈建模, 多轮训练

## 3 点简述
- 核心问题：传统强化学习依赖稀疏二元奖励，蒸馏需昂贵演示，缺乏中间监督信号
- 方法要点：引入文本反馈作为训练信号，提出自蒸馏和反馈建模两种方法，使模型内化反馈
- 实验或效果：在推理谜题、竞赛数学和创意写作任务中，方法均优于基线，验证有效性

## 摘要（原文）

> The success of RL for LLM post-training stems from an unreasonably uninformative source: a single bit of information per rollout as binary reward or preference label. At the other extreme, distillation offers dense supervision but requires demonstrations, which are costly and difficult to scale. We study text feedback as an intermediate signal: richer than scalar rewards, yet cheaper than complete demonstrations. Textual feedback is a natural mode of human interaction and is already abundant in many real-world settings, where users, annotators, and automated judges routinely critique LLM outputs. Towards leveraging text feedback at scale, we formalize a multi-turn RL setup, RL from Text Feedback (RLTF), where text feedback is available during training but not at inference. Therefore, models must learn to internalize the feedback in order to improve their test-time single-turn performance. To do this, we propose two methods: Self Distillation (RLTF-SD), which trains the single-turn policy to match its own feedback-conditioned second-turn generations; and Feedback Modeling (RLTF-FM), which predicts the feedback as an auxiliary objective. We provide theoretical analysis on both methods, and empirically evaluate on reasoning puzzles, competition math, and creative writing tasks. Our results show that both methods consistently outperform strong baselines across benchmarks, highlighting the potential of RL with an additional source of rich supervision at scale.

