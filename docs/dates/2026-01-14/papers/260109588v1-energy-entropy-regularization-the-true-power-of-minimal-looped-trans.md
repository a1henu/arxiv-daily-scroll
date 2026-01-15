---
layout: default
title: Energy-Entropy Regularization: The True Power of Minimal Looped Transformers
---

# Energy-Entropy Regularization: The True Power of Minimal Looped Transformers
**arXiv**：[2601.09588v1](https://arxiv.org/abs/2601.09588) · [PDF](https://arxiv.org/pdf/2601.09588.pdf)  
**作者**：Wai-Lun Lam  

**一句话要点**：提出能量-熵正则化框架，以解决单头循环Transformer在非凸损失景观中的训练难题。

**关键词**：循环Transformer, 能量-熵正则化, Tsallis熵, 哈密顿动力学, 损失景观优化, 归纳头任务

## 3 点简述
- 单头循环Transformer在基准任务中因高度非凸损失景观而训练失败或性能不佳。
- 利用Tsallis熵和哈密顿动力学将参数更新视为物理流，重塑损失景观几何。
- 成功训练模型维度d=8的单头循环Transformer，在1000令牌序列上解决归纳头任务。

## 摘要（原文）

> Recent research suggests that looped Transformers have superior reasoning capabilities compared to standard deep architectures. Current approaches to training single-head looped architectures on benchmark tasks frequently fail or yield suboptimal performance due to a highly non-convex and irregular loss landscape. In these settings, optimization often stagnates in poor local minima and saddle points of the loss landscape, preventing the model from discovering the global minimum point. The internal mechanisms of these single-head looped transformer models remain poorly understood, and training them from scratch remains a significant challenge. In this paper, we propose a novel training framework that leverages Tsallis entropy and Hamiltonian dynamics to transform the geometry of the loss landscape. By treating the parameter updates as a physical flow, we successfully trained a single-head looped Transformer with model dimension $d = 8$ to solve induction head task with input sequence length of 1000 tokens. This success reveals the internal mechanism behind the superior reasoning capability.

