---
layout: default
title: Neural-Symbolic Integration with Evolvable Policies
---

# Neural-Symbolic Integration with Evolvable Policies
**arXiv**：[2601.04799v1](https://arxiv.org/abs/2601.04799) · [PDF](https://arxiv.org/pdf/2601.04799.pdf)  
**作者**：Marios Thoma, Vassilis Vassiliades, Loizos Michael  

**一句话要点**：提出基于进化策略的神经符号集成框架，以解决非可微符号策略学习问题

**关键词**：神经符号集成, 进化策略, 非可微策略学习, 可进化性框架, 机器教练语义

## 3 点简述
- 现有神经符号框架依赖预定义或可微符号策略，限制在无领域知识或非可微场景的应用
- 通过进化过程同时学习非可微符号策略和神经网络权重，利用突变和选择机制逼近目标策略
- 实验显示从空策略和随机权重出发，能近似非可微目标策略，中位正确率接近100%

## 摘要（原文）

> Neural-Symbolic (NeSy) Artificial Intelligence has emerged as a promising approach for combining the learning capabilities of neural networks with the interpretable reasoning of symbolic systems. However, existing NeSy frameworks typically require either predefined symbolic policies or policies that are differentiable, limiting their applicability when domain expertise is unavailable or when policies are inherently non-differentiable. We propose a framework that addresses this limitation by enabling the concurrent learning of both non-differentiable symbolic policies and neural network weights through an evolutionary process. Our approach casts NeSy systems as organisms in a population that evolve through mutations (both symbolic rule additions and neural weight changes), with fitness-based selection guiding convergence toward hidden target policies. The framework extends the NEUROLOG architecture to make symbolic policies trainable, adapts Valiant's Evolvability framework to the NeSy context, and employs Machine Coaching semantics for mutable symbolic representations. Neural networks are trained through abductive reasoning from the symbolic component, eliminating differentiability requirements. Through extensive experimentation, we demonstrate that NeSy systems starting with empty policies and random neural weights can successfully approximate hidden non-differentiable target policies, achieving median correct performance approaching 100%. This work represents a step toward enabling NeSy research in domains where the acquisition of symbolic knowledge from experts is challenging or infeasible.

