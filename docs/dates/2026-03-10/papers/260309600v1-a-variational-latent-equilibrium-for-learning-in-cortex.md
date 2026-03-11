---
layout: default
title: A Variational Latent Equilibrium for Learning in Cortex
---

# A Variational Latent Equilibrium for Learning in Cortex
**arXiv**：[2603.09600v1](https://arxiv.org/abs/2603.09600) · [PDF](https://arxiv.org/pdf/2603.09600.pdf)  
**作者**：Simon Brandt, Paul Haider, Walter Senn, Federico Benitez, Mihai A. Petrovici  

**一句话要点**：提出变分潜在平衡框架，以生物合理方式近似BPTT，用于大脑时空深度学习。

**关键词**：时空信用分配, 变分潜在平衡, 生物合理学习, 连续时间网络, 能量函数, 局部学习

## 3 点简述
- 核心问题：BPTT算法与大脑神经环路和动力学不兼容，需生物合理近似。
- 方法要点：基于能量守恒和极值作用原理，推导实时误差动态，实现时空局部学习。
- 实验或效果：提供理论框架，为大脑时空深度学习及物理电路设计提供蓝图。

## 摘要（原文）

> Brains remain unrivaled in their ability to recognize and generate complex spatiotemporal patterns. While AI is able to reproduce some of these capabilities, deep learning algorithms remain largely at odds with our current understanding of brain circuitry and dynamics. This is prominently the case for backpropagation through time (BPTT), the go-to algorithm for learning complex temporal dependencies. In this work we propose a general formalism to approximate BPTT in a controlled, biologically plausible manner. Our approach builds on, unifies and extends several previous approaches to local, time-continuous, phase-free spatiotemporal credit assignment based on principles of energy conservation and extremal action. Our starting point is a prospective energy function of neuronal states, from which we calculate real-time error dynamics for time-continuous neuronal networks. In the general case, this provides a simple and straightforward derivation of the adjoint method result for neuronal networks, the time-continuous equivalent to BPTT. With a few modifications, we can turn this into a fully local (in space and time) set of equations for neuron and synapse dynamics. Our theory provides a rigorous framework for spatiotemporal deep learning in the brain, while simultaneously suggesting a blueprint for physical circuits capable of carrying out these computations. These results reframe and extend the recently proposed Generalized Latent Equilibrium (GLE) model.

