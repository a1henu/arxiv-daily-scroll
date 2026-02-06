---
layout: default
title: Conditional Diffusion Guidance under Hard Constraint: A Stochastic Analysis Approach
---

# Conditional Diffusion Guidance under Hard Constraint: A Stochastic Analysis Approach
**arXiv**：[2602.05533v1](https://arxiv.org/abs/2602.05533) · [PDF](https://arxiv.org/pdf/2602.05533.pdf)  
**作者**：Zhengyi Guo, Wenpin Tang, Renyuan Xu  

**一句话要点**：提出基于随机分析的硬约束条件扩散引导框架，用于安全关键应用和罕见事件模拟。

**关键词**：扩散模型, 条件生成, 硬约束, 随机分析, 罕见事件模拟, 鞅理论

## 3 点简述
- 研究扩散模型在硬约束下的条件生成问题，要求样本以概率一满足约束。
- 基于Doob's h变换和鞅表示，开发无需修改预训练分数网络的引导动力学框架。
- 提出两种离策略学习算法，提供非渐近保证，实验验证硬约束执行和罕见事件生成效果。

## 摘要（原文）

> We study conditional generation in diffusion models under hard constraints, where generated samples must satisfy prescribed events with probability one. Such constraints arise naturally in safety-critical applications and in rare-event simulation, where soft or reward-based guidance methods offer no guarantee of constraint satisfaction. Building on a probabilistic interpretation of diffusion models, we develop a principled conditional diffusion guidance framework based on Doob's h-transform, martingale representation and quadratic variation process. Specifically, the resulting guided dynamics augment a pretrained diffusion with an explicit drift correction involving the logarithmic gradient of a conditioning function, without modifying the pretrained score network. Leveraging martingale and quadratic-variation identities, we propose two novel off-policy learning algorithms based on a martingale loss and a martingale-covariation loss to estimate h and its gradient using only trajectories from the pretrained model. We provide non-asymptotic guarantees for the resulting conditional sampler in both total variation and Wasserstein distances, explicitly characterizing the impact of score approximation and guidance estimation errors. Numerical experiments demonstrate the effectiveness of the proposed methods in enforcing hard constraints and generating rare-event samples.

