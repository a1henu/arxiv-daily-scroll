---
layout: default
title: Meta-learning three-factor plasticity rules for structured credit assignment with sparse feedback
---

# Meta-learning three-factor plasticity rules for structured credit assignment with sparse feedback
**arXiv**：[2512.09366v1](https://arxiv.org/abs/2512.09366) · [PDF](https://arxiv.org/pdf/2512.09366.pdf)  
**作者**：Dimitra Maoutsa  

**一句话要点**：提出元学习框架以发现用于稀疏反馈下循环网络结构化信用分配的局部可塑性规则

**关键词**：元学习, 结构化信用分配, 稀疏反馈, 局部可塑性规则, 循环神经网络, 生物可信学习

## 3 点简述
- 核心问题：生物神经网络如何从稀疏延迟反馈中实现结构化信用分配，现有人工方法依赖非生物可信的全局规则。
- 方法要点：通过元学习框架，结合局部类新赫布更新和基于切线传播的外循环优化，发现三因子可塑性规则。
- 实验或效果：规则仅使用局部信息和延迟奖励支持长时程信用分配，为循环电路学习提供生物基础机制新见解。

## 摘要（原文）

> Biological neural networks learn complex behaviors from sparse, delayed feedback using local synaptic plasticity, yet the mechanisms enabling structured credit assignment remain elusive. In contrast, artificial recurrent networks solving similar tasks typically rely on biologically implausible global learning rules or hand-crafted local updates. The space of local plasticity rules capable of supporting learning from delayed reinforcement remains largely unexplored. Here, we present a meta-learning framework that discovers local learning rules for structured credit assignment in recurrent networks trained with sparse feedback. Our approach interleaves local neo-Hebbian-like updates during task execution with an outer loop that optimizes plasticity parameters via \textbf{tangent-propagation through learning}. The resulting three-factor learning rules enable long-timescale credit assignment using only local information and delayed rewards, offering new insights into biologically grounded mechanisms for learning in recurrent circuits.

