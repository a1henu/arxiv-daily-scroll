---
layout: default
title: MulFeRL: Enhancing Reinforcement Learning with Verbal Feedback in a Multi-turn Loop
---

# MulFeRL: Enhancing Reinforcement Learning with Verbal Feedback in a Multi-turn Loop
**arXiv**：[2601.22900v1](https://arxiv.org/abs/2601.22900) · [PDF](https://arxiv.org/pdf/2601.22900.pdf)  
**作者**：Xuancheng Li, Haitao Li, Yujia Zhou, YiqunLiu, Qingyao Ai  

**一句话要点**：提出多轮反馈增强强化学习框架，以解决失败样本中稀疏奖励问题

**关键词**：强化学习, 多轮反馈, 失败样本优化, 结构化反馈, 泛化能力

## 3 点简述
- 核心问题：强化学习中仅依赖标量奖励在失败样本上信息稀疏，缺乏失败原因指导
- 方法要点：基于动态多轮再生、跨轮优化信号和结构化反馈注入机制构建框架
- 实验或效果：在OpenR1-Math上训练，优于监督微调和基线，并展现良好泛化能力

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is widely used to improve reasoning in multiple domains, yet outcome-only scalar rewards are often sparse and uninformative, especially on failed samples, where they merely indicate failure and provide no insight into why the reasoning fails. In this paper, we investigate how to leverage richer verbal feedback to guide RLVR training on failed samples, and how to convert such feedback into a trainable learning signal. Specifically, we propose a multi-turn feedback-guided reinforcement learning framework. It builds on three mechanisms: (1) dynamic multi-turn regeneration guided by feedback, triggered only on failed samples, (2) two complementary learning signals for within-turn and cross-turn optimization, and (3) structured feedback injection into the model's reasoning process. Trained on sampled OpenR1-Math, the approach outperforms supervised fine-tuning and RLVR baselines in-domain and generalizes well out-of-domain.

