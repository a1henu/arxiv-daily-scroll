---
layout: default
title: Unrewarded Exploration in Large Language Models Reveals Latent Learning from Psychology
---

# Unrewarded Exploration in Large Language Models Reveals Latent Learning from Psychology
**arXiv**：[2601.22474v1](https://arxiv.org/abs/2601.22474) · [PDF](https://arxiv.org/pdf/2601.22474.pdf)  
**作者**：Jian Xiong, Jingbo Zhou, Zihan Zhou, Yixiong Xiao, Le Zhang, Jingyong Ye, Rui Qian, Yang Zhou, Dejing Dou  

**一句话要点**：揭示大语言模型在无奖励探索中展现心理学潜在学习动态，提升任务性能

**关键词**：大语言模型, 潜在学习, 无奖励探索, 强化学习, 认知科学, 模型训练

## 3 点简述
- 核心问题：大语言模型训练过度依赖奖励学习，限制灵活性与泛化能力，心理学中的潜在学习现象在模型中是否出现未知。
- 方法要点：采用两阶段训练，先无奖励探索组织知识，后引入奖励增强性能，避免奖励驱动偏差。
- 实验或效果：跨多模型家族和任务域实验证实潜在学习动态存在，模型最终能力优于全程奖励强化学习。

## 摘要（原文）

> Latent learning, classically theorized by Tolman, shows that biological agents (e.g., rats) can acquire internal representations of their environment without rewards, enabling rapid adaptation once rewards are introduced. In contrast, from a cognitive science perspective, reward learning remains overly dependent on external feedback, limiting flexibility and generalization. Although recent advances in the reasoning capabilities of large language models (LLMs), such as OpenAI-o1 and DeepSeek-R1, mark a significant breakthrough, these models still rely primarily on reward-centric reinforcement learning paradigms. Whether and how the well-established phenomenon of latent learning in psychology can inform or emerge within LLMs' training remains largely unexplored. In this work, we present novel findings from our experiments that LLMs also exhibit the latent learning dynamics. During an initial phase of unrewarded exploration, LLMs display modest performance improvements, as this phase allows LLMs to organize task-relevant knowledge without being constrained by reward-driven biases, and performance is further enhanced once rewards are introduced. LLMs post-trained under this two-stage exploration regime ultimately achieve higher competence than those post-trained with reward-based reinforcement learning throughout. Beyond these empirical observations, we also provide theoretical analyses for our experiments explaining why unrewarded exploration yields performance gains, offering a mechanistic account of these dynamics. Specifically, we conducted extensive experiments across multiple model families and diverse task domains to establish the existence of the latent learning dynamics in LLMs.

