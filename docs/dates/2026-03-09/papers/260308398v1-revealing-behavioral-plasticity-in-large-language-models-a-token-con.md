---
layout: default
title: Revealing Behavioral Plasticity in Large Language Models: A Token-Conditional Perspective
---

# Revealing Behavioral Plasticity in Large Language Models: A Token-Conditional Perspective
**arXiv**：[2603.08398v1](https://arxiv.org/abs/2603.08398) · [PDF](https://arxiv.org/pdf/2603.08398.pdf)  
**作者**：Liyuan Mao, Le Yu, Jing Zhou, Chujie Zheng, Bowen Yu, Chang Gao, Shixuan Liu, An Yang, Weinan Zhang, JunYang Lin  

**一句话要点**：提出Token-Conditioned Reinforcement Learning以稳定大语言模型的行为可塑性

**关键词**：大语言模型, 行为可塑性, 令牌条件生成, 强化学习, 推理模型适应

## 3 点简述
- 揭示大语言模型具有内在行为可塑性，可通过令牌条件生成在推理时切换行为模式
- 提出ToCoRL框架，利用强化学习将临时行为适应转化为稳定可学习模式
- 实验表明ToCoRL能实现精确行为控制，如让推理模型在事实问答中表现优异

## 摘要（原文）

> In this work, we reveal that Large Language Models (LLMs) possess intrinsic behavioral plasticity-akin to chameleons adapting their coloration to environmental cues-that can be exposed through token-conditional generation and stabilized via reinforcement learning. Specifically, by conditioning generation on carefully selected token prefixes sampled from responses exhibiting desired behaviors, LLMs seamlessly adapt their behavioral modes at inference time (e.g., switching from step-by-step reasoning to direct answering) without retraining. Based on this insight, we propose Token-Conditioned Reinforcement Learning (ToCoRL), a principled framework that leverages RL to internalize this chameleon-like plasticity, transforming transient inference-time adaptations into stable and learnable behavioral patterns. ToCoRL guides exploration with token-conditional generation and keep enhancing exploitation, enabling emergence of appropriate behaviors. Extensive experiments show that ToCoRL enables precise behavioral control without capability degradation. Notably, we show that large reasoning models, while performing strongly on complex mathematics, can be effectively adapted to excel at factual question answering, which was a capability previously hindered by their step-by-step reasoning patterns.

