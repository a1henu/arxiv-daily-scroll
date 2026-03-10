---
layout: default
title: Training event-based neural networks with exact gradients via Differentiable ODE Solving in JAX
---

# Training event-based neural networks with exact gradients via Differentiable ODE Solving in JAX
**arXiv**：[2603.08146v1](https://arxiv.org/abs/2603.08146) · [PDF](https://arxiv.org/pdf/2603.08146.pdf)  
**作者**：Lukas König, Manuel Kuhn, David Kappel, Anand Subramoney  

**一句话要点**：提出Eventax框架，通过可微分ODE求解实现事件驱动神经网络的精确梯度训练

**关键词**：脉冲神经网络, 可微分ODE求解, 精确梯度训练, 事件驱动计算, JAX框架, 神经元模型扩展

## 3 点简述
- 现有脉冲神经网络梯度训练方法存在离散时间与连续时间间的权衡问题
- Eventax结合可微分数值ODE求解器与事件驱动脉冲处理，支持任意ODE定义的神经元模型
- 在多个基准测试中验证了框架的灵活性和实用性，包括复杂神经元模型的应用

## 摘要（原文）

> Existing frameworks for gradient-based training of spiking neural networks face a trade-off: discrete-time methods using surrogate gradients support arbitrary neuron models but introduce gradient bias and constrain spike-time resolution, while continuous-time methods that compute exact gradients require analytical expressions for spike times and state evolution, restricting them to simple neuron types such as Leaky Integrate and Fire (LIF). We introduce the Eventax framework, which resolves this trade-off by combining differentiable numerical ODE solvers with event-based spike handling. Built in JAX, our frame-work uses Diffrax ODE-solvers to compute gradients that are exact with respect to the forward simulation for any neuron model defined by ODEs . It also provides a simple API where users can specify just the neuron dynamics, spike conditions, and reset rules. Eventax prioritises modelling flexibility, supporting a wide range of neuron models, loss functions, and network architectures, which can be easily extended. We demonstrate Eventax on multiple benchmarks, including Yin-Yang and MNIST, using diverse neuron models such as Leaky Integrate-and-fire (LIF), Quadratic Integrate-and-fire (QIF), Exponential integrate-and-fire (EIF), Izhikevich and Event-based Gated Recurrent Unit (EGRU) with both time-to-first-spike and state-based loss functions, demonstrating its utility for prototyping and testing event-based architectures trained with exact gradients. We also demonstrate the application of this framework for more complex neuron types by implementing a multi-compartment neuron that uses a model of dendritic spikes in human layer 2/3 cortical Pyramidal neurons for computation. Code available at https://github.com/efficient-scalable-machine-learning/eventax.

