---
layout: default
title: Drift-Diffusion Matching: Embedding dynamics in latent manifolds of asymmetric neural networks
---

# Drift-Diffusion Matching: Embedding dynamics in latent manifolds of asymmetric neural networks
**arXiv**：[2602.14885v1](https://arxiv.org/abs/2602.14885) · [PDF](https://arxiv.org/pdf/2602.14885.pdf)  
**作者**：Ramón Nartallo-Kaluarachchi, Renaud Lambiotte, Alain Goriely  

**一句话要点**：提出漂移-扩散匹配框架，在非对称RNN的低维流形中嵌入任意随机动力学系统

**关键词**：循环神经网络, 非对称连接, 随机动力学系统, 低维流形嵌入, 非平衡统计力学, 联想记忆

## 3 点简述
- 核心问题：经典RNN模型依赖对称连接，限制网络动力学为梯度流，无法模拟生物网络的丰富时间依赖行为。
- 方法要点：引入漂移-扩散匹配框架，训练连续时间RNN在低维潜在子空间中表示任意随机微分方程的漂移和扩散，包括非线性与非平衡动力学。
- 实验或效果：构建RNN实现随机系统，通过输入驱动切换和自主过渡探索吸引子，作为联想和序列记忆模型，并基于非对称性和时间不可逆性分解网络以阐明编码机制。

## 摘要（原文）

> Recurrent neural networks (RNNs) provide a theoretical framework for understanding computation in biological neural circuits, yet classical results, such as Hopfield's model of associative memory, rely on symmetric connectivity that restricts network dynamics to gradient-like flows. In contrast, biological networks support rich time-dependent behaviour facilitated by their asymmetry. Here we introduce a general framework, which we term drift-diffusion matching, for training continuous-time RNNs to represent arbitrary stochastic dynamical systems within a low-dimensional latent subspace. Allowing asymmetric connectivity, we show that RNNs can faithfully embed the drift and diffusion of a given stochastic differential equation, including nonlinear and nonequilibrium dynamics such as chaotic attractors. As an application, we construct RNN realisations of stochastic systems that transiently explore various attractors through both input-driven switching and autonomous transitions driven by nonequilibrium currents, which we interpret as models of associative and sequential (episodic) memory. To elucidate how these dynamics are encoded in the network, we introduce decompositions of the RNN based on its asymmetric connectivity and its time-irreversibility. Our results extend attractor neural network theory beyond equilibrium, showing that asymmetric neural populations can implement a broad class of dynamical computations within low-dimensional manifolds, unifying ideas from associative memory, nonequilibrium statistical mechanics, and neural computation.

