---
layout: default
title: SnareNet: Flexible Repair Layers for Neural Networks with Hard Constraints
---

# SnareNet: Flexible Repair Layers for Neural Networks with Hard Constraints
**arXiv**：[2602.09317v1](https://arxiv.org/abs/2602.09317) · [PDF](https://arxiv.org/pdf/2602.09317.pdf)  
**作者**：Ya-Chi Chu, Alkiviades Boukas, Madeleine Udell  

**一句话要点**：提出SnareNet，通过可微修复层和自适应松弛，确保神经网络输出满足输入依赖的非线性约束。

**关键词**：神经网络约束, 可微修复层, 自适应松弛, 优化学习, 轨迹规划, 可行性控制

## 3 点简述
- 核心问题：神经网络作为代理求解器或控制策略时，无约束预测可能违反物理、操作或安全要求。
- 方法要点：引入可微修复层在约束映射范围内迭代导航，结合自适应松弛设计，从初始化时捕获网络并逐步收紧至可行集。
- 实验或效果：在优化学习和轨迹规划基准测试中，相比先前工作，SnareNet在满足约束的同时提升了目标质量。

## 摘要（原文）

> Neural networks are increasingly used as surrogate solvers and control policies, but unconstrained predictions can violate physical, operational, or safety requirements. We propose SnareNet, a feasibility-controlled architecture for learning mappings whose outputs must satisfy input-dependent nonlinear constraints. SnareNet appends a differentiable repair layer that navigates in the constraint map's range space, steering iterates toward feasibility and producing a repaired output that satisfies constraints to a user-specified tolerance. To stabilize end-to-end training, we introduce adaptive relaxation, which designs a relaxed feasible set that snares the neural network at initialization and shrinks it into the feasible set, enabling early exploration and strict feasibility later in training. On optimization-learning and trajectory planning benchmarks, SnareNet consistently attains improved objective quality while satisfying constraints more reliably than prior work.

