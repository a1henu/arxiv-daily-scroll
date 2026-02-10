---
layout: default
title: Reasoning aligns language models to human cognition
---

# Reasoning aligns language models to human cognition
**arXiv**：[2602.08693v1](https://arxiv.org/abs/2602.08693) · [PDF](https://arxiv.org/pdf/2602.08693.pdf)  
**作者**：Gonçalo Guiomar, Elia Torre, Pehuen Moure, Victoria Shavina, Mario Giulianelli, Shih-Chii Liu, Valerio Mante  

**一句话要点**：提出主动概率推理任务，揭示思维链推理使语言模型在不确定性决策中更接近人类认知。

**关键词**：语言模型对齐, 思维链推理, 不确定性决策, 认知建模, 主动推理

## 3 点简述
- 核心问题：语言模型在不确定性下是否像人类一样决策，思维链推理的作用是什么。
- 方法要点：引入主动概率推理任务，分离证据采样与推断，拟合机制模型分析认知偏差。
- 实验或效果：基准测试显示思维链推理显著提升推断性能，使信念轨迹更人类化，但采样改进有限。

## 摘要（原文）

> Do language models make decisions under uncertainty like humans do, and what role does chain-of-thought (CoT) reasoning play in the underlying decision process? We introduce an active probabilistic reasoning task that cleanly separates sampling (actively acquiring evidence) from inference (integrating evidence toward a decision). Benchmarking humans and a broad set of contemporary large language models against near-optimal reference policies reveals a consistent pattern: extended reasoning is the key determinant of strong performance, driving large gains in inference and producing belief trajectories that become strikingly human-like, while yielding only modest improvements in active sampling. To explain these differences, we fit a mechanistic model that captures systematic deviations from optimal behavior via four interpretable latent variables: memory, strategy, choice bias, and occlusion awareness. This model places humans and models in a shared low-dimensional cognitive space, reproduces behavioral signatures across agents, and shows how chain-of-thought shifts language models toward human-like regimes of evidence accumulation and belief-to-choice mapping, tightening alignment in inference while leaving a persistent gap in information acquisition.

