---
layout: default
title: Agentic Critical Training
---

# Agentic Critical Training
**arXiv**：[2603.08706v1](https://arxiv.org/abs/2603.08706) · [PDF](https://arxiv.org/pdf/2603.08706.pdf)  
**作者**：Weize Liu, Minghui Liu, Sy-Tuyen Ho, Souradip Chakraborty, Xiyao Wang, Furong Huang  

**一句话要点**：提出Agentic Critical Training以通过强化学习训练大语言模型自主判断动作质量

**关键词**：大语言模型代理, 强化学习, 自主推理, 动作质量评估, 泛化能力

## 3 点简述
- 核心问题：模仿学习训练的大语言模型代理缺乏对动作质量的理解，无法自主反思。
- 方法要点：采用强化学习范式，通过奖励模型正确判断动作优劣来驱动自主推理能力发展。
- 实验或效果：在三个代理基准上平均提升5.07点，优于模仿学习和强化学习基线，并展示出强泛化能力。

## 摘要（原文）

> Training large language models (LLMs) as autonomous agents often begins with imitation learning, but it only teaches agents what to do without understanding why: agents never contrast successful actions against suboptimal alternatives and thus lack awareness of action quality. Recent approaches attempt to address this by introducing self-reflection supervision derived from contrasts between expert and alternative actions. However, the training paradigm fundamentally remains imitation learning: the model imitates pre-constructed reflection text rather than learning to reason autonomously. We propose Agentic Critical Training (ACT), a reinforcement learning paradigm that trains agents to identify the better action among alternatives. By rewarding whether the model's judgment is correct, ACT drives the model to autonomously develop reasoning about action quality, producing genuine self-reflection rather than imitating it. Across three challenging agent benchmarks, ACT consistently improves agent performance when combined with different post-training methods. It achieves an average improvement of 5.07 points over imitation learning and 4.62 points over reinforcement learning. Compared to approaches that inject reflection capability through knowledge distillation, ACT also demonstrates clear advantages, yielding an average improvement of 2.42 points. Moreover, ACT enables strong out-of-distribution generalization on agentic benchmarks and improves performance on general reasoning benchmarks without any reasoning-specific training data, highlighting the value of our method. These results suggest that ACT is a promising path toward developing more reflective and capable LLM agents.

