---
layout: default
title: Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients
---

# Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients
**arXiv**：[2601.23135v1](https://arxiv.org/abs/2601.23135) · [PDF](https://arxiv.org/pdf/2601.23135.pdf)  
**作者**：Cheng Ge, Caitlyn Heqi Yin, Hao Liang, Jiawei Zhang  

**一句话要点**：从局部曲率视角解释GRPO中标准差归一化作为自适应梯度，提升收敛速度

**关键词**：强化学习, 策略优化, 梯度归一化, 自适应梯度, 语言模型推理

## 3 点简述
- 核心问题：GRPO中标准差归一化为何及何时有效，缺乏理论解释
- 方法要点：基于序列级策略梯度的局部曲率分析，证明归一化实现自适应梯度
- 实验或效果：在GSM8K和MATH基准上识别三个训练阶段，验证理论增益

## 摘要（原文）

> Reinforcement learning (RL) has become a key driver of language model reasoning. Among RL algorithms, Group Relative Policy Optimization (GRPO) is the de facto standard, avoiding the need for a critic by using per-prompt baselines and variance normalization. Yet why and when this normalization helps remains unclear. In this work, we provide an explanation through the lens of local curvature of the sequence-level policy gradient: standard deviation normalization implements an adaptive gradient. Theoretically, under mild conditions, GRPO enjoys a strictly improved convergence rate over unnormalized REINFORCE, with gains characterized by the average within-prompt reward standard deviation across prompts and iterations. Empirically, our analysis on GSM8K and MATH benchmarks reveals three distinct training phases governed by the interplay between feature orthogonality and reward variance: (I) an early acceleration phase where high variance and orthogonality favor adaptive scaling; (II) a relatively stable transition phase; and (III) a late-stage regime where the loss of orthogonality limits further gains. Together, these results provide a principled account of when std normalization helps in GRPO, and offer broader insights into the design of critic-free RL algorithms.

