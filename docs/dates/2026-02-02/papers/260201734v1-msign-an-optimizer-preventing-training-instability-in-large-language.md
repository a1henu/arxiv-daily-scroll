---
layout: default
title: MSign: An Optimizer Preventing Training Instability in Large Language Models via Stable Rank Restoration
---

# MSign: An Optimizer Preventing Training Instability in Large Language Models via Stable Rank Restoration
**arXiv**：[2602.01734v1](https://arxiv.org/abs/2602.01734) · [PDF](https://arxiv.org/pdf/2602.01734.pdf)  
**作者**：Lianhai Ren, Yucheng Ding, Xiao Liu, Qianxiao Li, Peng Cheng, Yeyun Gong  

**一句话要点**：提出MSign优化器，通过稳定秩恢复防止大语言模型训练不稳定

**关键词**：大语言模型, 训练稳定性, 优化器设计, 梯度爆炸, 稳定秩, 雅可比矩阵

## 3 点简述
- 核心问题：大语言模型预训练中梯度爆炸导致训练失败，浪费计算资源
- 方法要点：基于稳定秩下降和雅可比矩阵对齐理论，设计周期性矩阵符号操作恢复稳定秩
- 实验或效果：在5M至3B参数模型上验证，有效防止训练失败，计算开销低于7.0%

## 摘要（原文）

> Training instability remains a critical challenge in large language model (LLM) pretraining, often manifesting as sudden gradient explosions that waste significant computational resources. We study training failures in a 5M-parameter NanoGPT model scaled via $μ$P, identifying two key phenomena preceding collapse: (1) rapid decline in weight matrix stable rank (ratio of squared Frobenius norm to squared spectral norm), and (2) increasing alignment between adjacent layer Jacobians. We prove theoretically that these two conditions jointly cause exponential gradient norm growth with network depth. To break this instability mechanism, we propose MSign, a new optimizer that periodically applies matrix sign operations to restore stable rank. Experiments on models from 5M to 3B parameters demonstrate that MSign effectively prevents training failures with a computational overhead of less than 7.0%.

