---
layout: default
title: Outcome-Based RL Provably Leads Transformers to Reason, but Only With the Right Data
---

# Outcome-Based RL Provably Leads Transformers to Reason, but Only With the Right Data
**arXiv**：[2601.15158v1](https://arxiv.org/abs/2601.15158) · [PDF](https://arxiv.org/pdf/2601.15158.pdf)  
**作者**：Yuval Ran-Milo, Yotam Alexander, Shahar Mendel, Nadav Cohen  

**一句话要点**：证明基于结果的强化学习能引导Transformer推理，但依赖简单示例数据分布

**关键词**：Transformer推理, 强化学习, 梯度流分析, 数据分布, 链式思维, 数学推理

## 3 点简述
- 核心问题：稀疏奖励如何驱动梯度下降发现系统性推理机制
- 方法要点：分析单层Transformer在合成图遍历任务中的梯度流动态
- 实验或效果：理论结果在合成数据和真实语言模型数学推理任务中得到验证

## 摘要（原文）

> Transformers trained via Reinforcement Learning (RL) with outcome-based supervision can spontaneously develop the ability to generate intermediate reasoning steps (Chain-of-Thought). Yet the mechanism by which sparse rewards drive gradient descent to discover such systematic reasoning remains poorly understood. We address this by analyzing the gradient flow dynamics of single-layer Transformers on a synthetic graph traversal task that cannot be solved without Chain-of-Thought (CoT) but admits a simple iterative solution. We prove that despite training solely on final-answer correctness, gradient flow drives the model to converge to a structured, interpretable algorithm that iteratively traverses the graph vertex-by-vertex. We characterize the distributional properties required for this emergence, identifying the critical role of "simple examples": instances requiring fewer reasoning steps. When the training distribution places sufficient mass on these simpler instances, the model learns a generalizable traversal strategy that extrapolates to longer chains; when this mass vanishes, gradient-based learning becomes infeasible. We corroborate our theoretical results through experiments on synthetic data and with real-world language models on mathematical reasoning tasks, validating that our theoretical findings carry over to practical settings.

