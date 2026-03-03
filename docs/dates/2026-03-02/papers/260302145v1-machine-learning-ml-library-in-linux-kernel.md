---
layout: default
title: Machine Learning (ML) library in Linux kernel
---

# Machine Learning (ML) library in Linux kernel
**arXiv**：[2603.02145v1](https://arxiv.org/abs/2603.02145) · [PDF](https://arxiv.org/pdf/2603.02145.pdf)  
**作者**：Viacheslav Dubeyko  

**一句话要点**：提出Linux内核中的机器学习库架构以解决内核空间无浮点运算支持的性能问题

**关键词**：Linux内核, 机器学习库, 内核空间, 浮点运算, 性能优化, 概念验证

## 3 点简述
- 核心问题：Linux内核因无浮点运算支持，直接引入机器学习模型可能导致性能下降
- 方法要点：设计内核空间ML库架构，通过代理与用户空间线程交互，实现ML模型在内核中的应用
- 实验或效果：已实现概念验证项目，展示建议的可行性并设计交互接口

## 摘要（原文）

> Linux kernel is a huge code base with enormous number of subsystems and possible configuration options that results in unmanageable complexity of elaborating an efficient configuration. Machine Learning (ML) is approach/area of learning from data, finding patterns, and making predictions without implementing algorithms by developers that can introduce a self-evolving capability in Linux kernel. However, introduction of ML approaches in Linux kernel is not easy way because there is no direct use of floating-point operations (FPU) in kernel space and, potentially, ML models can be a reason of significant performance degradation in Linux kernel. Paper suggests the ML infrastructure architecture in Linux kernel that can solve the declared problem and introduce of employing ML models in kernel space. Suggested approach of kernel ML library has been implemented as Proof Of Concept (PoC) project with the goal to demonstrate feasibility of the suggestion and to design the interface of interaction the kernel-space ML model proxy and the ML model user-space thread.

